from UsrCadastros import *
from widgets import Widgets

class PermissoesSistema(Widgets, Pessoas, Produtos, Icons):
    def permissoes_sistema(self, principal_frame):
        self.images_base64()

        self.window_one.title('Permissões do Sistema')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_permissoes_sistema()

    def create_widgets_permissoes_sistema(self):
        # Login
        self.fr_login_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_login_permissoes.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_login_permissoes = customtkinter.CTkLabel(self.fr_login_permissoes, text="Login")
        self.lb_login_permissoes.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.25)

        self.entry_login_permissoes = customtkinter.CTkEntry(self.fr_login_permissoes, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_login_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nome Completo
        self.fr_nome_completo_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nome_completo_permissoes.place(relx=0.105, rely=0, relwidth=0.2, relheight=0.07)

        self.lb_nome_completo_permissoes = customtkinter.CTkLabel(self.fr_nome_completo_permissoes, text="Nome Completo")
        self.lb_nome_completo_permissoes.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_nome_completo_permissoes = customtkinter.CTkEntry(self.fr_nome_completo_permissoes, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_nome_completo_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # E-mail
        self.fr_email_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_email_permissoes.place(relx=0.31, rely=0, relwidth=0.25, relheight=0.07)

        self.lb_email_permissoes = customtkinter.CTkLabel(self.fr_email_permissoes, text="E-mail")
        self.lb_email_permissoes.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_email_permissoes = customtkinter.CTkEntry(self.fr_email_permissoes, fg_color="white", text_color="black",
                                                                     justify=tk.LEFT)
        self.entry_email_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Botão de consulta
        self.fr_botoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botoes.place(relx=0.565, rely=0, relwidth=0.075, relheight=0.07)

        # Lupa
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botoes, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_permissoes)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.6)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botoes, image=icone_salvar, text='',
                                                    fg_color='transparent', command=self.salvar_permissoes)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # Item
        self.fr_item_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_item_permissoes.place(relx=0, rely=0.075, relwidth=0.07, relheight=0.07)

        self.lb_item_permissoes = customtkinter.CTkLabel(self.fr_item_permissoes, text="Item")
        self.lb_item_permissoes.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.25)

        self.entry_item_permissoes = customtkinter.CTkEntry(self.fr_item_permissoes, fg_color="white", text_color="black",
                                                             justify=tk.LEFT)
        self.entry_item_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Empresa
        self.fr_empresa_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_empresa_permissoes.place(relx=0.075, rely=0.075, relwidth=0.3, relheight=0.07)

        self.lb_empresa_permissoes = customtkinter.CTkLabel(self.fr_empresa_permissoes, text="Empresa")
        self.lb_empresa_permissoes.place(relx=0.15, rely=0, relwidth=0.7, relheight=0.25)

        self.entry_empresa_permissoes = customtkinter.CTkEntry(self.fr_empresa_permissoes, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_empresa_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # C. Resultado
        self.fr_resultado_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_resultado_permissoes.place(relx=0.38, rely=0.075, relwidth=0.3, relheight=0.07)

        self.lb_resultado_permissoes = customtkinter.CTkLabel(self.fr_resultado_permissoes, text="C. Resultado")
        self.lb_resultado_permissoes.place(relx=0.15, rely=0, relwidth=0.7, relheight=0.25)

        self.entry_resultado_permissoes = customtkinter.CTkEntry(self.fr_resultado_permissoes, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_resultado_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Modulos
        self.fr_modulos_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_modulos_permissoes.place(relx=0.685, rely=0.075, relwidth=0.15, relheight=0.07)

        self.lb_modulos_permissoes = customtkinter.CTkLabel(self.fr_modulos_permissoes, text="Modulos")
        self.lb_modulos_permissoes.place(relx=0.15, rely=0, relwidth=0.7, relheight=0.25)

        self.entry_modulos_permissoes = customtkinter.CTkEntry(self.fr_modulos_permissoes, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_modulos_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nivel
        self.fr_nivel_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nivel_permissoes.place(relx=0.84, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_nivel_permissoes = customtkinter.CTkLabel(self.fr_nivel_permissoes, text="Nível")
        self.lb_nivel_permissoes.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.25)

        self.entry_nivel_permissoes = customtkinter.CTkEntry(self.fr_nivel_permissoes, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_nivel_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Status
        self.fr_status_permissoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_status_permissoes.place(relx=0.945, rely=0.075, relwidth=0.05, relheight=0.07)

        self.lb_status_permissoes = customtkinter.CTkLabel(self.fr_status_permissoes, text="Status")
        self.lb_status_permissoes.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_status_permissoes = customtkinter.CTkEntry(self.fr_status_permissoes, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_status_permissoes.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "ID", "Empresa", "Código", "Descrição Centro", "Módulo do Sistema", "Nível", "Status"
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

        col_widths = [10, 30, 10, 30, 15, 10, 10]
        headers = ["ID", "Empresa", "Código", "Descrição Centro", "Módulo do Sistema", "Nível", "Status"]

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

        self.tree.bind("<Double-1>", self.lpermissoes_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)


    def consulta_permissoes(self):
        self.tree.delete(*self.tree.get_children())

        query = """
            SELECT 
                PP.Permissao_Cod AS Codigo,
                PP.UsR_Login AS Usr_Login,
                PP.Empresa_ID AS Empresa_ID,
                ee.Pri_Descricao AS Empresa_DS,
                PP.Permissao_CC AS Centro_ID,
                COALESCE(cc.Cen_Descricao, '') AS Centro_DS,
                PP.Permissao_Modulo AS Modulo,
                PP.Permissao_Tipo AS Tipo,
                PP.Permissao_Status AS Status
            FROM 
                TB_Permissoes AS PP
            LEFT JOIN 
                centrocusto cc ON cc.Cen_ID = PP.Permissao_CC AND cc.Empresa_ID = PP.Empresa_ID
            LEFT JOIN 
                TB_Empresas ee ON ee.Pri_Cnpj = PP.Empresa_ID
            ORDER BY 
                ee.Pri_Descricao;
        """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Nenhum usuário encontrado.", parent=self.frame_principal)
            return

        # Inserir dados na tabela
        for item in consulta:
            formatted_item = (
                str(item['Codigo']),
                str(item['Empresa_DS']),
                str(item['Centro_ID']),
                str(item['Centro_DS']),
                str(item['Modulo']),
                str(item['Tipo']),
                str(item['Status']),
            )
            self.tree.insert('', 'end', values=formatted_item)


    def salvar_permissoes(self):

        if self.entry_login_permissoes.get() == '':
            messagebox.showinfo("Aviso", "Campo login não pode ser vazio.", parent=self.frame_principal)
            return

        try:
            db.begin_transaction()
            senha_padrao = 'c6*L@48p'
            hash_senha_padrao = hashlib.md5(senha_padrao.encode()).hexdigest()

            query = """
                    INSERT INTO TB_Permissoes (UsR_Login, Empresa_ID, Permissao_CC, Permissao_Modulo, Permissao_Tipo, Permissao_Status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) \
                    """

            valores = (self.entry_login_permissoes.get(), self.entry_empresa_permissoes.get(), self.entry_resultado_permissoes.get(),
                       self.entry_modulos_permissoes.get(), self.entry_nivel_permissoes.get(), self.entry_status_permissoes.get())

            db.executar_consulta(query, valores)
            db.commit_transaction()

            messagebox.showinfo("Aviso", "Permissão criada com sucesso!", parent=self.frame_principal)
        except:
            messagebox.showerror("Erro", "Erro ao salvar nova permissão!", parent=self.frame_principal)
            return

    def lpermissoes_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.entry_item_permissoes.configure(state='normal')
            self.entry_item_permissoes.delete(0, tk.END)
            self.entry_item_permissoes.insert(0, self.item[0])
            self.entry_item_permissoes.configure(state='readonly')

            self.entry_empresa_permissoes.configure(state='normal')
            self.entry_empresa_permissoes.delete(0, tk.END)
            self.entry_empresa_permissoes.insert(0, self.item[1])
            self.entry_empresa_permissoes.configure(state='readonly')

            self.entry_resultado_permissoes.configure(state='normal')
            self.entry_resultado_permissoes.delete(0, tk.END)
            self.entry_resultado_permissoes.insert(0, self.item[2])
            self.entry_resultado_permissoes.configure(state='readonly')

            self.entry_modulos_permissoes.configure(state='normal')
            self.entry_modulos_permissoes.delete(0, tk.END)
            self.entry_modulos_permissoes.insert(0, self.item[4])
            self.entry_modulos_permissoes.configure(state='readonly')

            self.entry_nivel_permissoes.configure(state='normal')
            self.entry_nivel_permissoes.delete(0, tk.END)
            self.entry_nivel_permissoes.insert(0, self.item[5])
            self.entry_nivel_permissoes.configure(state='readonly')

            self.entry_status_permissoes.configure(state='normal')
            self.entry_status_permissoes.delete(0, tk.END)
            self.entry_status_permissoes.insert(0, self.item[6])
            self.entry_status_permissoes.configure(state='readonly')