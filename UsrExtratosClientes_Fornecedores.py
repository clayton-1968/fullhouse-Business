from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Extrato_Clientes_Fornecedores(Widgets):
    def extrato_clientes_fornecedores(self):
        self.window_one.title('Relatório Contas a Pagar/Receber')
        self.clearFrame_principal()
        self.frame_cabecalho_extrato_clientes_fornecedores(self.principal_frame)
        self.frame_list_extrato(self.principal_frame)

    ################# dividindo a janela ###############
    def frame_cabecalho_extrato_clientes_fornecedores(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth,
                         relheight=coordenadas_relheight)
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

        # Unidade de Negócio
        coordenadas_relx = 0.26
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.17
        coordenadas_relheight = 0.07
        fr_unidade_negocio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_unidade_negocio.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth,
                                 relheight=coordenadas_relheight)
        lb_unidade_negocio = customtkinter.CTkLabel(fr_unidade_negocio, text="Unidade Negócios")
        lb_unidade_negocio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        unidade_negocios = []

        self.entry_unidade_negocio = AutocompleteCombobox(fr_unidade_negocio, width=30, font=('Times', 11),
                                                          completevalues=unidade_negocios)
        self.entry_unidade_negocio.pack()
        self.entry_unidade_negocio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_unidade_negocio.bind("<Button-1>",
                                        lambda event: self.atualizar_unidade_negocios(event, self.entry_empresa.get(),
                                                                                      self.entry_unidade_negocio))
        self.entry_unidade_negocio.bind('<Down>',
                                        lambda event: self.atualizar_unidade_negocios(event, self.entry_empresa.get(),
                                                                                      self.entry_unidade_negocio))

        # Período Vencimento
        TDta_Inicio = datetime.strptime("01/01/2000", "%d/%m/%Y")
        TDta_Fim = datetime.now()

        coordenadas_relx = 0.435
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.17
        coordenadas_relheight = 0.07
        fr_periodo = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_periodo.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth,
                         relheight=coordenadas_relheight)
        lb_periodo = customtkinter.CTkLabel(fr_periodo, text="Período Vencimento")
        lb_periodo.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        lb_dt_venc_inicio = customtkinter.CTkLabel(fr_periodo, text="Data Início")
        lb_dt_venc_inicio.place(relx=0.01, rely=0.30, relheight=0.125, relwidth=0.20)
        self.entry_dt_venc_inicio = customtkinter.CTkEntry(fr_periodo, fg_color="white", text_color="black",
                                                           justify=tk.CENTER)
        self.entry_dt_venc_inicio.delete(0, 'end')
        self.entry_dt_venc_inicio.insert(0, TDta_Inicio.strftime("%d/%m/%Y"))
        self.entry_dt_venc_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_venc_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_venc_inicio))
        self.entry_dt_venc_inicio.bind("<Return>",
                                       lambda event: self.muda_barrinha_dta(event, self.entry_dt_venc_inicio,
                                                                            self.entry_dt_venc_fim))

        lb_dt_venc_fim = customtkinter.CTkLabel(fr_periodo, text="Data Fim")
        lb_dt_venc_fim.place(relx=0.47, rely=0.30, relheight=0.125, relwidth=0.35)
        self.entry_dt_venc_fim = customtkinter.CTkEntry(fr_periodo, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_dt_venc_fim.delete(0, 'end')
        self.entry_dt_venc_fim.insert(0, TDta_Fim.strftime("%d/%m/%Y"))
        self.entry_dt_venc_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_venc_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_venc_inicio))
        self.entry_dt_venc_fim.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_venc_fim,
                                                                                     self.entry_info_pag_valor_parc))

        # Pessoa
        coordenadas_relx = 0.61
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.34
        coordenadas_relheight = 0.07
        fr_pessoa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_pessoa.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth,
                        relheight=coordenadas_relheight)
        lb_pessoa = customtkinter.CTkLabel(fr_pessoa, text="Cliente/Fornecedor/Prestador Serviços")
        lb_pessoa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        pessoas = []

        self.entry_pessoa = AutocompleteCombobox(fr_pessoa, width=30, font=('Times', 11), completevalues=pessoas)
        self.entry_pessoa.pack()
        self.entry_pessoa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_pessoa.bind("<Button-1>",
                               lambda event: self.atualizar_pessoa(event, self.entry_empresa.get(), self.entry_pessoa))
        self.entry_pessoa.bind('<Down>',
                               lambda event: self.atualizar_pessoa(event, self.entry_empresa.get(), self.entry_pessoa))

        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_extrato = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent',
                                                             command=self.consulta_extrato)
        self.btn_consultar_extrato.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)

    def frame_list_extrato(self, janela):
        ## Listbox _ Informações Pesquisa
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background="white", foreground="black", fieldbackground="white", borderwidth=0)

        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.085, relwidth=0.99, relheight=0.91)

        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Widgets - Listar Parcelas
        self.LExtrato = ttk.Treeview(self.fr_list, height=7, column=(
            'ID',
            'Descricao',
            'Dta_Vencto_Liquidacao',
            'Tipo',
            'Banco',
            'Referencia',
            'Debitos',
            'Creditos',
            'Saldo'
        ), show='headings')

        self.LExtrato.heading('#0', text='#', anchor='center')
        self.LExtrato.heading('#1', text='ID', anchor='center')
        self.LExtrato.heading('#2', text='Descrição', anchor='center')
        self.LExtrato.heading('#3', text='Data (Vcto/Liq.)', anchor='center')
        self.LExtrato.heading('#4', text='Tipo', anchor='center')
        self.LExtrato.heading('#5', text='Banco', anchor='center')
        self.LExtrato.heading('#6', text='Referência', anchor='center')
        self.LExtrato.heading('#7', text='Débitos', anchor='center')
        self.LExtrato.heading('#8', text='Créditos', anchor='center')
        self.LExtrato.heading('#9', text='Saldo', anchor='center')

        Col = 30

        self.LExtrato.column('#0', width=2, anchor='w')
        self.LExtrato.column('ID', width=15, anchor='e')
        self.LExtrato.column('Descricao', width=800, anchor='w')
        self.LExtrato.column('Dta_Vencto_Liquidacao', width=5, anchor='c')
        self.LExtrato.column('Tipo', width=Col, anchor='c')
        self.LExtrato.column('Banco', width=Col, anchor='c')
        self.LExtrato.column('Referencia', width=Col, anchor='c')
        self.LExtrato.column('Debitos', width=Col, anchor='e')
        self.LExtrato.column('Creditos', width=Col, anchor='e')
        self.LExtrato.column('Saldo', width=Col, anchor='e')

        self.LExtrato.pack(expand=True, fill='both')
        self.LExtrato.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)

    def consulta_extrato(self):
        if self.entry_empresa.get() != '':
            ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
            return

        if self.entry_pessoa.get() != '':
            ID_Pessoa = self.obter_Pessoa_ID(self.entry_pessoa.get())
        else:
            ID_Pessoa = self.entry_pessoa.get()

        if self.entry_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.entry_unidade_negocio.get())
        else:
            ID_Unidade = self.entry_unidade_negocio.get()

        Dta_Vcto_Inicio = self.entry_dt_venc_inicio.get()
        Dta_Vcto_Fim = self.entry_dt_venc_fim.get()
        Dta_Vcto_Inicio_str = datetime.strptime(Dta_Vcto_Inicio, "%d/%m/%Y")
        last_year = Dta_Vcto_Inicio_str - timedelta(days=365)
        Dta_Lcto = last_year.strftime('%Y-%m-%d')
        Dta_Anterior = last_year.strftime('%Y%m%d')

        Dta_Vcto_Inicio = datetime.strptime(Dta_Vcto_Inicio, "%d/%m/%Y").strftime('%Y-%m-%d')
        Dta_Vcto_Fim = datetime.strptime(Dta_Vcto_Fim, "%d/%m/%Y").strftime('%Y-%m-%d')

        # Limpa a lista atual antes de inserir novos resultados
        self.LExtrato.delete(*self.LExtrato.get_children())

        # Lista para armazenar as condições
        params = []
        conditions_1 = []
        conditions_2 = []
        conditions_3 = []
        conditions_4 = []

        conditions_1.append("dd.ID_Empresa = %s ")
        params = [ID_Empresa]
        if ID_Pessoa != '':
            conditions_1.append("dd.ID_Pessoa = %s ")
            params.append(ID_Pessoa)
        if ID_Unidade != '':
            conditions_1.append("dd.ID_Unidade = %s ")
            params.append(ID_Unidade)
        conditions_1.append("dd.Doc_Dta_Documento BETWEEN %s AND %s")
        params.append(Dta_Vcto_Inicio)
        params.append(Dta_Vcto_Fim)

        conditions_2.append("ff.ID_Empresa = %s ")
        params.append(ID_Empresa)
        if ID_Pessoa != '':
            conditions_2.append("ff.ID_Pessoa = %s ")
            params.append(ID_Pessoa)
        if ID_Unidade != '':
            conditions_2.append("ff.ID_Unidade = %s ")
            params.append(ID_Unidade)
        conditions_2.append("ff.Fin_Dta_Liquidacao BETWEEN %s AND %s")
        params.append(Dta_Vcto_Inicio)
        params.append(Dta_Vcto_Fim)
        conditions_2.append("ff.Fin_VlR_Liquidacao<>0")

        conditions_3.append("dd.ID_Empresa = %s ")
        params.append(ID_Empresa)
        if ID_Pessoa != '':
            conditions_3.append("dd.ID_Pessoa = %s ")
            params.append(ID_Pessoa)
        if ID_Unidade != '':
            conditions_3.append("dd.ID_Unidade = %s ")
            params.append(ID_Unidade)
        conditions_3.append("dd.Doc_Dta_Documento<=%s")
        params.append(Dta_Anterior)

        conditions_4.append("ff.ID_Empresa = %s ")
        params.append(ID_Empresa)
        if ID_Pessoa != '':
            conditions_4.append("ff.ID_Pessoa = %s ")
            params.append(ID_Pessoa)
        if ID_Unidade != '':
            conditions_4.append("ff.ID_Unidade = %s ")
            params.append(ID_Unidade)
        conditions_4.append("ff.Fin_Dta_Liquidacao<=%s")
        params.append(Dta_Anterior)
        conditions_4.append("ff.Fin_VlR_Liquidacao<>0")

        strSql = f"""
                    SELECT  
                    Empresa_Codigo, 
                    Empresa_Descricao, 
                    Pessoa_Codigo, 
                    Pessoa_Descricao, 
                    Unidade_ID, 
                    Unidade_Descricao, 
                    Nr_Documento, 
                    Dta, 
                    SUM(Vlr) AS Vlr, 
                    Bco, 
                    Tipo
                    FROM (
                    SELECT
                    dd.ID_Empresa                       AS Empresa_Codigo,
                    pp.Pri_Descricao                    AS Empresa_Descricao,
                    dd.ID_Pessoa                        AS Pessoa_Codigo,
                    pp1.Pessoas_Descricao               AS Pessoa_Descricao,
                    dd.ID_Unidade                       AS Unidade_ID,
                    un.Unidade_Descricao                AS Unidade_Descricao,
                    'Documento Fiscal'                  AS Tipo,
                    dd.Doc_Num_Documento                AS Nr_Documento,
                    1                                   AS Parcela,
                    dd.Doc_Dta_Documento                AS Dta,
                    dd.Doc_VlR  *-1                     AS Vlr,
                    ''                                  As Bco
                    FROM TB_CB_Doc dd
                    INNER JOIN TB_Empresas        pp  ON pp.Pri_Cnpj=dd.ID_Empresa
                    INNER JOIN TB_Pessoas         pp1 ON pp1.Pessoas_CPF_CNPJ=dd.ID_Pessoa AND pp1.Empresa_ID=dd.ID_Empresa
                    INNER JOIN TB_UnidadesNegocio un  ON un.Unidade_ID=dd.ID_Unidade AND un.Empresa_ID=dd.ID_Empresa
                    WHERE {' AND '.join(conditions_1)}

                    Union ALL

                    SELECT
                    ff.ID_Empresa                       AS Empresa_Codigo,
                    pp.Pri_Descricao                    AS Empresa_Descricao,
                    ff.ID_Pessoa                        AS Pessoa_Codigo,
                    pp1.Pessoas_Descricao               AS Pessoa_Descricao,
                    ff.ID_Unidade                       AS Unidade_ID,
                    un.Unidade_Descricao                AS Unidade_Descricao,
                    'Liquidacao'                        AS Tipo,
                    ff.Fin_Num_documento                AS Nr_Documento,
                    ff.Fin_Parcela                      AS Parcela,
                    COALESCE(ff.Fin_Dta_Liquidacao,0)   AS Dta,
                    COALESCE(ff.Fin_VlR_Liquidacao,0)   AS Vlr,
                    COALESCE(ff.ID_Bco_Liquidacao, 0)   As Bco
                    FROM TB_Financeiro ff
                    INNER JOIN TB_Empresas        pp  ON pp.Pri_Cnpj=ff.ID_Empresa
                    INNER JOIN TB_Pessoas         pp1 ON pp1.Pessoas_CPF_CNPJ=ff.ID_Pessoa AND pp1.Empresa_ID=ff.ID_Empresa
                    INNER JOIN TB_UnidadesNegocio un  ON un.Unidade_ID=ff.ID_Unidade AND un.Empresa_ID=ff.ID_Empresa
                    WHERE {' AND '.join(conditions_2)}

                    Union ALL

                    SELECT
                    dd.ID_Empresa                       AS Empresa_Codigo,
                    pp.Pri_Descricao                    AS Empresa_Descricao,
                    dd.ID_Pessoa                        AS Pessoa_Codigo,
                    pp1.Pessoas_Descricao               AS Pessoa_Descricao,
                    dd.ID_Unidade                       AS Unidade_ID,
                    un.Unidade_Descricao                AS Unidade_Descricao,
                    'SaldoInicial'                      AS Tipo,
                    '-'                                 AS Nr_Documento,
                    '00'                                AS Parcela,
                    {Dta_Lcto}                          AS Dta,
                    SUM(dd.Doc_VlR*-1)                  AS Vlr,
                    ''                                  As Bco
                    FROM TB_CB_Doc dd
                    INNER JOIN TB_Empresas        pp  ON pp.Pri_Cnpj=dd.ID_Empresa
                    INNER JOIN TB_Pessoas         pp1 ON pp1.Pessoas_CPF_CNPJ=dd.ID_Pessoa AND pp1.Empresa_ID=dd.ID_Empresa
                    INNER JOIN TB_UnidadesNegocio un  ON un.Unidade_ID=dd.ID_Unidade AND un.Empresa_ID=dd.ID_Empresa
                    WHERE {' AND '.join(conditions_3)}
                    GROUP BY dd.ID_Empresa, pp.Pri_Descricao, dd.ID_Pessoa, pp1.Pessoas_Descricao, dd.ID_Unidade, un.Unidade_Descricao

                    Union ALL

                    SELECT
                    ff.ID_Empresa                           AS Empresa_Codigo,
                    pp.Pri_Descricao                        AS Empresa_Descricao,
                    ff.ID_Pessoa                            AS Pessoa_Codigo,
                    pp1.Pessoas_Descricao                   AS Pessoa_Descricao,
                    ff.ID_Unidade                           AS Unidade_ID,
                    un.Unidade_Descricao                    AS Unidade_Descricao,
                    'SaldoInicial'                          AS Tipo,
                    '-'                                     AS Nr_Documento,
                    '00'                                    AS Parcela,
                    {Dta_Lcto}                              AS Dta,
                    SUM(COALESCE(ff.Fin_VlR_Liquidacao,0))  AS Vlr,
                    '0'                                     AS Bco
                    FROM TB_Financeiro ff
                    INNER JOIN TB_Empresas        pp  ON pp.Pri_Cnpj=ff.ID_Empresa
                    INNER JOIN TB_Pessoas         pp1 ON pp1.Pessoas_CPF_CNPJ=ff.ID_Pessoa AND pp1.Empresa_ID=ff.ID_Empresa
                    INNER JOIN TB_UnidadesNegocio un  ON un.Unidade_ID=ff.ID_Unidade AND un.Empresa_ID=ff.ID_Empresa
                    WHERE {' AND '.join(conditions_4)}
                    GROUP BY ff.ID_Empresa, pp.Pri_Descricao, ff.ID_Pessoa, pp1.Pessoas_Descricao , ff.ID_Unidade, un.Unidade_Descricao
                    ) AS COMPLETO
                    GROUP BY Empresa_Codigo, Empresa_Descricao, Pessoa_Codigo, Pessoa_Descricao, Unidade_ID, Unidade_Descricao, Nr_Documento, Bco , Parcela, Dta, Tipo
                    ORDER BY Unidade_ID, Pessoa_Codigo, Dta, vlr DESC
                """

        results = db.executar_consulta(strSql, params)

        # Carregar Lista
        icon_image = self.base64_to_photoimage('lupa')

        # Configura as tags para o Treeview
        self.LExtrato.tag_configure('vermelho', foreground='red')  # Define a tag 'vermelho' para texto vermelho
        self.LExtrato.tag_configure('preto', foreground='black')  # Define a tag 'preto' para texto preto
        tags = []

        total = 0
        saldo = 0

        # Agrupando dados por Unidade
        unidade_map = {}
        for entry in results:
            ID_Unidade = entry["Unidade_ID"]
            if ID_Unidade not in unidade_map:
                unidade_map[ID_Unidade] = {"DS_Unidade": entry["Unidade_Descricao"], "pessoas": {}}

            ID_Pessoa = entry["Pessoa_Codigo"]
            if ID_Pessoa not in unidade_map[ID_Unidade]["pessoas"]:
                unidade_map[ID_Unidade]["pessoas"][ID_Pessoa] = {"DS_Pessoa": entry["Pessoa_Descricao"],
                                                                 "transactions": []}

            unidade_map[ID_Unidade]["pessoas"][ID_Pessoa]["transactions"].append(entry)

        # Agrupando dados por Unidade
        for ID_Unidade, unit_data in unidade_map.items():
            # Adiciona a entrada da Unidade
            unit_item = self.LExtrato.insert("", "end", text=ID_Unidade,
                                             values=(ID_Unidade, unit_data["DS_Unidade"], '', '', '', '', '', '', ''))

            for ID_Pessoa, person_data in unit_data["pessoas"].items():
                # Adiciona a entrada da Pessoa
                # print(person_data["DS_Pessoa"])
                person_item = self.LExtrato.insert("", "end", text=ID_Pessoa, values=(
                    ID_Pessoa, person_data["DS_Pessoa"], '', '', '', '', '', '', ''))

                saldo = 0  # Reinicia o saldo para cada pessoa

                for transaction in person_data["transactions"]:
                    # Formata a data do documento
                    Dta_Documento = transaction["Dta"]
                    Dta_obj = datetime.strptime(Dta_Documento, "%Y-%m-%d")
                    # Dta_Documento = datetime.strptime(Dta_Documento, "%Y/%m/%d")
                    Dta_Documento = Dta_obj.strftime("%d/%m/%Y")
                    # Dta_Documento = transaction["Dta"]
                    tipo = transaction["Tipo"]
                    banco = transaction["Bco"]
                    nr_documento = transaction["Nr_Documento"]
                    vlr = transaction["Vlr"]

                    # Verifica se o valor é negativo para formatar os débitos e créditos
                    debit = f"{abs(vlr):,.2f}" if vlr < 0 else "0.00"
                    credit = "0.00" if vlr < 0 else f"{vlr:,.2f}"

                    # Atualiza o saldo
                    saldo += vlr
                    total += vlr

                    # Adiciona a linha de transação na lista
                    # print(person_item, Dta_Documento, tipo, banco, nr_documento, debit, credit, f"{saldo:,.2f}")
                    self.LExtrato.insert("", "end", text="", values=(
                        '', '', Dta_Documento, tipo, banco, nr_documento, debit, credit, f"{saldo:,.2f}"))

        self.LExtrato.tag_configure('odd', background='#eee')
        self.LExtrato.tag_configure('even', background='#ddd')
        self.LExtrato.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.LExtrato.yview)


Extrato_Clientes_Fornecedores()