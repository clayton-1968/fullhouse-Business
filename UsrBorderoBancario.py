from UsrCadastros import *
from widgets import Widgets

class BorderoBancario(Widgets, Pessoas, Produtos, Icons):

    def consultar_bordero(self, principal_frame):
        self.images_base64()

        self.window_one.title('Borderô Bancário')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_bordero()

    def create_widgets_bordero(self):
        # Data Vcto
        self.fr_dt_vcto = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)

        self.fr_dt_vcto.place(relx=0, rely=0, relwidth=0.14, relheight=0.09)

        self.lb_dt_vcto = customtkinter.CTkLabel(self.fr_dt_vcto, text="Data Vcto")
        self.lb_dt_vcto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        # Data inicio
        self.lb_dt_inicio = customtkinter.CTkLabel(self.fr_dt_vcto, text="Data Início")

        self.lb_dt_inicio.place(relx=0.10, rely=0.28, relheight=0.15, relwidth=0.35)

        self.entry_dt_inicio = customtkinter.CTkEntry(self.fr_dt_vcto, fg_color="white", text_color="black",
                                                      justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_inicio,
                                                                                   self.entry_dt_inicio))
        # Data fim
        self.lb_dt_fim = customtkinter.CTkLabel(self.fr_dt_vcto, text="Data Fim")

        self.lb_dt_fim.place(relx=0.55, rely=0.28, relheight=0.15, relwidth=0.35)

        self.entry_dt_fim = customtkinter.CTkEntry(self.fr_dt_vcto, fg_color="white", text_color="black",
                                                   justify=tk.CENTER)
        self.entry_dt_fim.delete(0, 'end')
        self.entry_dt_fim.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_fim))
        self.entry_dt_fim.bind("<Return>",
                               lambda event: self.muda_barrinha_dta(event, self.entry_dt_fim, self.entry_dt_fim))

        # Origem
        self.fr_origem = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_origem.place(relx=0.145, rely=0.0, relwidth=0.15, relheight=0.07)

        self.lb_origem = customtkinter.CTkLabel(self.fr_origem, text="Origem")
        self.lb_origem.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_origem = customtkinter.CTkOptionMenu(self.fr_origem, values=["A RECEBER", "A PAGAR"], fg_color="white",
                                                       text_color="black")
        self.combo_origem.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Situação
        self.fr_situacao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_situacao.place(relx=0.3, rely=0, relwidth=0.15, relheight=0.07)

        self.lb_situacao = customtkinter.CTkLabel(self.fr_situacao, text="Situação")
        self.lb_situacao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_situacao = customtkinter.CTkOptionMenu(self.fr_situacao, values=["TODOS", "EM ABERTO", "LIQUIDADOS"], fg_color="white",
                                                       text_color="black")
        self.combo_situacao.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Botão de consulta
        self.fr_botao_consulta = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_consulta.place(relx=0.455, rely=0, relwidth=0.05, relheight=0.07)

        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botao_consulta, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_bordero)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.25, rely=0.25, relwidth=0.50, relheight=0.5)


        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.095, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Origem", "Fornecedor/Cliente", "Nr. Documento",
            "Valor do título", "Vencimento", "Data liquidação", "Informações Liquidação",
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

        col_widths = [10, 20, 10, 10, 10, 10, 500]
        headers = ["Origem", "Fornecedor/Cliente", "Nr. Documento",
            "Valor do título", "Vencimento", "Data liquidação", "Informações Liquidação"]

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


    def consulta_bordero(self):
        pass

BorderoBancario()
