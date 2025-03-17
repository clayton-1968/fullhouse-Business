from imports import *
from widgets import Widgets
################# criando janela ###############
class Simulador_Maps(Widgets):
    def simulador_maps(self):
        self.janela_maps = customtkinter.CTk()
        self.janela_maps.title('Maps Estudos de Negócios')
        self.janela_maps.geometry("1124x760+0+0")
        self.janela_maps.resizable(True, True)
        
        self.frame_maps(self.janela_maps)
        # self.frame_novosnegocios(self.janela_maps)

        self.janela_maps.focus_force()
        self.janela_maps.grab_set()
        self.janela_maps.mainloop()

    def frame_maps(self, janela):
        url = self.lista[0].get('Http')
        if not url:  # Verifica se a string está vazia após a remoção dos espaços em branco
            messagebox.showerror("Erro", "Por favor, ajuste o endereço do maps.")
            return        
        url = url.strip()  # Remove espaços em branco no início e no fim
        webbrowser.open(url)

Simulador_Maps()