from UsrCadastros import *
from widgets import Widgets


class InformeGestao(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def informe_gestao(self, principal_frame):
        self.images_base64()

        self.window_one.title('Relatório Informe de Gestão')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_info_gestao()

    def create_widgets_info_gestao(self):
        # CNPJ
        self.fr_cnpj_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cnpj_info_gestao.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_cnpj_info_gestao = customtkinter.CTkLabel(self.fr_cnpj_info_gestao, text="CNPJ")
        self.lb_cnpj_info_gestao.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_cnpj_info_gestao = customtkinter.CTkEntry(self.fr_cnpj_info_gestao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_cnpj_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nome (Empresa)
        self.frame_empresa(self.frame_principal, 0.105, 0, 0.30, 0.07)

        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_banco))

        # Código Orçamento
        self.fr_codigo_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_codigo_info_gestao.place(relx=0.41, rely=0, relwidth=0.075, relheight=0.07)

        self.lb_codigo_info_gestao = customtkinter.CTkLabel(self.fr_codigo_info_gestao, text="Código Orçamento")
        self.lb_codigo_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_codigo_info_gestao = customtkinter.CTkEntry(self.fr_codigo_info_gestao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_codigo_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Descrição Orçamento
        self.fr_descricao_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_info_gestao.place(relx=0.485, rely=0, relwidth=0.20, relheight=0.07)

        self.lb_descricao_info_gestao = customtkinter.CTkLabel(self.fr_descricao_info_gestao, text="Descrição Orçamento")
        self.lb_descricao_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_info_gestao = customtkinter.CTkEntry(self.fr_descricao_info_gestao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_descricao_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Código Unid. Negócios
        self.fr_codigo_un_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_codigo_un_info_gestao.place(relx=0.69, rely=0, relwidth=0.075, relheight=0.07)

        self.lb_codigo_un_info_gestao = customtkinter.CTkLabel(self.fr_codigo_un_info_gestao, text="Código Unid. Negócios")
        self.lb_codigo_un_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_codigo_un_info_gestao = customtkinter.CTkEntry(self.fr_codigo_un_info_gestao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_codigo_un_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Descrição Unid. Negócios
        self.fr_descricao_un_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_un_info_gestao.place(relx=0.77, rely=0, relwidth=0.20, relheight=0.07)

        self.lb_descricao_un_info_gestao = customtkinter.CTkLabel(self.fr_descricao_un_info_gestao, text="Descrição Unid. Negócios")
        self.lb_descricao_un_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_un_info_gestao = customtkinter.CTkEntry(self.fr_descricao_un_info_gestao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_descricao_un_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Data Inicio
        self.fr_data_inicio_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_data_inicio_info_gestao.place(relx=0, rely=0.075, relwidth=0.10, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_inicio_info_gestao, text="Data Início")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_inicio_info_gestao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt.place(relx=0.275, rely=0.35, relwidth=0.485, relheight=0.50)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Frame botão R$/Mil
        self.fr_rs_mil_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_rs_mil_box.place(relx=0.105, rely=0.075, relwidth=0.10, relheight=0.07)

        # Box R$/Mil
        self.rs_mil_var = tk.BooleanVar()
        self.rs_mil_cbox = customtkinter.CTkCheckBox(self.fr_rs_mil_box, text="R$/Mil",
                                                        variable=self.rs_mil_var)
        self.rs_mil_cbox.place(relx=0.05, rely=0.25, relwidth=0.95, relheight=0.5)

        # Frame botão Acumul.
        self.fr_acumul_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_acumul_box.place(relx=0.21, rely=0.075, relwidth=0.10, relheight=0.07)

        # Box Acumul.
        self.acumul_var = tk.BooleanVar()
        self.acumul_cbox = customtkinter.CTkCheckBox(self.fr_acumul_box, text="Acumul.",
                                                        variable=self.acumul_var)
        self.acumul_cbox.place(relx=0.05, rely=0.25, relwidth=0.95, relheight=0.5)

        # Frame botões
        self.fr_botoes_info_gestao_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_botoes_info_gestao_box.place(relx=0.315, rely=0.075, relwidth=0.55, relheight=0.07)

        # Box Receitas
        self.receitas_var = tk.BooleanVar()
        self.receitas_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Receitas",
                                                        variable=self.receitas_var)
        self.receitas_cbox.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.5)

        # Box Custos
        self.custos_var = tk.BooleanVar()
        self.custos_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Custos",
                                                        variable=self.custos_var)
        self.custos_cbox.place(relx=0.205, rely=0.25, relwidth=0.15, relheight=0.5)

        # Box Despesas
        self.despesas_var = tk.BooleanVar()
        self.despesas_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Despesas",
                                                        variable=self.despesas_var)
        self.despesas_cbox.place(relx=0.36, rely=0.25, relwidth=0.15, relheight=0.5)

        # Box Investimentos
        self.investimentos_var = tk.BooleanVar()
        self.investimentos_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Investimentos",
                                                        variable=self.investimentos_var)
        self.investimentos_cbox.place(relx=0.515, rely=0.25, relwidth=0.15, relheight=0.5)

        # Box Estoques
        self.estoques_var = tk.BooleanVar()
        self.estoques_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Estoques",
                                                        variable=self.estoques_var)
        self.estoques_cbox.place(relx=0.67, rely=0.25, relwidth=0.15, relheight=0.5)

        # Box Ativos/Passivos
        self.ativos_pass_var = tk.BooleanVar()
        self.ativos_pass_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Ativos/Passivos",
                                                        variable=self.ativos_pass_var)
        self.ativos_pass_cbox.place(relx=0.825, rely=0.25, relwidth=0.15, relheight=0.5)

        # Frame botão Consultar
        self.fr_botao_consulta_info_ges = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_botao_consulta_info_ges.place(relx=0.87, rely=0.075, relwidth=0.10, relheight=0.07)

        # Botão de consulta
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta_info_gestao = customtkinter.CTkButton(self.fr_botao_consulta_info_ges, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_infos_gestao)
        self.btn_consulta_info_gestao.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta_info_gestao.pack(pady=10)
        self.btn_consulta_info_gestao.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.5)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_tree.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Código", "Descrição", "Real>>Jul", "Orc.>>Jul", "Var. Mês",
            "Real Acumu.>>Jul", "Orc. Acumu.>>Jul", "Var. Acumu",
        ), show='headings')

        # Atualiza o layout
        self.tree.update_idletasks()

        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color,
                            borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        col_widths = [10, 30, 10, 10, 10, 10, 10, 10]

        headers = ["Código", "Descrição", "Real>>Jul", "Orc.>>Jul", "Var. Mês",
            "Real Acumu.>>Jul", "Orc. Acumu.>>Jul", "Var. Acumu",]

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

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)

    def consulta_infos_gestao(self):
        pass