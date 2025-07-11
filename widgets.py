from imports import *
from PIL import ImageTk, Image

################# criando janela ###############

class Widgets(Consultas, Limpeza, Formatos, Formularios, Functions, Gravar, Atualizar_Combo):
    # Frames Padrão

    def frame_empresa(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Empresa
        self.fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_empresa = customtkinter.CTkLabel(self.fr_empresa, text="Empresa")
        self.lb_empresa.place(relx=0.225, rely=0, relheight=0.25, relwidth=0.55)

        self.empresas = []
        self.empresas = [empresa[1] for empresa in self.empresas]

        self.combo_empresa = AutocompleteCombobox(self.fr_empresa, width=30, font=('Times', 11), completevalues=self.empresas)
        self.combo_empresa.pack()
        self.combo_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.combo_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.combo_empresa))
        self.combo_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.combo_empresa))

    def frame_Unidade_Negocio(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Unidade de Negócio
        self.fr_unidade_negocio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_unidade_negocio.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_unidade_negocio = customtkinter.CTkLabel(self.fr_unidade_negocio, text="Unidade Negócios")
        self.lb_unidade_negocio.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.unidade_negocios = []
        self.combo_unidade_negocio = AutocompleteCombobox(self.fr_unidade_negocio, width=30, font=('Times', 11), completevalues=self.unidade_negocios)
        self.combo_unidade_negocio.pack()
        self.combo_unidade_negocio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.combo_unidade_negocio.bind("<Button-1>", lambda event: self.atualizar_unidade_negocios(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela), self.combo_unidade_negocio))
        self.combo_unidade_negocio.bind('<Down>', lambda event: self.atualizar_unidade_negocios(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela), self.combo_unidade_negocio))

    def frame_pessoa(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Pessoa
        self.fr_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_pessoa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_pessoa = customtkinter.CTkLabel(self.fr_pessoa, text="Cliente/Fornecedor/Prestador Serviços")
        self.lb_pessoa.place(relx=0.225, rely=0, relheight=0.25, relwidth=0.55)

        self.pessoas = []
        self.combo_pessoa = AutocompleteCombobox(self.fr_pessoa, width=30, font=('Times', 11), completevalues=self.pessoas)
        self.combo_pessoa.pack()
        self.combo_pessoa.place(relx=0.01, rely=0.5, relwidth=0.89, relheight=0.4)
        self.combo_pessoa.bind("<Button-1>", lambda event:  self.atualizar_pessoa(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela),self.combo_pessoa))
        self.combo_pessoa.bind('<Down>', lambda event:  self.atualizar_pessoa(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela), self.combo_pessoa))

    def frame_uf(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Estado
        self.fr_uf = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_uf.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_estado = customtkinter.CTkLabel(self.fr_uf, text="UF")
        self.lb_estado.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.uf = self.get_uf()
        self.combo_uf = AutocompleteCombobox(self.fr_uf, width=30, font=('Times', 11), completevalues=self.uf)
        self.combo_uf.pack()
        self.combo_uf.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

    def frame_municipio(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Municipio
        self.fr_municipio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_municipio.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_municipio = customtkinter.CTkLabel(self.fr_municipio, text="Município")
        self.lb_municipio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        self.municipios = []
        self.combo_municipio = AutocompleteCombobox(self.fr_municipio, width=30, font=('Times', 11), completevalues=self.municipios)
        self.combo_municipio.pack()
        self.combo_municipio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.combo_municipio.bind("<Button-1>", lambda event: self.atualizar_municipio(event, self.combo_uf.get(), self.combo_municipio))
        self.combo_municipio.bind('<Down>', lambda event: self.atualizar_municipio(event, self.combo_uf.get(), self.combo_municipio))

    def frame_tpo_projeto(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Tipo do Projeto
        self.fr_tpo_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_tpo_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_tpo_projeto = customtkinter.CTkLabel(self.fr_tpo_projeto, text="Tipo do Projeto")
        self.lb_tpo_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        self.tpo_projeto = self.get_tpo_projetos()
        self.tpo_projeto_dict = {nome: id for id, nome, imposto in self.tpo_projeto}
        self.impostos = 0
        self.tpo_projeto = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in self.tpo_projeto]

        self.combo_tpo_projeto = AutocompleteCombobox(self.fr_tpo_projeto, width=30, font=('Times', 11), completevalues=self.tpo_projeto)
        self.combo_tpo_projeto.pack()
        self.combo_tpo_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.combo_tpo_projeto.bind("<Button-1>", lambda event: self.atualizar_tpo_projeto(event, self.combo_tpo_projeto))
        self.combo_tpo_projeto.bind('<Down>', lambda event: self.atualizar_tpo_projeto(event, self.combo_tpo_projeto))
    
    def frame_nome_projeto(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Nome do Projeto
        self.fr_nome_cenario = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_nome_cenario.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_nome_cenario = customtkinter.CTkLabel(self.fr_nome_cenario, text="Nome do Cenário")
        self.lb_nome_cenario.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        nome_cenario = []
        self.entry_nome_cenario = AutocompleteCombobox(self.fr_nome_cenario, width=30, font=('Times', 11), completevalues=nome_cenario)
        self.entry_nome_cenario.pack()
        self.entry_nome_cenario.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)
        self.entry_nome_cenario.bind("<Button-1>", lambda event: 
                                                                self.atualizar_nome_cenario(event,
                                                                self.obter_Empresa_ID(self.combo_empresa.get(), janela), 
                                                                self.combo_municipio.get(), 
                                                                self.combo_uf.get(), 
                                                                self.combo_tpo_projeto.get(), 
                                                                self.entry_nome_cenario))
        self.entry_nome_cenario.bind('<Down>', lambda event: 
                                                                self.atualizar_nome_cenario(event,
                                                                self.obter_Empresa_ID(self.combo_empresa.get(), janela), 
                                                                self.combo_municipio.get(), 
                                                                self.combo_uf.get(), 
                                                                self.combo_tpo_projeto.get(), 
                                                                self.entry_nome_cenario))
    
    def fram_status(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Status
        self.fr_status = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_status.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_status_fr = customtkinter.CTkLabel(self.fr_status, text="Status do Estudo")
        self.lb_status_fr.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        status = []
        self.combo_status = AutocompleteCombobox(self.fr_status, width=30, font=('Times', 11), completevalues=status)
        self.combo_status.pack()
        self.combo_status.place(relx=0.01, rely=0.5,relwidth=0.98, relheight=0.4)
        self.combo_status.bind("<Button-1>", lambda event: self.atualizar_status(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela), self.combo_status))
        self.combo_status.bind('<Down>', lambda event: self.atualizar_status(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela), self.combo_status))
    
    def fram_frete(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight):
        # Frete
        self.fr_frete = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_frete.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.lb_frete_fr = customtkinter.CTkLabel(self.fr_frete, text="Frete")
        self.lb_frete_fr.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.frete = []
        self.frete = self.get_frete() 
        self.frete_dict = {nome: id for id, nome in self.frete}
        self.frete_dict_1 = {id: nome for id, nome in self.frete}
        self.frete = [frete[1] for frete in self.frete]

        self.combo_frete = AutocompleteCombobox(self.fr_frete, width=30, font=('Times', 11), completevalues=self.frete)
        self.combo_frete.set('Sem ocorrência de transporte')
        self.combo_frete.pack()
        self.combo_frete.place(relx=0.01, rely=0.5,relwidth=0.98, relheight=0.4)
        self.combo_frete.bind("<Button-1>", lambda event: self.atualizar_frete(event, self.combo_frete))
        self.combo_frete.bind('<Down>', lambda event: self.atualizar_frete(event, self.combo_frete))


