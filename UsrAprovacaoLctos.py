import customtkinter

from UsrCadastros import *
from widgets import Widgets


class AprovacaoLctos(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def aprovacao_lctos(self, principal_frame):
        self.images_base64()

        self.window_one.title('Aprovação de Lançamentos Financeiros')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_aprovacao_lctos()

    def create_widgets_aprovacao_lctos(self):
        # Empresa

        self.frame_empresa(self.frame_principal, 0, 0, 0.30, 0.07)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))
        # self.combo_empresa.bind("<<ComboboxSelected>>", self.preenche_cnpj)

        # CNPJ
        # self.fr_cnpj = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        # self.fr_cnpj.place(relx=0.31, rely=0.02, relwidth=0.10, relheight=0.09)

        # self.lb_cnpj = customtkinter.CTkLabel(self.fr_cnpj, text="CPF/CNPJ")
        # self.lb_cnpj.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        # self.entry_cnpj = customtkinter.CTkEntry(self.fr_cnpj, fg_color="white", text_color="black",
        #                                                    justify=tk.RIGHT)
        # self.entry_cnpj.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Unidade de Negócio
        self.fr_unidade_negocio = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_unidade_negocio.place(relx=0.305, rely=0, relwidth=0.17, relheight=0.07)


        self.lb_unidade_negocio = customtkinter.CTkLabel(self.fr_unidade_negocio, text="Unidade Negócios")
        self.lb_unidade_negocio.place(relx=0.225, rely=0, relheight=0.25, relwidth=0.55)

        unidade_negocios = []
        self.entry_unidade_negocio = AutocompleteCombobox(self.fr_unidade_negocio, width=30, font=('Times', 11),
                                                          completevalues=unidade_negocios)
        self.entry_unidade_negocio.pack()
        self.entry_unidade_negocio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_unidade_negocio.bind("<Button-1>", lambda event:
        self.atualizar_unidade_negocios(event, self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one),
                                        self.entry_unidade_negocio))
        self.entry_unidade_negocio.bind('<Down>', lambda event:
        self.atualizar_unidade_negocios(event, self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one),
                                        self.entry_unidade_negocio))

        # Centro de Resultado
        self.fr_centro = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_centro.place(relx=0, rely=0.075, relwidth=0.4925, relheight=0.07)


        self.lb_centro = customtkinter.CTkLabel(self.fr_centro, text="Centro de Resultado")
        self.lb_centro.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        centro = []
        self.entry_centro = AutocompleteCombobox(self.fr_centro, width=30, font=('Times', 11), completevalues=centro)
        self.entry_centro.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_centro.bind("<Button-1>",
                               lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(
                                   self.combo_empresa.get(), self.window_one),
                                                                             self.entry_centro))
        self.entry_centro.bind('<Down>',
                               lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(
                                   self.combo_empresa.get(), self.window_one),
                                                                             self.entry_centro))
        self.entry_centro.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_natureza))

        # Natureza
        self.fr_natureza = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_natureza.place(relx=0.4975, rely=0.075, relwidth=0.4725, relheight=0.07)
        self.lb_natureza = customtkinter.CTkLabel(self.fr_natureza, text="Natureza Financeira")
        self.lb_natureza.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        natureza = []
        self.entry_natureza = AutocompleteCombobox(self.fr_natureza, width=30, font=('Times', 11),
                                                   completevalues=natureza)
        self.entry_natureza.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_natureza.bind("<Button-1>", lambda event: self.atualizar_natureza_financeira(event,
                                                                                                self.obter_Empresa_ID(
                                                                                                    self.combo_empresa.get(),
                                                                                                    self.window_one),
                                                                                                self.entry_natureza))
        self.entry_natureza.bind('<Down>', lambda event: self.atualizar_natureza_financeira(event,
                                                                                            self.obter_Empresa_ID(
                                                                                                self.combo_empresa.get(),
                                                                                                self.window_one),
                                                                                            self.entry_natureza))
        self.entry_natureza.bind("<Return>", lambda event: self.muda_barrinha(event, None))

        # Data
        self.fr_data = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_data.place(relx=0.48, rely=0, relwidth=0.14, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data, text="Data")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt.place(relx=0.275, rely=0.35, relwidth=0.485, relheight=0.50)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Frame botão consulta e aprovados
        self.fr_botao_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_botao_box.place(relx=0.625, rely=0, relwidth=0.24, relheight=0.07)

        # Box aprovados
        self.aprovados_var = tk.BooleanVar()
        self.aprovados_cbox = customtkinter.CTkCheckBox(self.fr_botao_box, text="Aprovados",
                                                        variable=self.aprovados_var)
        self.aprovados_cbox.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.5)

        # Botão de consulta
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botao_box, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_aprovacoes)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.5)

        # Botão Sair da aprovação
        icon_image = self.base64_to_photoimage('sair')
        self.btn_sair_aprovacao = customtkinter.CTkButton(self.frame_principal, text='Sair', image=icon_image, fg_color='transparent', command=self.tela_principal)
        self.btn_sair_aprovacao.pack(pady=10)
        self.btn_sair_aprovacao.place(relx=0.955, rely=0.02, relwidth=0.04, relheight=0.05)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_tree.place(relx=0.005, rely=0.15, relwidth=0.99, relheight=0.875)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Unid_ID",
            "Centro_ID",
            "Natureza_ID",
            "Pessoa_ID",
            "Pessoas_Descricao",
            "Nr_Documento",
            "Valor",
            "Status"),
                                 show='headings')
        # "CpfCnpj", "Descricao", "Unid_ID", "Unidade_Negocio", "Centro_ID", "Centro_Resultado", "Natureza_ID",
        # "Natureza_Financeira", "Valor", "Nr_Documento", "Status", "Anexo"), show='headings')

        # Atualiza o layout
        self.tree.update_idletasks()

        # Adequa as colunas ao conteudo
        for col in self.tree["columns"]:
            largura_max = tk.font.Font().measure(col)

            for item in self.tree.get_children():
                valor = self.tree.set(item, col)
                largura = tk.font.Font().measure(valor)
                if largura > largura_max:
                    largura_max = largura

            self.tree.column(col, width=largura_max + 20)

        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color,
                            borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        col_widths = [10, 10, 10, 10, 30, 10, 20, 5]
        headers = ["Unidade", "Centro", "Natureza", "CNPJ/CPF", "Descricao", "Nr. Documento", "Valor", "Status"]

        for col, header, width in zip(self.tree['columns'], headers, col_widths):
            self.tree.heading(col, text=header)
            self.tree.column(col, width=width, anchor='e')

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind("<Double-1>", self.aprovar_documento)

        # Scroll
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.rowconfigure(0, weight=1)
        self.fr_tree.columnconfigure(0, weight=1)

    def aprovar_documento(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            try:
                self.item = self.tree.item(self.selected_item)


                self.doc_id = self.item['values'][5]

                query = f"""
                    UPDATE TB_Itens SET Doc_AprovacaoJose = 'S', Doc_AprovacaoZe = 'S' 
                    WHERE Doc_Num_Documento = "{self.doc_id}"
                """

                myresult = db._querying(query)

                self.item['values'][7] = 'S'

                self.tree.item(self.selected_item, values=self.item['values'])

                messagebox.showinfo("Aviso", "Documento aprovado!", parent=self.window_one)
            except:
                messagebox.showerror("Erro", "Ocorreu um erro ao tentar aprovar um documento!", parent=self.window_one)
                return

    def consulta_aprovacoes(self):
        self.tree.delete(*self.tree.get_children())

        query = """
                    SELECT DISTINCT ID_Unidade, ID_CR, ID_Natureza, ID_Pessoa, Pessoas_Descricao,
                    Doc_Num_Documento, Vlr_Total, Doc_AprovacaoJose
                    FROM TB_Itens
                    LEFT JOIN TB_Pessoas ON TB_Itens.ID_Pessoa = TB_Pessoas.Pessoas_CPF_CNPJ
                    WHERE 1=1
        """

        if self.combo_empresa.get():
            self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
            query += f' AND ID_Empresa = "{self.id_empresa}"'

        if self.entry_unidade_negocio.get():
            self.id_unidade = self.obter_Unidade_ID(self.entry_unidade_negocio.get(), self.window_one)
            query += f' AND ID_Unidade = "{self.id_unidade}"'

        if self.entry_centro.get():
            self.id_cr = self.obter_Centro_ID(self.entry_centro.get(), self.window_one)
            query += f' AND ID_CR = "{self.id_cr}"'

        if self.entry_natureza.get():
            self.id_natureza = self.obter_Natureza_ID(self.entry_natureza.get(), self.window_one)
            query += f' AND ID_Natureza = "{self.id_natureza}"'

        if self.aprovados_var.get():
            query += ' AND Doc_AprovacaoJose = "S" AND Doc_AprovacaoZe = "S"'
        else:
            query += ' AND Doc_AprovacaoJose = "N" AND Doc_AprovacaoZe = "N"'

        # O CAMPO DATA NÃO ESTÁ SENDO FILTRADO PORQUE NÃO TEMOS O CAMPO NA TABELA

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!", parent=self.window_one)
            return

        # Inserir dados na tabela

        for item in consulta:
            formatted_item = (
                str(item['ID_Unidade']),
                str(item['ID_CR']),
                str(item['ID_Natureza']),
                str(item['ID_Pessoa']),
                str(item['Pessoas_Descricao']),
                str(item['Doc_Num_Documento']),
                f"{float(str(item['Vlr_Total'])):,.2f}".replace(",", "v").replace(".", ",").replace("v", "."),
                str(item['Doc_AprovacaoJose']),
            )
            self.tree.insert('', 'end', values=formatted_item)