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

    def criar_widgets_baixas_financeiras(self):
        # Empresa
        self.frame_empresa(self.frame_principal, 0, 0, 0.40, 0.07)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))
        
        # Pessoas
        self.frame_pessoa(self.frame_principal, 0.405, 0, 0.35, 0.07)
        self.combo_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        bt_cadastro_pessoas = customtkinter.CTkButton(self.fr_pessoa, text='...', font=('Arial', 30), fg_color='green', command=self.cad_pessoas)
        bt_cadastro_pessoas.place(relx=0.905, rely=0.5, relwidth=0.05, relheight=0.35)
        bt_cadastro_pessoas.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        # Box Somente Pendentes
        self.fr_botao_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_box.place(relx=0.76, rely=0, relwidth=0.22, relheight=0.07)

        self.somente_pend_var = tk.BooleanVar()
        self.somente_pend_cbox = customtkinter.CTkCheckBox(self.fr_botao_box, text="Pendentes",
                            variable=self.somente_pend_var)
        self.somente_pend_cbox.place(relx=0.01, rely=0.25, relwidth=0.6, relheight=0.5)

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
                                                    fg_color='transparent', command=self.grava_bx_pagtos)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.75, rely=0.25, relwidth=0.24, relheight=0.5)

        # Botão Sair das baixas
        icon_image = self.base64_to_photoimage('sair')
        self.btn_sair_baixas = customtkinter.CTkButton(self.frame_principal, text='Sair', image=icon_image, fg_color='transparent', command=self.tela_principal)
        self.btn_sair_baixas.pack(pady=10)
        self.btn_sair_baixas.place(relx=0.955, rely=0, relwidth=0.04, relheight=0.05)

        # Arquivo
        self.fr_arquivo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_arquivo.place(relx=0, rely=0.075, relwidth=0.15, relheight=0.07)

        self.lb_arquivo = customtkinter.CTkLabel(self.fr_arquivo, text="Arquivo")
        self.lb_arquivo.place(relx=0.225, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_arquivo = customtkinter.CTkEntry(self.fr_arquivo, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_arquivo.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Tipo de baixa
        self.fr_baixa = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_baixa.place(relx=0.155, rely=0.075, relwidth=0.15, relheight=0.07)

        self.lb_baixa = customtkinter.CTkLabel(self.fr_baixa, text="Tipo de Baixa")
        self.lb_baixa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_baixa = customtkinter.CTkOptionMenu(self.fr_baixa, values=["EFETUAR BAIXA", "CANCELAR BAIXA"], fg_color="white",
                                                       text_color="black")
        self.combo_baixa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Período
        self.fr_periodo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_periodo.place(relx=0.31, rely=0.075, relwidth=0.14, relheight=0.09)
        self.lb_periodo = customtkinter.CTkLabel(self.fr_periodo, text="Período")
        self.lb_periodo.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        # Data inicio
        self.lb_dt_inicio = customtkinter.CTkLabel(self.fr_periodo, text="Data Início")
        self.lb_dt_inicio.place(relx=0.1, rely=0.25, relheight=0.15, relwidth=0.35)

        self.entry_dt_inicio = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_inicio, self.entry_dt_inicio))

        # Data fim
        self.lb_dt_fim = customtkinter.CTkLabel(self.fr_periodo, text="Data Fim")
        self.lb_dt_fim.place(relx=0.55, rely=0.25, relheight=0.15, relwidth=0.35)

        self.entry_dt_fim = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_fim.delete(0, 'end')
        self.entry_dt_fim.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_fim))
        self.entry_dt_fim.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_fim, self.entry_dt_fim))

        # Banco
        self.fr_banco = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_banco.place(relx=0.455, rely=0.075, relwidth=0.20, relheight=0.07)

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
        self.fr_agencia.place(relx=0.66, rely=0.075, relwidth=0.14, relheight=0.07)

        self.lb_agencia = customtkinter.CTkLabel(self.fr_agencia, text="Agência")
        self.lb_agencia.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.agencias = []
        self.entry_agencia = AutocompleteCombobox(self.fr_agencia, width=30, justify=tk.RIGHT, font=('Times', 8),
                                                completevalues=self.agencias)
        
        self.entry_agencia.place(relx=0.01, rely=0.5, relwidth=0.97, relheight=0.4)
        self.entry_agencia.bind("<Button-1>", lambda event: self.atualizar_agencias(
                                                                    event,
                                                                    self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one), 
                                                                    self.obter_banco(self.entry_banco.get(), self.window_one), 
                                                                    self.entry_agencia, 
                                                                    ))
        self.entry_agencia.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Conta
        self.fr_contacorrente = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_contacorrente.place(relx=0.805, rely=0.075, relwidth=0.14, relheight=0.07)

        self.lb_contacorrente = customtkinter.CTkLabel(self.fr_contacorrente, text="Conta")
        self.lb_contacorrente.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.contascorrente = []
        self.entry_contacorrente = AutocompleteCombobox(self.fr_contacorrente, width=30, justify=tk.RIGHT, font=('Times', 8),
                                                completevalues=self.contascorrente)
        self.entry_contacorrente.place(relx=0.01, rely=0.5, relwidth=0.97, relheight=0.4)
        self.entry_contacorrente.bind("<Button-1>", lambda event: self.atualizar_contascorrente(
                                                                    event,
                                                                    self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one), 
                                                                    self.obter_banco(self.entry_banco.get(), self.window_one), 
                                                                    self.entry_contacorrente))

        self.entry_contacorrente.bind("<Return>", lambda event: self.muda_barrinha(event, None))

        # self.entry_contacorrente_dv = customtkinter.CTkEntry(self.fr_contacorrente, fg_color="white", text_color="black",
        #                                                justify=tk.RIGHT)
        # self.entry_contacorrente_dv.place(relx=0.62, rely=0.5, relwidth=0.35, relheight=0.4)
        # self.entry_contacorrente_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Data Baixa
        self.fr_dt_baixa = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_dt_baixa.place(relx=0, rely=0.17, relwidth=0.07, relheight=0.07)
        self.lb_dt_baixa = customtkinter.CTkLabel(self.fr_dt_baixa, text="Data Baixa")
        self.lb_dt_baixa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_baixa = customtkinter.CTkEntry(self.fr_dt_baixa, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_baixa.delete(0, 'end')
        self.entry_dt_baixa.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_baixa.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_baixa.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_baixa))
        self.entry_dt_baixa.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_baixa, self.entry_dt_baixa))

        # CPF/CNPJ
        self.fr_cpf_cnpj = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_cpf_cnpj.place(relx=0.075, rely=0.17, relwidth=0.15, relheight=0.07)

        self.lb_cpf_cnpj = customtkinter.CTkLabel(self.fr_cpf_cnpj, text="CPF/CNPJ")
        self.lb_cpf_cnpj.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_cpf_cnpj = customtkinter.CTkEntry(self.fr_cpf_cnpj, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_cpf_cnpj.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Descrição
        self.fr_descricao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_descricao.place(relx=0.23, rely=0.17, relwidth=0.3, relheight=0.07)


        self.lb_descricao = customtkinter.CTkLabel(self.fr_descricao, text="Descrição")
        self.lb_descricao.place(relx=0.22, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_descricao = customtkinter.CTkEntry(self.fr_descricao, fg_color="white", text_color="black", justify=tk.LEFT)
        self.entry_descricao.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Nr. Documento
        self.fr_nr_documento = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_nr_documento.place(relx=0.535, rely=0.17, relwidth=0.13, relheight=0.07)

        self.lb_nr_documento = customtkinter.CTkLabel(self.fr_nr_documento, text="Nr. Documento")
        self.lb_nr_documento.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_nr_documento = customtkinter.CTkEntry(self.fr_nr_documento, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_nr_documento.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Valor
        self.fr_valor = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_valor.place(relx=0.67, rely=0.17, relwidth=0.15, relheight=0.07)

        self.lb_valor = customtkinter.CTkLabel(self.fr_valor, text="Valor")
        self.lb_valor.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_valor = customtkinter.CTkEntry(self.fr_valor, fg_color="white", text_color="black",
                                                           justify=tk.RIGHT)
        self.entry_valor.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Nr. Parc.
        self.fr_nr_parc = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nr_parc.place(relx=0.825, rely=0.17, relwidth=0.10, relheight=0.07)

        self.lb_nr_parc = customtkinter.CTkLabel(self.fr_nr_parc, text="Nr. Parc")
        self.lb_nr_parc.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_nr_parc = customtkinter.CTkEntry(self.fr_nr_parc, fg_color="white", text_color="black",
                                                           justify=tk.RIGHT)
        self.entry_nr_parc.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Data Doc.
        self.fr_dt_doc = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_dt_doc.place(relx=0, rely=0.245, relwidth=0.07, relheight=0.07)

        self.lb_dt_doc = customtkinter.CTkLabel(self.fr_dt_doc, text="Data Doc.")
        self.lb_dt_doc.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_doc = customtkinter.CTkEntry(self.fr_dt_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_doc.delete(0, 'end')
        self.entry_dt_doc.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_doc.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_doc.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_doc))
        self.entry_dt_doc.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_doc, self.entry_dt_doc))

        # Situação
        self.fr_situacao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_situacao.place(relx=0.075, rely=0.245, relwidth=0.07, relheight=0.07)


        self.lb_situacao = customtkinter.CTkLabel(self.fr_situacao, text="Situação")
        self.lb_situacao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_situacao = customtkinter.CTkOptionMenu(self.fr_situacao, values=["L", "F"], fg_color="white",
                                                       text_color="black")
        self.combo_situacao.place(relx=0.05, rely=0.5, relwidth=0.94, relheight=0.4)

        # Unidade
        self.fr_unidade = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_unidade.place(relx=0.15, rely=0.245, relwidth=0.07, relheight=0.07)


        self.lb_unidade = customtkinter.CTkLabel(self.fr_unidade, text="Unidade")
        self.lb_unidade.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_unidade = customtkinter.CTkEntry(self.fr_unidade, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_unidade.place(relx=0.01, rely=0.5, relwidth=0.97, relheight=0.4)

        # Valor Liquidado
        self.fr_valor_liquidado = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_valor_liquidado.place(relx=0.225, rely=0.245, relwidth=0.15, relheight=0.07)

        self.lb_valor_liquidado = customtkinter.CTkLabel(self.fr_valor_liquidado, text="Valor Liquidado")
        self.lb_valor_liquidado.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_valor_liquidado = customtkinter.CTkEntry(self.fr_valor_liquidado, fg_color="white", text_color="black",
                                                           justify=tk.RIGHT)
        self.entry_valor_liquidado.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_tree.place(relx=0, rely=0.32, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Data Pagto", "CpF/CnPj", "Beneficiário", "Nr. Documento",
            "Valor", "Nr. Parc.", "Data Doc.", "Situação", "Unidade", "Valor Efetivo"
        ), show='headings')

        # Atualiza o layout
        self.tree.update_idletasks()

        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        col_widths = [10, 20, 800, 10, 10, 10, 10, 10, 8, 8, 8]

        headers = ["Data Pagto", "CpF/CnPj", "Beneficiário", "Nr. Documento", "Valor", "Nr. Parc.", "Data Doc.",
                   "Situação", "Unidade", "Valor Efetivo"]
        
        for col, header, width in zip(self.tree['columns'], headers, col_widths):
            self.tree.heading(col, text=header)
            self.tree.column(col, width=width, anchor='e')

        # Adequa as colunas ao conteudo
        for col in self.tree["columns"]:
            largura_max = tk.font.Font().measure(col)

            for item in self.tree.get_children():
                valor = self.tree.set(item, col)
                largura = tk.font.Font().measure(valor)
                if largura > largura_max:
                    largura_max = largura

            self.tree.column(col, width=largura_max + 20)

        self.tree.bind("<Double-1>", self.lbaixas_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)

    def consulta_titulos(self):
        
        self.tree.delete(*self.tree.get_children())

        try:
            if self.entry_dt_inicio.get():
                self.dt_inicio = datetime.strptime(self.entry_dt_inicio.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            if self.entry_dt_fim.get():
                self.dt_fim = datetime.strptime(self.entry_dt_fim.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            if self.entry_dt_doc.get():
                self.dt_doc = datetime.strptime(self.entry_dt_doc.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            if self.entry_dt_baixa.get():
                self.dt_baixa = datetime.strptime(self.entry_dt_baixa.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use DD/MM/YYYY")
            return

        if self.combo_baixa.get() == "EFETUAR BAIXA":
            query = """
                        SELECT
                            dc.Doc_Aprovacao                        AS Doc_Aprovacao,
                            CAST(ii.Fin_Num_documento AS CHAR)      AS Num_Documento,
                            ii.ID_Empresa                           AS ID_Empresa,
                            pp.Pessoas_Descricao                    AS Pessoas_Descricao,
                            ii.ID_Pessoa                            AS ID_Pessoa,
                            pp.Pessoas_Descricao                    AS DS_Pessoa,
                            pp.Pessoas_Tipo                         AS Tipo_Empresa,
                            ii.ID_Unidade                           AS Unidade,
                            ff.Unidade_Descricao                    AS Unidade_Descricao,
                            ii.Fin_Parcela                          AS Parcela,
                            dc.Doc_Dta_Documento                    AS Dta_Vcto,
                            ii.Fin_VlR_Parcela                      AS Vlr_Parcela,
                            ii.Fin_Dta_Liquidacao                   AS Dta_Liquidacao,
                            ii.Fin_VlR_Liquidacao                   AS Vlr_Liquidacao,
                            ii.ID_Bco_Liquidacao                    AS ID_Bco_Liquidacao
                        FROM TB_Financeiro ii
                        LEFT JOIN TB_CB_Doc dc ON dc.ID_Empresa=ii.ID_Empresa AND dc.ID_Pessoa=ii.ID_Pessoa 
                            AND dc.ID_Unidade=ii.ID_Unidade AND dc.Doc_Num_Documento=ii.Fin_Num_Documento
                        LEFT JOIN TB_Pessoas pp ON pp.Pessoas_CPF_CNPJ=ii.ID_Pessoa AND pp.Empresa_ID=ii.ID_Empresa
                        LEFT JOIN TB_UnidadesNegocio ff ON ff.Unidade_ID=ii.ID_Unidade AND ff.Empresa_ID=ii.ID_Empresa
                        WHERE dc.Doc_Aprovacao = 'S'
                    """

            if self.combo_empresa.get():
                self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
                query += f" AND ii.ID_Empresa = '{self.id_empresa}'"

            if self.combo_pessoa.get():
                self.id_pessoa = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
                query += f" AND ii.ID_Pessoa = '{self.id_pessoa}'"

            query += f" AND ii.Fin_Dta_Vcto BETWEEN '{self.dt_inicio}' AND '{self.dt_fim}'"

            if self.somente_pend_var.get():
                query += " AND ii.Fin_Dta_Liquidacao IS NULL"

            query += " ORDER BY ii.Fin_Dta_Liquidacao, ii.ID_Pessoa, ii.Fin_Num_documento, ii.Fin_Parcela"

            
            myresult = db._querying(query)
            consulta = [(consulta) for consulta in myresult]

            # Inserir dados na tabela
            for item in consulta:
                Dta_Liquidacao = item['Dta_Liquidacao']
                # Verifica se Dta_Liquidacao não é None ou vazio
                if Dta_Liquidacao not in (None, '', '0000-00-00'):
                    str(Dta_Liquidacao.strftime("%d/%m/%Y"))
                else:
                    Dta_Liquidacao = ''
                
                formatted_item = (
                    str(Dta_Liquidacao.strftime("%d/%m/%Y")) if Dta_Liquidacao not in (None, '', '0000-00-00') else '',
                    str(item['ID_Pessoa']),
                    str(item['DS_Pessoa']) if item['DS_Pessoa'] else "Não Cadastrado!",

                    str(item['Num_Documento']),

                    f"{float(item['Vlr_Parcela']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Vlr_Parcela'] else '0,00',
                    str(item['Parcela']),
                    str(item['Dta_Vcto'].strftime("%d/%m/%Y")),
                    "L",
                    str(item['Unidade']),
                    f"{float(item['Vlr_Liquidacao']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Vlr_Liquidacao'] else '0,00',
                )
                
                self.tree.insert('', 'end', values=formatted_item)

            # Second query for TB_Faturas
            query = """
                        SELECT 
                            TB_Pessoas.Pessoas_Descricao    AS Pessoas_Descricao, 
                            Fat_Pessoa                      AS Fat_Pessoa,
                            CAST(Fat_NumDoc AS CHAR)        AS Fat_NumDoc, 
                            Fat_Vlr                         AS Fat_Vlr,        
                            Fat_Vencimento                  AS Fat_Vencimento, 
                            Fat_Data                        AS Fat_Data
                        FROM TB_Faturas
                        LEFT JOIN TB_Pessoas ON TB_Pessoas.Pessoas_CPF_CNPJ=Fat_Pessoa AND TB_Pessoas.Empresa_ID=TB_Faturas.Fat_Empresa
                        LEFT JOIN TB_UnidadesNegocio ON TB_UnidadesNegocio.Unidade_ID=TB_Faturas.Fat_IDUnidade
                        WHERE Fat_DtaBaixa IS NULL
                    """

            if self.combo_empresa.get():
                self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
                query += f" AND Fat_Empresa = '{self.id_empresa}'"

            if self.combo_pessoa.get():
                self.id_pessoa = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
                query += f" AND Fat_Pessoa = '{self.id_pessoa}'"

            query += f" AND Fat_Data BETWEEN '{self.dt_inicio}' AND '{self.dt_fim}'"

            myresult = db._querying(query)
            consulta_2 = [(consulta_2) for consulta_2 in myresult]

            if not consulta and not consulta_2:
                messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!", parent=self.window_one)
                return

            # Inserir dados na tabela
            for item in consulta_2:
                formatted_item = (
                    "",
                    str(item['Fat_Pessoa']),
                    str(item['Pessoas_Descricao']),

                    str(item['Fat_NumDoc']),

                    f"{float(item['Fat_Vlr']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Fat_Vlr'] else '0,00',
                    "1",
                    str(item['Fat_Data'].strftime("%d/%m/%Y")),
                    "F",
                    "O",
                    ""
                )
                self.tree.insert('', 'end', values=formatted_item)

        elif self.combo_baixa.get() == "CANCELAR BAIXA":
            query = """
            SELECT
                dc.Doc_Aprovacao                    AS Doc_Aprovacao,
                CAST(ii.Fin_Num_documento AS CHAR)  AS Num_Documento,
                ii.ID_Empresa                       AS ID_Empresa,
                pp.Pessoas_Descricao                AS Pessoas_Descricao,
                ii.ID_Pessoa                        AS ID_Pessoa,
                pp1.Pessoas_Descricao               AS DS_Pessoa,
                pp1.Pessoas_Tipo                    AS Tipo_Empresa,
                ii.ID_Fazenda                       AS Unidade,
                ff.Unidade_Descricao                AS Unidade_Descricao,
                ii.Fin_Parcela                      AS Parcela,
                dc.Doc_Dta_Documento                AS Dta_Vcto,
                ii.Fin_VlR_Parcela                  AS Vlr_Parcela,
                ii.Fin_Dta_Liquidacao               AS Dta_Liquidacao,
                ii.Fin_VlR_Liquidacao               AS Vlr_Liquidacao,
                ii.ID_Bco_Liquidacao                AS ID_Bco_Liquidacao
            FROM TB_Financeiro ii
            INNER JOIN TB_CB_Doc dc ON dc.ID_Empresa=ii.ID_Empresa AND dc.ID_Pessoa=ii.ID_Pessoa 
                AND dc.ID_Fazenda=ii.ID_Fazenda AND dc.Doc_Num_Documento=ii.Fin_Num_Documento
            INNER JOIN TB_Pessoas pp ON pp.Pessoas_CPF_CNPJ=ii.ID_Empresa
            INNER JOIN TB_Pessoas pp1 ON pp1.Pessoas_CPF_CNPJ=ii.ID_Pessoa
            INNER JOIN TB_UnidadesNegocio ff ON ff.Unidade_ID=ii.ID_Fazenda
            WHERE dc.Doc_Aprovacao = 'X'
            """

            if self.combo_empresa.get():
                self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get())
                query += f" AND ii.ID_Empresa = '{self.id_empresa}'"

            if self.combo_pessoa.get():
                self.id_pessoa = self.obter_Pessoa_ID(self.combo_pessoa.get())
                query += f" AND ii.ID_Pessoa = '{self.id_pessoa}'"

            query += f" AND ii.Fin_Dta_Liquidacao BETWEEN '{self.dt_inicio}' AND '{self.dt_fim}'"

            if self.somente_pend_var.get():
                query += " AND ii.Fin_Dta_Liquidacao IS NOT NULL"

            query += " ORDER BY ii.Fin_Dta_Liquidacao, ii.ID_Pessoa, ii.Fin_Num_documento, ii.Fin_Parcela"

            myresult = db._querying(query)
            consulta = [(consulta) for consulta in myresult]

            # Inserir dados na tabela
            for item in consulta:
                Dta_Liquidacao = item['Dta_Liquidacao']
                if Dta_Liquidacao not in (None, '', '0000-00-00'):
                    str(Dta_Liquidacao.strftime("%d/%m/%Y")),
                else:
                    Dta_Liquidacao = ''
                    
                formatted_item = (
                    str(Dta_Liquidacao.strftime("%d/%m/%Y")) if Dta_Liquidacao not in (None, '', '0000-00-00') else '',
                    str(item['ID_Pessoa']),
                    str(item['DS_Pessoa']) if item['DS_Pessoa'] else "Não Cadastrado!",

                    str(item['Num_Documento']),
                    f"{float(item['Vlr_Parcela']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Vlr_Parcela'] else '0,00',
                    str(item['Parcela']),
                    str(item['Dta_Vcto'].strftime("%d/%m/%Y")),
                    "L",
                    str(item['Unidade']),
                    f"{float(item['Vlr_Liquidacao']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Vlr_Liquidacao'] else '0,00',
                )
                self.tree.insert('', 'end', values=formatted_item)

            # Second query for TB_Faturas with canceled baixas
            query = """
                        SELECT 
                            TB_Pessoas.Pessoas_Descricao    AS Pessoas_Descricao, 
                            Fat_Pessoa                      AS Fat_Pessoa,
                            CAST(Fat_NumDoc AS CHAR)        AS Fat_NumDoc, 
                            Fat_VlrBaixa                    AS Fat_VlrBaixa, 
                            Fat_DtaBaixa                    AS Fat_DtaBaixa, 
                            Fat_Vlr                         AS Fat_Vlr, 
                            Fat_Vencimento                  AS Fat_Vencimento, 
                            Fat_Data                        AS Fat_Data
                        FROM TB_Faturas
                        LEFT JOIN TB_Pessoas ON TB_Pessoas.Pessoas_CPF_CNPJ = Fat_Pessoa
                        LEFT JOIN TB_UnidadesNegocio ON TB_UnidadesNegocio.Unidade_ID = TB_Faturas.Fat_IDFaz
                        WHERE Fat_DtaBaixa IS NOT NULL
                    """

            if self.combo_empresa.get():
                self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
                query += f" AND Fat_Empresa = '{self.id_empresa}'"

            if self.combo_pessoa.get():
                self.id_pessoa = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
                query += f" AND Fat_Pessoa = '{self.id_pessoa}'"

            query += f" AND Fat_DtaBaixa BETWEEN '{self.dt_inicio}' AND '{self.dt_fim}'"

            myresult = db._querying(query)
            consulta_2 = [(consulta_2) for consulta_2 in myresult]

            if not consulta and not consulta_2:
                messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!", parent=self.window_one)
                return

            # Inserir dados na tabela
            for item in consulta_2:
                Dta_Liquidacao = item['Fat_DtaBaixa']
                if Dta_Liquidacao not in (None, '', '0000-00-00'):
                    str(Dta_Liquidacao.strftime("%d/%m/%Y")),
                else:
                    Dta_Liquidacao = ''

                formatted_item = (
                    str(Dta_Liquidacao.strftime("%d/%m/%Y")) if Dta_Liquidacao not in (None, '', '0000-00-00') else '',
                    str(item['Fat_Pessoa']),
                    str(item['Pessoas_Descricao']),

                    str(item['Fat_NumDoc']),

                    f"{float(item['Fat_Vlr']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Fat_Vlr'] else '0,00',
                    "1",
                    str(item['Fat_Data'].strftime("%d/%m/%Y")),
                    "F",
                    "O",
                    f"{float(item['Fat_VlrBaixa']):,.2f}".replace(",", "v").replace(".", ",").replace("v", ".") if item['Fat_VlrBaixa'] else '0,00',

                )
                self.tree.insert('', 'end', values=formatted_item)

    def grava_bx_pagtos(self):
        self.dt_baixa   = ''
        self.id_banco   = ''
        self.id_agencia = ''
        self.nr_conta   = ''
           
        if not self.entry_banco.get():
            messagebox.showerror("Erro", "Banco, não podem ser vazio!", parent=self.window_one)
            self.entry_banco.focus()
            return
        
        if not self.entry_agencia.get():
            messagebox.showerror("Erro", "Agência não podem ser vazio!", parent=self.window_one)
            self.entry_agencia.focus()
            return
        
        if not self.entry_contacorrente.get():
            messagebox.showerror("Erro", "Conta não podem ser vazio!", parent=self.window_one)
            self.entry_contacorrente.focus()
            return

        if not self.entry_dt_baixa.get():
            messagebox.showerror("Erro", "A data de baixa não pode estar vazia.", parent=self.window_one)
            self.entry_dt_baixa.focus()
            return
        try:
            self.dt_baixa = datetime.strptime(self.entry_dt_baixa.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.", parent=self.window_one)
            self.entry_dt_baixa.focus()
            return

        self.id_banco = self.obter_banco(self.entry_banco.get(), self.window_one)

        # Validar e converter a data do documento, se estiver preenchida
        if self.entry_dt_doc.get():
            try:
                self.dt_doc = datetime.strptime(self.entry_dt_doc.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data inválido para data do documento. Use DD/MM/AAAA.", parent=self.window_one)
                self.entry_dt_doc.focus()
                return
            
        if self.combo_empresa.get():
            self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)

        if self.entry_cpf_cnpj:
            self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)

        try:
            if self.combo_baixa.get() == "EFETUAR BAIXA":
                query = f"SELECT * FROM TB_TravaLancamento WHERE Empresa_ID = '{self.id_empresa}'"

                myresult = db._querying(query)
                consulta = [(consulta) for consulta in myresult]

                if consulta:
                    dta_trava_dia = consulta[0]['Dta_Trava'].day
                    rvDta_trava_dia = f"{dta_trava_dia:02d}"
                    dta_trava_mes = consulta[0]['Dta_Trava'].month
                    rvDta_tava_mes = f"{dta_trava_mes:02d}"
                    dta_trava_ano = consulta[0]['Dta_Trava'].year
                    self.data_trava = f"{dta_trava_ano}-{rvDta_tava_mes}-{rvDta_trava_dia}"

                    if self.data_trava > self.dt_baixa:
                        messagebox.showinfo("Aviso", "Data de Baixa não pode ser anterior a data de trava do "
                                                     f"sistema - {self.data_trava}", parent=self.window_one)
                        return

                if self.dt_baixa and self.dt_doc > self.dt_baixa:
                    messagebox.showinfo("Aviso", "Data de Baixa não pode ser menor que a data do documento!", parent=self.window_one)
                    return

                if self.combo_situacao.get() == "L":
                    teste = self.entry_nr_documento.get()
                    
                    query = f"""
                        UPDATE TB_Financeiro SET 
                        Fin_Dta_Liquidacao='{self.dt_baixa}', 
                        Fin_VlR_Liquidacao={str(self.entry_valor_liquidado.get()).replace(".", "").replace(",", ".")}, 
                        ID_Bco_Liquidacao='{self.id_banco}', 
                        Fin_Agencia_Liquidacao='{self.entry_agencia.get()}', 
                        Fin_Conta_Liquidacao='{self.entry_contacorrente.get()}' 
                        WHERE ID_Empresa='{self.id_empresa}' 
                        AND ID_Pessoa='{self.entry_cpf_cnpj.get()}' 
                        AND Fin_Parcela='{self.entry_nr_parc.get()}' 
                        AND ID_Unidade='{self.entry_unidade.get()}' 
                        AND Fin_Num_documento='{self.entry_nr_documento.get()}'
                    """
                else:
                    query = f"""
                        UPDATE TB_Faturas SET 
                        Fat_DtaBaixa='{self.dt_baixa}', 
                        Fat_VlrBaixa='{str(self.entry_valor_liquidado.get()).replace(".", "").replace(",", ".")}' 
                        WHERE Fat_NumDoc='{self.entry_nr_documento.get()}' 
                        AND Fat_Pessoa='{self.entry_cpf_cnpj.get()}' 
                        AND Fat_Empresa='{self.id_empresa}'
                    """

                try:
                    myresult = db._querying(query)
                    self.limpar_campos_baixas()
                    self.consulta_titulos()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao processar a query: {str(e)}", parent=self.window_one)
                finally:
                    return
            
            elif self.combo_baixa.get() == "CANCELAR BAIXA":
                query = f"SELECT * FROM TB_TravaLancamento WHERE Empresa_ID='{self.id_empresa}'"

                myresult = db._querying(query)
                consulta = [(consulta) for consulta in myresult]

                if consulta:
                    dta_trava_dia = consulta[0]['Dta_Trava'].day
                    rvDta_trava_dia = f"{dta_trava_dia:02d}"
                    dta_trava_mes = consulta[0]['Dta_Trava'].month
                    rvDta_tava_mes = f"{dta_trava_mes:02d}"
                    dta_trava_ano = consulta[0]['Dta_Trava'].year
                    self.data_trava = f"{dta_trava_ano}-{rvDta_tava_mes}-{rvDta_trava_dia}"

                    if self.data_trava > self.dt_baixa:
                        messagebox.showinfo("Aviso", "Data de Baixa não pode ser anterior a data de trava do "
                                                     f"sistema - {self.data_trava}", parent=self.window_one)
                        return

                if self.combo_situacao.get() == "L":
                    query = f"""
                        UPDATE TB_Financeiro SET 
                        Fin_Dta_Liquidacao=NULL, 
                        Fin_VlR_Liquidacao=NULL, 
                        ID_Bco_Liquidacao=NULL, 
                        Fin_Conta_Liquidacao=NULL, 
                        Fin_Agencia_Liquidacao=NULL 
                        WHERE ID_Empresa='{self.id_empresa}' 
                        AND ID_Pessoa='{self.entry_cpf_cnpj.get()}' 
                        AND Fin_Parcela='{self.entry_nr_parc.get()}' 
                        AND ID_Fazenda='{self.entry_unidade.get()}' 
                        AND Fin_Num_documento='{self.entry_nr_documento.get()}'
                    """
                else:
                    query = f"""
                        UPDATE TB_Faturas SET 
                        Fat_DtaBaixa=NULL, 
                        Fat_VlrBaixa=NULL 
                        WHERE Fat_NumDoc='{self.entry_nr_documento.get()}' 
                        AND Fat_Pessoa='{self.entry_cpf_cnpj.get()}'
                    """

                try:
                    myresult = db._querying(query)
                    self.limpar_campos_baixas()
                    self.consulta_titulos()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao processar a query: {str(e)}", parent=self.window_one)
                finally:
                    return
                
        except Exception as e:
            messagebox.showerror("Erro", str(e), parent=self.window_one)
            return

    def lbaixas_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.entry_dt_baixa.delete(0, tk.END)
            self.entry_dt_baixa.insert(0, self.item[0])

            self.entry_cpf_cnpj.configure(state='normal')
            self.entry_cpf_cnpj.delete(0, tk.END)
            self.entry_cpf_cnpj.insert(0, self.item[1])
            self.entry_cpf_cnpj.configure(state='readonly')

            self.entry_descricao.configure(state='normal')
            self.entry_descricao.delete(0, tk.END)
            self.entry_descricao.insert(0, self.item[2])
            self.entry_descricao.configure(state='readonly')

            self.entry_nr_documento.configure(state='normal')
            self.entry_nr_documento.delete(0, tk.END)
            nr_documento = str(self.item[3]) if self.item[3] is not None else ""
            nr_documento = nr_documento.lstrip('*')  # Remove o asterisco do início
            self.entry_nr_documento.insert(0, nr_documento)
            self.entry_nr_documento.configure(state='readonly')

            self.entry_valor.configure(state='normal')
            self.entry_valor.delete(0, tk.END)
            self.entry_valor.insert(0, self.item[4])
            self.entry_valor.configure(state='readonly')

            self.entry_nr_parc.configure(state='normal')
            self.entry_nr_parc.delete(0, tk.END)
            self.entry_nr_parc.insert(0, self.item[5])
            self.entry_nr_parc.configure(state='readonly')

            self.entry_dt_doc.configure(state='normal')
            self.entry_dt_doc.delete(0, tk.END)
            self.entry_dt_doc.insert(0, self.item[6])
            self.entry_dt_doc.configure(state='readonly')

            self.combo_situacao.configure(state='normal')
            self.combo_situacao.set(self.item[7])
            self.combo_situacao.configure(state='readonly')

            self.entry_unidade.configure(state='normal')
            self.entry_unidade.delete(0, tk.END)
            self.entry_unidade.insert(0, self.item[8])
            self.entry_unidade.configure(state='readonly')

            self.entry_valor_liquidado.delete(0, tk.END)
            self.entry_valor_liquidado.insert(0, self.item[9] if self.item[9] != '0,00' else self.item[4])

    def limpar_campos_baixas(self):
        valor_decimal = '0,00'
        valor_percente = '0,00 %'
        valor_percente_taxa_vpl = '12,00 %'
        valor_m2 = '0,00  m²'
        valor_inicio = '1º mês'
        curva_basica = 'Padrão 1 Mês'
        sistema_amortizacao = 'PRICE'
        dta_atual = datetime.now()
        prazo = 1
        
        # Altera para o estado normal
        self.entry_cpf_cnpj.configure(state='normal')
        self.entry_descricao.configure(state='normal')
        self.entry_nr_documento.configure(state='normal')
        self.entry_valor.configure(state='normal')
        self.entry_nr_parc.configure(state='normal')
        self.entry_dt_doc.configure(state='normal')
        self.entry_unidade.configure(state='normal')
        
        # Limpa a entrada
        self.entry_dt_baixa.delete(0, 'end')
        self.entry_cpf_cnpj.delete(0, 'end')
        self.entry_descricao.delete(0, 'end')
        self.entry_nr_documento.delete(0, 'end')
        self.entry_valor.delete(0, 'end')
        self.entry_nr_parc.delete(0, 'end')
        self.entry_dt_doc.delete(0, 'end')
        self.combo_situacao.set('L')
        self.entry_unidade.delete(0, 'end')
        self.entry_valor_liquidado.delete(0, 'end')

        # Inserir valores padrão
        self.entry_valor.insert(0, valor_decimal.strip())
        self.entry_valor_liquidado.insert(0, valor_decimal.strip())
        
        # Altera para somente leitura os campos de entrada
        self.entry_cpf_cnpj.configure(state='readonly')
        self.entry_descricao.configure(state='readonly')
        self.entry_nr_documento.configure(state='readonly')
        self.entry_valor.configure(state='readonly')
        self.entry_nr_parc.configure(state='readonly')
        self.entry_dt_doc.configure(state='readonly')
        self.entry_unidade.configure(state='readonly')
        

BaixasFinanceiras()
