from UsrCadastros import *
from widgets import Widgets

class GerenciadorReunioes(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def gerenciador_reunioes(self, principal_frame):
        self.images_base64()
        self.window_one.title('Ata e Reuniões')
        self.clearFrame_principal()
        self.frame_principal = principal_frame
        self.create_widgets_gerenciador_reunioes()

        # Armazena a reuniao selecionada
        self.reuniao_id_selecionado = None


    def create_widgets_gerenciador_reunioes(self):

        #CNPJ
        self.fr_cnpj_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cnpj_reuniao.place(relx=0, rely=0, relwidth=0.2, relheight=0.07)

        self.lb_cnpj_reuniao = customtkinter.CTkLabel(self.fr_cnpj_reuniao, text="CNPJ")
        self.lb_cnpj_reuniao.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_cnpj_reuniao = customtkinter.CTkEntry(self.fr_cnpj_reuniao, fg_color="white", text_color="black",
                                                        justify=tk.CENTER,)
        self.entry_cnpj_reuniao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Empresa
        self.frame_empresa(self.frame_principal, 0.2, 0, 0.30, 0.07)
        self.combo_empresa.bind("<<ComboboxSelected>>", self.preencher_cnpj_reuniao)
        self.combo_empresa.bind("<<ComboboxSelected>>", lambda event: self.consulta_reunioes(), add="+")

        # Sim
        self.fr_sim_box_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_sim_box_reuniao.place(relx=0.5, rely=0, relwidth=0.05, relheight=0.07)

        self.sim_var_reuniao = tk.BooleanVar()
        self.sim_cbox_reuniao = customtkinter.CTkCheckBox(self.fr_sim_box_reuniao, text="Sim",variable=self.sim_var_reuniao)
        self.sim_cbox_reuniao.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

        # Descrição (20%)
        self.fr_descricao_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_reuniao.place(relx=0.55, rely=0, relwidth=0.30, relheight=0.07)

        self.lb_descricao_reuniao = customtkinter.CTkLabel(self.fr_descricao_reuniao, text="Descrição")
        self.lb_descricao_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_reuniao = customtkinter.CTkEntry(self.fr_descricao_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_descricao_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        # Data (10%)
        self.fr_data_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_reuniao.place(relx=0.85, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_data_reuniao = customtkinter.CTkLabel(self.fr_data_reuniao, text="Data Reunião")
        self.lb_data_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_reuniao = customtkinter.CTkEntry(self.fr_data_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_reuniao.delete(0, 'end')
        self.entry_dt_reuniao.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_reuniao.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt_reuniao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_reuniao))
        self.entry_dt_reuniao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_reuniao, self.entry_dt_reuniao))

        # Botão Consultar (10%)
        self.fr_botao_consulta_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_consulta_reuniao.place(relx=0.95, rely=0, relwidth=0.05, relheight=0.07)

        self.icone_pesquisa_reuniao = self.base64_to_photoimage('lupa')
        self.btn_consulta_reuniao = customtkinter.CTkButton(
            self.fr_botao_consulta_reuniao,
            image=self.icone_pesquisa_reuniao,
            text='',
            fg_color='transparent',
            command = self.consulta_reunioes
        )
        self.btn_consulta_reuniao.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        # Data Providência
        self.fr_data_provid_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_provid_reuniao.place(relx=0, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data_provid_reuniao = customtkinter.CTkLabel(self.fr_data_provid_reuniao, text="Data Providência")
        self.lb_data_provid_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_provid_reuniao = customtkinter.CTkEntry(self.fr_data_provid_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_provid_reuniao.delete(0, 'end')
        self.entry_dt_provid_reuniao.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_provid_reuniao.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt_provid_reuniao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_provid_reuniao))
        self.entry_dt_provid_reuniao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_provid_reuniao, self.entry_dt_provid_reuniao))

        # Descrição Providência
        self.fr_descricao_provid_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_descricao_provid_reuniao.place(relx=0.1, rely=0.07, relwidth=0.30, relheight=0.07)

        self.lb_descricao_provid_reuniao = customtkinter.CTkLabel(self.fr_descricao_provid_reuniao, text="Descrição Providência")
        self.lb_descricao_provid_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_provid_reuniao = customtkinter.CTkEntry(self.fr_descricao_provid_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_descricao_provid_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        # Data Programada
        self.fr_data_program_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_program_reuniao.place(relx=0.4, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data_program_reuniao = customtkinter.CTkLabel(self.fr_data_program_reuniao, text="Data Programada")
        self.lb_data_program_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_program_reuniao = customtkinter.CTkEntry(self.fr_data_program_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_program_reuniao.delete(0, 'end')
        self.entry_dt_program_reuniao.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_program_reuniao.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt_program_reuniao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_program_reuniao))
        self.entry_dt_program_reuniao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_program_reuniao, self.entry_dt_program_reuniao))

        # Data Conclusão
        self.fr_data_concl_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_data_concl_reuniao.place(relx=0.5, rely=0.07, relwidth=0.1, relheight=0.07)

        self.lb_data_conclu_reuniao = customtkinter.CTkLabel(self.fr_data_concl_reuniao, text="Data Conclusão")
        self.lb_data_conclu_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_conclu_reuniao = customtkinter.CTkEntry(self.fr_data_concl_reuniao, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_conclu_reuniao.delete(0, 'end')
        self.entry_dt_conclu_reuniao.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_conclu_reuniao.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt_conclu_reuniao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_conclu_reuniao))
        self.entry_dt_conclu_reuniao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_conclu_reuniao, self.entry_dt_conclu_reuniao))

        # Responsável
        self.fr_responsavel_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_responsavel_reuniao.place(relx=0.6, rely=0.07, relwidth=0.30, relheight=0.07)

        self.lb_responsavel_reuniao = customtkinter.CTkLabel(self.fr_responsavel_reuniao, text="Responsável")
        self.lb_responsavel_reuniao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.usuarios = []
        self.entry_responsavel_reuniao = AutocompleteCombobox(self.fr_responsavel_reuniao, font=('Times', 11), width=30, completevalues=self.usuarios)
        self.entry_responsavel_reuniao.pack()
        self.entry_responsavel_reuniao.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)
        self.entry_responsavel_reuniao.bind("<Button-1>", lambda event: self.retornar_usuarios(self.entry_responsavel_reuniao))
        self.entry_responsavel_reuniao.bind('<Down>', lambda event: self.retornar_usuarios(self.entry_responsavel_reuniao))

        # Botão Salvar (10%)
        self.fr_botao_salvar_reuniao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_salvar_reuniao.place(relx=0.90, rely=0.07, relwidth=0.05, relheight=0.07)

        self.icone_salvar_reuniao = self.base64_to_photoimage('save')
        self.btn_salvar_reuniao = customtkinter.CTkButton(
            self.fr_botao_salvar_reuniao,
            image=self.icone_salvar_reuniao,
            text='',
            fg_color='transparent',
            command = self.salvar_reuniao
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
            fg_color='transparent',
            command = self.abrir_tela_log
        )
        self.btn_consulta_log.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "ID", "Empresa", "Descrição", "Data", "Usuário"
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

        col_widths = [10, 30, 30, 10, 10]

        headers = ["ID", "Empresa", "Descrição", "Data", "Usuário"]

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

        self.tree.bind("<Button-1>", self.lreunicoes_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)


    def retornar_usuarios(self, target):
        query = """
            SELECT UsuarioNome from usuarios
        """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Usuários não encontrados!", parent=self.window_one)
            return

        self.usuarios = [item["UsuarioNome"] for item in myresult]

        target.set_completion_list(self.usuarios)

    def preencher_cnpj_reuniao(self, event):
        empresa_selecionada = self.combo_empresa.get()

        if empresa_selecionada:
            cnpj = self.empresas_dict.get(empresa_selecionada)

            if cnpj:
                self.entry_cnpj_reuniao.delete(0, 'end')
                self.entry_cnpj_reuniao.insert(0, cnpj)
            else:
                self.entry_cnpj_reuniao.delete(0, 'end')
        else:
            self.entry_cnpj_reuniao.delete(0, 'end')


    def salvar_reuniao(self):
        if not self.entry_cnpj_reuniao.get():
            messagebox.showerror("Erro", "Empresa não pode ser vazio!", parent=self.window_one)
            self.entry_cnpj_reuniao.focus()
            return

        if not self.entry_descricao_reuniao.get():
            messagebox.showerror("Erro", "Descrição da reunião não pode ser vazio!", parent=self.window_one)
            self.entry_descricao_reuniao.focus()
            return

        if not self.entry_dt_reuniao.get():
            messagebox.showerror("Erro", "Data não pode ser vazia!", parent=self.window_one)
            self.entry_dt_reuniao.focus()
            return

        if not self.entry_responsavel_reuniao.get():
            messagebox.showerror("Erro", "Responsável não pode ser vazio!.", parent=self.window_one)
            self.entry_responsavel_reuniao.focus()
            return

        if not self.entry_responsavel_reuniao.get():
            messagebox.showerror("Erro", "Responsável não pode ser vazio!.", parent=self.window_one)
            self.entry_responsavel_reuniao.focus()
            return

        if not self.entry_descricao_provid_reuniao.get():
            messagebox.showerror("Erro", "Descrição da Providência não pode ser vazia!.", parent=self.window_one)
            self.entry_descricao_provid_reuniao.focus()
            return

        if not self.entry_dt_provid_reuniao.get():
            messagebox.showerror("Erro", "Data da Providência não pode ser vazia!.", parent=self.window_one)
            self.entry_dt_provid_reuniao.focus()
            return

        if not self.entry_dt_program_reuniao.get():
            messagebox.showerror("Erro", "Data Programada não pode ser vazia!.", parent=self.window_one)
            self.entry_dt_program_reuniao.focus()
            return

        if not self.entry_dt_conclu_reuniao.get():
            messagebox.showerror("Erro", "Data da Conclusão não pode ser vazia!.", parent=self.window_one)
            self.entry_dt_conclu_reuniao.focus()
            return

        try:
            self.entry_dt_reuniao = datetime.strptime(self.entry_dt_reuniao.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            self.entry_dt_provid_reuniao = datetime.strptime(self.entry_dt_provid_reuniao.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            self.entry_dt_program_reuniao = datetime.strptime(self.entry_dt_program_reuniao.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            self.entry_dt_conclu_reuniao = datetime.strptime(self.entry_dt_conclu_reuniao.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.", parent=self.window_one)
            return

        self.reuniao_id = None

        try:
            vs_sql = """INSERT INTO reuniao_cadastro 
                            (
                                    Empresa_ID, 
                                    Reuniao_DS, 
                                    Reuniao_Dta,
                                    Reuniao_Usr_id 
                            ) 
                            VALUES (%s, %s, %s, %s)
                            """
            values = (
                self.entry_cnpj_reuniao.get(),
                self.entry_descricao_reuniao.get(),
                self.entry_dt_reuniao,
                self.entry_responsavel_reuniao.get()
            )
            db.executar_consulta(vs_sql, values)

            query_last_id = "SELECT LAST_INSERT_ID()"
            self.reuniao_id = db._querying(query_last_id)[0]['LAST_INSERT_ID()']

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o cadastro da reunião: {str(e)}", parent=self.window_one)
            return

        try:
            # Consulta para obter o máximo Reuniao_Providencia_ID para esta empresa
            query_max_id = """
                SELECT COALESCE(MAX(Reuniao_Providencia_ID), 0) + 1 as next_id 
                FROM reuniao_assuntos 
                WHERE Empresa_ID = %s
            """
            result_max_id = db.executar_consulta(query_max_id, (self.entry_cnpj_reuniao.get(),))

            if result_max_id and len(result_max_id) > 0:
                self.reuniao_providencia_id = result_max_id[0]['next_id']
            else:
                self.reuniao_providencia_id = 1  # Primeiro registro para esta empresa

            vs_sql = """INSERT INTO reuniao_assuntos
                            (
                                    Empresa_ID, 
                                    Reuniao_ID, 
                                    Reuniao_Providencia_ID,
                                    Reuniao_Providencia_DS,
                                    Reuniao_Providencia_Dta_Registro,
                                    Reuniao_Providencia_Dta_Conclusao,
                                    Reuniao_Usr_ID
                            ) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """
            values = (
                self.entry_cnpj_reuniao.get(),
                self.reuniao_id,
                self.reuniao_providencia_id,
                self.entry_descricao_provid_reuniao.get(),
                self.entry_dt_provid_reuniao,
                self.entry_dt_conclu_reuniao,
                self.entry_responsavel_reuniao.get()
            )
            myresult = db.executar_consulta(vs_sql, values)

            messagebox.showinfo("Aviso", "Reunião inserida com sucesso!", parent=self.window_one)

            self.consulta_reunioes()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o cadastro do assunto da reunião: {str(e)}", parent=self.window_one)


    def consulta_reunioes(self):
        # Limpa a treeview antes de nova consulta
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            cnpj_empresa = self.entry_cnpj_reuniao.get()

            if not cnpj_empresa:
                messagebox.showinfo("Aviso", "Selecione uma empresa!")
                return

            str_sql = f"""
                SELECT Reuniao_ID, Empresa_ID, Reuniao_DS, Reuniao_Dta, Reuniao_Usr_id
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
                    reuniao_data = reuniao['Reuniao_Dta']
                    reuniao_user_id= reuniao['Reuniao_Usr_id']

                    self.reuniao_dict[reuniao_descricao] = reuniao_id
                    descricoes.append(reuniao_descricao)

                    # Adiciona à treeview
                    self.tree.insert("", "end", values=(
                        reuniao_id,
                        cnpj_empresa,
                        reuniao_descricao,
                        reuniao_data,
                        reuniao_user_id
                    ))

                # Ajusta a largura das colunas após inserir os dados
                for col in self.tree["columns"]:
                    self.tree.column(col, width=tk.font.Font().measure(col) + 20)

                    # Verifica o maior valor na coluna
                    max_width = tk.font.Font().measure(col)
                    for item in self.tree.get_children():
                        valor = self.tree.set(item, col)
                        item_width = tk.font.Font().measure(valor)
                        if item_width > max_width:
                            max_width = item_width

                    self.tree.column(col, width=max_width + 20)

            else:
                messagebox.showinfo("Info", "Nenhuma reunião encontrada!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar reuniões: {str(e)}")

    def lreunicoes_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.reuniao_id_selecionado = self.item[0]

            self.entry_cnpj_reuniao.configure(state='normal')
            self.entry_cnpj_reuniao.delete(0, tk.END)
            self.entry_cnpj_reuniao.insert(0, self.item[1])

            self.entry_descricao_reuniao.configure(state='normal')
            self.entry_descricao_reuniao.delete(0, tk.END)
            self.entry_descricao_reuniao.insert(0, self.item[2])

            self.entry_dt_reuniao.delete(0, tk.END)
            self.entry_dt_reuniao.insert(0, datetime.strptime(str(self.item[3]), "%Y-%m-%d").strftime("%d/%m/%Y"))

            self.entry_responsavel_reuniao.configure(state='normal')
            self.entry_responsavel_reuniao.delete(0, tk.END)
            self.entry_responsavel_reuniao.insert(0, self.item[4])


    def abrir_tela_log(self):
        if not self.reuniao_id_selecionado:
            messagebox.showwarning("Aviso", "Selecione um Reunião!")
            return

        self.janela_log_reuniao = customtkinter.CTkToplevel(self.window_one)
        self.janela_log_reuniao.title('Log')
        self.janela_log_reuniao.geometry("400x150")
        self.janela_log_reuniao.resizable(False, False)
        self.janela_log_reuniao.lift()

        # Frame principal
        self.frame_versao_principal_log = customtkinter.CTkFrame(self.janela_log_reuniao, fg_color='black')
        self.frame_versao_principal_log.pack(pady=1, padx=1, fill="both", expand=True)

        # Data Providência
        self.fr_data_provid_log = customtkinter.CTkFrame(self.frame_versao_principal_log, border_color="gray75",
                                                         border_width=1)
        self.fr_data_provid_log.place(relx=0, rely=0, relwidth=0.3, relheight=0.3)

        self.lb_data_provid_log = customtkinter.CTkLabel(self.fr_data_provid_log, text="Data Providência")
        self.lb_data_provid_log.place(relx=0.1, rely=0, relheight=0.4, relwidth=0.8)

        self.entry_dt_provid_log = customtkinter.CTkEntry(self.fr_data_provid_log, fg_color="white", text_color="black",
                                                          justify=tk.CENTER)
        self.entry_dt_provid_log.delete(0, 'end')
        self.entry_dt_provid_log.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_provid_log.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
        self.entry_dt_provid_log.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_provid_log))

        # Descrição Providência
        self.fr_descricao_provid_log = customtkinter.CTkFrame(self.frame_versao_principal_log, border_color="gray75",
                                                              border_width=1)
        self.fr_descricao_provid_log.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)

        self.lb_descricao_provid_log = customtkinter.CTkLabel(self.fr_descricao_provid_log,
                                                              text="Descrição Providência")
        self.lb_descricao_provid_log.place(relx=0.1, rely=0, relheight=0.4, relwidth=0.8)

        self.entry_descricao_provid_log = customtkinter.CTkEntry(self.fr_descricao_provid_log, fg_color="white",
                                                                 text_color="black", justify=tk.CENTER)
        self.entry_descricao_provid_log.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)

        # Flag para controle do estado da aplicação
        self.app_closing = False

        # Vincular o evento de fechamento da janela
        self.janela_log_reuniao.protocol("WM_DELETE_WINDOW",
                                             lambda: self.on_closing_tela(self.janela_log_reuniao))

        self.carregar_dados_log(self.reuniao_id_selecionado)

        self.janela_log_reuniao.focus_force()
        self.janela_log_reuniao.grab_set()


    def carregar_dados_log(self, reuniao_id):
        try:
            str_sql = f"""
                SELECT Reuniao_Providencia_DS, Reuniao_Providencia_Dta_Registro
                FROM reuniao_assuntos 
                WHERE Reuniao_ID = '{reuniao_id}'
                ORDER BY Reuniao_Providencia_Dta_Registro DESC 
                LIMIT 1
            """

            myresult = db._querying(str_sql)

            if myresult:
                providencia = myresult[0]
                descricao = providencia.get('Reuniao_Providencia_DS', '')
                data_str = providencia.get('Reuniao_Providencia_Dta_Registro', '')

                if data_str:
                    try:
                        data_obj = datetime.strptime(str(data_str), "%Y-%m-%d")
                        data_formatada = data_obj.strftime("%d/%m/%Y")
                        self.entry_dt_provid_log.delete(0, tk.END)
                        self.entry_dt_provid_log.insert(0, data_formatada)
                    except ValueError:
                        self.entry_dt_provid_log.delete(0, tk.END)
                        self.entry_dt_provid_log.insert(0, str(data_str))

                self.entry_descricao_provid_log.delete(0, tk.END)
                self.entry_descricao_provid_log.insert(0, descricao)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar informações do log: {str(e)}")
