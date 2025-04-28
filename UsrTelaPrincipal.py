from imports import *

################# criando janela ###############
class Tela_Principal():
    def tela_principal(self):
        self.window_one.title('Gestor de Negócios')
        self.frame_cabecalho_tela_principal(self.window_one)

################# dividindo a janela ###############
    
    def frame_cabecalho_tela_principal(self, janela):
        # Adicionando um espaço para permitir que outros widgets fiquem acima (se houver)
        spacer = ctk.CTkLabel(self.principal_frame, text="")
        spacer.pack(expand=True)
        
        # Criando o label para a versão do aplicativo
        lb_version = ctk.CTkLabel(self.principal_frame, text="Versão: 1.0.0", text_color='white')
        lb_version.pack(side="bottom", pady=(5, 0), padx=10, fill="x")  # Posicionando no rodapé

        # Criando o label para o copyright
        lb_copyright = ctk.CTkLabel(self.principal_frame, text="Feito por FullHouse Serviços em Tecnologia - Todos os direitos reservados", text_color='white')
        lb_copyright.pack(side="bottom", pady=(0, 10), padx=10, fill="x")  # Posicionando no rodapé

        

    