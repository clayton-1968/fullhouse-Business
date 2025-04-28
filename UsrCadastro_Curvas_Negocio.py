from imports import *
from widgets import Widgets

################# criando janela ###############
class Cadastrar_Curvas_Negocio(Widgets):
    def cadastrar_curvas_negocio(self):
        self.window_one.title('Cadastro Curvas de Negócios')
        self.clearFrame_principal()
        self.frame_cabecalho_cadastro_curvas_linha_1(self.principal_frame)
    
        
################# dividindo a janela ###############
    def frame_cabecalho_cadastro_curvas_linha_1(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.455
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa", anchor='w')
        lb_empresa.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_curva))

        # Nome da Curva
        coordenadas_relx = 0.465
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.33
        coordenadas_relheight = 0.07
        fr_nome_curva = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_curva.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_nome_curva = customtkinter.CTkLabel(fr_nome_curva, text="Nome da Curva", anchor='w')
        lb_nome_curva.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        curvas = []

        self.entry_nome_curva = AutocompleteCombobox(fr_nome_curva, width=30, font=('Times', 11), completevalues=curvas)
        self.entry_nome_curva.pack()
        self.entry_nome_curva.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_nome_curva.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela),  self.entry_nome_curva))
        self.entry_nome_curva.bind("<KeyRelease>", lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_nome_curva))
        self.entry_nome_curva.bind('<Down>', lambda event: self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_nome_curva))
        self.entry_nome_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_prazo_curva))
        
        # Prazo da Curva
        coordenadas_relx=0.80
        coordenadas_rely=0.01
        coordenadas_relwidth=0.06
        coordenadas_relheight=0.07
        fr_prazo_curva = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_prazo_curva.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_prazo_curva = customtkinter.CTkLabel(fr_prazo_curva, text="Prazo(meses)", anchor='w')
        lb_prazo_curva.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.entry_prazo_curva = customtkinter.CTkEntry(fr_prazo_curva, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_prazo_curva.place(relx=0.01, rely=0.5, relwidth=0.97, relheight=0.4)
        self.entry_prazo_curva.bind("<Return>", lambda event: self.format_mes(event, self.entry_prazo_curva))
        self.entry_prazo_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_etapas_curva))

        # Botão de Consultar Gráfico
        icon_image = self.base64_to_photoimage('olho')
        self.btn_consultar_grafico = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=[])
        self.btn_consultar_grafico.place(relx=0.865, rely=0.012, relwidth=0.04, relheight=0.05)

        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_curva = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=self.consulta_curvas)
        self.btn_consultar_curva.place(relx=0.91, rely=0.012, relwidth=0.04, relheight=0.05)
        
        # Botão de Salvar
        icon_image = self.base64_to_photoimage('save')
        self.btn_salvar_curva = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=self.gravar_curvas)
        self.btn_salvar_curva.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)

        # Etapas da Curva
        coordenadas_relx = 0.005
        coordenadas_rely = 0.085
        coordenadas_relwidth = 0.855
        coordenadas_relheight = 0.07
        fr_etapas_curva = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_etapas_curva.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_etapas_curva = customtkinter.CTkLabel(fr_etapas_curva, text="Etapas da Curva", anchor='w')
        lb_etapas_curva.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        ## Etapa
        etapas = []
        self.entry_etapas_curva = AutocompleteCombobox(fr_etapas_curva, width=30, font=('Times', 11), completevalues=etapas)
        self.entry_etapas_curva.pack()
        self.entry_etapas_curva.place(relx=0.001, rely=0.5, relwidth=0.54, relheight=0.4)
        self.entry_etapas_curva.bind("<Button-1>", lambda event: self.atualizar_etapas_curvas(event, self.entry_etapas_curva))
        self.entry_etapas_curva.bind("<KeyRelease>", lambda event: self.atualizar_etapas_curvas(event, self.entry_etapas_curva))
        self.entry_etapas_curva.bind('<Down>', lambda event: self.atualizar_etapas_curvas(event, self.entry_etapas_curva))
        self.entry_etapas_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_inicio_curva))

        ## Botão Adicionar Etapas ...
        icon_image = self.base64_to_photoimage('trespontos')
        self.btn_adicionar_etapas_dacurva = customtkinter.CTkButton(fr_etapas_curva, text='', image=icon_image, fg_color='transparent', command=[])
        self.btn_adicionar_etapas_dacurva.place(relx=0.545, rely=0.5, relwidth=0.04, relheight=0.4)
        
        ## Inicio Etapa
        lb_inicio_curva = customtkinter.CTkLabel(fr_etapas_curva, text="Início da Curva", anchor='w')
        lb_inicio_curva.place(relx=0.59, rely=0.25, relheight=0.25, relwidth=0.10)

        self.entry_inicio_curva = customtkinter.CTkEntry(fr_etapas_curva, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_inicio_curva.place(relx=0.59, rely=0.5, relwidth=0.10, relheight=0.4)
        self.entry_inicio_curva.bind("<Return>", lambda event: self.format_mes(event, self.entry_inicio_curva))
        self.entry_inicio_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_fim_curva))
        
        ## Fim Etapa
        lb_final_curva = customtkinter.CTkLabel(fr_etapas_curva, text="Final da Curva", anchor='w')
        lb_final_curva.place(relx=0.695, rely=0.25, relheight=0.25, relwidth=0.10)

        self.entry_fim_curva = customtkinter.CTkEntry(fr_etapas_curva, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_fim_curva.place(relx=0.695, rely=0.5, relwidth=0.10, relheight=0.4)
        self.entry_fim_curva.bind("<Return>", lambda event: self.format_mes(event, self.entry_fim_curva))
        self.entry_fim_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_per_aplicado))
        
        # ## Percentual Aplicado
        lb_per_aplicado = customtkinter.CTkLabel(fr_etapas_curva, text="% Unitário", anchor='w')
        lb_per_aplicado.place(relx=0.80, rely=0.25, relheight=0.25, relwidth=0.10)

        self.entry_per_aplicado = customtkinter.CTkEntry(fr_etapas_curva, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_per_aplicado.place(relx=0.80, rely=0.5, relwidth=0.10, relheight=0.4)
        self.entry_per_aplicado.bind("<Return>", lambda event: self.format_per(event, self.entry_per_aplicado, self.entry_per_check_aplicado))

        # Botão Adicionar Etapa na Curva
        icon_image = self.base64_to_photoimage('savedown')
        self.btn_adicionar_etapa_curva = customtkinter.CTkButton(fr_etapas_curva, text='', image=icon_image, fg_color='transparent', command=self.incluir_etapas_click)
        self.btn_adicionar_etapa_curva.place(relx=0.905, rely=0.4, relwidth=0.04, relheight=0.4)

        # Botão Excluir Etapa da Curva
        icon_image = self.base64_to_photoimage('trash')  
        self.btn_excluir_etapa_curva = customtkinter.CTkButton(fr_etapas_curva, text='', image=icon_image, fg_color='transparent', command=self.excluir_etapas)
        self.btn_excluir_etapa_curva.place(relx=0.95, rely=0.4, relwidth=0.04, relheight=0.4)
        
        # Check Percentual Aplicado
        coordenadas_relx = 0.935
        coordenadas_rely = 0.085
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        fr_per_check_aplicado = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_per_check_aplicado.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_per_check_aplicado = customtkinter.CTkLabel(fr_per_check_aplicado, text="Check", anchor='w')
        lb_per_check_aplicado.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        self.entry_per_check_aplicado = customtkinter.CTkEntry(fr_per_check_aplicado, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_per_check_aplicado.configure(state='disabled')
        self.entry_per_check_aplicado.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)

    def consulta_curvas(self):
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.', parent=self.window_one)
            self.entry_empresa.focus()
            return
        
        if not self.entry_nome_curva.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo do Nome da Curva!!!.', parent=self.window_one)
            self.entry_nome_curva.focus()
            return
        
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get(), self.window_one)
        DS_Curva = self.entry_nome_curva.get().strip()
        
        # Preparar a tabela
        self.fr_list_curvas = customtkinter.CTkFrame(self.principal_frame, border_color="gray75", border_width=1)
        self.fr_list_curvas.place(relx=0.005, rely=0.16, relwidth=0.99, relheight=0.835)
        
        # Widgets - Listar Itens
        self.LItens_curvas = ttk.Treeview(self.fr_list_curvas, height=12, column=(
                                                                        'curva', 
                                                                        'prazo', 
                                                                        'etapa', 
                                                                        'inicio',
                                                                        'fim',
                                                                        'per_aplicado'
                                                                        ), show='headings')
        self.LItens_curvas.heading('curva', text="Curva de Negócio")
        self.LItens_curvas.column('curva', width=300, anchor='w')
        self.LItens_curvas.heading('prazo', text="Prazo Curva")
        self.LItens_curvas.column('prazo', width=10, anchor='c')
        self.LItens_curvas.heading('etapa', text="Etapa")
        self.LItens_curvas.column('etapa', width=300, anchor='w')
        self.LItens_curvas.heading('inicio', text="Início")
        self.LItens_curvas.column('inicio', width=10, anchor='c')
        self.LItens_curvas.heading('fim', text="Fim")
        self.LItens_curvas.column('fim', width=10, anchor='c')
        self.LItens_curvas.heading('per_aplicado', text="% Aplicado")
        self.LItens_curvas.column('per_aplicado', width=10, anchor='e')
        
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        
        self.scrollbar_curvas = ttk.Scrollbar(self.fr_list_curvas, orient='vertical')
        self.scrollbar_curvas.pack(side='right', fill='y')
        
        self.LItens_curvas.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.99)

        self.LItens_curvas.delete(*self.LItens_curvas.get_children())  # Limpa a tabela
        self.entry_prazo_curva.delete(0, tk.END)
        self.entry_etapas_curva.delete(0, tk.END)
        self.entry_inicio_curva.delete(0, tk.END)
        self.entry_fim_curva.delete(0, tk.END)
        self.entry_per_aplicado.delete(0, tk.END)   
       
        # Parametros da consulta
        conditions = []  
        # Condições iniciais
        if ID_Empresa is not None:
            conditions.append("Empresa_ID = %s")
            params = [ID_Empresa]
        
        if DS_Curva is not None:
            conditions.append("DS_Curva = %s")
            params.append(DS_Curva)
        
        # SQL para buscar os dados
        vs_sql = f"""
                        SELECT 
                            Empresa_ID, 
                            DS_Curva, 
                            Prazo_Curva,
                            Tipo_Periodo_Curva,
                            Mes_Inicio, 
                            Mes_Fim,
                            Per_Mensal
                        FROM Curva_Tempo
                        WHERE {' AND '.join(conditions)}
                        ORDER BY DS_Curva, CAST(Mes_Inicio AS UNSIGNED), CAST(Mes_Fim AS UNSIGNED)
                        
                  """
       
        myresult = db.executar_consulta(vs_sql, params)
        consulta = [(consulta) for consulta in myresult]
        
        if not consulta:
            messagebox.showinfo('Aviso', 'Não Existem Dados Para Esta Consulta!', parent=self.window_one)
            return
                
        # Inserir dados na tabela
        for item in consulta:
            formatted_item = (
                    item.get('DS_Curva'),
                    self.format_mes_fx(item.get('Prazo_Curva')),
                    item.get('Tipo_Periodo_Curva'),
                    self.format_mes_fx(item.get('Mes_Inicio')),
                    self.format_mes_fx(item.get('Mes_Fim')),
                    self.format_per_fx(item.get('Per_Mensal'))
                )
            
            self.LItens_curvas.insert('', 'end', values=formatted_item)

        self.LItens_curvas.configure(yscrollcommand=self.scrollbar_curvas.set)
        self.scrollbar_curvas.configure(command=self.LItens_curvas.yview)
        self.LItens_curvas.bind("<Double-1>", self.OnDoubleClick_Curvas)
        self.entry_empresa.focus()

    def OnDoubleClick_Curvas(self, event):
        selected_item = self.LItens_curvas.selection()
        if selected_item:
            values = self.LItens_curvas.item(selected_item, 'values')
            
            ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get(), self.window_one)
            DS_Curva = values[0]
            Prazo_Curva = values[1]
            Tipo_Periodo_Curva = values[2]
            Mes_Inicio = values[3]
            Mes_Fim = values[4]
            Per_Mensal = values[5]

            self.entry_nome_curva.delete(0, tk.END)
            self.entry_prazo_curva.delete(0, tk.END)
            self.entry_etapas_curva.delete(0, tk.END)
            self.entry_inicio_curva.delete(0, tk.END)
            self.entry_fim_curva.delete(0, tk.END)
            self.entry_per_aplicado.delete(0, tk.END)   

            self.entry_nome_curva.insert(0, DS_Curva)
            self.entry_prazo_curva.insert(0, self.format_mes_fx(Prazo_Curva))
            self.entry_etapas_curva.insert(0, Tipo_Periodo_Curva)
            self.entry_inicio_curva.insert(0, self.format_mes_fx(Mes_Inicio))
            self.entry_fim_curva.insert(0, self.format_mes_fx(Mes_Fim))
            self.entry_per_aplicado.insert(0, Per_Mensal)
            
            self.atualizar_empresas(event, self.entry_empresa)
            self.atualizar_curvas(event, self.obter_Empresa_ID(self.entry_empresa.get(), self.window_one), self.entry_nome_curva)
            self.atualizar_etapas_curvas(event, self.entry_etapas_curva)

    def gravar_curvas(self):
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.', parent=self.window_one)
            self.entry_empresa.focus()
            return
        
        if not self.entry_nome_curva.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo Nome da Curva!!!.', parent=self.window_one)
            self.entry_nome_curva.focus()
            return
        
        if not self.entry_prazo_curva.get():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Prazo da Curva!!!.', parent=self.window_one)
            self.entry_prazo_curva.focus()
            return
        
        
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get(), self.window_one)
        DS_Curva = self.entry_nome_curva.get().strip()
        Prazo_Curva = float(self.entry_prazo_curva.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        Tipo_Periodo_Curva = self.entry_etapas_curva.get().strip()
        
        # Consultar se a curva já existe
        vs_sql = f"""
                    SELECT * FROM Curvas 
                    WHERE 
                        Empresa_ID='{ID_Empresa}'
                        AND Nome_Curva='{DS_Curva}'
                """
        myresult = db._querying(vs_sql)
        if myresult:
            vs_sql = f"""
                        UPDATE Curvas SET
                            Prazo_Curva={Prazo_Curva}
                        WHERE 
                            Empresa_ID='{ID_Empresa}'
                            AND Nome_Curva='{DS_Curva}'
                    """
            db._querying(vs_sql)
        else:
            vs_sql = f"""
                        INSERT INTO Curvas (
                                            Empresa_ID, 
                                            Nome_Curva, 
                                            Prazo_Curva
                                            )
                                    VALUES(
                                            '{ID_Empresa}', 
                                            '{DS_Curva}', 
                                            {int(Prazo_Curva)}
                                            )
                    """
            db._querying(vs_sql)
        
        vs_sql = f"""
                    SELECT * FROM Curva_Tempo 
                    WHERE 
                        Empresa_ID='{ID_Empresa}'
                        AND DS_Curva='{DS_Curva}'
                """
        
        myresult = db._querying(vs_sql)
        if myresult:
            vs_sql = f"""
                        DELETE FROM Curva_Tempo 
                        WHERE 
                            Empresa_ID='{ID_Empresa}'
                            AND DS_Curva='{DS_Curva}'
                    """
            
            db._querying(vs_sql)
            
        # Agora, iteramos sobre os itens na TreeView e inserimos os novos registros
        for item in self.LItens_curvas.get_children():
            values = self.LItens_curvas.item(item)['values']
            Tipo_Periodo_Curva = values[2]
            Mes_Inicial = values[3]
            Mes_Final = values[4]
            Per_Uso = float(values[5].replace('%', '').replace(',', '.')) / 100

            vs_sql = f"""
                        INSERT INTO Curva_Tempo 
                                        (
                                        Empresa_ID, 
                                        DS_Curva, 
                                        Prazo_Curva, 
                                        Tipo_Periodo_Curva, 
                                        Mes_Inicio, 
                                        Mes_Fim, 
                                        Per_Mensal
                                        )
                                VALUES (
                                    '{ID_Empresa}',
                                    '{DS_Curva}',
                                    {int(Prazo_Curva)},
                                    '{Tipo_Periodo_Curva}',
                                    {int(Mes_Inicial.replace('º mês', ''))},
                                    {int(Mes_Final.replace('º mês', ''))},
                                    {round(Per_Uso, 4)}
                                )
                    """
            db._querying(vs_sql)
        messagebox.showinfo('Aviso', 'Curva de Tempo Gravada com Sucesso!', parent=self.window_one)
            
    def incluir_etapas_click(self):
        if not self.entry_prazo_curva.get():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Prazo da Curva!!!.', parent=self.window_one)
            self.entry_prazo_curva.focus()
            return
        
        if self.entry_etapas_curva.get().strip():
            if self.entry_per_check_aplicado.get():
                check = float(self.entry_per_check_aplicado.get().replace('%', '').replace(',', '.')) / 100
            else:
                check = 0.0
                self.entry_per_check_aplicado.insert(0, self.format_per_fx(check))
                self.entry_per_check_aplicado.configure(state='disabled')
            
            nr_item = (1 + int(self.entry_fim_curva.get().replace('º mês', ''))) - int(self.entry_inicio_curva.get().replace('º mês', ''))
            check += (float(self.entry_per_aplicado.get().replace('%', '').replace(',', '.')) / 100) * nr_item
            
            if check > 1:
                messagebox.showinfo('Gestor Negócios', 'Erro - % Não pode ser maior que 100%!', parent=self.window_one)
                self.entry_per_aplicado.focus()
                return
            
            self.entry_per_check_aplicado.configure(state='normal')
            self.entry_per_check_aplicado.delete(0, tk.END)
            self.entry_per_check_aplicado.insert(0, self.format_per_fx(check))
            self.entry_per_check_aplicado.configure(state='disabled')
            
            self.incluir_etapas()
            self.entry_etapas_curva.focus()
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher a Etapa da Curva!', parent=self.window_one)
            self.entry_etapas_curva.focus()

    def incluir_etapas(self):
        # Implementar a lógica para incluir etapas
        # Esta função deve adicionar a nova etapa à lista (provavelmente ao Treeview)
        ds_curva = self.entry_nome_curva.get().strip()
        prazo_curva = self.format_mes_fx(self.entry_prazo_curva.get().strip())
        etapa = self.entry_etapas_curva.get().strip()
        inicio = self.format_mes_fx(self.entry_inicio_curva.get().strip())
        fim = self.format_mes_fx(self.entry_fim_curva.get().strip())
        per_aplicado = self.entry_per_aplicado.get().strip()

        # Verificar se self.LItens_curvas existe
        if not hasattr(self, 'LItens_curvas'):
            # Se não existir, criar o widget
            self.criar_LItens_curvas()  # Você precisa implementar este método
        
        # Adicionar a nova etapa ao Treeview
        self.LItens_curvas.insert('', 'end', values=(ds_curva, prazo_curva, etapa, inicio, fim, per_aplicado))

        # Limpar os campos após a inclusão
        self.entry_etapas_curva.delete(0, tk.END)
        self.entry_inicio_curva.delete(0, tk.END)
        self.entry_fim_curva.delete(0, tk.END)
        self.entry_per_aplicado.delete(0, tk.END)  
    
    def criar_LItens_curvas(self):
        # Implementar a criação do widget LItens_curvas aqui
        # Este método deve conter o código que originalmente criou o widget
        self.fr_list_curvas = customtkinter.CTkFrame(self.principal_frame, border_color="gray75", border_width=1)
        self.fr_list_curvas.place(relx=0.005, rely=0.16, relwidth=0.99, relheight=0.835)
        
        self.LItens_curvas = ttk.Treeview(self.fr_list_curvas, height=12, column=(
                                                                        'curva', 
                                                                        'prazo', 
                                                                        'etapa', 
                                                                        'inicio',
                                                                        'fim',
                                                                        'per_aplicado'
                                                                        ), show='headings')
        self.LItens_curvas.heading('curva', text="Curva de Negócio")
        self.LItens_curvas.column('curva', width=300, anchor='w')
        self.LItens_curvas.heading('prazo', text="Prazo Curva")
        self.LItens_curvas.column('prazo', width=10, anchor='c')
        self.LItens_curvas.heading('etapa', text="Etapa")
        self.LItens_curvas.column('etapa', width=300, anchor='w')
        self.LItens_curvas.heading('inicio', text="Início")
        self.LItens_curvas.column('inicio', width=10, anchor='c')
        self.LItens_curvas.heading('fim', text="Fim")
        self.LItens_curvas.column('fim', width=10, anchor='c')
        self.LItens_curvas.heading('per_aplicado', text="% Aplicado")
        self.LItens_curvas.column('per_aplicado', width=10, anchor='e')
        
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.scrollbar_curvas = ttk.Scrollbar(self.fr_list_curvas, orient='vertical')
        self.scrollbar_curvas.pack(side='right', fill='y')
        
        self.LItens_curvas.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.99)
    
    def excluir_etapas(self):
        # Verificar se há um item selecionado
        selected_item = self.LItens_curvas.selection()
        if not selected_item:
            messagebox.showinfo('Aviso', 'Nenhum item selecionado para exclusão.', parent=self.window_one)
            return

        # Obter o item selecionado
        item = self.LItens_curvas.item(selected_item[0])
        values = item['values']

        # Atualizar os campos com os valores do item selecionado
        self.entry_etapas_curva.delete(0, tk.END)
        self.entry_etapas_curva.insert(0, values[2])
        self.entry_inicio_curva.delete(0, tk.END)
        self.entry_inicio_curva.insert(0, values[3])
        self.entry_fim_curva.delete(0, tk.END)
        self.entry_fim_curva.insert(0, values[4])
        self.entry_per_aplicado.delete(0, tk.END)
        self.entry_per_aplicado.insert(0, values[5])

        # Remover o item da lista
        self.LItens_curvas.delete(selected_item[0])

        # Limpar os campos após a inclusão
        self.entry_etapas_curva.delete(0, tk.END)
        self.entry_inicio_curva.delete(0, tk.END)
        self.entry_fim_curva.delete(0, tk.END)
        self.entry_per_aplicado.delete(0, tk.END)  

        # Recalcular o percentual total
        per_total = 0
        for item in self.LItens_curvas.get_children():
            values = self.LItens_curvas.item(item)['values']
            per_total += float(values[5].replace('%', '').replace(',', '.')) / 100

        # Atualizar o campo de verificação
        self.entry_per_check_aplicado.configure(state='normal')
        self.entry_per_check_aplicado.delete(0, tk.END)
        self.entry_per_check_aplicado.insert(0, self.format_per_fx(per_total))
        self.entry_per_check_aplicado.configure(state='disabled')

        # Ordenar a lista
        # self.LItens_curvas.delete(*self.LItens_curvas.get_children())
        # sorted_items = sorted(self.LItens_curvas.get_children(), key=lambda x: int(self.LItens_curvas.item(x)['values'][3].replace('º mês', '')))
        # for item in sorted_items:
        #     self.LItens_curvas.move(item, '', 'end')  
    