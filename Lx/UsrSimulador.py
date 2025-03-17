from imports import *
from widgets import Widgets
from PIL import ImageTk, Image



################# criando janela ###############
class Simulador_Estudos(Widgets, Consultas, Limpeza, Formatos, Formularios, Functions, Gravar):
    def simulador_estudos(self):
        self.window_one.title('Simulador de Estudos de Negócios')
        self.clearFrame_principal()
        self.frame_dados(self.principal_frame)
        self.frame_novosnegocios(self.principal_frame)

    def frame_dados(self, janela):
        # Empresa
        coordenadas_relx = 0
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.34
        coordenadas_relheight = 0.07
        self.frame_empresa(janela, coordenadas_relx, coordenadas_rely,
                           coordenadas_relwidth, coordenadas_relheight)
        
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_uf))
        
        # Estado
        coordenadas_relx = 0.34
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        self.frame_uf(janela, coordenadas_relx, coordenadas_rely,coordenadas_relwidth, coordenadas_relheight)
        self.combo_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_municipio))

        # Municipio
        coordenadas_relx = 0.40
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        self.frame_municipio(janela, coordenadas_relx, coordenadas_rely,
                             coordenadas_relwidth, coordenadas_relheight)
        
        self.combo_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpo_projeto))

        # Tipo do Projeto
        coordenadas_relx=0.60
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        fr_tpo_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_tpo_projeto = customtkinter.CTkLabel(fr_tpo_projeto, text="Tipo do Projeto")
        lb_tpo_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        tpo_projeto = self.get_tpo_projetos()
        tpo_projeto = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in tpo_projeto]

        self.entry_tpo_projeto = AutocompleteCombobox(fr_tpo_projeto, width=30, font=('Times', 11), completevalues=tpo_projeto)
        self.entry_tpo_projeto.pack()
        self.entry_tpo_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_tpo_projeto.bind("<Button-1>", lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind('<Down>', lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_cenario))


        # Nome do Projeto
        coordenadas_relx = 0.80
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.15
        coordenadas_relheight = 0.07
        self.frame_nome_projeto(janela, coordenadas_relx, coordenadas_rely,
                                coordenadas_relwidth, coordenadas_relheight)
        # self.lista = []
        self.entry_nome_cenario.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_area_total))

        # Icon de Consulta
        coordenadas_relx = 0.95
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.05
        coordenadas_relheight = 0.07
        # self.icon_image = self.load_icon('consultar', size=(64, 64))  # Armazena a imagem
        self.btn_consultar = customtkinter.CTkButton(
                                                    janela,  
                                                    text='Consultar', 
                                                    fg_color='transparent', 
                                                    command=lambda: [self.button_consultar_simulacao(
                                                                                                    self.obter_Empresa_ID(self.combo_empresa.get()), 
                                                                                                    self.combo_uf.get(), 
                                                                                                    self.combo_municipio.get(), 
                                                                                                    self.combo_tpo_projeto.get(),
                                                                                                    self.entry_nome_cenario.get(),
                                                                                                    self.combo_empresa, 
                                                                                                    self.combo_uf, 
                                                                                                    self.combo_municipio, 
                                                                                                    self.combo_tpo_projeto,
                                                                                                    self.entry_nome_cenario
                                                                                                    )]
                                                        )
        
        self.btn_consultar.pack()
        self.btn_consultar.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.btn_consultar.bind("<Return>", lambda event: self.btn_consultar.invoke())
        
        # Icon Processar
        coordenadas_relx = 0.90
        coordenadas_rely = 0.90
        coordenadas_relwidth = 0.10
        coordenadas_relheight = 0.07
        self.btn_consultar = customtkinter.CTkButton(
                                                    janela, 
                                                    text='Processar',
                                                    fg_color='transparent', 
                                                    command=lambda: [self.Fluxo_Caixa(
                                                                                    self.obter_Empresa_ID(self.combo_empresa.get()), 
                                                                                    self.combo_uf.get(), 
                                                                                    self.combo_municipio.get(), 
                                                                                    self.entry_tpo_projeto.get(),
                                                                                    self.entry_nome_cenario.get(),
                                                                                    self.window_one 
                                                                                    )
                                                                    ]
                                                    ) 
        # self.btn_consultar = customtkinter.CTkButton(janela, image=self.load_icon(tipo, size=(64, 64)), text='',fg_color='transparent', command=self.Fluxo_Caixa)  # Tamanho desejado
        self.btn_consultar.pack()
        self.btn_consultar.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)

Simulador_Estudos()
