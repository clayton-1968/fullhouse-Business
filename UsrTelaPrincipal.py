from imports import *

################# criando janela ###############
class Tela_Principal():
    def tela_principal(self):
        self.window_one.title('Gestor de Negócios')
        self.frame_cabecalho_tela_principal(self.window_one)

################# dividindo a janela ###############
    
    def frame_cabecalho_tela_principal(self, janela):
        self.clearFrame_principal()

        # Criando um frame para conter a logo e as informações
        content_frame = ctk.CTkFrame(self.principal_frame, fg_color="transparent")
        content_frame.pack(expand=True, fill="both")
        
        # Exibindo a logo
        icon_image = self.base64_to_photoimage('logo')
        logo_label = ctk.CTkLabel(content_frame, image=icon_image, text="")
        logo_label.pack(pady=(50, 20))
        
        # Adicionando o título do aplicativo
        title_label = ctk.CTkLabel(content_frame, text="Gestor de Negócios", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=(0, 40))
        
        # Criando o label para a versão do aplicativo
        lb_version = ctk.CTkLabel(self.principal_frame, text=f"Versão: {self.versao_ds}", text_color='white')
        lb_version.pack(side="bottom", pady=(5, 0), padx=10, fill="x")  # Posicionando no rodapé

        # Criando o label para o copyright
        lb_copyright = ctk.CTkLabel(self.principal_frame, text="Feito por FullHouse Serviços em Tecnologia - Todos os direitos reservados", text_color='white')
        lb_copyright.pack(side="bottom", pady=(0, 10), padx=10, fill="x")  # Posicionando no rodapé

        

    