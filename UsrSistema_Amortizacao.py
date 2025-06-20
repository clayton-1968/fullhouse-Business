from UsrCadastros import *
from widgets import Widgets

class SistemaAmortizacao(Widgets, Pessoas, Produtos, Icons):

    def consultar_amortizacao(self, principal_frame):
        self.images_base64()

        self.window_one.title('Sistema Amortização')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_amortizacao()

    def create_widgets_amortizacao(self):
        # Código
        self.fr_codigo_amortizacao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_codigo_amortizacao.place(relx=0, rely=0, relwidth=0.2, relheight=0.07)

        self.lb_codigo_amortizacao = customtkinter.CTkLabel(self.fr_codigo_amortizacao, text="Código")
        self.lb_codigo_amortizacao.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_codigo_amortizacao = customtkinter.CTkEntry(self.fr_codigo_amortizacao, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_codigo_amortizacao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Descrição
        self.fr_descricao_amortizacao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_amortizacao.place(relx=0.205, rely=0, relwidth=0.3, relheight=0.07)

        self.lb_descricao_amortizacao = customtkinter.CTkLabel(self.fr_descricao_amortizacao, text="Descrição")
        self.lb_descricao_amortizacao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_amortizacao = customtkinter.CTkEntry(self.fr_descricao_amortizacao, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_descricao_amortizacao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Botão de consulta
        self.fr_botoes_amortizacao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                                border_width=1)
        self.fr_botoes_amortizacao.place(relx=0.51, rely=0, relwidth=0.1, relheight=0.07)

        # Lupa
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botoes_amortizacao, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_amortizacao)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.6)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botoes_amortizacao, image=icone_salvar, text='',
                                                  fg_color='transparent', command=self.salva_amortizacao)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.075, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "ID", "Descrição",
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

        col_widths = [10, 45]
        headers = ["ID", "Descrição"]

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

        self.tree.bind("<Double-1>", self.lamortizacao_sistema_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)


    def consulta_amortizacao(self):
        self.tree.delete(*self.tree.get_children())

        query = """
                SELECT Sistema_ID as Codigo, Tipo_Sistema_Amortizacao as Descricao FROM Sistemas_Amortizacao 
                ORDER BY Codigo;
                """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Nenhum sistema de amortização encontrado.", parent=self.frame_principal)
            return

        # Inserir dados na tabela
        for item in consulta:
            formatted_item = (
                str(item['Codigo']),
                str(item['Descricao']),
            )
            self.tree.insert('', 'end', values=formatted_item)


    def salva_amortizacao(self):
        if self.entry_codigo_amortizacao.get() == '':
            messagebox.showinfo("Aviso", "Campo código não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_descricao_amortizacao.get() == '':
            messagebox.showinfo("Aviso", "Campo descrição não pode ser vazio.", parent=self.frame_principal)
            return

        try:
            db.begin_transaction()

            query = """
                    INSERT INTO Sistemas_Amortizacao (Sistema_ID, Tipo_Sistema_Amortizacao)
                    VALUES (%s, %s)
                    """

            valores = (self.entry_codigo_amortizacao.get(), self.entry_descricao_amortizacao.get())

            db.executar_consulta(query, valores)
            db.commit_transaction()

            messagebox.showinfo("Aviso", "Sistemas de amortização criado com sucesso!", parent=self.frame_principal)
        except:
            messagebox.showerror("Erro", "Erro ao salvar novo sistema de amortização!", parent=self.frame_principal)
            return

    def lamortizacao_sistema_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.entry_codigo_amortizacao.configure(state='normal')
            self.entry_codigo_amortizacao.delete(0, tk.END)
            self.entry_codigo_amortizacao.insert(0, self.item[0])

            self.entry_descricao_amortizacao.configure(state='normal')
            self.entry_descricao_amortizacao.delete(0, tk.END)
            self.entry_descricao_amortizacao.insert(0, self.item[1])
