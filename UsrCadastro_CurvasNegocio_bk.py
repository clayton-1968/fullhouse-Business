from imports import *

class DraggablePoint:
    def __init__(self, ax, x, y, callback):
        self.ax = ax
        self.normal_size = 0.02
        self.highlight_size = 0.03
        self.point = Circle((x, y), self.normal_size, facecolor='red', edgecolor='black', alpha=0.7, zorder=10)
        self.ax.add_patch(self.point)
        self.annotation = self.ax.annotate(f"{y:.0%}", (x, y), xytext=(0, 10), textcoords="offset points", ha='center', va='bottom', visible=False, zorder=11)
        self.press = None
        self.callback = callback
        self.background = None
        self.is_highlighted = False

    def connect(self):
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.cidhover = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def on_press(self, event):
        if event.inaxes != self.point.axes: return
        contains, _ = self.point.contains(event)
        if not contains: return
        self.press = (self.point.center), event.xdata, event.ydata

    def on_motion(self, event):
        if self.press is None: return
        if event.inaxes != self.point.axes: return
        center, xpress, ypress = self.press
        new_y = max(0, min(center[1] + event.ydata - ypress, 1))
        self.point.center = (center[0], new_y)
        self.annotation.set_position((center[0], new_y))
        self.annotation.set_text(f"{new_y:.0%}")
        self.point.set_visible(True)
        self.annotation.set_visible(True)
        self.callback(self)

    def on_release(self, event):
        self.press = None

    def on_hover(self, event):
        if event.inaxes != self.point.axes: return
        contains, _ = self.point.contains(event)
        if contains:
            self.highlight()
        else:
            self.unhighlight()
        self.point.figure.canvas.get_tk_widget().config(cursor=CURSOR_HAND if contains else CURSOR_DEFAULT)

    def highlight(self):
        if not self.is_highlighted:
            self.point.set_radius(self.highlight_size)
            self.point.set_facecolor('yellow')
            self.is_highlighted = True
            self.callback(self)

    def unhighlight(self):
        if self.is_highlighted:
            self.point.set_radius(self.normal_size)
            self.point.set_facecolor('red')
            self.is_highlighted = False
            self.callback(self)

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gráfico de Curva de Negócio")
        
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(0, 1)
        self.ax.set_title("Curva de Negócio")
        self.ax.set_xlabel("Meses")
        self.ax.set_ylabel("Percentual")
        self.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        
        self.points = [DraggablePoint(self.ax, x, 0, self.update_curve) for x in range(31)]
        for point in self.points:
            point.connect()
        
        self.line, = self.ax.plot([p.point.center[0] for p in self.points], [p.point.center[1] for p in self.points], 'b-')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.canvas.draw()
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)

        self.print_button = tk.Button(self.root, text="Imprimir Coordenadas", command=self.print_coordinates)
        self.print_button.pack()

        self.max_x_entry = tk.Entry(self.root)
        self.max_x_entry.insert(0, "30")
        self.max_x_entry.pack()
        self.max_x_button = tk.Button(self.root, text="Atualizar Eixo X", command=self.update_x_axis)
        self.max_x_button.pack()

    def update_curve(self, moved_point=None):
        self.canvas.restore_region(self.background)
        x = [p.point.center[0] for p in self.points if p.point.get_visible()]
        y = [p.point.center[1] for p in self.points if p.point.get_visible()]
        self.line.set_data(x, y)
        self.ax.draw_artist(self.line)
        for point in self.points:
            self.ax.draw_artist(point.point)
            self.ax.draw_artist(point.annotation)
        self.canvas.blit(self.ax.bbox)

    def print_coordinates(self):
        for i, point in enumerate(self.points):
            x, y = point.point.center
            if point.point.get_visible():
                print(f"Ponto {i}: ({x:.2f}, {y:.2%})")
            else:
                print(f"Ponto {i}: ({x:.2f}, 0.00%)")

    def update_x_axis(self):
        try:
            new_max_x = int(float(self.max_x_entry.get()))
            if new_max_x <= 0:
                raise ValueError("O valor máximo do eixo X deve ser positivo.")
            
            old_max_x = int(self.ax.get_xlim()[1])
            
            if new_max_x > old_max_x:
                for x in range(old_max_x + 1, new_max_x + 1):
                    self.points.append(DraggablePoint(self.ax, x, 0, self.update_curve))
                    self.points[-1].connect()
            elif new_max_x < old_max_x:
                for point in self.points[new_max_x + 1:]:
                    point.point.remove()
                    point.annotation.remove()
                self.points = self.points[:new_max_x + 1]
            
            for i, point in enumerate(self.points):
                point.point.center = (i, point.point.center[1])
                point.annotation.set_position((i, point.point.center[1]))
            
            self.ax.set_xlim(0, new_max_x)
            self.canvas.draw()
            self.background = self.canvas.copy_from_bbox(self.ax.bbox)
            self.update_curve()
        except ValueError as e:
            tk.messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()