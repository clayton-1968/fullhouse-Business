from imports import *

class DraggablePoint:
    def __init__(self, ax, x, y):
        self.ax = ax  # Eixo onde o ponto será desenhado
        self.x = x  # Coordenada x inicial do ponto
        self.y = y  # Coordenada y inicial do ponto
        self.point, = ax.plot(x, y, 'ro', picker=5)  # Cria um ponto vermelho ('ro') que pode ser clicável (picker=5)
        self.cid = self.point.figure.canvas.mpl_connect('button_press_event', self.on_click)  # Conecta o evento de clicar
        self.cid_move = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_drag)  # Conecta o evento de mover
        self.cid_release = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)  # Conecta o evento de soltar
        self.dragging = False  # Variável para verificar se o ponto está sendo arrastado

    def on_click(self, event):
        # Verifica se o clique ocorreu no eixo onde o ponto está
        if event.inaxes == self.point.axes:
            # Use o método contains com um objeto MouseEvent
            contains, _ = self.point.contains(event)  # Mudança aqui
            if contains:
                self.dragging = True  # Inicia o arrasto se o ponto foi clicado

    def on_drag(self, event):
        # Se está arrastando, atualiza a posição do ponto
        if self.dragging:
            self.x = event.xdata  # Atualiza a coordenada x
            self.y = event.ydata  # Atualiza a coordenada y
            self.point.set_data([self.x], [self.y])  # Atualiza as coordenadas do ponto (utiliza listas)
            self.point.figure.canvas.draw()  # Atualiza a figura para refletir a nova posição

    def on_release(self, event):
        # Finaliza o arrasto quando o botão é solto
        self.dragging = False

class App:
    def __init__(self, root):
        self.root = root  # Inicializa a janela principal
        self.root.title("Gráfico com Arrasta e Solta")  # Título da janela
        
        self.fig, self.ax = plt.subplots(figsize=(5, 5))  # Cria a figura e o eixo
        self.ax.set_xlim(0, 10)  # Define os limites do eixo x
        self.ax.set_ylim(0, 10)  # Define os limites do eixo y
        
        # Cria um ponto arrastável
        self.point = DraggablePoint(self.ax, 5, 5)  # Ponto inicial na posição (5, 5)
        
        # Conecta a figura ao tkinter para exibição
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Ajusta o canvas para preencher a janela
        
        self.canvas.draw()  # Desenha a figura na tela

if __name__ == "__main__":
    # Inicializa a aplicação
    root = tk.Tk()  # Cria a janela principal
    app = App(root)  # Inicia a aplicação
    root.mainloop()  # Inicia o loop principal do tkinter