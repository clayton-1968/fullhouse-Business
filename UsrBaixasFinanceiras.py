from UsrCadastros import *
from widgets import Widgets

class BaixasFinanceiras(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def baixas_financeiras(self, principal_frame):
        self.images_base64()

        self.window_one.title('Baixas financeiras')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        # Variáveis de dados
        self.tpessoa_id = tk.StringVar(value="0")
        self.tpessoa_ds = tk.StringVar(value="Todos")
        self.tbaixa_tpo = tk.StringVar(value="EFETUAR BAIXA")
        self.tdta_inicio = tk.StringVar(value="01/01/2000")
        self.tdta_fim = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y"))

        # Criar widgets
        self.criar_widgets_baixas_financeiras()

    def preenche_cnpj(self, event):
        if self.combo_empresa.get():
            self.cnpj = self.obter_Empresa_ID(self.combo_empresa.get())

            self.entry_cnpj.delete(0, tk.END)
            self.entry_cnpj.insert(0, self.cnpj)

    def criar_widgets_baixas_financeiras(self):
        # Empresa
        self.frame_empresa(self.frame_principal, 0, 0.02, 0.30, 0.09)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))
        self.combo_empresa.bind("<<ComboboxSelected>>", self.preenche_cnpj)

        # CNPJ
        self.fr_cnpj = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cnpj.place(relx=0.31, rely=0.02, relwidth=0.10, relheight=0.09)

        self.lb_cnpj = customtkinter.CTkLabel(self.fr_cnpj, text="CPF/CNPJ")
        self.lb_cnpj.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_cnpj = customtkinter.CTkEntry(self.fr_cnpj, fg_color="white", text_color="black",
                                                           justify=tk.RIGHT)
        self.entry_cnpj.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Pessoas
        self.frame_pessoa(self.frame_principal, 0.42, 0.02, 0.35, 0.09)
        self.combo_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        bt_cadastro_pessoas = customtkinter.CTkButton(self.fr_pessoa, text='...', font=('Arial', 30), fg_color='green', command=self.cad_pessoas)
        bt_cadastro_pessoas.place(relx=0.905, rely=0.5, relwidth=0.05, relheight=0.35)
        bt_cadastro_pessoas.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        # Box Somente Pendentes
        self.fr_botao_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_box.place(relx=0.78, rely=0.02, relwidth=0.22, relheight=0.09)

        self.somente_pend_var = tk.BooleanVar()
        self.aprovados_cbox = customtkinter.CTkCheckBox(self.fr_botao_box, text="Somente Pendentes",
                            variable=self.somente_pend_var)
        self.aprovados_cbox.place(relx=0.01, rely=0.25, relwidth=0.6, relheight=0.5)

        # Botão de consulta
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botao_box, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_titulos)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.5, rely=0.25, relwidth=0.24, relheight=0.5)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botao_box, image=icone_salvar, text='',
                                                    fg_color='transparent', command=self.gravar_bxpagtos)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.75, rely=0.25, relwidth=0.24, relheight=0.5)

        # Arquivo
        self.fr_arquivo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_arquivo.place(relx=0, rely=0.12, relwidth=0.15, relheight=0.09)

        self.lb_arquivo = customtkinter.CTkLabel(self.fr_arquivo, text="Arquivo")
        self.lb_arquivo.place(relx=0.225, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_arquivo = customtkinter.CTkEntry(self.fr_arquivo, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_arquivo.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Tipo de baixa
        self.fr_baixa = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_baixa.place(relx=0.16, rely=0.12, relwidth=0.15, relheight=0.09)

        self.lb_baixa = customtkinter.CTkLabel(self.fr_baixa, text="Tipo de Baixa")
        self.lb_baixa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_baixa = customtkinter.CTkOptionMenu(self.fr_baixa, values=["", "EFETUAR BAIXA"], fg_color="white",
                                                       text_color="black")
        self.combo_baixa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Período
        self.fr_periodo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_periodo.place(relx=0.32, rely=0.12, relwidth=0.14, relheight=0.09)
        self.lb_periodo = customtkinter.CTkLabel(self.fr_periodo, text="Período")
        self.lb_periodo.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        # Data inicio
        self.lb_dt_inicio = customtkinter.CTkLabel(self.fr_periodo, text="Data Início")
        self.lb_dt_inicio.place(relx=0.1, rely=0.25, relheight=0.125, relwidth=0.35)

        self.entry_dt_inicio = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_inicio, self.entry_dt_inicio))

        # Data fim
        self.lb_dt_fim = customtkinter.CTkLabel(self.fr_periodo, text="Data Fim")
        self.lb_dt_fim.place(relx=0.6, rely=0.25, relheight=0.125, relwidth=0.35)

        self.entry_dt_fim = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_fim.delete(0, 'end')
        self.entry_dt_fim.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_fim))
        self.entry_dt_fim.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_fim, self.entry_dt_fim))

        # Banco
        self.fr_banco = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_banco.place(relx=0.47, rely=0.12, relwidth=0.20, relheight=0.09)

        self.lb_banco = customtkinter.CTkLabel(self.fr_banco, text="Banco")
        self.lb_banco.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.bancos = []
        self.entry_banco = AutocompleteCombobox(self.fr_banco, width=30, justify=tk.LEFT, font=('Times', 8),
                                                completevalues=self.bancos)
        self.entry_banco.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_banco.bind("<Button-1>", lambda event: self.atualizar_bancos(event, self.entry_banco))
        self.entry_banco.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia))

        # Agência
        self.fr_agencia = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_agencia.place(relx=0.68, rely=0.12, relwidth=0.14, relheight=0.09)

        self.lb_agencia = customtkinter.CTkLabel(self.fr_agencia, text="Agência")
        self.lb_agencia.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_agencia = customtkinter.CTkEntry(self.fr_agencia, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_agencia.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.4)
        self.entry_agencia.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia_dv))

        self.entry_agencia_dv = customtkinter.CTkEntry(self.fr_agencia, fg_color="white", text_color="black",
                                                       justify=tk.RIGHT)
        self.entry_agencia_dv.place(relx=0.62, rely=0.5, relwidth=0.35, relheight=0.4)
        self.entry_agencia_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Conta
        self.fr_contacorrente = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_contacorrente.place(relx=0.83, rely=0.12, relwidth=0.14, relheight=0.09)

        self.lb_contacorrente = customtkinter.CTkLabel(self.fr_contacorrente, text="Conta")
        self.lb_contacorrente.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_contacorrente = customtkinter.CTkEntry(self.fr_contacorrente, fg_color="white", text_color="black",
                                                          justify=tk.RIGHT)
        self.entry_contacorrente.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.4)
        self.entry_contacorrente.bind("<Return>", lambda event: self.muda_barrinha(event, None))

        self.entry_contacorrente_dv = customtkinter.CTkEntry(self.fr_contacorrente, fg_color="white", text_color="black",
                                                       justify=tk.RIGHT)
        self.entry_contacorrente_dv.place(relx=0.62, rely=0.5, relwidth=0.35, relheight=0.4)
        self.entry_contacorrente_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Frame título
        self.ft_titulo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.ft_titulo.place(relx=0, rely=0.22, relwidth=1, relheight=0.12)

        self.lb_periodo = customtkinter.CTkLabel(self.ft_titulo, text="Título")
        self.lb_periodo.place(relx=0, rely=0, relheight=0.25, relwidth=0.1)

        # Data Baixa
        self.fr_dt_baixa = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_dt_baixa.place(relx=0.01, rely=0.2, relwidth=0.07, relheight=0.7)
        self.lb_dt_baixa = customtkinter.CTkLabel(self.fr_dt_baixa, text="Data Baixa")
        self.lb_dt_baixa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_baixa = customtkinter.CTkEntry(self.fr_dt_baixa, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_baixa.delete(0, 'end')
        self.entry_dt_baixa.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_baixa.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_baixa.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_baixa))
        self.entry_dt_baixa.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_baixa, self.entry_dt_baixa))

        # CPF/CNPJ
        self.fr_cpf_cnpj = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_cpf_cnpj.place(relx=0.09, rely=0.22, relwidth=0.15, relheight=0.7)

        self.lb_cpf_cnpj = customtkinter.CTkLabel(self.fr_cpf_cnpj, text="CPF/CNPJ")
        self.lb_cpf_cnpj.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_cpf_cnpj = customtkinter.CTkEntry(self.fr_cpf_cnpj, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_cpf_cnpj.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Descrição
        self.fr_descricao = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_descricao.place(relx=0.25, rely=0.22, relwidth=0.3, relheight=0.7)

        self.lb_descricao = customtkinter.CTkLabel(self.fr_descricao, text="Descrição")
        self.lb_descricao.place(relx=0.22, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_cpf_cnpj = customtkinter.CTkEntry(self.fr_descricao, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_cpf_cnpj.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Nr. Documento
        self.fr_nr_documento = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_nr_documento.place(relx=0.56, rely=0.22, relwidth=0.13, relheight=0.7)

        self.lb_nr_documento = customtkinter.CTkLabel(self.fr_nr_documento, text="Nr. Documento")
        self.lb_nr_documento.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_nr_documento = customtkinter.CTkEntry(self.fr_nr_documento, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_nr_documento.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Valor
        self.fr_valor = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_valor.place(relx=0.70, rely=0.22, relwidth=0.15, relheight=0.7)

        self.lb_valor = customtkinter.CTkLabel(self.fr_valor, text="Valor")
        self.lb_valor.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_valor = customtkinter.CTkEntry(self.fr_valor, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_valor.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Nr. Parc.
        self.fr_nr_parc = customtkinter.CTkFrame(self.ft_titulo, border_color="gray75", border_width=1)
        self.fr_nr_parc.place(relx=0.86, rely=0.22, relwidth=0.10, relheight=0.7)

        self.lb_nr_parc = customtkinter.CTkLabel(self.fr_nr_parc, text="Nr. Parc")
        self.lb_nr_parc.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_nr_parc = customtkinter.CTkEntry(self.fr_nr_parc, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_nr_parc.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Frame título 2
        self.ft_titulo2 = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.ft_titulo2.place(relx=0, rely=0.34, relwidth=1, relheight=0.12)

        # Data Doc.
        self.fr_dt_doc = customtkinter.CTkFrame(self.ft_titulo2, border_color="gray75", border_width=1)
        self.fr_dt_doc.place(relx=0.01, rely=0.2, relwidth=0.07, relheight=0.7)
        self.lb_dt_doc = customtkinter.CTkLabel(self.fr_dt_doc, text="Data Doc.")
        self.lb_dt_doc.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_doc = customtkinter.CTkEntry(self.fr_dt_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_doc.delete(0, 'end')
        self.entry_dt_doc.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_doc.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_doc.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_doc))
        self.entry_dt_doc.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_doc, self.entry_dt_doc))

        # Situação
        self.fr_situacao = customtkinter.CTkFrame(self.ft_titulo2, border_color="gray75", border_width=1)
        self.fr_situacao.place(relx=0.09, rely=0.2, relwidth=0.07, relheight=0.7)

        self.lb_situacao = customtkinter.CTkLabel(self.fr_situacao, text="Situação")
        self.lb_situacao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_situacao = customtkinter.CTkOptionMenu(self.fr_situacao, values=["L", "F"], fg_color="white",
                                                       text_color="black")
        self.combo_situacao.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Unidade
        self.fr_unidade = customtkinter.CTkFrame(self.ft_titulo2, border_color="gray75", border_width=1)
        self.fr_unidade.place(relx=0.17, rely=0.2, relwidth=0.07, relheight=0.7)

        self.lb_unidade = customtkinter.CTkLabel(self.fr_unidade, text="Unidade")
        self.lb_unidade.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_unidade = customtkinter.CTkEntry(self.fr_unidade, fg_color="white", text_color="black")
        self.entry_unidade.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Valor Liquidado
        self.fr_valor_liquidado = customtkinter.CTkFrame(self.ft_titulo2, border_color="gray75", border_width=1)
        self.fr_valor_liquidado.place(relx=0.25, rely=0.22, relwidth=0.15, relheight=0.7)

        self.lb_valor_liquidado = customtkinter.CTkLabel(self.fr_valor_liquidado, text="Valor Liquidado")
        self.lb_valor_liquidado.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_valor_liquidado = customtkinter.CTkEntry(self.fr_valor_liquidado, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_valor_liquidado.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.35, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Data Pagto", "CpF/CnPj", "Beneficiário", "Nr. Documento",
            "Valor", "Nr. Parc.", "Data Doc.", "Situação", "Unidade", "Valor Efetivo"
        ), show='headings')

        col_widths = [40, 60, 60, 80, 50, 60, 30, 40, 30, 60, 60]
        headers = ["Data Pagto", "CpF/CnPj", "Beneficiário", "Nr. Documento", "Valor", "Nr. Parc.", "Data Doc.",
                   "Situação", "Unidade", "Valor Efetivo"]

        for col, header, width in zip(self.tree['columns'], headers, col_widths):
            self.tree.heading(col, text=header)
            self.tree.column(col, width=width)

        self.tree.pack(expand=True, fill=tk.BOTH)

        # # Configurar colunas
        # colunas = [
        #     ("Data Pagto", 60), ("CpF/CnPj", 100), ("Beneficiário", 350),
        #     ("Nr. Documento", 80), ("Valor", 100), ("Nr. Parc.", 50),
        #     ("Data Doc.", 60), ("Situação", 50), ("Unidade", 50), ("Valor Efetivo", 100)
        # ]
        #
        # for col, width in colunas:
        #     self.lbaixas.heading(col, text=col)
        #     self.lbaixas.column(col, width=width, anchor=tk.CENTER)
        #
        # self.lbaixas.pack(fill=tk.BOTH, expand=True)
        # self.lbaixas.bind("<ButtonRelease-1>", self.lbaixas_click)
        #
        # # Frame de detalhes
        # detalhes_frame = ttk.LabelFrame(main_frame, text="Detalhes da Baixa", padding="10")
        # detalhes_frame.pack(fill=tk.X, pady=5)
        #
        # # Campos de detalhes
        # ttk.Label(detalhes_frame, text="Data Baixa:").grid(row=0, column=0, sticky=tk.W)
        # self.tbaixa_dta = ttk.Entry(detalhes_frame)
        # self.tbaixa_dta.grid(row=0, column=1, sticky=tk.W)
        # self.tbaixa_dta.bind("<KeyRelease>", self.formatar_data)
        #
        # ttk.Label(detalhes_frame, text="CPF/CNPJ:").grid(row=0, column=2, sticky=tk.W)
        # self.tbaixa_cpf_cnpj = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_cpf_cnpj.grid(row=0, column=3, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Favorecido:").grid(row=1, column=0, sticky=tk.W)
        # self.tbaixa_favorecido_ds = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_favorecido_ds.grid(row=1, column=1, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Nr. Documento:").grid(row=1, column=2, sticky=tk.W)
        # self.tbaixa_documento_nr = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_documento_nr.grid(row=1, column=3, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Valor:").grid(row=2, column=0, sticky=tk.W)
        # self.tbaixa_documento_valor = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_documento_valor.grid(row=2, column=1, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Nr. Parcela:").grid(row=2, column=2, sticky=tk.W)
        # self.tbaixa_parcela_nr = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_parcela_nr.grid(row=2, column=3, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Data Doc.:").grid(row=3, column=0, sticky=tk.W)
        # self.tbaixa_dtadocumento = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_dtadocumento.grid(row=3, column=1, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Situação:").grid(row=3, column=2, sticky=tk.W)
        # self.tbaixa_situacao = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_situacao.grid(row=3, column=3, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Unidade:").grid(row=4, column=0, sticky=tk.W)
        # self.tbaixa_unidade = ttk.Entry(detalhes_frame, state='readonly')
        # self.tbaixa_unidade.grid(row=4, column=1, sticky=tk.W)
        #
        # ttk.Label(detalhes_frame, text="Valor Liquidação:").grid(row=4, column=2, sticky=tk.W)
        # self.tbaixa_vlr_liquidacao = ttk.Entry(detalhes_frame)
        # self.tbaixa_vlr_liquidacao.grid(row=4, column=3, sticky=tk.W)
        #
        # # Frame Banco
        # banco_frame = ttk.LabelFrame(detalhes_frame, text="Dados Bancários", padding="10")
        # banco_frame.grid(row=5, column=0, columnspan=4, sticky=tk.W + tk.E, pady=5)
        #
        # ttk.Label(banco_frame, text="Banco:").grid(row=0, column=0, sticky=tk.W)
        # self.tbanco = ttk.Entry(banco_frame)
        # self.tbanco.grid(row=0, column=1, sticky=tk.W)
        # self.tbanco.bind("<Double-1>", self.tbanco_dblclick)
        #
        # ttk.Label(banco_frame, text="Agência:").grid(row=0, column=2, sticky=tk.W)
        # self.tagencia = ttk.Entry(banco_frame)
        # self.tagencia.grid(row=0, column=3, sticky=tk.W)
        #
        # ttk.Label(banco_frame, text="Conta:").grid(row=0, column=4, sticky=tk.W)
        # self.tconta = ttk.Entry(banco_frame)
        # self.tconta.grid(row=0, column=5, sticky=tk.W)
        #
        # # Botão Gravar
        # ttk.Button(detalhes_frame, text="Gravar Baixa", command=self.gravar_bxpagtos).grid(row=6, column=0,
        #                                                                                    columnspan=4, pady=10)

    def formatar_data(self, event):
        widget = event.widget
        texto = widget.get()

        if len(texto) == 2 and not texto.endswith("/"):
            widget.insert(2, "/")
            widget.icursor(3)
        elif len(texto) == 5 and not texto.endswith("/"):
            widget.insert(5, "/")
            widget.icursor(6)


    def tpessoa_id_dblclick(self, event):
        if not self.tcnpj.get():
            messagebox.showerror("Erro", "Preencher a Empresa!")
            return

        # Implementar consulta de pessoa
        messagebox.showinfo("Consulta", "Consulta de pessoa (implementar)")

    def tbanco_dblclick(self, event):
        if not self.tcnpj.get():
            messagebox.showerror("Erro", "Preencher a Empresa!")
            return

        # Implementar consulta de banco
        messagebox.showinfo("Consulta", "Consulta de banco (implementar)")

    def tbaixa_tpo_dblclick(self, event):
        # Implementar seleção de tipo de baixa
        messagebox.showinfo("Consulta", "Seleção de tipo de baixa (implementar)")

    def consulta_titulos(self):
        # Limpar a lista
        for item in self.lbaixas.get_children():
            self.lbaixas.delete(item)

        # Validar campos
        if not self.tcnpj.get():
            messagebox.showerror("Erro", "Empresa não pode ser vazia!")
            return

        try:
            # Converter datas para o formato do banco de dados
            dta_inicio = datetime.strptime(self.tdta_inicio.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            dta_fim = datetime.strptime(self.tdta_fim.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Data inválida!")
            return

        # Simular consulta (substituir por consulta real ao banco de dados)
        if self.tbaixa_tpo.get() == "EFETUAR BAIXA":
            # Simular dados de consulta
            dados = [
                (
                "01/01/2023", "12345678901", "Fornecedor Exemplo 1", "DOC001", "1000,00", "1", "01/01/2023", "L", "001",
                "1000,00"),
                ("", "98765432101", "Fornecedor Exemplo 2", "FAT002", "500,00", "1", "15/01/2023", "F", "002", ""),
            ]
        else:
            # Simular dados para cancelamento de baixa
            dados = [
                (
                "10/01/2023", "12345678901", "Fornecedor Exemplo 1", "DOC001", "1000,00", "1", "01/01/2023", "L", "001",
                "1000,00"),
                ("05/01/2023", "98765432101", "Fornecedor Exemplo 2", "FAT002", "500,00", "1", "15/01/2023", "F", "002",
                 "500,00"),
            ]

        # Adicionar dados à Treeview
        for item in dados:
            self.lbaixas.insert("", tk.END, values=item)

    def gravar_bxpagtos(self):
        # Validar campos obrigatórios
        if not self.tbaixa_dta.get():
            messagebox.showerror("Erro", "Data de baixa é obrigatória!")
            return

        if not self.tbaixa_vlr_liquidacao.get():
            messagebox.showerror("Erro", "Valor de liquidação é obrigatório!")
            return

        if self.tbaixa_dta.get() and (not self.tbanco.get() or not self.tagencia.get() or not self.tconta.get()):
            messagebox.showerror("Erro", "Preencher os dados do Agente Financeiro de Liquidação!")
            return

        try:
            # Converter data para verificação
            dta_baixa = datetime.strptime(self.tbaixa_dta.get(), "%d/%m/%Y")
            dta_documento = datetime.strptime(self.tbaixa_dtadocumento.get(), "%d/%m/%Y")

            if dta_baixa < dta_documento:
                messagebox.showerror("Erro", "Data de Baixa não pode ser menor que a data do documento!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Data inválida!")
            return

        # Simular gravação (substituir por operação real no banco de dados)
        if self.tbaixa_tpo.get() == "EFETUAR BAIXA":
            operacao = "baixa"
        else:
            operacao = "cancelamento"

        messagebox.showinfo("Sucesso", f"Operação de {operacao} realizada com sucesso!")
        self.consulta_titulos()  # Atualizar a lista

    def lbaixas_click(self, event):
        item = self.lbaixas.selection()
        if item:
            valores = self.lbaixas.item(item, "values")

            # Preencher campos com os valores selecionados
            self.tbaixa_dta.delete(0, tk.END)
            self.tbaixa_dta.insert(0, valores[0])

            self.tbaixa_cpf_cnpj.config(state='normal')
            self.tbaixa_cpf_cnpj.delete(0, tk.END)
            self.tbaixa_cpf_cnpj.insert(0, valores[1])
            self.tbaixa_cpf_cnpj.config(state='readonly')

            self.tbaixa_favorecido_ds.config(state='normal')
            self.tbaixa_favorecido_ds.delete(0, tk.END)
            self.tbaixa_favorecido_ds.insert(0, valores[2])
            self.tbaixa_favorecido_ds.config(state='readonly')

            self.tbaixa_documento_nr.config(state='normal')
            self.tbaixa_documento_nr.delete(0, tk.END)
            self.tbaixa_documento_nr.insert(0, valores[3])
            self.tbaixa_documento_nr.config(state='readonly')

            self.tbaixa_documento_valor.config(state='normal')
            self.tbaixa_documento_valor.delete(0, tk.END)
            self.tbaixa_documento_valor.insert(0, valores[4])
            self.tbaixa_documento_valor.config(state='readonly')

            self.tbaixa_parcela_nr.config(state='normal')
            self.tbaixa_parcela_nr.delete(0, tk.END)
            self.tbaixa_parcela_nr.insert(0, valores[5])
            self.tbaixa_parcela_nr.config(state='readonly')

            self.tbaixa_dtadocumento.config(state='normal')
            self.tbaixa_dtadocumento.delete(0, tk.END)
            self.tbaixa_dtadocumento.insert(0, valores[6])
            self.tbaixa_dtadocumento.config(state='readonly')

            self.tbaixa_situacao.config(state='normal')
            self.tbaixa_situacao.delete(0, tk.END)
            self.tbaixa_situacao.insert(0, valores[7])
            self.tbaixa_situacao.config(state='readonly')

            self.tbaixa_unidade.config(state='normal')
            self.tbaixa_unidade.delete(0, tk.END)
            self.tbaixa_unidade.insert(0, valores[8])
            self.tbaixa_unidade.config(state='readonly')

            self.tbaixa_vlr_liquidacao.delete(0, tk.END)
            self.tbaixa_vlr_liquidacao.insert(0, valores[9] if valores[9] else valores[4])

            # Dar foco ao campo de data
            self.tbaixa_dta.focus()


BaixasFinanceiras()
