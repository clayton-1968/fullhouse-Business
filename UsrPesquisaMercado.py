from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Pesquisa_Mercado(Widgets):
    
    def pesquisa_mercado(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        self.janela_pesquisa_mercado = customtkinter.CTkToplevel(self.window_one)
        self.janela_pesquisa_mercado.title('Pesquisa de Mercado')
        width = self.janela_pesquisa_mercado.winfo_screenwidth()
        height = self.janela_pesquisa_mercado.winfo_screenheight()
        self.janela_pesquisa_mercado.geometry(f"{width}x{height}+0+0") 
        self.janela_pesquisa_mercado.resizable(True, True)
        self.janela_pesquisa_mercado.lift()  # Traz a janela para frente   
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_pesquisa_mercado.protocol("WM_DELETE_WINDOW", self.on_closing_tela_pesquisa_mercado)

        self.frame_cabecalho_pesquisa(self.janela_pesquisa_mercado)
        self.frame_list_pesquisa(self.janela_pesquisa_mercado)
        self.frame_carregar_dados_pesquisa(Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area)
        
        self.janela_pesquisa_mercado.focus_force()
        self.janela_pesquisa_mercado.grab_set()    
        
################# dividindo a janela ###############
    def frame_cabecalho_pesquisa(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_uf))

        # Estado
        coordenadas_relx = 0.26
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        fr_uf = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_uf.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_estado = customtkinter.CTkLabel(fr_uf, text="UF")
        lb_estado.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        uf = self.get_uf()
        self.entry_uf = AutocompleteCombobox(fr_uf, width=30, font=('Times', 11), completevalues=uf)
        self.entry_uf.pack()
        self.entry_uf.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_municipio))

        # Municipio
        coordenadas_relx = 0.325
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        fr_municipio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_municipio.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_municipio = customtkinter.CTkLabel(fr_municipio, text="Município")
        lb_municipio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        municipios = self.get_municipios( self.entry_uf.get())
        
        self.entry_municipio = AutocompleteCombobox(fr_municipio, width=30, font=('Times', 11), completevalues=municipios)
        self.entry_municipio.pack()
        self.entry_municipio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_municipio.bind("<Button-1>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<KeyRelease>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind('<Down>', lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpo_projeto))

        # Tipo do Projeto
        coordenadas_relx=0.53
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        fr_tpo_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_tpo_projeto = customtkinter.CTkLabel(fr_tpo_projeto, text="Tipo do Projeto")
        lb_tpo_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        tpo_projeto = []
        
        self.entry_tpo_projeto = AutocompleteCombobox(fr_tpo_projeto, width=30, font=('Times', 11), completevalues=tpo_projeto)
        self.entry_tpo_projeto.pack()
        self.entry_tpo_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_tpo_projeto.bind("<Button-1>", lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind('<Down>', lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_cenario))
        
        
        # Nome do Projeto
        coordenadas_relx=0.735
        coordenadas_rely=0.01
        coordenadas_relwidth=0.255
        coordenadas_relheight=0.07
        fr_nome_cenario = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_cenario.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_nome_cenario = customtkinter.CTkLabel(fr_nome_cenario, text="Nome do Cenário")
        lb_nome_cenario.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        nome_cenario = []
        self.entry_nome_cenario = AutocompleteCombobox(fr_nome_cenario, width=30, font=('Times', 11), completevalues=nome_cenario)
        self.entry_nome_cenario.pack()
        self.entry_nome_cenario.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_nome_cenario.bind("<Button-1>", lambda event: 
                                                                self.atualizar_nome_cenario(event,
                                                                self.entry_empresa.get(), 
                                                                self.entry_municipio.get(), 
                                                                self.entry_uf.get(), 
                                                                self.entry_tpo_projeto.get(), 
                                                                self.entry_nome_cenario))
        self.entry_nome_cenario.bind('<Down>', lambda event: 
                                                                self.atualizar_nome_cenario(event,
                                                                self.entry_empresa.get(), 
                                                                self.entry_municipio.get(), 
                                                                self.entry_uf.get(), 
                                                                self.entry_tpo_projeto.get(), 
                                                                self.entry_nome_cenario))
        self.entry_nome_cenario.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_empreendimento))

        # Dados da Pesquisa
        # Informações do Empreendimento Pesquisado
        self.fr_informacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_informacoes.place(relx=0.005, rely=0.085, relwidth=0.985, relheight=0.07)
        self.lb_informacoes = customtkinter.CTkLabel(self.fr_informacoes, text="Informações do Empreendimento Pesquisado", text_color="white", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_informacoes.place(relx=0.05, rely=0, relheight=0.15, relwidth=0.50)

        # Nome do Empreendimento
        self.lb_nome_empreendimento = customtkinter.CTkLabel(self.fr_informacoes, text="Nome do Empreendimento", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_nome_empreendimento.place(relx=0.005, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_nome_empreendimento = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_nome_empreendimento.place(relx=0.005, rely=0.30, relwidth=0.25, relheight=0.6)

        self.entry_nome_empreendimento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_area_unidade))
        
        # Área Unidade
        self.lb_area_unidade = customtkinter.CTkLabel(self.fr_informacoes, text="Área Unidade - m²", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_area_unidade.place(relx=0.26, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_area_unidade = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_unidade.place(relx=0.26, rely=0.30, relwidth=0.08, relheight=0.6)

        self.entry_area_unidade.bind("<Return>", lambda event: self.format_m2(event, self.entry_area_unidade))
        self.entry_area_unidade.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_preco_unidade))

        # # Preço da Unidade
        self.lb_preco_unidade = customtkinter.CTkLabel(self.fr_informacoes, text="Preço da Unidade", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_preco_unidade.place(relx=0.345, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_preco_unidade = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_preco_unidade.place(relx=0.345, rely=0.30, relwidth=0.08, relheight=0.6)

        self.entry_preco_unidade.bind("<Return>", lambda event: self.format_valor(event, self.entry_preco_unidade))
        self.entry_preco_unidade.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_preco_m2_unidade))
        
        # # Preço m2 da Unidade
        self.lb_preco_m2_unidade = customtkinter.CTkLabel(self.fr_informacoes, text="Preço m²", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_preco_m2_unidade.place(relx=0.43, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_preco_m2_unidade = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_preco_m2_unidade.place(relx=0.43, rely=0.30, relwidth=0.08, relheight=0.6)

        self.entry_preco_m2_unidade.bind("<Return>", lambda event: self.format_valor(event, self.entry_preco_m2_unidade))
        self.entry_preco_m2_unidade.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_url))

        # # URL do Empreendimento
        self.lb_url = customtkinter.CTkLabel(self.fr_informacoes, text="url", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_url.place(relx=0.515, rely=0.15,relheight=0.15, relwidth=0.3)
        self.entry_url = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_url.place(relx=0.515, rely=0.30, relwidth=0.425, relheight=0.6)

        self.entry_url.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_area_aproveitamento))

        # Botão Gravar url Pesquisa
        icon_image = self.base64_to_photoimage('savedown')
        self.btn_gravar_pesquisa = customtkinter.CTkButton(self.fr_informacoes, text='', image=icon_image, command=self.gravar_pesquisa_mercado)
        self.btn_gravar_pesquisa.place(relx=0.95, rely=0.30, relwidth=0.04, relheight=0.60)

    def frame_list_pesquisa(self, janela):
        ## Listbox _ Informações Pesquisa
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.165, relwidth=0.985, relheight=0.85)

        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Widgets - Listar Parcelas
        self.LPesquisa_Mercado = ttk.Treeview(self.fr_list, height=7, column=(
                                                            'UF', 
                                                            'IBGE', 
                                                            'Municipio', 
                                                            'Tipo', 
                                                            'Estudo', 
                                                            'Empreendimento',
                                                            'Area_m2',
                                                            'Tickt',
                                                            'Valor_m2',
                                                            'url'
                                                            ), show='headings') # , show='headings'
        
        self.LPesquisa_Mercado.heading('#0', text='#', anchor='center')
        self.LPesquisa_Mercado.heading('#1', text='UF', anchor='center')
        self.LPesquisa_Mercado.heading('#2', text='IBGE', anchor='center')
        self.LPesquisa_Mercado.heading('#3', text='Município', anchor='center')
        self.LPesquisa_Mercado.heading('#4', text='Tipo', anchor='center')
        self.LPesquisa_Mercado.heading('#5', text='Estudo', anchor='center')
        self.LPesquisa_Mercado.heading('#6', text='Empreendimento', anchor='center')
        self.LPesquisa_Mercado.heading('#7', text='Área m² ', anchor='center')
        self.LPesquisa_Mercado.heading('#8', text='Tickt', anchor='center')
        self.LPesquisa_Mercado.heading('#9', text='Valor m²', anchor='center')
        self.LPesquisa_Mercado.heading('#10', text='url', anchor='center')

        self.LPesquisa_Mercado.column('#0', width=2, anchor='w')
        self.LPesquisa_Mercado.column('UF', width=10, anchor='w')
        self.LPesquisa_Mercado.column('IBGE', width=10, anchor='w')
        self.LPesquisa_Mercado.column('Municipio', width=50, anchor='w')
        self.LPesquisa_Mercado.column('Tipo', width=50, anchor='w')
        self.LPesquisa_Mercado.column('Estudo', width=50, anchor='w')
        self.LPesquisa_Mercado.column('Empreendimento', width=100, anchor='w')
        self.LPesquisa_Mercado.column('Area_m2', width=30, anchor='e')
        self.LPesquisa_Mercado.column('Tickt', width=30, anchor='e')
        self.LPesquisa_Mercado.column('Valor_m2', width=30, anchor='e')
        self.LPesquisa_Mercado.column('url', width=1000, anchor='w')
        
        self.LPesquisa_Mercado.pack(expand=True, fill='both')
        self.LPesquisa_Mercado.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.85)

        def selectec_maps():
            selected_item = self.LPesquisa_Mercado.selection()
            if selected_item:
                # Texto do item selecionado
                item_text = self.LPesquisa_Mercado.item(self.LPesquisa_Mercado.selection(), 'text')
                # Obtém os valores associados (como uma tupla)
                values = self.LPesquisa_Mercado.item(self.LPesquisa_Mercado.selection(), 'values')
                url = values[9]
                if url != '':
                    url = url.strip()  # Remove espaços em branco no início e no fim
                    webbrowser.open(url)
                else:
                    messagebox.showwarning("Maps", "Coordenadas Não Cadastrada!!!")
                    return

        def selected_excluir():
            Empresa_DS =  self.entry_empresa.get()
            UF = self.entry_uf.get()
            Cidade = self.entry_municipio.get()
            Tipo = self.entry_tpo_projeto.get()
            Nome_da_Area = self.entry_nome_cenario.get()

            selected_item = self.LPesquisa_Mercado.selection()
            if selected_item:
                # Texto do item selecionado
                item_text = self.LPesquisa_Mercado.item(self.LPesquisa_Mercado.selection(), 'text')
                # Obtém os valores associados (como uma tupla)
                values = self.LPesquisa_Mercado.item(self.LPesquisa_Mercado.selection(), 'values')
                pesquisa_empreendimento = values[5]
            else:
                pesquisa_empreendimento = ''
            
            if Empresa_DS == '': 
                messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
                return
            else:
                Empresa_ID = self.obter_Empresa_ID(Empresa_DS, janela)
            
            conditions = []  # Lista para armazenar as condições
            conditions.append("Empresa_ID = %s ")
            params = [Empresa_ID]

            if Cidade != '':
                conditions.append("Cidade = %s ")
                params.append(Cidade)
            else:
                messagebox.showinfo('Gestor Negócios', 'Município em Branco!!!.')
                return

            if UF != '':
                conditions.append("UF = %s ")
                params.append(UF)
            else:
                messagebox.showinfo('Gestor Negócios', 'UF em Branco!!!.')
                return

            if Tipo!= '':
                conditions.append("Tipo = %s ")
                params.append(Tipo)
            else:
                messagebox.showinfo('Gestor Negócios', 'Tipo do Projeto em Branco!!!.')
                return

            if Nome_da_Area!= '':
                conditions.append("Nome_da_Area = %s ")
                params.append(Nome_da_Area)
            else:
                messagebox.showinfo('Gestor Negócios', 'Nome do Estudo em Branco!!!.')
                return
            
            if pesquisa_empreendimento!= '':
                conditions.append("pesquisa_empreendimento = %s ")
                params.append(pesquisa_empreendimento)
            else:
                messagebox.showinfo('Gestor Negócios', 'Nome do Empreendimento Pesquisado em Branco!!!.')
                return
            
            strSql = f"""DELETE 
                         FROM TB_Pesquisa_Mercado
                         WHERE {' AND '.join(conditions)}"""
            
            results = db.executar_consulta(strSql, params)
            self.LPesquisa_Mercado.delete(self.row_id)

        def postPopUpMenu(event):
            self.row_id = self.LPesquisa_Mercado.identify_row(event.y)
            if self.row_id:  # Realiza a verificação se a linha existe.
                self.LPesquisa_Mercado.selection_set(self.row_id)
                row_values =self.LPesquisa_Mercado.item(self.row_id)['values']
                # print(row_values)
                postPopUpMenu = tk.Menu(self.LPesquisa_Mercado, tearoff=0, font=('Verdana', 11))
                postPopUpMenu.add_command(label='Maps', accelerator='Ctrl+M', command=selectec_maps)
                postPopUpMenu.add_separator()
                postPopUpMenu.add_command(label='Excluir Registro', accelerator='Delete', command=selected_excluir)
                postPopUpMenu.post(event.x_root, event.y_root)

        self.LPesquisa_Mercado.bind("<Double-1>", postPopUpMenu)  # 'Double-1' é o duplo clique do mouse
        self.LPesquisa_Mercado.bind("<Button-3>", postPopUpMenu)  # 'Button-3' é o clique direito do mouse
        self.LPesquisa_Mercado.bind('<Control-m>', lambda event: selectec_maps() if self.list_g.selection() else None)
        self.LPesquisa_Mercado.bind('<Delete>', lambda event: selected_excluir() if self.list_g.selection() else None)

    def frame_carregar_dados_pesquisa(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        self.limpar_campos_pesquisa_mercado()
        self.consultar_pesquisa_mercado(Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area)
    
    def consultar_pesquisa_mercado(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        if Empresa_DS == '': 
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        # Limpa a lista atual antes de inserir novos resultados
        self.limpar_campos_pesquisa_mercado
        self.LPesquisa_Mercado.delete(*self.LPesquisa_Mercado.get_children())

        conditions = []  # Lista para armazenar as condições
        conditions.append("Empresa_ID = %s ")
        params = [Empresa_ID]

        if Cidade != '':
            conditions.append("Cidade = %s ")
            params.append(Cidade)

        if UF != '':
            conditions.append("UF = %s ")
            params.append(UF)

        if Tipo!= '':
            conditions.append("Tipo = %s ")
            params.append(Tipo)

        if Nome_da_Area!= '':
            conditions.append("Nome_da_Area = %s ")
            params.append(Nome_da_Area)

        strSql = f"""SELECT 
                     Empresa_ID,
                     UF,
                     Municipio_ID,
                     Cidade,
                     Nome_da_Area,
                     Tipo,
                     pesquisa_empreendimento,
                     FORMAT(pesquisa_area_lote, 2, 'de_DE')   AS pesquisa_area_lote,
                     FORMAT(pesquisa_preco_venda, 2, 'de_DE') AS pesquisa_preco_venda,
                     FORMAT(pesquisa_preco_m2, 2, 'de_DE')    AS pesquisa_preco_m2,
                     pesquisa_url
                     FROM TB_Pesquisa_Mercado
                     WHERE {' AND '.join(conditions)} ORDER BY pesquisa_empreendimento"""
        
        results = db.executar_consulta(strSql, params)
        
        # Preenche Cabeçalho
        self.entry_empresa.set(Empresa_DS)
        self.entry_uf.set(UF)
        self.entry_municipio.set(Cidade)
        self.entry_tpo_projeto.set(Tipo)
        self.entry_nome_cenario.set(Nome_da_Area) 

        # Carregar Lista
        icon_image = self.base64_to_photoimage('lupa')
        for row in results:
            self.LPesquisa_Mercado.insert('', 'end', 
                               values=(
                                    row['UF'],
                                    row['Municipio_ID'],
                                    row['Cidade'],
                                    row['Tipo'],
                                    row['Nome_da_Area'],
                                    row['pesquisa_empreendimento'],
                                    row['pesquisa_area_lote'],
                                    row['pesquisa_preco_venda'],
                                    row['pesquisa_preco_m2'],
                                    row['pesquisa_url']
                                    )
                                )
            
        self.LPesquisa_Mercado.tag_configure('odd', background='#eee')
        self.LPesquisa_Mercado.tag_configure('even', background='#ddd')
        self.LPesquisa_Mercado.configure(yscrollcommand=self.scrollbar.set)
        # self.scrollbar.configure(command=self.LPesquisa_Mercado.yview)

    def gravar_pesquisa_mercado(self):
        Empresa_DS = self.entry_empresa.get()
        UF = self.entry_uf.get()
        self.atualizar_municipio_fx(self.entry_uf.get())
        IBGE = self.obter_municipio_IBGE(self.entry_municipio.get())
        Cidade = self.entry_municipio.get()
        Tipo = self.entry_tpo_projeto.get()
        Nome_da_Area = self.entry_nome_cenario.get()
        Pesquisa_Empreendimento = self.entry_nome_empreendimento.get()
        Pesquisa_Area_Unidade = float(self.entry_area_unidade.get().replace(" m²", "").replace(".", "").replace(",", ".")) 
        Pesquisa_Preco_Unidade = float(self.entry_preco_unidade.get().replace('.', '').replace(',', '.')[:15])
        Pesquisa_Preco_M2 = float(self.entry_preco_m2_unidade.get().replace('.', '').replace(',', '.')[:15])
        Pesquisa_url =self.entry_url.get()
        # Validação dos campos de input
        if not Empresa_DS: 
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        else:
            Empresa_ID = self.obter_Empresa_ID(Empresa_DS)

        if  not Cidade:
            messagebox.showinfo('Gestor Negócios', 'Município em Branco!!!.')
            return

        if not UF:
            messagebox.showinfo('Gestor Negócios', 'UF em Branco!!!.')
            return

        if not Tipo:
            messagebox.showinfo('Gestor Negócios', 'Tipo do Projeto em Branco!!!.')
            return

        if not Nome_da_Area:
            messagebox.showinfo('Gestor Negócios', 'Nome do Estudo em Branco!!!.')
            return
        
        if not Pesquisa_Empreendimento:
            messagebox.showinfo('Gestor Negócios', 'Nome do Empreendimento Pesquisado em Branco!!!.')
            return
        
        # Construindo a consulta SELECT
        query = """
                SELECT * FROM TB_Pesquisa_Mercado WHERE 
                Empresa_ID=%s 
                AND UF=%s 
                AND Cidade=%s 
                AND Tipo=%s 
                AND Nome_da_Area=%s 
                AND pesquisa_empreendimento=%s
        """
        params = (
                    Empresa_ID,
                    UF,
                    Cidade,
                    Tipo,
                    Nome_da_Area,
                    Pesquisa_Empreendimento
                )
        results = db.executar_consulta(query, params)
        
        if not results:
            # Inserindo um novo registro
            insert_query = """
                            INSERT INTO TB_Pesquisa_Mercado 
                            (
                            Empresa_ID, 
                            UF, 
                            Municipio_ID, 
                            Cidade, 
                            Tipo, 
                            Nome_da_Area, 
                            pesquisa_empreendimento, 
                            pesquisa_area_lote, 
                            pesquisa_preco_venda, 
                            pesquisa_preco_m2, 
                            pesquisa_url) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            insert_params = (
                Empresa_ID,
                UF,
                IBGE,
                Cidade,
                Tipo,
                Nome_da_Area,
                Pesquisa_Empreendimento,
                Pesquisa_Area_Unidade,
                Pesquisa_Preco_Unidade,
                Pesquisa_Preco_M2,
                Pesquisa_url
            )
            results = db.executar_consulta(insert_query, insert_params)
            self.LPesquisa_Mercado.insert('', 'end', 
                               values=(
                                    UF,
                                    IBGE,
                                    Cidade,
                                    Tipo,
                                    Nome_da_Area,
                                    Pesquisa_Empreendimento,
                                    Pesquisa_Area_Unidade,
                                    Pesquisa_Preco_Unidade,
                                    Pesquisa_Preco_M2,
                                    Pesquisa_url
                                    )
                                )
            # Exibe uma mensagem informando que a ação foi concluída
            messagebox.showinfo("Concluído", "Registro Gravado com sucesso!")
        else:
            # Exibe uma mensagem de alerta com opções Sim e Não
            resposta = messagebox.askyesno("Atenção", "Descrição da Pesquisa Já Exite, deseja sobrepor?")
            if resposta:  # Se o usuário clicou em "Sim"
                # Atualizando o registro existente
                update_query = """
                                UPDATE TB_Pesquisa_Mercado SET 
                                pesquisa_area_lote=%s, 
                                pesquisa_preco_venda=%s, 
                                pesquisa_preco_m2=%s, 
                                pesquisa_url=%s 
                                WHERE 
                                Empresa_ID=%s 
                                AND UF=%s 
                                AND Cidade=%s 
                                AND Tipo=%s 
                                AND Nome_da_Area=%s 
                                AND pesquisa_empreendimento=%s
                              """
                update_params = (
                                Pesquisa_Area_Unidade,
                                Pesquisa_Preco_Unidade,
                                Pesquisa_Preco_M2,
                                Pesquisa_url,
                                Empresa_ID,
                                UF,
                                Cidade,
                                Tipo,
                                Nome_da_Area,
                                Pesquisa_Empreendimento
                                )
                results = db.executar_consulta(update_query, update_params)
                messagebox.showinfo("Concluído", "Registro Alterado com sucesso!")
            else:  # Se o usuário clicou em "Não"
                return
        
        # Limpa a entrada
        valor_decimal = '0,00'
        valor_m2 = '0,00  m²'
        
        self.entry_nome_empreendimento.delete(0, 'end')
        self.entry_area_unidade.delete(0, 'end')
        self.entry_preco_unidade.delete(0, 'end')
        self.entry_preco_m2_unidade.delete(0, 'end')
        self.entry_url.delete(0, 'end')

        self.entry_area_unidade.insert(0, valor_m2.strip())
        self.entry_preco_unidade.insert(0, valor_decimal.strip())
        self.entry_preco_m2_unidade.insert(0, valor_decimal.strip())

Pesquisa_Mercado()
