from imports import *
from widgets import Widgets

################# criando janela ###############
class Cadastrar_Curvas_Negocio(Widgets):
    def cadastrar_curvas_negocio(self):
        self.window_one.title('Cadastro Curvas de Negócios')
        self.clearFrame_principal()
        self.frame_cabecalho_cadastro_curvas_linha_1(self.principal_frame)
        
################# dividindo a janela ###############
    def frame_cabecalho_cadastro_curvas_linha_1(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.455
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa", anchor='w')
        lb_empresa.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_orcamento))

        # Nome da Curva
        coordenadas_relx = 0.465
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.33
        coordenadas_relheight = 0.07
        fr_nome_curva = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_curva.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_nome_curva = customtkinter.CTkLabel(fr_nome_curva, text="Nome da Curva", anchor='w')
        lb_nome_curva.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        curvas = []

        self.entry_nome_curva = AutocompleteCombobox(fr_nome_curva, width=30, font=('Times', 11), completevalues=curvas)
        self.entry_nome_curva.pack()
        self.entry_nome_curva.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_nome_curva.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela),  self.entry_nome_curva))
        self.entry_nome_curva.bind("<KeyRelease>", lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_nome_curva))
        self.entry_nome_curva.bind('<Down>', lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_nome_curva))
        
        # Prazo da Curva
        coordenadas_relx=0.80
        coordenadas_rely=0.01
        coordenadas_relwidth=0.06
        coordenadas_relheight=0.07
        fr_prazo_curva = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_prazo_curva.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_prazo_curva = customtkinter.CTkLabel(fr_prazo_curva, text="Prazo(meses)", anchor='w')
        lb_prazo_curva.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.opcoes = ['1', 
                       '2', 
                       '3', 
                       '4', 
                       '5', 
                       '6', 
                       '7',  
                       '8', 
                       '9',  
                       '10', 
                       '11',  
                       '12', 
                       '13', 
                       '14', 
                       '15', 
                       '16', 
                       '17', 
                       '18', 
                       '19', 
                       '20', 
                       '21', 
                       '22', 
                       '23', 
                       '24', 
                       '25', 
                       '26', 
                       '27', 
                       '28', 
                       '29', 
                       '30',
                       '31',
                       '32', 
                       '33', 
                       '34', 
                       '35', 
                       '36',
                       '37', 
                       '38', 
                       '39', 
                       '40', 
                       '41',
                       '42', 
                       '43', 
                       '44', 
                       '45', 
                       '46',
                       '47', 
                       '48', 
                       '49', 
                       '50', 
                       '51',
                       '52', 
                       '53', 
                       '54', 
                       '55', 
                       '56',
                       '57', 
                       '58', 
                       '59', 
                       '60', 
                       ]
        self.entry_prazo_curva = customtkinter.CTkComboBox(fr_prazo_curva, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_prazo_curva.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_prazo_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.checkbox_ativo))

        # Botão Nova Curva
        icon_image = self.base64_to_photoimage('savedown')
        self.btn_criar_nova_curva = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=self.frame_grafico_curva_linha_2)
        self.btn_criar_nova_curva.place(relx=0.865, rely=0.012, relwidth=0.04, relheight=0.05)
        
        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_curva = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=[])
        self.btn_consultar_curva.place(relx=0.91, rely=0.012, relwidth=0.04, relheight=0.05)
        
        # Botão de Salvar
        icon_image = self.base64_to_photoimage('save')
        self.btn_salvar_curva = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=[])
        self.btn_salvar_curva.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)
    
    def frame_grafico_curva_linha_2(self):
        # Limpar gráfico existente, se houver
        if hasattr(self, 'grafico_curva'):
            self.grafico_curva.cleanup()
            delattr(self, 'grafico_curva')

        # Criar ou limpar o frame para o gráfico
        if hasattr(self, 'frame_grafico'):
            if self.frame_grafico.winfo_exists():
                for widget in self.frame_grafico.winfo_children():
                    widget.destroy()
            else:
                # Se o frame não existe mais, crie um novo
                self.frame_grafico = customtkinter.CTkFrame(self.principal_frame)
                self.frame_grafico.place(relx=0.005, rely=0.1, relwidth=0.99, relheight=0.85)
        else:
            # Se o atributo não existe, crie um novo frame
            self.frame_grafico = customtkinter.CTkFrame(self.principal_frame)
            self.frame_grafico.place(relx=0.005, rely=0.1, relwidth=0.99, relheight=0.85)

        # Criar o novo gráfico
        self.grafico_curva = GraphApp(
            self.frame_grafico, 
            self.entry_nome_curva.get(), 
            self.obter_Empresa_ID(self.entry_empresa.get(), self.window_one),
            self.entry_prazo_curva.get()
        )
        
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
        self.cids = []
        self.hover_timer = None

    def connect(self):
        self.cids.append(self.point.figure.canvas.mpl_connect('button_press_event', self.on_press))
        self.cids.append(self.point.figure.canvas.mpl_connect('button_release_event', self.on_release))
        self.cids.append(self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion))
        self.cids.append(self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_hover))
    
    def disconnect(self):
        for cid in self.cids:
            self.point.figure.canvas.mpl_disconnect(cid)
        self.cids.clear()

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
        if event.inaxes != self.point.axes:
            return
        contains, _ = self.point.contains(event)
        if contains:
            if self.hover_timer is None:
                self.hover_timer = threading.Timer(0.1, self.delayed_highlight)
                self.hover_timer.start()
        else:
            self.cancel_hover_timer()
            self.unhighlight()
        self.point.figure.canvas.get_tk_widget().config(cursor=CURSOR_HAND if contains else CURSOR_DEFAULT)

    def delayed_highlight(self):
        self.highlight()
        self.hover_timer = None

    def cancel_hover_timer(self):
        if self.hover_timer:
            self.hover_timer.cancel()
            self.hover_timer = None

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

class GraphApp():
    def __init__(self, frame, nome_curva, empresa_id, prazo_curva):
        self.frame = frame
        self.prazo_curva = int(prazo_curva)
        self.nome_curva = nome_curva
        self.empresa_id = empresa_id
        
        # Limpar o frame antes de criar um novo gráfico
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        self.ax.set_xlim(0, self.prazo_curva)
        self.ax.set_ylim(0, 1)
        self.ax.set_title(f"Curva de Negócio: {self.nome_curva}")
        self.ax.set_xlabel("Meses")
        self.ax.set_ylabel("Percentual")
        self.ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        
        # Distribuir o percentual uniformemente ao longo do prazo
        y_values = [i / self.prazo_curva for i in range(self.prazo_curva + 1)]
        self.points = [DraggablePoint(self.ax, x, y, self.update_curve) for x, y in enumerate(y_values)]
        for point in self.points:
            point.connect()
        
        # Crie a linha inicial com os pontos distribuídos
        x = [p.point.center[0] for p in self.points]
        y = [p.point.center[1] for p in self.points]
        self.line, = self.ax.plot(x, y, 'b-')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)

        self.update_lock = threading.Lock()
        self.is_updating = False

    def update_curve(self, moved_point=None):
        with self.update_lock:
            if self.is_updating:
                return
            self.is_updating = True

        try:
            sorted_points = sorted(self.points, key=lambda p: p.point.center[0])
            
            x = [p.point.center[0] for p in sorted_points]
            y = [p.point.center[1] for p in sorted_points]
            
            self.line.set_data(x, y)
            
            self.canvas.restore_region(self.background)
            self.ax.draw_artist(self.line)
            
            for point in sorted_points:
                self.ax.draw_artist(point.point)
                point.annotation.set_text(f"{point.point.center[1]:.0%}")
                point.annotation.set_visible(point.is_highlighted)
                self.ax.draw_artist(point.annotation)
            
            self.canvas.blit(self.ax.bbox)
            self.canvas.flush_events()
        finally:
            self.is_updating = False

    def print_coordinates(self):
        sorted_points = sorted(self.points, key=lambda p: p.point.center[0])
        for i, point in enumerate(sorted_points):
            x, y = point.point.center
            print(f"Mês {i}: {y:.2%}")
    
    def cleanup(self):
        for point in self.points:
            point.disconnect()
            point.callback = None
        self.points.clear()
        plt.close(self.fig)
        self.canvas.get_tk_widget().destroy()
        self.ax.clear()
        self.fig.clear()

    