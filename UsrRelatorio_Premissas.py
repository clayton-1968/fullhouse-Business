from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Resumo_Premissas(Widgets):
    def resumo_premissas(self):
        self.window_one.title('Relatório de Premissas')
        self.clearFrame_principal()
        self.frame_linha_premissas_1(self.principal_frame)
        self.frame_linha_premissas_2(self.principal_frame)
        
################# dividindo a janela ###############
    def frame_linha_premissas_1(self, janela):
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

        self.combo_empresa_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.combo_empresa_empresa.pack()
        self.combo_empresa_empresa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.combo_empresa_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.combo_empresa_empresa))
        self.combo_empresa_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.combo_empresa_empresa))
        self.combo_empresa_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.combo_empresa_empresa))
        self.combo_empresa_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_orcamento))

        # Orçamento
        coordenadas_relx = 0.465
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.33
        coordenadas_relheight = 0.07
        fr_orcamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_orcamento.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_orcamento = customtkinter.CTkLabel(fr_orcamento, text="Orçamento", anchor='w')
        lb_orcamento.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        orcamentos = []

        self.combo_orcamento = AutocompleteCombobox(fr_orcamento, width=30, font=('Times', 11), completevalues=orcamentos)
        self.combo_orcamento.pack()
        self.combo_orcamento.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.combo_orcamento.bind("<Button-1>", lambda event: self.atualizar_orcamentos(event, self.combo_empresa_empresa.get(), self.combo_orcamento))
        self.combo_orcamento.bind('<Down>', lambda event: self.atualizar_orcamentos(event, self.combo_empresa_empresa.get(), self.combo_orcamento))
        self.combo_orcamento.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_tipo_lcto_descr))

        # Tipo Lançamento
        fr_tpo_lancamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_lancamento.place(relx=0.80, rely=0.01,relwidth=0.10, relheight=0.07)
        lb_tpo_lancamento = customtkinter.CTkLabel(fr_tpo_lancamento, text="Tipo Lçto", anchor='w')
        lb_tpo_lancamento.place(relx=0.009, rely=0.01, relheight=0.30, relwidth=0.55)

        self.opcoes_lcto = ["CPA", "CRE", "CTA"]
        self.combo_tipo_lcto_descr = customtkinter.CTkComboBox(fr_tpo_lancamento, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes_lcto)
        self.combo_tipo_lcto_descr.place(relx=0.005, rely=0.5, relwidth=0.985, relheight=0.4)
        self.combo_tipo_lcto_descr.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_centro))

    def frame_linha_premissas_2(self, janela):
        # Centro de Resultado
        fr_centro = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_centro.place(relx=0.005, rely=0.085,relwidth=0.4925, relheight=0.07)
        lb_centro = customtkinter.CTkLabel(fr_centro, text="Centro de Resultado", anchor='w')
        lb_centro.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        centro = []
        self.entry_centro = AutocompleteCombobox(fr_centro, width=30, font=('Times', 11), completevalues=centro)
        self.entry_centro.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_centro.bind("<Button-1>", lambda event: self.atualizar_centro_resultado(event, self.combo_empresa_empresa.get(), self.entry_centro))
        self.entry_centro.bind('<Down>', lambda event: self.atualizar_centro_resultado(event, self.combo_empresa_empresa.get(), self.entry_centro))
        self.entry_centro.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_natureza))
        
        
        # Natureza
        fr_natureza = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_natureza.place(relx=0.5025, rely=0.085,relwidth=0.4925, relheight=0.07)
        lb_natureza = customtkinter.CTkLabel(fr_natureza, text="Natureza Financeira", anchor='w')
        lb_natureza.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        natureza = []
        self.entry_natureza = AutocompleteCombobox(fr_natureza, width=30, font=('Times', 11), completevalues=natureza)
        self.entry_natureza.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_natureza.bind("<Button-1>", lambda event: self.atualizar_natureza_financeira(event, self.combo_empresa_empresa.get(), self.entry_natureza))
        self.entry_natureza.bind('<Down>', lambda event: self.atualizar_natureza_financeira(event, self.combo_empresa_empresa.get(), self.entry_natureza))
        self.entry_natureza.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_centro_credito))


        def consultar():
            Empresa_DS = self.combo_empresa_empresa.get()
            Orc_DS     = self.combo_orcamento.get()
            Orc_Tpo    = self.combo_tipo_lcto_descr.get()
            Cen_DS     = self.entry_centro.get()
            Nat_DS     = self.entry_natureza.get()
            
            if Empresa_DS != '':
                ID_Empresa = self.obter_Empresa_ID(Empresa_DS)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            if Orc_DS != '':
                ID_Orc = self.obter_Orc_ID(Orc_DS)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!")
                return
            
            if Cen_DS != '':
                ID_Cen = self.obter_Centro_ID(Cen_DS)
            else:
                ID_Cen = ''

            if Nat_DS != '':
                ID_Nat = self.obter_Natureza_ID(Nat_DS)
            else:
                ID_Nat = ''
            
            lista = self.Consulta_Premissas(ID_Empresa, ID_Orc, Orc_Tpo, ID_Cen, ID_Nat)
            
            self.fr_list_premissas = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
            self.fr_list_premissas.place(relx=0.005, rely=0.16, relwidth=0.986, relheight=0.83)
            
            self.scrollbar_premissas = ttk.Scrollbar(self.fr_list_premissas, orient='vertical')
            self.scrollbar_premissas.pack(side='right', fill='y')
            
            # Widgets - Listar
            self.list_g = ttk.Treeview(self.fr_list_premissas, height=12,
                                       columns=(
                                                "ID", 
                                                "Centro Débito", 
                                                "Natureza Débito", 
                                                "Centro Crédito", 
                                                "Natureza Crédito",
                                                "Quantidade", 
                                                "Valor", 
                                                "Periodicidade", 
                                                "Dta Reajuste", 
                                                "Tpo Lçto", 
                                                "Dta Início", 
                                                "Dta Fim", 
                                                "Histórico"
                                                ),
                                            show='headings', 
                                            selectmode='browse'
                                        )
            self.list_g.pack(side='left', fill='both', expand=1)            
            
           
            # Configurando as headings e a largura das colunas
            column_widths = {
                "ID": 5,
                "Centro Débito": 120,
                "Natureza Débito": 120,
                "Centro Crédito": 120,
                "Natureza Crédito": 120,
                "Quantidade": 40,
                "Valor": 40,
                "Periodicidade": 20,
                "Dta Reajuste": 20,
                "Tpo Lçto": 20,
                "Dta Início": 20,
                "Dta Fim": 20,
                "Histórico": 500
            }

            for col in self.list_g['columns']:
                self.list_g.heading(col, text=col)
                if col == 'Centro Débito' or col == 'Natureza Débito' or col == 'Centro Crédito' or col == 'Natureza Crédito':
                    self.list_g.column(col, width=column_widths[col], anchor='w')
                elif col == 'Quantidade' or col == 'Valor':
                    self.list_g.column( col, width=column_widths[col], anchor='e')
                else:
                    self.list_g.column(col, width=column_widths[col], anchor='center')

            self.list_g.pack(pady=10)
            
            self.list_g.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.98)

            # Limpa a lista atual antes de inserir novos resultados
            self.list_g.delete(*self.list_g.get_children())

            for item in lista:
                Dta_Reajuste = item.get('Idx_Data')
                Dta_Inicio = item.get('Dta_Inicio')
                Dta_Fim = item.get('Dta_Fim')
                
                if Dta_Reajuste is not None:
                    data_reajuste_formatada = Dta_Reajuste.strftime('%d/%m/%Y')
                else:
                    data_reajuste_formatada = ''  # Valor padrão ou outro tratamento de erro

                if Dta_Inicio is not None:
                    data_inicio_formatada = Dta_Inicio.strftime('%d/%m/%Y')
                else:
                    data_inicio_formatada = ''  # Valor padrão ou outro tratamento de erro

                if Dta_Fim is not None:
                    data_fim_formatada = Dta_Fim.strftime('%d/%m/%Y')
                else:
                    data_fim_formatada = ''  # Valor padrão ou outro tratamento de erro
                 
                formatted_item = (
                    item.get('Prem_ID'),
                    item.get('Cen_DS_Debito'),
                    item.get('Con_DS_Debito'),
                    item.get('Cen_DS_Credito'),
                    item.get('Con_DS_Credito'),
                    item.get('Quantidade'),
                    item.get('Valor'),
                    item.get('Periodicidade_DS'),
                    data_reajuste_formatada,
                    item.get('Tpo_Lcto'),
                    data_inicio_formatada,
                    data_fim_formatada,
                    item.get('Historico')
                )
                self.list_g.insert('', 'end', values=formatted_item)

            self.list_g.tag_configure('odd', background='#eee')
            self.list_g.tag_configure('even', background='#ddd')
            self.list_g.configure(yscrollcommand=self.scrollbar_premissas.set)
            self.scrollbar_premissas.configure(command=self.list_g.yview)

            def selected_premissas():
                selected_item = self.list_g.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.list_g.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.list_g.item(selected_item, 'values')
                    
                    ID_Lcto = ''
                    if Empresa_DS != '':
                        ID_Empresa = self.obter_Empresa_ID(Empresa_DS)
                    else:
                        messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                        return
                    
                    if Orc_DS != '':
                        ID_Orc = self.obter_Orc_ID(Orc_DS)
                    else:
                        messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!")
                        return
                    
                    ID_Lcto = values[0]
                    self.premissas_orcamento(ID_Empresa, Empresa_DS, ID_Orc, Orc_DS, ID_Lcto)
            
            def selected_excluir():
                # self.list_g.delete(row_id)
                messagebox.showinfo("Informação", "Em Manutenção!!")
                
            def postPopUpMenu(event):
                row_id = self.list_g.identify_row(event.y)
                if row_id:  # Realiza a verificação se a linha existe.
                    self.list_g.selection_set(row_id)
                    row_values = self.list_g.item(row_id)['values']
                    # print(row_values)
                    
                    postPopUpMenu = tk.Menu(self.list_g, tearoff=0, font=('Verdana', 11))
                    
                    postPopUpMenu.add_command(label='Alterar Premissa', accelerator='Ctrl+S', command= selected_premissas)
                    postPopUpMenu.add_separator()
                    postPopUpMenu.add_command(label='Excluir Premissa', accelerator='Delete', command=selected_excluir)
                    postPopUpMenu.post(event.x_root, event.y_root)
            
            self.list_g.bind("<Double-1>", postPopUpMenu)  # 'Double-1' é o duplo clique do mouse
            self.list_g.bind("<Button-3>", postPopUpMenu)  # 'Button-3' é o clique direito do mouse
            self.list_g.bind('<Control-s>', lambda event: selected_premissas() if self.list_g.selection() else None)
            self.list_g.bind('<Delete>', lambda event: selected_excluir() if self.list_g.selection() else None)

        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=consultar)
        self.btn_consultar.pack(pady=10)
        self.btn_consultar.place(relx=0.905, rely=0.02, relwidth=0.04, relheight=0.05)

        # Botão Incluir Novo Estudo
        def nova_premissa():
            Empresa_DS = self.combo_empresa_empresa.get()
            Orc_DS     = self.combo_orcamento.get()
            ID_Lcto    = ''
            
            if Empresa_DS != '':
                ID_Empresa = self.obter_Empresa_ID(Empresa_DS)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            if Orc_DS != '':
                ID_Orc = self.obter_Orc_ID(Orc_DS)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!")
                return
            
            self.premissas_orcamento(ID_Empresa, Empresa_DS, ID_Orc, Orc_DS, ID_Lcto)

        icon_image = self.base64_to_photoimage('open_book')
        self.btn_novo_estudo = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=nova_premissa)
        self.btn_novo_estudo.pack(pady=10)
        self.btn_novo_estudo.place(relx=0.95, rely=0.02, relwidth=0.04, relheight=0.05)
    
    def Consulta_Premissas(self, ID_Empresa, ID_Orc, Orc_Tpo, ID_Cen, ID_Nat):
        ID_Empresa = str(ID_Empresa.strip()) if ID_Empresa != '' else None
        ID_Orc = ID_Orc.strip() if ID_Orc != '' else None
        Orc_Tpo = Orc_Tpo.strip() if Orc_Tpo != '' else None
        ID_Cen = ID_Cen.strip() if ID_Cen != '' else None
        ID_Nat = ID_Nat.strip() if ID_Nat != '' else None
        
        conditions = []  # Lista para armazenar as condições
        # Condições iniciais
        params = []
        if ID_Empresa is not None:
            conditions.append("pp.Pri_ID = %s")
            params.append(ID_Empresa)

        if ID_Orc is not None:
            conditions.append("pp.Orc_ID = %s")
            params.append(ID_Orc)

        if ID_Cen is not None:
            if Orc_Tpo == "CPA":
                conditions.append("pp.Cen_ID_Debito = %s")
            else:
                conditions.append("pp.Cen_ID_Credito = %s")
            params.append(ID_Cen)
        
        if ID_Nat is not None:
            if Orc_Tpo == "CPA":
                conditions.append("pp.Con_ID_Debito = %s")
            else:
                conditions.append("pp.Con_ID_Credito = %s")
            params.append(ID_Nat)

        strSql = f"""
                    SELECT 
                        pp.Orc_ID                                   AS Orc_ID, 
                        pp.Prem_ID                                  AS Prem_ID, 
                        pp.Cen_ID_Debito                            AS Cen_ID_Debito,  
                        cc2.Cen_Descricao                           AS Cen_DS_Debito, 
                        pp.Con_ID_Debito                            AS Con_ID_Debito,  
                        cc.Nat_Descricao                            AS Con_DS_Debito, 
                        pp.Cen_ID_Credito                           AS Cen_ID_Credito, 
                        cc3.Cen_Descricao                           AS Cen_DS_Credito, 
                        pp.Con_ID_Credito                           AS Con_ID_Credito, 
                        cc1.Nat_Descricao                           AS Con_DS_Credito, 
                        pp.Prem_Historico                           AS Historico, 
                        FORMAT(pp.Preco_ID, 2, 'de_DE')             AS Preco_ID, 
                        cc4.Preco_Descricao                         AS Preco_DS, 
                        FORMAT(cc4.Preco_Valor, 2, 'de_DE')         AS Valor, 
                        FORMAT(pp.Prem_Quantidade, 2, 'de_DE')      AS Quantidade, 
                        cc6.TipodeMedida_Diminutivo                 AS Tpo_Medida, 
                        Tipo_Lcto                                   AS Tpo_Lcto, 
                        pp.Prem_Dedutivel                           AS Dedutivel, 
                        pp.Prem_Financeiro                          AS Financeiro, 
                        pp.Prem_PrazoPgto                           AS PrazoPgto, 
                        pp.Prem_aVista                              AS aVista, 
                        pp.Prem_aPrazo                              AS aPrazo, 
                        pp.Prem_nrParc                              AS Nr_Parcelas, 
                        pp.Prem_txJuros                             AS Tx_Juros, 
                        pp.Prem_ICMS                                AS ICMS, 
                        pp.Prem_PISCofins                           AS Pis_Cofins, 
                        pp.Nat_ID                                   AS Nat_ID, 
                        
                        pp.Idx_ID                                   AS Idx_ID, 
                        cc7.Idx_DS                                  AS Idx_DS, 
                        pp.Idx_Data                                 AS Idx_Data, 
                        pp.Periodi_ID                               AS Periodicidade_ID, 
                        cc8.Periodi_Descricao                       AS Periodicidade_DS, 
                        pp.Prem_DtaInicio                           AS Dta_Inicio, 
                        pp.Prem_DtaFim                              AS Dta_Fim, 
                        pp.Status_ID                                AS Status_ID 
                    FROM orc_premissas pp 
                    INNER JOIN TB_Natureza       cc  ON cc.Nat_ID=pp.Con_ID_Debito and cc.Empresa_ID=pp.Pri_ID
                    INNER JOIN TB_Natureza       cc1 ON cc1.Nat_ID=pp.Con_ID_Credito and cc1.Empresa_ID=pp.Pri_ID 
                    INNER JOIN centrocusto       cc2 ON cc2.Cen_ID=pp.Cen_ID_Debito and cc2.Empresa_ID=pp.Pri_ID
                    INNER JOIN centrocusto       cc3 ON cc3.Cen_ID=pp.Cen_ID_Credito and cc3.Empresa_ID=pp.Pri_ID
                    INNER JOIN orc_precos        cc4 ON cc4.Preco_ID=pp.Preco_ID and cc4.Orc_ID=pp.Orc_ID and cc4.Empresa_ID=pp.Pri_ID
                    INNER JOIN TB_TiposdeMedida  cc6 ON cc6.TipodeMedida_ID=cc4.Unidade_ID 
                    INNER JOIN Orc_idx           cc7 ON cc7.Idx_ID=pp.Idx_ID
                    INNER JOIN orc_periodicidade cc8 ON cc8.Periodi_ID=pp.Periodi_ID
                    WHERE {' AND '.join(conditions)} 
                    ORDER BY Cen_ID_Debito, Con_ID_Debito"""

        myresult = db.executar_consulta(strSql, params)
        consulta = [(consulta) for consulta in myresult]

        return consulta

Resumo_Premissas()
