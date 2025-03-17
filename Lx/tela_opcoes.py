from imports import *

################# criando janela ###############
class Opcoes_Modulos():
    def opcoes_modulos(self, event):
        self.janela_opcoes = customtkinter.CTk()
        self.janela_opcoes.title('Opções')
        self.janela_opcoes.geometry("300x50")
        self.janela_opcoes.resizable(True, True)
        
        self.frame_opcoes(self.janela_opcoes)
        
        self.janela_opcoes.mainloop()
    
    def button_modulo_new(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Drop down button
        self.fr_comboModulos = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_comboModulos.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_comboModulos = customtkinter.CTkLabel(self.fr_comboModulos, text="Modulos")
        self.lb_comboModulos.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)
        self.comboModulos = ttk.Combobox(self.fr_comboModulos, values=["Simulador", "Pesquisa Mercado", "Google Maps"])
        self.comboModulos.place(relx=0, rely=0,relwidth=0.98, relheight=0.98)
       
        def callbackFunc(event):
            self.modulo = self.comboModulos.get()
            if self.modulo == 'Simulador':
                selected_item = self.list_g.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.list_g.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.list_g.item(selected_item, 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
                    UF = values[6]
                    Cidade = values[5]
                    Tipo = values[3]
                    Nome_da_Area = values[4]
                    self.janela_opcoes.destroy()
                    if hasattr(self, 'janela_simulador_rel') and self.janela_simulador_rel is not None and self.janela_simulador_rel.winfo_exists():
                        self.janela_simulador_rel.destroy()
                        self.janela_simulador_rel = None  # Initialize the attribute

                    # self.window_one.iconify() # Minimizar a tela
                    self.simulador_estudos_rel(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
            
            elif self.modulo == 'Pesquisa Mercado':
                self.janela_opcoes.destroy()
                messagebox.showinfo("Informação", "Em Manutenção!!")

            elif self.modulo == 'Google Maps':
                selected_item = self.list_g.selection()
                if selected_item:
                    # Texto do item selecionado
                    item_text = self.list_g.item(self.list_g.selection(), 'text')
                    # Obtém os valores associados (como uma tupla)
                    values = self.list_g.item(self.list_g.selection(), 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
                    UF = values[6]
                    Cidade = values[5]
                    Tipo = values[3]
                    Nome_da_Area = values[4]
                    self.janela_opcoes.destroy()
                    
                    self.lista_negocio = self.Consulta_Negocio(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
                    if self.lista_negocio[0].get('Http') != '':
                        url = self.lista_negocio[0].get('Http')
                    else:
                        messagebox.showwarning("Maps", "Coordenadas Não Cadastrada!!!")
                        return
                    
                    url = url.strip()  # Remove espaços em branco no início e no fim
                    webbrowser.open(url)
            
        self.comboModulos.bind("<<ComboboxSelected>>", callbackFunc)
        
    def frame_opcoes(self, janela):
        # Opções
        coordenadas_relx = 0.01
        coordenadas_rely = 0.05
        coordenadas_relwidth = 0.98
        coordenadas_relheight = 0.85
        self.modulo = self.button_modulo_new(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)

Opcoes_Modulos()