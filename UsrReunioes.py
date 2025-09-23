from UsrCadastros import *
from widgets import Widgets

class GerenciadorReunioes(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def gerenciador_reunioes(self, principal_frame):
        self.images_base64()
        self.window_one.title('Ata e Reuniões')
        self.clearFrame_principal()
        self.frame_principal = principal_frame
        self.create_widgets_gerenciador_reunioes()


    def create_widgets_gerenciador_reunioes(self):

        #CNPJ
        self.fr_cnpj_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cnpj_reuniao.place(relx=0, rely=0, relwidth=0.2, relheight=0.07)

        self.lb_cnpj_reuniao = customtkinter.CTkLabel(self.fr_cnpj_reuniao, text="CNPJ")
        self.lb_cnpj_reuniao.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_cnpj_reuniao = customtkinter.CTkEntry(self.fr_cnpj_reuniao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_cnpj_reuniao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_cnpj_reuniao.configure(state='readonly')

        # Empresa
        self.frame_empresa(self.frame_principal, 0.2, 0, 0.30, 0.07)
        self.combo_empresa.bind("<<ComboboxSelected>>", self.preencher_cnpj_reuniao)

        # Sim
        self.fr_sim_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_sim_box.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.07)

        # Sim
        self.sim_var = tk.BooleanVar()
        self.sim_cbox = customtkinter.CTkCheckBox(self.fr_sim_box, text="Sim",variable=self.sim_var)
        self.sim_cbox.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

        # Descrição (20%)
        self.fr_descricao_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_reuniao.place(relx=0.50, rely=0, relwidth=0.30, relheight=0.07)

        self.lb_descricao_reuniao = customtkinter.CTkLabel(self.fr_descricao_reuniao, text="Descrição")
        self.lb_descricao_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_reuniao = customtkinter.CTkEntry(self.fr_descricao_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_descricao_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        # Data (10%)
        self.fr_data_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_reuniao.place(relx=0.80, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_reuniao, text="Data Reunião")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, "01/01/2000")
        self.entry_dt.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Botão Gravar (10%)
        self.fr_botao_gravar_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_gravar_reuniao.place(relx=0.90, rely=0, relwidth=0.05, relheight=0.07)

        self.icone_gravar_reuniao = self.base64_to_photoimage('open_book')
        self.btn_gravar_reuniao = customtkinter.CTkButton(
            self.fr_botao_gravar_reuniao,
            image=self.icone_gravar_reuniao,
            text='',
            fg_color='transparent'
        )
        self.btn_gravar_reuniao.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        # Botão Consultar (10%)
        self.fr_botao_consulta_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_consulta_reuniao.place(relx=0.95, rely=0, relwidth=0.05, relheight=0.07)

        self.icone_pesquisa_reuniao = self.base64_to_photoimage('lupa')
        self.btn_consulta_reuniao = customtkinter.CTkButton(
            self.fr_botao_consulta_reuniao,
            image=self.icone_pesquisa_reuniao,
            text='',
            fg_color='transparent'
        )
        self.btn_consulta_reuniao.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        #Data Providência
        self.fr_data_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_reuniao.place(relx=0, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_reuniao, text="Data Providência")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, "01/01/2000")
        self.entry_dt.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Descrição Providência
        self.fr_descricao_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_reuniao.place(relx=0.1, rely=0.07, relwidth=0.30, relheight=0.07)

        self.lb_descricao_reuniao = customtkinter.CTkLabel(self.fr_descricao_reuniao, text="Descrição Providência")
        self.lb_descricao_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_reuniao = customtkinter.CTkEntry(self.fr_descricao_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_descricao_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        #Data Programada
        self.fr_data_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_reuniao.place(relx=0.4, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_reuniao, text="Data Programada")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, "01/01/2000")
        self.entry_dt.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        #Data Conclusão
        self.fr_data_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_reuniao.place(relx=0.5, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_reuniao, text="Data Conclusão")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, "01/01/2000")
        self.entry_dt.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Responsável
        self.fr_descricao_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_reuniao.place(relx=0.6, rely=0.07, relwidth=0.30, relheight=0.07)

        self.lb_descricao_reuniao = customtkinter.CTkLabel(self.fr_descricao_reuniao, text="Responsável")
        self.lb_descricao_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_reuniao = customtkinter.CTkEntry(self.fr_descricao_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_descricao_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        # Botão Salvar (10%)
        self.fr_botao_salvar_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_salvar_reuniao.place(relx=0.90, rely=0.07, relwidth=0.05, relheight=0.07)

        self.icone_salvar_reuniao = self.base64_to_photoimage('save')
        self.btn_salvar_reuniao = customtkinter.CTkButton(
            self.fr_botao_salvar_reuniao,
            image=self.icone_salvar_reuniao,
            text='',
            fg_color='transparent'
        )
        self.btn_salvar_reuniao.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        # Log
        self.fr_botao_consulta_log = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_consulta_log.place(relx=0.95, rely=0.07, relwidth=0.05, relheight=0.07)

        self.icone_pesquisa_log = self.base64_to_photoimage('open_book')
        self.btn_consulta_log = customtkinter.CTkButton(
            self.fr_botao_consulta_log,
            image=self.icone_pesquisa_log,
            text='',
            fg_color='transparent'
        )
        self.btn_consulta_log.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)


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

        headers = ["Tar", "Log", "Descrição", "Tipo", "Data Inclusão",
            "Data Programada", "Data Conlusão", "Responsável",]

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

    def preencher_cnpj_reuniao(self, event):
        empresa_selecionada = self.combo_empresa.get()
        self.carregar_reuniao()

        if empresa_selecionada:
            cnpj = self.empresas_dict.get(empresa_selecionada)

            if cnpj:
                self.entry_cnpj_reuniao.delete(0, 'end')
                self.entry_cnpj_reuniao.insert(0, cnpj)
            else:
                # Se não encontrar o CNPJ, limpa o campo
                self.entry_cnpj_reuniao.delete(0, 'end')
        else:
            # Se nenhuma empresa estiver selecionada, limpa o campo
            self.entry_cnpj_reuniao.delete(0, 'end')


    def carregar_reuniao(self):
        try:
            cnpj_empresa = self.entry_cnpj_reuniao.get().strip()

            if not cnpj_empresa:
                self.combo_descricao_reuniao.configure(values=[])
                self.combo_descricao_reuniao.set("")
                self.entry_cnpj_reuniao.delete(0, 'end')
                return

            str_sql = f"""
                SELECT Reuniao_ID, Reuniao_DS 
                FROM reuniao_cadastro 
                WHERE Empresa_ID = '{cnpj_empresa}'
                ORDER BY Reuniao_DS
            """

            myresult = db._querying(str_sql)

            if myresult:
                self.reuniao_dict = {}
                descricoes = []

                for reuniao in myresult:
                    reuniao_id = reuniao['Reuniao_ID']
                    reuniao_descricao = reuniao['Reuniao_DS']
                    self.reuniao_dict[reuniao_descricao] = reuniao_id
                    descricoes.append(reuniao_descricao)

                self.combo_descricao_reuniao.configure(values=descricoes)

                if descricoes:
                    self.combo_descricao_reuniao.set(descricoes[0])
                    self.atualizar_codigo_reuniao()
            else:
                self.combo_descricao_reuniao.configure(values=[])
                self.combo_descricao_reuniao.set("")
                self.entry_codigo_reuniao.delete(0, 'end')
                messagebox.showinfo("Info", "Nenhuma reunião encontrada!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar reuniões: {str(e)}")

    