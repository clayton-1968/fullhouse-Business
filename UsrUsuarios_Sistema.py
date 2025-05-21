from UsrCadastros import *
from widgets import Widgets

class UsuariosSistema(Widgets, Pessoas, Produtos, Icons):
    def usuarios_sistema(self, principal_frame):
        self.images_base64()

        self.window_one.title('Usuarios Sistema')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_usuarios_sistema_widgets()


    def create_usuarios_sistema_widgets(self):
        # ID
        self.fr_id_user_sistema = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_id_user_sistema.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_id_user_sistema = customtkinter.CTkLabel(self.fr_id_user_sistema, text='ID')
        self.lb_id_user_sistema.place(relx=0.45, rely=0, relwidth=0.1, relheight=0.55)

        self.entry_id_user_sistema = customtkinter.CTkEntry(self.fr_id_user_sistema, fg_color="gray", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_id_user_sistema.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_id_user_sistema.configure(state='readonly')

        # Login
        self.fr_login_user_sistema = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_login_user_sistema.place(relx=0.105, rely=0, relwidth=0.2, relheight=0.07)

        self.lb_login_user_sistema = customtkinter.CTkLabel(self.fr_login_user_sistema, text='Login')
        self.lb_login_user_sistema.place(relx=0.425, rely=0, relwidth=0.15, relheight=0.55)

        self.entry_login_user_sistema = customtkinter.CTkEntry(self.fr_login_user_sistema, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_login_user_sistema.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nome
        self.fr_nome_user_sistema = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nome_user_sistema.place(relx=0.31, rely=0, relwidth=0.25, relheight=0.07)

        self.lb_login_user_sistema = customtkinter.CTkLabel(self.fr_nome_user_sistema, text='Nome')
        self.lb_login_user_sistema.place(relx=0.45, rely=0, relwidth=0.1, relheight=0.55)

        self.entry_nome_user_sistema = customtkinter.CTkEntry(self.fr_nome_user_sistema, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_nome_user_sistema.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Email
        self.fr_email_user_sistema = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_email_user_sistema.place(relx=0.565, rely=0, relwidth=0.25, relheight=0.07)

        self.lb_email_user_sistema = customtkinter.CTkLabel(self.fr_email_user_sistema, text='Email')
        self.lb_email_user_sistema.place(relx=0.45, rely=0, relwidth=0.1, relheight=0.55)

        self.entry_email_user_sistema = customtkinter.CTkEntry(self.fr_email_user_sistema, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_email_user_sistema.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Status
        self.fr_status_user_sistema = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_status_user_sistema.place(relx=0.82, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_status_user_sistema = customtkinter.CTkLabel(self.fr_status_user_sistema, text='Status')
        self.lb_status_user_sistema.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.55)

        self.entry_status_user_sistema = customtkinter.CTkEntry(self.fr_status_user_sistema, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_status_user_sistema.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Botão de consulta
        self.fr_botoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botoes.place(relx=0.925, rely=0, relwidth=0.075, relheight=0.07)

        # Lupa
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botoes, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_usuarios)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.6)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botoes, image=icone_salvar, text='',
                                                    fg_color='transparent', command=self.salvar_usuario)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.071, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "ID", "Login", "Nome", "Email", "Status"
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

        col_widths = [10, 20, 800, 10, 10, 10, 10, 10, 10, 10, 10]
        headers = ["ID", "Login", "Nome", "Email", "Status"]

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

        self.tree.bind("<Double-1>", self.lusuarios_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)


    def consulta_usuarios(self):
        self.tree.delete(*self.tree.get_children())

        query = """
            SELECT Usr_ID, Usr_Login, Usr_Nome, Usr_Email, Usr_Status from usuarios
        """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Nenhum usuário encontrado.", parent=self.frame_principal)
            return

        # Inserir dados na tabela
        for item in consulta:
            formatted_item = (
                str(item['Usr_ID']),
                str(item['Usr_Login']),
                str(item['Usr_Nome']),
                str(item['Usr_Email']),
                str(item['Usr_Status']),
            )
            self.tree.insert('', 'end', values=formatted_item)

    def salvar_usuario(self):

        if self.entry_email_user_sistema.get() == '':
            messagebox.showinfo("Aviso", "Campo email não pode ser vazio.", parent=self.frame_principal)
            return

        if self.entry_nome_user_sistema.get() == '':
            messagebox.showinfo("Aviso", "Campo nome não pode ser vazio.", parent=self.frame_principal)
            return

        if self.entry_login_user_sistema.get() == '':
            messagebox.showinfo("Aviso", "Campo login não pode ser vazio.", parent=self.frame_principal)
            return

        if self.entry_status_user_sistema.get() == '':
            messagebox.showinfo("Aviso", "Campo status não pode ser vazio.", parent=self.frame_principal)
            return

        try:
            db.begin_transaction()
            senha_padrao = 'c6*L@48p'
            hash_senha_padrao = hashlib.md5(senha_padrao.encode()).hexdigest()

            query = """
                INSERT INTO usuarios (Usr_Nome, Usr_Login, Usr_Email, Usr_senhaexcel, Usr_Status, DataCadastro) 
                    VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (self.entry_nome_user_sistema.get(), self.entry_login_user_sistema.get(), self.entry_email_user_sistema.get(),
                       str(hash_senha_padrao), self.entry_status_user_sistema.get(), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            db.executar_consulta(query, valores)
            db.commit_transaction()

            messagebox.showinfo("Aviso", "Usuário criado com sucesso!", parent=self.frame_principal)
        except:
            messagebox.showerror("Erro", "Erro ao salvar novo usuário!", parent=self.frame_principal)
            return

    def lusuarios_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.entry_id_user_sistema.configure(state='normal')
            self.entry_id_user_sistema.delete(0, tk.END)
            self.entry_id_user_sistema.insert(0, self.item[0])
            self.entry_id_user_sistema.configure(state='readonly')

            self.entry_login_user_sistema.configure(state='normal')
            self.entry_login_user_sistema.delete(0, tk.END)
            self.entry_login_user_sistema.insert(0, self.item[1])
            self.entry_login_user_sistema.configure(state='readonly')

            self.entry_nome_user_sistema.configure(state='normal')
            self.entry_nome_user_sistema.delete(0, tk.END)
            self.entry_nome_user_sistema.insert(0, self.item[2])
            self.entry_nome_user_sistema.configure(state='readonly')

            self.entry_email_user_sistema.configure(state='normal')
            self.entry_email_user_sistema.delete(0, tk.END)
            self.entry_email_user_sistema.insert(0, self.item[3])
            self.entry_email_user_sistema.configure(state='readonly')

            self.entry_status_user_sistema.configure(state='normal')
            self.entry_status_user_sistema.delete(0, tk.END)
            self.entry_status_user_sistema.insert(0, self.item[4])
            self.entry_status_user_sistema.configure(state='readonly')


UsuariosSistema()