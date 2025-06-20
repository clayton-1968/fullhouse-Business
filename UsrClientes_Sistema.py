from UsrCadastros import *
from widgets import Widgets

class ClientesSistema(Widgets, Pessoas, Produtos, Icons):

    def consultar_clientes_sistema(self, principal_frame):
        self.images_base64()

        self.window_one.title('Clientes do Sistema')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_clientes_sistema()

    def create_widgets_clientes_sistema(self):
        # Tipo
        self.fr_tipo_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tipo_clientes_sist.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_tipo_clientes_sist = customtkinter.CTkLabel(self.fr_tipo_clientes_sist, text="Tipo")
        self.lb_tipo_clientes_sist.place(relx=0.3, rely=0, relheight=0.25, relwidth=0.35)

        self.entry_tipo_clientes_sist = customtkinter.CTkEntry(self.fr_tipo_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_tipo_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # CPF/CNPJ
        self.fr_cpf_cnpj_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cpf_cnpj_clientes_sist.place(relx=0.105, rely=0, relwidth=0.15, relheight=0.07)

        self.lb_cpf_cnpj_clientes_sist = customtkinter.CTkLabel(self.fr_cpf_cnpj_clientes_sist, text="CPF/CNPJ")
        self.lb_cpf_cnpj_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_cpf_cnpj_clientes_sist = customtkinter.CTkEntry(self.fr_cpf_cnpj_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_cpf_cnpj_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nome
        self.fr_nome_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nome_clientes_sist.place(relx=0.26, rely=0, relwidth=0.3, relheight=0.07)

        self.lb_nome_clientes_sist = customtkinter.CTkLabel(self.fr_nome_clientes_sist, text="Nome")
        self.lb_nome_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_nome_clientes_sist = customtkinter.CTkEntry(self.fr_nome_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_nome_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Regime Tributário
        self.fr_regim_trib_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_regim_trib_clientes_sist.place(relx=0.565, rely=0, relwidth=0.15, relheight=0.07)

        self.lb_regim_trib_clientes_sist = customtkinter.CTkLabel(self.fr_regim_trib_clientes_sist, text="Regime Tributário")
        self.lb_regim_trib_clientes_sist.place(relx=0.05, rely=0, relheight=0.25, relwidth=0.9)

        self.entry_regim_trib_clientes_sist = customtkinter.CTkEntry(self.fr_regim_trib_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_regim_trib_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Ativo
        self.fr_botao_box_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botao_box_clientes_sist.place(relx=0.72, rely=0, relwidth=0.1, relheight=0.07)

        # Box ativo
        self.ativo_var = tk.BooleanVar()
        self.ativo_cbox = customtkinter.CTkCheckBox(self.fr_botao_box_clientes_sist, text="Ativo",
                                                        variable=self.ativo_var)
        self.ativo_cbox.place(relx=0.05, rely=0.25, relwidth=0.7, relheight=0.5)

        # Botão de consulta
        self.fr_botoes_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                                border_width=1)
        self.fr_botoes_clientes_sist.place(relx=0.825, rely=0, relwidth=0.1, relheight=0.07)

        # Lupa
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botoes_clientes_sist, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_clientes_sist)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.6)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botoes_clientes_sist, image=icone_salvar, text='',
                                                  fg_color='transparent', command=self.salva_clientes_sist)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # CEP
        self.fr_cep_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cep_clientes_sist.place(relx=0, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_cep_clientes_sist = customtkinter.CTkLabel(self.fr_cep_clientes_sist, text="CEP")
        self.lb_cep_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_cep_clientes_sist = customtkinter.CTkEntry(self.fr_cep_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_cep_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Município
        self.fr_municipio_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_municipio_clientes_sist.place(relx=0.105, rely=0.075, relwidth=0.2, relheight=0.07)

        self.lb_municipio_clientes_sist = customtkinter.CTkLabel(self.fr_municipio_clientes_sist, text="Município")
        self.lb_municipio_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_municipio_clientes_sist = customtkinter.CTkEntry(self.fr_municipio_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_municipio_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # UF
        self.fr_uf_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_uf_clientes_sist.place(relx=0.31, rely=0.075, relwidth=0.05, relheight=0.07)

        self.lb_uf_clientes_sist = customtkinter.CTkLabel(self.fr_uf_clientes_sist, text="UF")
        self.lb_uf_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_uf_clientes_sist = customtkinter.CTkEntry(self.fr_uf_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_uf_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Endereço
        self.fr_endereco_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_endereco_clientes_sist.place(relx=0.365, rely=0.075, relwidth=0.3, relheight=0.07)

        self.lb_fr_endereco_clientes_sist = customtkinter.CTkLabel(self.fr_endereco_clientes_sist, text="Endereço")
        self.lb_fr_endereco_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_fr_endereco_clientes_sist = customtkinter.CTkEntry(self.fr_endereco_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_fr_endereco_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Número
        self.fr_numero_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_numero_clientes_sist.place(relx=0.67, rely=0.075, relwidth=0.05, relheight=0.07)

        self.lb_numero_clientes_sist = customtkinter.CTkLabel(self.fr_numero_clientes_sist, text="Número")
        self.lb_numero_clientes_sist.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_numero_clientes_sist = customtkinter.CTkEntry(self.fr_numero_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_numero_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Complemento
        self.fr_complemento_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_complemento_clientes_sist.place(relx=0.725, rely=0.075, relwidth=0.15, relheight=0.07)

        self.lb_complemento_clientes_sist = customtkinter.CTkLabel(self.fr_complemento_clientes_sist, text="Complemento")
        self.lb_complemento_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_complemento_clientes_sist = customtkinter.CTkEntry(self.fr_complemento_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_complemento_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Bairro
        self.fr_bairro_clientes_sist = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_bairro_clientes_sist.place(relx=0.88, rely=0.075, relwidth=0.12, relheight=0.07)

        self.lb_bairro_clientes_sist = customtkinter.CTkLabel(self.fr_bairro_clientes_sist, text="Bairro")
        self.lb_bairro_clientes_sist.place(relx=0.2, rely=0, relheight=0.25, relwidth=0.6)

        self.entry_bairro_clientes_sist = customtkinter.CTkEntry(self.fr_bairro_clientes_sist, fg_color="white",
                                                            text_color="black",
                                                            justify=tk.LEFT)
        self.entry_bairro_clientes_sist.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Tipo", "CPF/CNPJ", "Descrição", "CEP", "Logradouro", "Nr.", "Complemento", "Bairro", "UF",
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

        col_widths = [10, 15, 30, 10, 30, 10, 20, 20, 10]
        headers = ["Tipo", "CPF/CNPJ", "Descrição", "CEP", "Logradouro", "Nr.", "Complemento", "Bairro", "UF"]

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

        self.tree.bind("<Double-1>", self.lclientes_sistema_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)


    def consulta_clientes_sist(self):
        self.tree.delete(*self.tree.get_children())

        query = """
                SELECT Pessoas_Tipo as Tipo, Pessoas_CPF_CNPJ as CPFCNPJ, Pessoas_Descricao as Descricao,
                Pessoas_CEP as CEP, Pessoas_EndLogradouro as Logradouro, Pessoas_EndNumero as Numero, 
                Pessoas_EndComplemento as Complemento, Pessoas_EndBairro as Bairro, Pessoas_UF as UF FROM TB_Pessoas 
                ORDER BY Descricao;
                """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Nenhum sistema de amortização encontrado.", parent=self.frame_principal)
            return

        # Inserir dados na tabela
        for item in consulta:
            formatted_item = (
                str(item['Tipo']),
                str(item['CPFCNPJ']),
                str(item['Descricao']),
                str(item['CEP']),
                str(item['Logradouro']),
                str(item['Numero']),
                str(item['Complemento']),
                str(item['Bairro']),
                str(item['UF']),
            )
            self.tree.insert('', 'end', values=formatted_item)


    def salva_clientes_sist(self):
        if self.entry_tipo_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo Tipo não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_cpf_cnpj_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo CPF/CNPJ não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_nome_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo Nome não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_cep_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo CEP não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_uf_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo UF não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_numero_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo Número não pode ser vazio.", parent=self.frame_principal)
            return
        if self.entry_bairro_clientes_sist.get() == '':
            messagebox.showinfo("Aviso", "Campo Bairro não pode ser vazio.", parent=self.frame_principal)
            return

        try:
            db.begin_transaction()

            query = """
                    INSERT INTO TB_Pessoas (Pessoas_Tipo, Pessoas_CPF_CNPJ, Pessoas_EndLogradouro, Pessoas_EndNumero, 
                    Pessoas_EndBairro, Pessoas_EndComplemento, Pessoas_CEP, Pessoas_UF)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """

            valores = (self.entry_tipo_clientes_sist.get(), self.entry_cpf_cnpj_clientes_sist.get(), self.entry_fr_endereco_clientes_sist.get(),
                       self.entry_numero_clientes_sist.get(), self.entry_bairro_clientes_sist.get(), self.entry_complemento_clientes_sist.get(),
                       self.entry_cep_clientes_sist.get(), self.entry_uf_clientes_sist.get())

            db.executar_consulta(query, valores)
            db.commit_transaction()

            messagebox.showinfo("Aviso", "Cliente criado com sucesso!", parent=self.frame_principal)
        except:
            messagebox.showerror("Erro", "Erro ao salvar novo cliente!", parent=self.frame_principal)
            return

    def lclientes_sistema_click(self, event):
        self.selected_item = self.tree.selection()
        if self.selected_item:
            self.item = self.tree.item(self.selected_item)['values']

            self.entry_tipo_clientes_sist.configure(state='normal')
            self.entry_tipo_clientes_sist.delete(0, tk.END)
            self.entry_tipo_clientes_sist.insert(0, self.item[0])

            self.entry_cpf_cnpj_clientes_sist.configure(state='normal')
            self.entry_cpf_cnpj_clientes_sist.delete(0, tk.END)
            self.entry_cpf_cnpj_clientes_sist.insert(0, self.item[1])

            self.entry_nome_clientes_sist.configure(state='normal')
            self.entry_nome_clientes_sist.delete(0, tk.END)
            self.entry_nome_clientes_sist.insert(0, self.item[2])

            self.entry_cep_clientes_sist.configure(state='normal')
            self.entry_cep_clientes_sist.delete(0, tk.END)
            self.entry_cep_clientes_sist.insert(0, self.item[3])

            self.entry_fr_endereco_clientes_sist.configure(state='normal')
            self.entry_fr_endereco_clientes_sist.delete(0, tk.END)
            self.entry_fr_endereco_clientes_sist.insert(0, self.item[4])

            self.entry_numero_clientes_sist.configure(state='normal')
            self.entry_numero_clientes_sist.delete(0, tk.END)
            self.entry_numero_clientes_sist.insert(0, self.item[5])

            self.entry_complemento_clientes_sist.configure(state='normal')
            self.entry_complemento_clientes_sist.delete(0, tk.END)
            self.entry_complemento_clientes_sist.insert(0, self.item[6])

            self.entry_bairro_clientes_sist.configure(state='normal')
            self.entry_bairro_clientes_sist.delete(0, tk.END)
            self.entry_bairro_clientes_sist.insert(0, self.item[7])

            self.entry_uf_clientes_sist.configure(state='normal')
            self.entry_uf_clientes_sist.delete(0, tk.END)
            self.entry_uf_clientes_sist.insert(0, self.item[8])

