from imports import *
from PIL import ImageTk, Image

################# criando janela ###############
# Cadastro de Fornecedores e Clientes
class Pessoas(Icons, Functions):

    def cad_pessoas(self):
        
        self.janela_cadastro_pessoas = customtkinter.CTkToplevel(self.window_one)
        self.janela_cadastro_pessoas.title('Cadastro de Clientes e Fornecedores')
        self.janela_cadastro_pessoas.geometry("1680x800")
        self.janela_cadastro_pessoas.resizable(True, True)
        self.janela_cadastro_pessoas.lift()  # Traz a janela para frente   

        self.frame_cad_principal = customtkinter.CTkFrame(self.janela_cadastro_pessoas, fg_color='black')  # Frame Principal para cadastro
        self.frame_cad_principal.pack(pady=10, padx=10, fill="both", expand=True)
        customtkinter.CTkLabel(self.frame_cad_principal, text="", font=("Roboto", 30, "bold")).pack(pady=10)
        
        self.frame_cad_treeview = customtkinter.CTkFrame(self.frame_cad_principal, fg_color='black')  # Frame Principal para cadastro
        # self.frame_cad_treeview.pack(pady=1, padx=1, fill="both", expand=True)
        self.frame_cad_treeview.place(relx= 0.005, rely=0.31, relwidth=.99, relheight=0.69)
        customtkinter.CTkLabel(self.frame_cad_treeview, text="", font=("Roboto", 30, "bold")).pack(pady=10)
        
       # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_cadastro_pessoas.protocol("WM_DELETE_WINDOW", lambda:  self.on_closing_tela(self.janela_cadastro_pessoas))

        self.images_base64()

        self.frame_cad_empresa(self.frame_cad_principal)
        self.frame_cad_linha_1(self.frame_cad_principal)
        self.frame_cad_linha_2(self.frame_cad_principal)
        self.frame_cad_linha_3(self.frame_cad_principal)
        self.frame_cad_linha_4(self.frame_cad_treeview)
        
        self.janela_cadastro_pessoas.focus_force()
        self.janela_cadastro_pessoas.grab_set()
        # self.janela_cadastro_pessoas.mainloop()
    
    def frame_cad_empresa(self, janela):
        # Empresa
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx= 0.005, rely=0.01, relwidth=0.34, relheight=0.07)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []
        empresas = [empresa[1] for empresa in empresas]

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tipo_pessoa))  
    
    def frame_cad_linha_1(self, janela):
        # Tipo CPF ou CNPJ
        fr_tipo_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tipo_pessoa.place(relx=0.005, rely=0.085, relwidth=0.04, relheight=0.07)

        lb_tipo_pessoa = customtkinter.CTkLabel(fr_tipo_pessoa, text="Tipo")
        lb_tipo_pessoa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.opcoes = ['J', 'F']
        self.entry_tipo_pessoa = customtkinter.CTkComboBox(fr_tipo_pessoa, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_tipo_pessoa.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)
        self.entry_tipo_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_cpf_cpj_pessoa))

        # CPF ou CNPJ
        fr_cpf_cpj_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_cpf_cpj_pessoa.place(relx=0.05, rely=0.085, relwidth=0.10, relheight=0.07)

        lb_cpf_cpj_pessoa = customtkinter.CTkLabel(fr_cpf_cpj_pessoa, text="CPF/CNPJ")
        lb_cpf_cpj_pessoa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_cpf_cpj_pessoa = customtkinter.CTkEntry(fr_cpf_cpj_pessoa, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_cpf_cpj_pessoa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_cpf_cpj_pessoa.bind("<KeyRelease>", lambda event: self.format_cpf_cnpj(event, self.entry_cpf_cpj_pessoa, self.entry_tipo_pessoa))
        self.entry_cpf_cpj_pessoa.bind("<Return>", lambda event: self.checar_cpf_cnpj(event, self.entry_cpf_cpj_pessoa, self.entry_tipo_pessoa, self.entry_nome_pessoa))  
        
        # Nome do Cadastrado
        fr_nome_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_pessoa.place(relx=0.155, rely=0.085, relwidth=0.255, relheight=0.07)

        lb_nome_pessoa = customtkinter.CTkLabel(fr_nome_pessoa, text="Nome")
        lb_nome_pessoa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_nome_pessoa = customtkinter.CTkEntry(fr_nome_pessoa, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_nome_pessoa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_nome_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_proprietario))

        # Proprietário (S/N)
        fr_tipo_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tipo_pessoa.place(relx=0.415, rely=0.085, relwidth=0.04, relheight=0.07)

        lb_tipo_pessoa = customtkinter.CTkLabel(fr_tipo_pessoa, text="Tipo")
        lb_tipo_pessoa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.opcoes = ['N', 'S']
        self.entry_proprietario = customtkinter.CTkComboBox(fr_tipo_pessoa, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_proprietario.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)
        self.entry_proprietario.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_banco))     
    
        # Banco
        fr_banco = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_banco.place(relx=0.46, rely=0.085, relwidth=0.10, relheight=0.07)

        lb_banco = customtkinter.CTkLabel(fr_banco, text="Banco")
        lb_banco.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.bancos = []
        self.entry_banco = AutocompleteCombobox(fr_banco, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.bancos)
        self.entry_banco.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_banco.bind("<Button-1>", lambda event: self.atualizar_bancos(event, self.entry_banco))
        self.entry_banco.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia))

        # Agencia
        fr_agencia = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_agencia.place(relx=0.565, rely=0.085, relwidth=0.14, relheight=0.07)

        lb_agencia = customtkinter.CTkLabel(fr_agencia, text="Agência")
        lb_agencia.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_agencia = customtkinter.CTkEntry(fr_agencia, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_agencia.place(relx=0.01, rely=0.5, relwidth=0.80, relheight=0.4)
        self.entry_agencia.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia_dv))

        self.entry_agencia_dv = customtkinter.CTkEntry(fr_agencia, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_agencia_dv.place(relx=0.81, rely=0.5, relwidth=0.16, relheight=0.4)
        self.entry_agencia_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Conta Corrente
        fr_contacorrente = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_contacorrente.place(relx=0.71, rely=0.085, relwidth=0.14, relheight=0.07)

        lb_contacorrente = customtkinter.CTkLabel(fr_contacorrente, text="Conta Corrente")
        lb_contacorrente.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_contacorrente = customtkinter.CTkEntry(fr_contacorrente, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_contacorrente.place(relx=0.01, rely=0.5, relwidth=0.80, relheight=0.4)
        self.entry_contacorrente.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente_dv))

        self.entry_contacorrente_dv = customtkinter.CTkEntry(fr_contacorrente, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_contacorrente_dv.place(relx=0.81, rely=0.5, relwidth=0.16, relheight=0.4)
        self.entry_contacorrente_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_chave_pix))

        # Chave Pix
        fr_chave_pix = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_chave_pix.place(relx=0.855, rely=0.085, relwidth=0.14, relheight=0.07)

        lb_chave_pix = customtkinter.CTkLabel(fr_chave_pix, text="Chave Pix")
        lb_chave_pix.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_chave_pix = customtkinter.CTkEntry(fr_chave_pix, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_chave_pix.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_chave_pix.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_cep))

    def frame_cad_linha_2(self, janela):
        # CEP
        fr_cep = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_cep.place(relx=0.005, rely=0.16, relwidth=0.08, relheight=0.07)

        lb_cep = customtkinter.CTkLabel(fr_cep, text="CEP")
        lb_cep.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_cep = customtkinter.CTkEntry(fr_cep, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_cep.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_cep.bind("<Return>", lambda event: self.formatar_cep(event, 
                                                                        self.entry_cep, 
                                                                        self.entry_endereco, 
                                                                        self.entry_endereco_bairro, 
                                                                        self.entry_uf, 
                                                                        self.entry_municipio))
    
        # Estado
        self.fr_uf = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_uf.place(relx=0.09, rely=0.16, relwidth=0.04, relheight=0.07)
        self.lb_estado = customtkinter.CTkLabel(self.fr_uf, text="UF")
        self.lb_estado.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        self.uf = self.get_uf()
        self.entry_uf = AutocompleteCombobox(self.fr_uf, width=30, font=('Times', 11), completevalues=self.uf)
        self.entry_uf.pack()
        self.entry_uf.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_municipio))

        # Municipio
        fr_municipio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_municipio.place(relx=0.135, rely=0.16, relwidth=0.14, relheight=0.07)

        lb_municipio = customtkinter.CTkLabel(fr_municipio, text="Município")
        lb_municipio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.municipios = []
        self.entry_municipio = AutocompleteCombobox(fr_municipio, width=30, font=('Times', 11), completevalues=self.municipios)
        self.entry_municipio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_municipio.bind("<Button-1>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind('<Down>', lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_endereco))

        # Endereço
        fr_endereco = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_endereco.place(relx=0.28, rely=0.16, relwidth=0.38, relheight=0.07)

        lb_endereco = customtkinter.CTkLabel(fr_endereco, text="Endereço")
        lb_endereco.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_endereco = customtkinter.CTkEntry(fr_endereco, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_endereco.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_endereco.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_endereco_nr))

        # Nr do Endereço
        fr_endereco_nr = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_endereco_nr.place(relx=0.665, rely=0.16, relwidth=0.07, relheight=0.07)

        lb_endereco_nr = customtkinter.CTkLabel(fr_endereco_nr, text="Nr.")
        lb_endereco_nr.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_endereco_nr = customtkinter.CTkEntry(fr_endereco_nr, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_endereco_nr.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_endereco_nr.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_endereco_complemento))

        # Complemento endereço
        fr_endereco_complemento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_endereco_complemento.place(relx=0.74, rely=0.16, relwidth=0.14, relheight=0.07)

        lb_endereco_complemento = customtkinter.CTkLabel(fr_endereco_complemento, text="Compl.")
        lb_endereco_complemento.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_endereco_complemento = customtkinter.CTkEntry(fr_endereco_complemento, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_endereco_complemento.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_endereco_complemento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_endereco_bairro))

        # Bairro
        fr_endereco_bairro = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_endereco_bairro.place(relx=0.885, rely=0.16, relwidth=0.11, relheight=0.07)

        lb_endereco_bairro = customtkinter.CTkLabel(fr_endereco_bairro, text="Bairro")
        lb_endereco_bairro.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_endereco_bairro = customtkinter.CTkEntry(fr_endereco_bairro, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_endereco_bairro.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_endereco_bairro.bind("<Return>", lambda event: self.muda_barrinha(event,  self.entry_incricao_municipal))

        # Botão Consultar
        bt_consultar_pessoa = customtkinter.CTkButton(janela, image=self.btconsulta_img, text='', command=self.consulta_pessoas) 
        bt_consultar_pessoa.place(relx=0.915, rely=0.01, relwidth=0.03, relheight=0.04)

        # Botão Salvar
        bt_salvar_pessoa = customtkinter.CTkButton(janela, image=self.btsave_img, text='', command=self.gravar_pessoas) 
        bt_salvar_pessoa.place(relx=0.955, rely=0.01, relwidth=0.03, relheight=0.04)

    def frame_cad_linha_3(self, janela):
        # Inscrição Municipal
        fr_incricao_municipal = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_incricao_municipal.place(relx=0.005, rely=0.235, relwidth=0.14, relheight=0.07)

        lb_incricao_municipal = customtkinter.CTkLabel(fr_incricao_municipal, text="Inscrição Municipal")
        lb_incricao_municipal.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_incricao_municipal = customtkinter.CTkEntry(fr_incricao_municipal, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_incricao_municipal.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_incricao_municipal.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_incricao_estadual))

        # Inscrição Estadual
        fr_incricao_estadual = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_incricao_estadual.place(relx=0.15, rely=0.235, relwidth=0.14, relheight=0.07)

        lb_incricao_estadual = customtkinter.CTkLabel(fr_incricao_estadual, text="Inscrição Estadual")
        lb_incricao_estadual.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_incricao_estadual = customtkinter.CTkEntry(fr_incricao_estadual, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_incricao_estadual.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_incricao_estadual.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_suframa))

        # Suframa
        fr_suframa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_suframa.place(relx=0.295, rely=0.235, relwidth=0.14, relheight=0.07)

        lb_suframa = customtkinter.CTkLabel(fr_suframa, text="Suframa")
        lb_suframa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_suframa = customtkinter.CTkEntry(fr_suframa, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_suframa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_suframa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_telefone))

        # Telefone Fixo
        fr_telefone = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_telefone.place(relx=0.44, rely=0.235, relwidth=0.14, relheight=0.07)

        lb_telefone = customtkinter.CTkLabel(fr_telefone, text="Telefone Fixo")
        lb_telefone.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_telefone = customtkinter.CTkEntry(fr_telefone, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_telefone.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_telefone.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_celular_whatsapp))

        # Celular/WhatsApp
        fr_celular_whatsapp = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_celular_whatsapp.place(relx=0.585, rely=0.235, relwidth=0.14, relheight=0.07)

        lb_celular_whatsapp = customtkinter.CTkLabel(fr_celular_whatsapp, text="Celular/WhatsApp")
        lb_celular_whatsapp.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_celular_whatsapp = customtkinter.CTkEntry(fr_celular_whatsapp, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_celular_whatsapp.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_celular_whatsapp.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_email))

        # Email
        fr_email = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_email.place(relx=0.73, rely=0.235, relwidth=0.265, relheight=0.07)

        lb_email = customtkinter.CTkLabel(fr_email, text="Email")
        lb_email.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_email = customtkinter.CTkEntry(fr_email, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_email.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_email.bind("<Return>", lambda event: self.check_email(event, self.entry_email))
        self.entry_email.bind("<Return>", lambda event: self.muda_barrinha(event, self.bt_pag_salvar_pessoa))

    def frame_cad_linha_4(self, janela):
        # Widgets - Listar Itens
        self.LItens_cadastro_pessoas = ttk.Treeview(janela, height=12, column=('Tpo', 'CpF_CnPj', 'Descricao', 'Banco', 'Agencia', 'Agencia_D', 
                                                              'Conta', 'Conta_D', 'Pix', 'Proprietario_sn', 'Endereco', 'Endereco_Nr',
                                                              'Endereco_Bairro', 'Endereco_Compl', 'Endereco_UF', 'IbGe', 'Endereco_Cidade',
                                                              'CeP', 'Insc_Estadual', 'Insc_Municipal', 'Insc_Suframa', 'Telefone_fixo',
                                                              'WhatsApp', 'Email'), show='headings')
        
       
        self.LItens_cadastro_pessoas.heading('Tpo', text="T")
        self.LItens_cadastro_pessoas.column('Tpo', width=5, anchor='c')
        self.LItens_cadastro_pessoas.heading('CpF_CnPj', text="CPf/CnPj")
        self.LItens_cadastro_pessoas.column('CpF_CnPj', width=80, anchor='w')
        self.LItens_cadastro_pessoas.heading('Descricao', text="Descrição")
        self.LItens_cadastro_pessoas.column('Descricao', width=250, anchor='w')
        self.LItens_cadastro_pessoas.heading('Banco', text="Banco")
        self.LItens_cadastro_pessoas.column('Banco', width=80, anchor='w')
        self.LItens_cadastro_pessoas.heading('Agencia', text="Agência")
        self.LItens_cadastro_pessoas.column('Agencia', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Agencia_D', text="D")
        self.LItens_cadastro_pessoas.column('Agencia_D', width=5, anchor='e')
        self.LItens_cadastro_pessoas.heading('Conta', text="Conta")
        self.LItens_cadastro_pessoas.column('Conta', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Conta_D', text="D")
        self.LItens_cadastro_pessoas.column('Conta_D', width=5, anchor='e')
        self.LItens_cadastro_pessoas.heading('Pix', text="Pix")
        self.LItens_cadastro_pessoas.column('Pix', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Proprietario_sn', text="Propr.")
        self.LItens_cadastro_pessoas.column('Proprietario_sn', width=5, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco', text="Endereço")
        self.LItens_cadastro_pessoas.column('Endereco', width=100, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Nr', text="Nr")
        self.LItens_cadastro_pessoas.column('Endereco_Nr', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Bairro', text="Bairro")
        self.LItens_cadastro_pessoas.column('Endereco_Bairro', width=100, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Compl', text="Complemento")
        self.LItens_cadastro_pessoas.column('Endereco_Compl', width=100, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_UF', text="UF")
        self.LItens_cadastro_pessoas.column('Endereco_UF', width=50, anchor='e')
        self.LItens_cadastro_pessoas.heading('IbGe', text="IBGE")
        self.LItens_cadastro_pessoas.column('IbGe', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Cidade', text="Município")
        self.LItens_cadastro_pessoas.column('Endereco_Cidade', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('CeP', text="CEP")
        self.LItens_cadastro_pessoas.column('CeP', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Insc_Estadual', text="Insc. Estadual")
        self.LItens_cadastro_pessoas.column('Insc_Estadual', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Insc_Municipal', text="Insc. Municipal")
        self.LItens_cadastro_pessoas.column('Insc_Municipal', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Insc_Suframa', text="Suframa")
        self.LItens_cadastro_pessoas.column('Insc_Suframa', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Telefone_fixo', text="Telefone")
        self.LItens_cadastro_pessoas.column('Telefone_fixo', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('WhatsApp', text="WhatsApp")
        self.LItens_cadastro_pessoas.column('WhatsApp', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Email', text="WhatsApp")
        self.LItens_cadastro_pessoas.column('Email', width=80, anchor='e')

        self.LItens_cadastro_pessoas.place(relx=0, rely=0.01, relwidth=1, relheight=0.985)
        # self.LItens.bind("<Double-1>", self.OnDoubleClick)
        self.entry_tipo_lcto_descr.focus()
        self.limpar_campos_lcto()

Pessoas()

# Cadastro de Produtos
class Produtos(Icons, Functions):

    def cad_produtos(self):
        
        self.janela_cadastro_produtos = customtkinter.CTkToplevel(self.window_one)
        self.janela_cadastro_produtos.title('Cadastro de Produtos')
        self.janela_cadastro_produtos.geometry("1680x800")
        self.janela_cadastro_produtos.resizable(True, True)
        self.janela_cadastro_produtos.lift()  # Traz a janela para frente   

        self.frame_produtos_principal = customtkinter.CTkFrame(self.janela_cadastro_produtos, fg_color='black')  # Frame Principal para cadastro
        self.frame_produtos_principal.pack(pady=10, padx=10, fill="both", expand=True)
        customtkinter.CTkLabel(self.frame_produtos_principal, text="", font=("Roboto", 30, "bold")).pack(pady=10)
        
        self.frame_cad_produtos_treeview = customtkinter.CTkFrame(self.frame_produtos_principal, fg_color='black')  # Frame Principal para cadastro
        self.frame_cad_produtos_treeview.place(relx= 0.005, rely=0.085, relwidth=.99, relheight=0.91)
        customtkinter.CTkLabel(self.frame_cad_produtos_treeview, text="", font=("Roboto", 30, "bold")).pack(pady=10)
         
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_cadastro_produtos.protocol("WM_DELETE_WINDOW", lambda:  self.on_closing_tela(self.janela_cadastro_produtos))

        self.images_base64()

        self.frame_produto_linha_1(self.frame_produtos_principal)
        self.frame_produto_linha_2(self.frame_cad_produtos_treeview)

        self.janela_cadastro_produtos.focus_force()
        self.janela_cadastro_produtos.grab_set()
        # self.janela_cadastro_produtos.mainloop()
    
    def frame_produto_linha_1(self, janela):
        # Empresa
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx= 0.005, rely=0.01, relwidth=0.30, relheight=0.07)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []
        empresas = [empresa[1] for empresa in empresas]
        
        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.set(self.combo_empresa.get())
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_descricao_produto))  
    
        # Produto
        fr_descricao_produto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_descricao_produto.place(relx=0.31, rely=0.01, relwidth=0.27, relheight=0.07)
        
        lb_descricao_produto = customtkinter.CTkLabel( fr_descricao_produto, text="Descrição")
        lb_descricao_produto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_descricao_produto = customtkinter.CTkEntry( fr_descricao_produto, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_descricao_produto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_descricao_produto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_ncm_produto))  

        # NCM
        fr_ncm_produto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_ncm_produto.place(relx=0.585, rely=0.01, relwidth=0.105, relheight=0.07)

        lb_ncm_produto = customtkinter.CTkLabel(fr_ncm_produto, text="NCM")
        lb_ncm_produto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_ncm_produto = customtkinter.CTkEntry(fr_ncm_produto, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_ncm_produto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_ncm_produto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_spead_produto))

        # Tipo Spead
        fr_tpo_produto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_produto.place(relx=0.695, rely=0.01, relwidth=0.12, relheight=0.07)

        lb_tpo_produto = customtkinter.CTkLabel(fr_tpo_produto, text="Spead")
        lb_tpo_produto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        spead = []
        spead = [spead[1] for spead in spead]
        self.entry_spead_produto = AutocompleteCombobox(fr_tpo_produto, width=30, font=('Times', 11), completevalues=spead)
        self.entry_spead_produto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_spead_produto.bind("<Button-1>", lambda event: self.atualizar_spead(event, self.entry_spead_produto))
        self.entry_spead_produto.bind('<Down>', lambda event: self.atualizar_spead(event, self.entry_spead_produto))
        self.entry_spead_produto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpomedida_produto))

        # Tipo de Medida
        fr_tpomedida_produto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpomedida_produto.place(relx=0.82, rely=0.01, relwidth=0.105, relheight=0.07)

        lb_tpomedida_produto = customtkinter.CTkLabel(fr_tpomedida_produto, text="Unidade Medida")
        lb_tpomedida_produto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        unidade_medida = []
        unidade_medida = [unidade[1] for unidade in unidade_medida]
        self.entry_tpomedida_produto = AutocompleteCombobox(fr_tpomedida_produto, width=30, font=('Times', 11), completevalues=unidade_medida)
        self.entry_tpomedida_produto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_tpomedida_produto.bind("<Button-1>", lambda event: self.atualizar_unidade_medida(event, self.entry_tpomedida_produto))
        self.entry_tpomedida_produto.bind('<Down>', lambda event: self.atualizar_unidade_medida(event, self.entry_tpomedida_produto))
        self.entry_tpomedida_produto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpomedida_produto))

        # Botão Consultar
        bt_consultar_produto = customtkinter.CTkButton(janela, image=self.btconsulta_img, text='', command=self.consulta_produtos) #   image=self.btconsulta_img,image=self.btsave_img,
        bt_consultar_produto.place(relx=0.93, rely=0.01, relwidth=0.03, relheight=0.04)

        # Botão Salvar
        bt_salvar_produto = customtkinter.CTkButton(janela, image=self.btsave_img, text='', command=self.gravar_produtos) #  image=self.btsave_img,
        bt_salvar_produto.place(relx=0.965, rely=0.01, relwidth=0.03, relheight=0.04)

    def frame_produto_linha_2(self, janela):
        # Widgets - Listar Itens
        self.LItens_produtos = ttk.Treeview(janela, height=12, column=('Nr', 'Descricao', 'NCM', 'Tipo_ID', 'Tipo', 'Unidade_Medida_ID', 'Unidade_Medida'), show='headings')
        self.LItens_produtos.heading('Nr', text="Nr.")
        self.LItens_produtos.column('Nr', width=5, anchor='e')
        self.LItens_produtos.heading('Descricao', text="Descrição")
        self.LItens_produtos.column('Descricao', width=350, anchor='w')
        self.LItens_produtos.heading('NCM', text="NCM")
        self.LItens_produtos.column('NCM', width=50, anchor='w')
        self.LItens_produtos.heading('Tipo_ID', text="ID")
        self.LItens_produtos.column('Tipo_ID', width=4, anchor='c')
        self.LItens_produtos.heading('Tipo', text="Tipo Spead")
        self.LItens_produtos.column('Tipo', width=50, anchor='w')
        self.LItens_produtos.heading('Unidade_Medida_ID', text="U.M.")
        self.LItens_produtos.column('Unidade_Medida_ID', width=10, anchor='c')
        self.LItens_produtos.heading('Unidade_Medida', text="U.M. Descrição")
        self.LItens_produtos.column('Unidade_Medida', width=50, anchor='w')

        self.LItens_produtos.place(relx=0, rely=0.01, relwidth=1, relheight=0.985)
        # self.LItens.bind("<Double-1>", self.OnDoubleClick)
        self.entry_descricao_produto.focus()
        # self.limpar_campos_lcto()

Produtos()

class Versoes(Icons, Functions):

    def cad_versoes(self):
        
        self.janela_cadastro_versao = customtkinter.CTkToplevel(self.window_one)
        self.janela_cadastro_versao.title('Cadastro de Versões')
        self.janela_cadastro_versao.geometry("1680x800")
        self.janela_cadastro_versao.resizable(True, True)
        self.janela_cadastro_versao.lift()  # Traz a janela para frente   

        self.frame_versao_principal = customtkinter.CTkFrame(self.janela_cadastro_versao, fg_color='black')
        self.frame_versao_principal.pack(pady=10, padx=10, fill="both", expand=True)
        customtkinter.CTkLabel(self.frame_versao_principal, text="", font=("Roboto", 30, "bold")).pack(pady=10)
        
        self.frame_cad_versao_treeview = customtkinter.CTkFrame(self.frame_versao_principal, fg_color='black') 
        self.frame_cad_versao_treeview.place(relx= 0.005, rely=0.085, relwidth=.99, relheight=0.91)
        customtkinter.CTkLabel(self.frame_cad_versao_treeview, text="", font=("Roboto", 30, "bold")).pack(pady=10)
         
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_cadastro_versao.protocol("WM_DELETE_WINDOW", lambda:  self.on_closing_tela(self.janela_cadastro_versao))

        self.images_base64()

        self.frame_versao_linha_1(self.frame_versao_principal)
        self.frame_versao_linha_2(self.frame_cad_versao_treeview)

        self.janela_cadastro_versao.focus_force()
        self.janela_cadastro_versao.grab_set()
        
        self.consulta_versoes()
            
    def frame_versao_linha_1(self, janela):
        # Versão
        fr_versao = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_versao.place(relx= 0.005, rely=0.01, relwidth=0.92, relheight=0.07)
        
        # versão id
        lb_versao_id = customtkinter.CTkLabel(fr_versao, text="Id", anchor='w')
        lb_versao_id.place(relx=0.005, rely=0.06, relheight=0.25, relwidth=0.25)
        
        self.entry_versao_id = customtkinter.CTkEntry(fr_versao, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_versao_id.place(relx=0.005, rely=0.5, relwidth=0.05, relheight=0.4)
        self.entry_versao_id.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_versao_nr))  

        # versão número
        lb_versao_nr = customtkinter.CTkLabel(fr_versao, text="Versão", anchor='w')
        lb_versao_nr.place(relx=0.06, rely=0.06, relheight=0.25, relwidth=0.25)
        
        self.entry_versao_nr = customtkinter.CTkEntry(fr_versao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_versao_nr.place(relx=0.06, rely=0.5, relwidth=0.10, relheight=0.4)
        self.entry_versao_nr.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_versao_ds))

        # versão descrição das alterações ou inclusões
        lb_tpo_versao_ds = customtkinter.CTkLabel(fr_versao, text="Descrição da Versão", anchor='w')
        lb_tpo_versao_ds.place(relx=0.165, rely=0.06, relheight=0.25, relwidth=0.25)
        
        self.entry_versao_ds = customtkinter.CTkEntry(fr_versao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_versao_ds.place(relx=0.165, rely=0.5, relwidth=0.725, relheight=0.4)
        self.entry_versao_ds.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_versao_dta))

        # versão data
        lb_versao_dta = customtkinter.CTkLabel(fr_versao, text="Data", anchor='w')
        lb_versao_dta.place(relx=0.895, rely=0.06, relheight=0.25, relwidth=0.10)
        
        self.entry_versao_dta = customtkinter.CTkEntry(fr_versao, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_versao_dta.place(relx=0.895, rely=0.5, relwidth=0.10, relheight=0.4)
        self.entry_versao_dta.bind("<Button-1>", lambda event: self.calendario(event, self.entry_versao_dta))
        self.entry_versao_dta.bind("<Return>", lambda event: self.muda_barrinha(event, bt_consultar_versao))

        # Botão Consultar
        bt_consultar_versao = customtkinter.CTkButton(janela, image=self.btconsulta_img, text='', command=self.consulta_versoes)
        bt_consultar_versao.place(relx=0.93, rely=0.01, relwidth=0.03, relheight=0.04)

        # Botão Salvar
        bt_salvar_versao = customtkinter.CTkButton(janela, image=self.btsave_img, text='', command=self.gravar_versoes)
        bt_salvar_versao.place(relx=0.965, rely=0.01, relwidth=0.03, relheight=0.04)
    
    def frame_versao_linha_2(self, janela):
        # Widgets - Listar Itens
        self.LItens_versao = ttk.Treeview(janela, height=12, column=('Id', 'Codigo', 'Descricao', 'dta'), show='headings')
        self.LItens_versao.heading('Id', text="ID")
        self.LItens_versao.column('Id', width=5, anchor='e')
        self.LItens_versao.heading('Codigo', text="Código")
        self.LItens_versao.column('Codigo', width=10, anchor='w')
        self.LItens_versao.heading('Descricao', text="Descrição")
        self.LItens_versao.column('Descricao', width=800, anchor='w')
        self.LItens_versao.heading('dta', text="Data")
        self.LItens_versao.column('dta', width=50, anchor='c')
        
        self.LItens_versao.place(relx=0, rely=0.01, relwidth=1, relheight=0.985)
        # self.LItens.bind("<Double-1>", self.OnDoubleClick)
        self.entry_versao_ds.focus()
        # self.limpar_campos_lcto()

    def gravar_versoes(self):
        # Definição de variáveis
        versao_id = self.entry_versao_id.get().strip()
        versao_codigo = self.entry_versao_nr.get().strip()  
        versao_descricao = self.entry_versao_ds.get().strip()  
        versao_dta = datetime.strptime(self.entry_versao_dta.get(), "%d/%m/%Y")
        versao_dta = versao_dta.strftime("%Y-%m-%d")  
        
        if not versao_codigo:
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo Código da Versão!!!.')
            self.entry_versao_nr.focus()
            return

        try:
            datetime.strptime(versao_dta, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Data da versão com preenchimento errado!")
            return
        
            
        # Consulta para verificar se o produto já existe
        vs_sql = """SELECT * FROM sys_versao 
                    WHERE 
                        versao_nr=%s
                    """
        myresult = db.executar_consulta(vs_sql, (str(versao_codigo)))
        
        if not myresult:  # Se não encontrou registros
            # Inserção do novo produto
            vs_sql = """INSERT INTO sys_versao 
                        (
                            versao_nr,
                            versao_ds,
                            versao_dta
                                
                        ) 
                        VALUES (%s, %s, %s)
                     """
            values = (
                    versao_codigo,
                    versao_descricao,
                    versao_dta
                    )
            myresult = db.executar_consulta(vs_sql,  values)
            
        else:
            # Atualização do produto existente
            vs_sql = """UPDATE TB_Produtos SET 
                                versao_ds = %s, 
                                versao_dta = %s, 
                        WHERE 
                            versao_nr=%s
                        """
            myresult = db.executar_consulta(vs_sql,  (versao_descricao, 
                                                      versao_dta))
    
    def consulta_versoes(self):
        
        # Preparar a tabela
        self.LItens_versao.delete(*self.LItens_versao.get_children())  # Limpa a tabela
        self.LItens_versao.heading('Id', text="ID")
        self.LItens_versao.column('Id', width=5, anchor='c')
        self.LItens_versao.heading('Codigo', text="Código")
        self.LItens_versao.column('Codigo', width=10, anchor='e')
        self.LItens_versao.heading('Descricao', text="Descrição")
        self.LItens_versao.column('Descricao', width=800, anchor='w')
        self.LItens_versao.heading('dta', text="Data")
        self.LItens_versao.column('dta', width=50, anchor='c')
        
        # SQL para buscar os dados
        vs_sql = """
                    SELECT
                        versao_id,
                        versao_nr,
                        versao_ds,
                        versao_dta
                    FROM
                        sys_versao
                    ORDER BY versao_nr ASC """
        
        myresult = db._querying(vs_sql)
        consulta = [(consulta) for consulta in myresult]
        
        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!")
            return
                
        # Inserir dados na tabela
        
        for item in consulta:
            Dta_Registro = item.get('versao_dta')
            data_formatada = Dta_Registro.strftime('%d/%m/%Y')
            formatted_item = (
                    item.get('versao_id'),
                    item.get('versao_nr'),
                    item.get('versao_ds'),
                    data_formatada
                )
            self.LItens_versao.insert('', 'end', values=formatted_item)

Versoes()

#Cadastro de Novos Projetos
class Projetos(Icons, Functions):
    
    def cad_projetos(self):
        
        self.janela_cadastro_projetos = customtkinter.CTkToplevel(self.window_one)
        self.janela_cadastro_projetos.title('Cadastro de Projetos')
        self.janela_cadastro_projetos.geometry("1680x800")
        self.janela_cadastro_projetos.resizable(True, True)
        self.janela_cadastro_projetos.lift()  # Traz a janela para frente   

        self.frame_projetos_principal = customtkinter.CTkFrame(self.janela_cadastro_projetos, fg_color='black')
        self.frame_projetos_principal.pack(pady=10, padx=10, fill="both", expand=True)
        customtkinter.CTkLabel(self.frame_projetos_principal, text="", font=("Roboto", 30, "bold")).pack(pady=10)
        
        self.frame_cad_projetos_treeview = customtkinter.CTkFrame(self.frame_projetos_principal, fg_color='black') 
        self.frame_cad_projetos_treeview.place(relx= 0.005, rely=0.085, relwidth=.99, relheight=0.91)
        customtkinter.CTkLabel(self.frame_cad_projetos_treeview, text="", font=("Roboto", 30, "bold")).pack(pady=10)
         
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_cadastro_projetos.protocol("WM_DELETE_WINDOW", lambda:  self.on_closing_tela(self.janela_cadastro_projetos))

        self.images_base64()

        self.frame_projetos_linha_1(self.frame_projetos_principal)
        self.frame_projetos_linha_2(self.frame_projetos_principal)
        self.frame_projetos_linha_3(self.frame_projetos_principal)
        self.frame_projetos_linha_4(self.frame_projetos_principal)
        
        self.janela_cadastro_projetos.focus_force()
        self.janela_cadastro_projetos.grab_set()
        
        self.consulta_projetos()
            
    def frame_projetos_linha_1(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_uf))

        # Estado
        coordenadas_relx = 0.26
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        fr_uf = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_uf.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_estado = customtkinter.CTkLabel(fr_uf, text="UF")
        lb_estado.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        uf = self.get_uf()
        self.entry_uf = AutocompleteCombobox(fr_uf, width=30, font=('Times', 11), completevalues=uf)
        self.entry_uf.pack()
        self.entry_uf.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_municipio))
    
        
        # Municipio
        coordenadas_relx = 0.325
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        fr_municipio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_municipio.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_municipio = customtkinter.CTkLabel(fr_municipio, text="Município")
        lb_municipio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        municipios = self.get_municipios( self.entry_uf.get())
        
        self.entry_municipio = AutocompleteCombobox(fr_municipio, width=30, font=('Times', 11), completevalues=municipios)
        self.entry_municipio.pack()
        self.entry_municipio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_municipio.bind("<Button-1>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<KeyRelease>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind('<Down>', lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpo_projeto))      

        # Tipo do Programa
        coordenadas_relx=0.53
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        fr_tpo_programa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_programa.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_tpo_programa = customtkinter.CTkLabel(fr_tpo_programa, text="Tipo do Programa")
        lb_tpo_programa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        tpo_programa = [] #self.get_tpo_programa()
        tpo_programa = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in tpo_programa]

        self.entry_tpo_programa = AutocompleteCombobox(fr_tpo_programa, width=30, font=('Times', 11), completevalues=tpo_programa)
        self.entry_tpo_programa.pack()
        self.entry_tpo_programa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        # self.entry_tpo_programa.bind("<Button-1>", lambda event: self.atualizar_tpo_programa(self, self.entry_tpo_programa))
        # self.entry_tpo_programa.bind('<Down>', lambda event: self.atualizar_tpo_programa(self, self.entry_tpo_programa))
        self.entry_tpo_programa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_cenario))

        # Tipo do Empreendimento
        coordenadas_relx=0.735
        coordenadas_rely=0.01
        coordenadas_relwidth=0.19
        coordenadas_relheight=0.07
        fr_tpo_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_tpo_projeto = customtkinter.CTkLabel(fr_tpo_projeto, text="Tipo do Empreendimento")
        lb_tpo_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        tpo_projeto = self.get_tpo_projetos()
        tpo_projeto = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in tpo_projeto]

        self.entry_tpo_projeto = AutocompleteCombobox(fr_tpo_projeto, width=30, font=('Times', 11), completevalues=tpo_projeto)
        self.entry_tpo_projeto.pack()
        self.entry_tpo_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_tpo_projeto.bind("<Button-1>", lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind('<Down>', lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_cenario))

        # Botão Consultar
        bt_consultar_projetos = customtkinter.CTkButton(janela, image=self.btconsulta_img, text='', command=self.consulta_projetos)
        bt_consultar_projetos.place(relx=0.93, rely=0.01, relwidth=0.03, relheight=0.04)

        # Botão Salvar
        bt_salvar_projetos = customtkinter.CTkButton(janela, image=self.btsave_img, text='', command=self.gravar_projetos)
        bt_salvar_projetos.place(relx=0.965, rely=0.01, relwidth=0.03, relheight=0.04)

    def frame_projetos_linha_2(self, janela):
        # Centro de Resultado
        coordenadas_relx = 0.005
        coordenadas_rely = 0.085
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_itens_nota_centro_result = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_itens_nota_centro_result.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_itens_nota_centro = customtkinter.CTkLabel(fr_itens_nota_centro_result, text='Centro de Resultado')
        lb_itens_nota_centro.place(relx=0.05, rely=0, relwidth=0.6, relheight=0.25)

        self.centro_resultado = []
        self.entry_itens_nota_centro = AutocompleteCombobox(fr_itens_nota_centro_result, width=30, font=('Times', 11), completevalues=self.centro_resultado)
        self.entry_itens_nota_centro.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_itens_nota_centro.bind("<Button-1>", lambda event: self.atualizar_centro_resultado(event, self.combo_empresa.get(), self.entry_itens_nota_centro))
        self.entry_itens_nota_centro.bind('<Down>', lambda event: self.atualizar_centro_resultado(event, self.combo_empresa.get(), self.entry_itens_nota_centro))
        self.entry_itens_nota_centro.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_natureza))

        # Status
        coordenadas_relx=0.26
        coordenadas_rely=0.085
        coordenadas_relwidth=0.19
        coordenadas_relheight=0.07
        fr_informacoes_status = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_informacoes_status.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_informacoes_status = customtkinter.CTkLabel(fr_informacoes_status, text="Status")
        lb_informacoes_status.place(relx=0.01, rely=0.11, relheight=0.07, relwidth=0.70)

        status = []

        self.entry_informacoes_status = AutocompleteCombobox(fr_informacoes_status, width=30, font=('Times', 11), completevalues=status)
        self.entry_informacoes_status.pack()
        self.entry_informacoes_status.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_informacoes_status.bind("<Button-1>", lambda event: self.atualizar_status(event, self.entry_empresa.get(), self.entry_informacoes_status))
        self.entry_informacoes_status.bind('<Down>', lambda event: self.atualizar_status(event, self.entry_empresa.get(), self.entry_informacoes_status))
        self.entry_informacoes_status.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_anexos))

        # Nome do Projeto
        coordenadas_relx=0.455
        coordenadas_rely=0.085
        coordenadas_relwidth=0.255
        coordenadas_relheight=0.07
        fr_nome_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_nome_projeto = customtkinter.CTkLabel(fr_nome_projeto, text="Nome do Projeto")
        lb_nome_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        nome_projeto = []

        self.entry_nome_projeto = AutocompleteCombobox(fr_nome_projeto, width=30, font=('Times', 11), completevalues=nome_projeto)
        self.entry_nome_projeto.pack()
        self.entry_nome_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_nome_projeto.bind("<Button-1>", lambda event: 
                                                                self.atualizar_nome_cenario(event,
                                                                self.entry_empresa.get(), 
                                                                self.entry_municipio.get(), 
                                                                self.entry_uf.get(), 
                                                                self.entry_tpo_projeto.get(), 
                                                                self.entry_nome_projeto))
        self.entry_nome_projeto.bind('<Down>', lambda event: 
                                                                self.atualizar_nome_projeto(event,
                                                                self.entry_empresa.get(), 
                                                                self.entry_municipio.get(), 
                                                                self.entry_uf.get(), 
                                                                self.entry_tpo_projeto.get(), 
                                                                self.entry_nome_projeto))
        self.entry_nome_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_empreendimento))

        # Setor
        coordenadas_relx=0.715
        coordenadas_rely=0.085
        coordenadas_relwidth=0.10
        coordenadas_relheight=0.07
        fr_setor = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_setor.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_setor = customtkinter.CTkLabel(fr_setor, text="Setor")
        lb_setor.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_setor = customtkinter.CTkEntry(fr_setor, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_setor.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_setor.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_cep))
        
        # Prioridade
        coordenadas_relx=0.82
        coordenadas_rely=0.085
        coordenadas_relwidth=0.10
        coordenadas_relheight=0.07
        fr_setor = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_setor.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_setor = customtkinter.CTkLabel(fr_setor, text="Prioridade")
        lb_setor.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_setor = customtkinter.CTkEntry(fr_setor, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_setor.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_setor.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_cep))

        # Opções Status
        coordenadas_relx=0.925
        coordenadas_rely=0.085
        coordenadas_relwidth=0.07
        coordenadas_relheight=0.07
        fr_status = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_status.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_status = customtkinter.CTkLabel(fr_status, text="Status")
        lb_status.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.check_var_ativo = customtkinter.StringVar(value="on")
        self.checkbox_ativo = customtkinter.CTkCheckBox(fr_status, text='Sim', variable=self.check_var_ativo, onvalue="on", offvalue="off")
        self.checkbox_ativo.place(relx=0.1, rely=0.30, relheight=0.5, relwidth=0.50)
        
    
    def frame_projetos_linha_3(self, janela):
        # Observação
        coordenadas_relx=0.005
        coordenadas_rely=0.16
        coordenadas_relwidth=0.985
        coordenadas_relheight=0.07
        fr_obs = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_obs.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_obs = customtkinter.CTkLabel(fr_obs, text="Observação")
        lb_obs.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_obs = customtkinter.CTkEntry(fr_obs, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_obs.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_obs.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_cep))
    
    def frame_projetos_linha_4(self, janela):
        # Widgets - Listar Itens
        self.LItens_projetos = ttk.Treeview(janela, height=12, column=(
                                                                        'Id', 
                                                                        'descricao', 
                                                                        'uf', 
                                                                        'municipio', 
                                                                        'centro_resultado',
                                                                        'tpo_programa',
                                                                        'tpo_empreendimento',
                                                                        'situacao',
                                                                        'prioridade',
                                                                        'setor',
                                                                        'obs',
                                                                        'status',

                                                                        ), show='headings')
        self.LItens_projetos.heading('Id', text="Nr.")
        self.LItens_projetos.column('Id', width=5, anchor='e')
        self.LItens_projetos.heading('descricao', text="Descrição")
        self.LItens_projetos.column('descricao', width=300, anchor='w')
        self.LItens_projetos.heading('uf', text="UF")
        self.LItens_projetos.column('uf', width=5, anchor='w')
        self.LItens_projetos.heading('municipio', text="Municipio")
        self.LItens_projetos.column('municipio', width=50, anchor='c')
        self.LItens_projetos.heading('centro_resultado', text="Centro Resultado")
        self.LItens_projetos.column('centro_resultado', width=50, anchor='c')
        self.LItens_projetos.heading('tpo_programa', text="Tipo Programa")
        self.LItens_projetos.column('tpo_programa', width=50, anchor='c')
        self.LItens_projetos.heading('tpo_empreendimento', text="Tipo Empreendimento")
        self.LItens_projetos.column('tpo_empreendimento', width=50, anchor='c')
        self.LItens_projetos.heading('situacao', text="Situação")
        self.LItens_projetos.column('situacao', width=50, anchor='c')
        self.LItens_projetos.heading('prioridade', text="Prioridade")
        self.LItens_projetos.column('prioridade', width=50, anchor='c')
        self.LItens_projetos.heading('setor', text="Setor")
        self.LItens_projetos.column('setor', width=50, anchor='c')
        self.LItens_projetos.heading('obs', text="Obs.")
        self.LItens_projetos.column('obs', width=50, anchor='c')
        self.LItens_projetos.heading('status', text="Status")
        self.LItens_projetos.column('status', width=50, anchor='c')
        
        self.LItens_projetos.place(relx=0.001, rely=0.25, relwidth=1, relheight=0.985)
        # self.LItens.bind("<Double-1>", self.OnDoubleClick)
        self.entry_empresa.focus()
        # self.limpar_campos_lcto()
        
    def gravar_projetos(self):
        # Definição de variáveis
        versao_id = self.entry_versao_id.get().strip()
        versao_codigo = self.entry_versao_nr.get().strip()  
        versao_descricao = self.entry_versao_ds.get().strip()  
        versao_dta = datetime.strptime(self.entry_versao_dta.get(), "%d/%m/%Y")
        versao_dta = versao_dta.strftime("%Y-%m-%d")  
        
        if not versao_codigo:
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo Código da Versão!!!.')
            self.entry_versao_nr.focus()
            return

        try:
            datetime.strptime(versao_dta, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Data da versão com preenchimento errado!")
            return
        
            
        # Consulta para verificar se o produto já existe
        vs_sql = """SELECT * FROM sys_versao 
                    WHERE 
                        versao_nr=%s
                    """
        myresult = db.executar_consulta(vs_sql, (str(versao_codigo)))
        
        if not myresult:  # Se não encontrou registros
            # Inserção do novo produto
            vs_sql = """INSERT INTO sys_versao 
                        (
                            versao_nr,
                            versao_ds,
                            versao_dta
                                
                        ) 
                        VALUES (%s, %s, %s)
                     """
            values = (
                    versao_codigo,
                    versao_descricao,
                    versao_dta
                    )
            myresult = db.executar_consulta(vs_sql,  values)
            
        else:
            # Atualização do produto existente
            vs_sql = """UPDATE TB_Produtos SET 
                                versao_ds = %s, 
                                versao_dta = %s, 
                        WHERE 
                            versao_nr=%s
                        """
            myresult = db.executar_consulta(vs_sql,  (versao_descricao, 
                                                      versao_dta))
    
    def consulta_projetos(self):
        
        # Preparar a tabela
        self.LItens_projetos.delete(*self.LItens_versao.get_children())  # Limpa a tabela
        self.LItens_projetos.heading('Id', text="ID")
        self.LItens_projetos.column('Id', width=5, anchor='c')
        self.LItens_projetos.heading('Codigo', text="Código")
        self.LItens_projetos.column('Codigo', width=10, anchor='e')
        self.LItens_projetos.heading('Descricao', text="Descrição")
        self.LItens_projetos.column('Descricao', width=800, anchor='w')
        self.LItens_projetos.heading('dta', text="Data")
        self.LItens_projetos.column('dta', width=50, anchor='c')
        
        # SQL para buscar os dados
        vs_sql = """
                    SELECT
                        versao_id,
                        versao_nr,
                        versao_ds,
                        versao_dta
                    FROM
                        sys_versao
                    ORDER BY versao_nr ASC """
        
        myresult = db._querying(vs_sql)
        consulta = [(consulta) for consulta in myresult]
        
        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!")
            return
                
        # Inserir dados na tabela
        
        for item in consulta:
            Dta_Registro = item.get('versao_dta')
            data_formatada = Dta_Registro.strftime('%d/%m/%Y')
            formatted_item = (
                    item.get('versao_id'),
                    item.get('versao_nr'),
                    item.get('versao_ds'),
                    data_formatada
                )
            self.LItens_projetos.insert('', 'end', values=formatted_item)

Projetos()