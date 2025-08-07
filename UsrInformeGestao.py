from UsrCadastros import *
from widgets import Widgets


class InformeGestao(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def informe_gestao(self, principal_frame):
        self.images_base64()

        self.window_one.title('Relatório Informe de Gestão')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_info_gestao()

    def create_widgets_info_gestao(self):
        # CNPJ
        self.fr_cnpj_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                          border_width=1)
        self.fr_cnpj_info_gestao.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_cnpj_info_gestao = customtkinter.CTkLabel(self.fr_cnpj_info_gestao, text="CNPJ")
        self.lb_cnpj_info_gestao.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_cnpj_info_gestao = customtkinter.CTkEntry(self.fr_cnpj_info_gestao, fg_color="white",
                                                             text_color="black",
                                                             justify=tk.CENTER)
        self.entry_cnpj_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Nome (Empresa)
        self.frame_empresa(self.frame_principal, 0.105, 0, 0.30, 0.07)

        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_banco))

        # Código Orçamento
        self.fr_codigo_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                            border_width=1)
        self.fr_codigo_info_gestao.place(relx=0.41, rely=0, relwidth=0.075, relheight=0.07)

        self.lb_codigo_info_gestao = customtkinter.CTkLabel(self.fr_codigo_info_gestao, text="Cód. Orç.")
        self.lb_codigo_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_codigo_info_gestao = customtkinter.CTkEntry(self.fr_codigo_info_gestao, fg_color="white",
                                                               text_color="black",
                                                               justify=tk.CENTER)
        self.entry_codigo_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Descrição Orçamento
        self.fr_descricao_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                               border_width=1)
        self.fr_descricao_info_gestao.place(relx=0.485, rely=0, relwidth=0.20, relheight=0.07)

        self.lb_descricao_info_gestao = customtkinter.CTkLabel(self.fr_descricao_info_gestao,
                                                               text="Descrição Orçamento")
        self.lb_descricao_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_info_gestao = customtkinter.CTkEntry(self.fr_descricao_info_gestao, fg_color="white",
                                                                  text_color="black",
                                                                  justify=tk.CENTER)
        self.entry_descricao_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Código Unid. Negócios
        self.fr_codigo_un_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                               border_width=1)
        self.fr_codigo_un_info_gestao.place(relx=0.69, rely=0, relwidth=0.075, relheight=0.07)

        self.lb_codigo_un_info_gestao = customtkinter.CTkLabel(self.fr_codigo_un_info_gestao, text="Cód. Unid.")
        self.lb_codigo_un_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_codigo_un_info_gestao = customtkinter.CTkEntry(self.fr_codigo_un_info_gestao, fg_color="white",
                                                                  text_color="black",
                                                                  justify=tk.CENTER)
        self.entry_codigo_un_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Descrição Unid. Negócios
        self.fr_descricao_un_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                                  border_width=1)
        self.fr_descricao_un_info_gestao.place(relx=0.77, rely=0, relwidth=0.20, relheight=0.07)

        self.lb_descricao_un_info_gestao = customtkinter.CTkLabel(self.fr_descricao_un_info_gestao,
                                                                  text="Descrição Unid. Negócios")
        self.lb_descricao_un_info_gestao.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_descricao_un_info_gestao = customtkinter.CTkEntry(self.fr_descricao_un_info_gestao,
                                                                     fg_color="white", text_color="black",
                                                                     justify=tk.CENTER)
        self.entry_descricao_un_info_gestao.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Data Inicio
        self.fr_data_inicio_info_gestao = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                                 border_width=1)
        self.fr_data_inicio_info_gestao.place(relx=0, rely=0.075, relwidth=0.10, relheight=0.07)

        self.lb_data = customtkinter.CTkLabel(self.fr_data_inicio_info_gestao, text="Data Início")
        self.lb_data.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt = customtkinter.CTkEntry(self.fr_data_inicio_info_gestao, fg_color="white",
                                               text_color="black", justify=tk.CENTER)
        self.entry_dt.delete(0, 'end')
        self.entry_dt.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt.place(relx=0.275, rely=0.35, relwidth=0.485, relheight=0.50)
        self.entry_dt.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt))
        self.entry_dt.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt, self.entry_dt))

        # Frame botão R$/Mil
        self.fr_rs_mil_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_rs_mil_box.place(relx=0.105, rely=0.075, relwidth=0.10, relheight=0.07)

        # Box R$/Mil
        self.rs_mil_var = tk.BooleanVar()
        self.rs_mil_cbox = customtkinter.CTkCheckBox(self.fr_rs_mil_box, text="R$/Mil",
                                                     variable=self.rs_mil_var)
        self.rs_mil_cbox.place(relx=0.05, rely=0.25, relwidth=0.95, relheight=0.5)

        # Frame botão Acumul.
        self.fr_acumul_box = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_acumul_box.place(relx=0.21, rely=0.075, relwidth=0.10, relheight=0.07)

        # Box Acumul.
        self.acumul_var = tk.BooleanVar()
        self.acumul_cbox = customtkinter.CTkCheckBox(self.fr_acumul_box, text="Acumul.",
                                                     variable=self.acumul_var)
        self.acumul_cbox.place(relx=0.05, rely=0.25, relwidth=0.95, relheight=0.5)

        # Frame container para Natureza
        self.fr_natureza_container = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                            border_width=1)
        self.fr_natureza_container.place(relx=0.315, rely=0.075, relwidth=0.55, relheight=0.07)

        # Label "Natureza" acima dos checkboxes
        self.lb_natureza = customtkinter.CTkLabel(self.fr_natureza_container, text="Natureza")
        self.lb_natureza.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.2)

        # Frame interno para os checkboxes (dentro do container)
        self.fr_botoes_info_gestao_box = customtkinter.CTkFrame(self.fr_natureza_container, fg_color="transparent")
        self.fr_botoes_info_gestao_box.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)

        # Box Receitas
        self.receitas_var = tk.BooleanVar()
        self.receitas_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Receitas",
                                                       variable=self.receitas_var)
        self.receitas_cbox.place(relx=0.02, rely=0.1, relwidth=0.15, relheight=0.8)

        # Box Custos
        self.custos_var = tk.BooleanVar()
        self.custos_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Custos",
                                                     variable=self.custos_var)
        self.custos_cbox.place(relx=0.18, rely=0.1, relwidth=0.15, relheight=0.8)

        # Box Despesas
        self.despesas_var = tk.BooleanVar()
        self.despesas_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Despesas",
                                                       variable=self.despesas_var)
        self.despesas_cbox.place(relx=0.34, rely=0.1, relwidth=0.15, relheight=0.8)

        # Box Investimentos
        self.investimentos_var = tk.BooleanVar()
        self.investimentos_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Investimentos",
                                                            variable=self.investimentos_var)
        self.investimentos_cbox.place(relx=0.50, rely=0.1, relwidth=0.15, relheight=0.8)

        # Box Estoques
        self.estoques_var = tk.BooleanVar()
        self.estoques_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Estoques",
                                                       variable=self.estoques_var)
        self.estoques_cbox.place(relx=0.66, rely=0.1, relwidth=0.15, relheight=0.8)

        # Box Ativos/Passivos
        self.ativos_pass_var = tk.BooleanVar()
        self.ativos_pass_cbox = customtkinter.CTkCheckBox(self.fr_botoes_info_gestao_box, text="Ativos/Passivos",
                                                          variable=self.ativos_pass_var)
        self.ativos_pass_cbox.place(relx=0.82, rely=0.1, relwidth=0.15, relheight=0.8)

        # Frame botão Consultar
        self.fr_botao_consulta_info_ges = customtkinter.CTkFrame(self.frame_principal, border_color="gray75",
                                                                 border_width=1)
        self.fr_botao_consulta_info_ges.place(relx=0.87, rely=0.075, relwidth=0.10, relheight=0.07)

        # Botão de consulta centralizado
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta_info_gestao = customtkinter.CTkButton(
            self.fr_botao_consulta_info_ges,
            image=icone_pesquisa,
            text='',
            fg_color='transparent',
            command=self.consulta_infos_gestao
        )
        # Centraliza o botão no frame
        self.btn_consulta_info_gestao.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.15, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Código", "Descrição", "Real>>Jul", "Orc.>>Jul", "Var. Mês",
            "Real Acumu.>>Jul", "Orc. Acumu.>>Jul", "Var. Acumu",
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

        col_widths = [10, 30, 10, 10, 10, 10, 10, 10]

        headers = ["Código", "Descrição", "Real>>Jul", "Orc.>>Jul", "Var. Mês",
            "Real Acumu.>>Jul", "Orc. Acumu.>>Jul", "Var. Acumu",]

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

    def consulta_infos_gestao(self):
        # Limpa a treeview antes de nova consulta
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obtém os valores dos campos
        cnpj = self.entry_cnpj_info_gestao.get()
        orc_id = self.entry_codigo_info_gestao.get()
        unidade_id = self.entry_codigo_un_info_gestao.get()
        data_inicio = self.entry_dt.get()

        # Verifica se a data é válida
        try:
            dia, mes, ano = map(int, data_inicio.split('/'))
            data_valida = True
        except:
            messagebox.showerror("Erro", "Data inválida!")
            return

        # Obtém os valores dos checkboxes
        divisor = 1000 if self.rs_mil_var.get() else 1
        acumulado = self.acumul_var.get()
        receitas = self.receitas_var.get()
        custos = self.custos_var.get()
        despesas = self.despesas_var.get()
        investimentos = self.investimentos_var.get()
        estoques = self.estoques_var.get()
        ativos_passivos = self.ativos_pass_var.get()

        # Verifica se pelo menos um tipo de natureza foi selecionado
        if not (receitas or custos or despesas or investimentos or estoques or ativos_passivos):
            messagebox.showerror("Erro", "Selecione pelo menos um tipo de natureza!")
            return

        # Mapeia o mês para abreviação (como no VBA)
        meses = {
            1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr",
            5: "Mai", 6: "Jun", 7: "Jul", 8: "Ago",
            9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
        }
        mes_abrev = meses.get(mes, "")

        # Atualiza os cabeçalhos das colunas com o mês atual
        headers = [
            "Código", "Descrição",
            f"Real>>{mes_abrev}", f"Orc.>>{mes_abrev}", "Var. Mês",
            f"Real Acumu.>>{mes_abrev}", f"Orc. Acumu.>>{mes_abrev}", "Var. Acumu"
        ]

        for col, header in zip(self.tree['columns'], headers):
            self.tree.heading(col, text=header)

        # Define as datas para a consulta
        if acumulado:
            dta_inicio = "19000101"
        else:
            dta_inicio = f"{ano}0101"

        dta_inicio_mes = f"{ano}{mes:02d}01"

        # Obtém a data atual para ser usada como data fim
        data_atual = datetime.now()
        dia_atual = data_atual.day
        mes_atual = data_atual.month
        ano_atual = data_atual.year
        dta_fim = f"{ano_atual}{mes_atual:02d}{dia_atual:02d}"

        sql = f"""
        SELECT 
            'CR' AS Tipo, 
            Codigo_CR, 
            Descricao_CR, 
            SUM(Vlr_Mes) AS Vlr_Mes, 
            SUM(Vlr_Orc_Mes) AS Vlr_Orc_Mes, 
            SUM(Vlr_Acumulado) AS Vlr_Acumulado, 
            SUM(Vlr_Orcado) AS Vlr_Orcado
        FROM (
            -- Consulta para valores reais do mês
            SELECT 
                ii.ID_CR AS Codigo_CR,
                cc.Cen_Descricao AS Descricao_CR,
                SUM(ii.Vlr_Total) AS Vlr_Mes,
                0 AS Vlr_Orc_Mes,
                0 AS Vlr_Acumulado,
                0 AS Vlr_Orcado
            FROM TB_Itens ii
            INNER JOIN TB_CB_Doc dc ON dc.ID_Empresa=ii.ID_Empresa 
                AND dc.ID_Unidade=ii.ID_Unidade 
                AND dc.ID_Pessoa=ii.ID_Pessoa 
                AND dc.Doc_Num_Documento=ii.Doc_Num_Documento
            LEFT JOIN centrocusto cc ON cc.Cen_ID=ii.ID_CR AND cc.Empresa_ID=dc.ID_Empresa
            WHERE dc.Doc_Dta_Documento BETWEEN '{dta_inicio_mes}' AND '{dta_fim}'
            AND ISNULL(ii.Transferido)
            {"AND ii.ID_Unidade='" + unidade_id + "'" if unidade_id else ""}
            AND dc.ID_Empresa = '{cnpj}'
            AND (
                {"(ii.ID_Natureza BETWEEN '10000000' AND '19999999') OR" if receitas else ""}
                {"(ii.ID_Natureza BETWEEN '20000000' AND '29999999') OR" if custos else ""}
                {"(ii.ID_Natureza BETWEEN '30000000' AND '39999999') OR" if despesas else ""}
                {"(ii.ID_Natureza BETWEEN '40000000' AND '49999999') OR" if investimentos else ""}
                {"(ii.ID_Natureza BETWEEN '99000000' AND '99999999') OR" if estoques else ""}
                {"(ii.ID_Natureza BETWEEN '50000000' AND '59999999') OR" if ativos_passivos else ""}
                1=0
            )
            GROUP BY Codigo_CR, Descricao_CR

            UNION ALL

            -- Consulta para valores acumulados reais
            SELECT 
                ii.ID_CR AS Codigo_CR,
                cc.Cen_Descricao AS Descricao_CR,
                0 AS Vlr_Mes,
                0 AS Vlr_Orc_Mes,
                SUM(ii.Vlr_Total) AS Vlr_Acumulado,
                0 AS Vlr_Orcado
            FROM TB_Itens ii
            INNER JOIN TB_CB_Doc dc ON dc.ID_Empresa=ii.ID_Empresa 
                AND dc.ID_Unidade=ii.ID_Unidade 
                AND dc.ID_Pessoa=ii.ID_Pessoa 
                AND dc.Doc_Num_Documento=ii.Doc_Num_Documento
            LEFT JOIN centrocusto cc ON cc.Cen_ID=ii.ID_CR AND cc.Empresa_ID=dc.ID_Empresa
            WHERE dc.Doc_Dta_Documento BETWEEN '{dta_inicio}' AND '{dta_fim}'
            AND ISNULL(ii.Transferido)
            {"AND ii.ID_Unidade='" + unidade_id + "'" if unidade_id else ""}
            AND dc.ID_Empresa = '{cnpj}'
            AND (
                {"(ii.ID_Natureza BETWEEN '10000000' AND '19999999') OR" if receitas else ""}
                {"(ii.ID_Natureza BETWEEN '20000000' AND '29999999') OR" if custos else ""}
                {"(ii.ID_Natureza BETWEEN '30000000' AND '39999999') OR" if despesas else ""}
                {"(ii.ID_Natureza BETWEEN '40000000' AND '49999999') OR" if investimentos else ""}
                {"(ii.ID_Natureza BETWEEN '99000000' AND '99999999') OR" if estoques else ""}
                {"(ii.ID_Natureza BETWEEN '50000000' AND '59999999') OR" if ativos_passivos else ""}
                1=0
            )
            GROUP BY Codigo_CR, Descricao_CR

            UNION ALL

            -- Consulta para valores orçados do mês
            SELECT 
                oo.ID_CR AS Codigo_CR,
                cc.Cen_Descricao AS Descricao_CR,
                0 AS Vlr_Mes,
                SUM(COALESCE(oo.Orc_Vlr,0)) AS Vlr_Orc_Mes,
                0 AS Vlr_Acumulado,
                0 AS Vlr_Orcado
            FROM TB_Orcamento oo
            LEFT JOIN centrocusto cc ON cc.Cen_ID=oo.ID_CR AND cc.Empresa_ID=oo.ID_Empresa
            WHERE oo.Orc_Dta BETWEEN '{dta_inicio_mes}' AND '{dta_fim}'
            {"AND oo.ID_Unidade='" + unidade_id + "'" if unidade_id else ""}
            AND oo.ID_Empresa = '{cnpj}'
            AND (
                {"(oo.ID_Natureza BETWEEN '10000000' AND '19999999') OR" if receitas else ""}
                {"(oo.ID_Natureza BETWEEN '20000000' AND '29999999') OR" if custos else ""}
                {"(oo.ID_Natureza BETWEEN '30000000' AND '39999999') OR" if despesas else ""}
                {"(oo.ID_Natureza BETWEEN '40000000' AND '49999999') OR" if investimentos else ""}
                {"(oo.ID_Natureza BETWEEN '99000000' AND '99999999') OR" if estoques else ""}
                {"(oo.ID_Natureza BETWEEN '50000000' AND '59999999') OR" if ativos_passivos else ""}
                1=0
            )
            GROUP BY Codigo_CR, Descricao_CR

            UNION ALL

            -- Consulta para valores orçados acumulados
            SELECT 
                oo.ID_CR AS Codigo_CR,
                cc.Cen_Descricao AS Descricao_CR,
                0 AS Vlr_Mes,
                0 AS Vlr_Orc_Mes,
                0 AS Vlr_Acumulado,
                SUM(COALESCE(oo.Orc_Vlr,0)) AS Vlr_Orcado
            FROM TB_Orcamento oo
            LEFT JOIN centrocusto cc ON cc.Cen_ID=oo.ID_CR AND cc.Empresa_ID=oo.ID_Empresa
            WHERE oo.Orc_Dta BETWEEN '{dta_inicio}' AND '{dta_fim}'
            {"AND oo.ID_Unidade='" + unidade_id + "'" if unidade_id else ""}
            AND oo.ID_Empresa = '{cnpj}'
            AND oo.ID_Orc = '{orc_id}'
            AND (
                {"(oo.ID_Natureza BETWEEN '10000000' AND '19999999') OR" if receitas else ""}
                {"(oo.ID_Natureza BETWEEN '20000000' AND '29999999') OR" if custos else ""}
                {"(oo.ID_Natureza BETWEEN '30000000' AND '39999999') OR" if despesas else ""}
                {"(oo.ID_Natureza BETWEEN '40000000' AND '49999999') OR" if investimentos else ""}
                {"(oo.ID_Natureza BETWEEN '99000000' AND '99999999') OR" if estoques else ""}
                {"(oo.ID_Natureza BETWEEN '50000000' AND '59999999') OR" if ativos_passivos else ""}
                1=0
            )
            GROUP BY Codigo_CR, Descricao_CR
        ) AS COMPLETO
        GROUP BY Codigo_CR, Descricao_CR
        ORDER BY Codigo_CR, Descricao_CR
        """

        try:
            myresult = db._querying(sql)
            resultados = [resultados for resultados in myresult]

            if not resultados:
                messagebox.showinfo("Aviso", "Não existem dados na consulta!")
                return

            # Variáveis para totais
            total_mes_cr = 0
            total_acu_cr = 0
            total_orc = 0
            total_mes_cr_orc = 0

            # Preenche a treeview com os resultados
            for row in resultados:
                codigo = row['Codigo_CR']
                descricao = row['Descricao_CR']
                vlr_mes = row['Vlr_Mes'] / divisor
                vlr_orc_mes = row['Vlr_Orc_Mes'] / divisor
                vlr_acu = row['Vlr_Acumulado'] / divisor
                vlr_orcado = row['Vlr_Orcado'] / divisor

                # Calcula as variações
                if vlr_orc_mes > 0:
                    var_mes = (vlr_mes + vlr_orc_mes)
                else:
                    var_mes = (vlr_mes - vlr_orc_mes)

                if vlr_orcado > 0:
                    var_acu = (vlr_acu + vlr_orcado)
                else:
                    var_acu = (vlr_acu - vlr_orcado)

                # Adiciona à treeview
                self.tree.insert("", "end", values=(
                    codigo,
                    descricao,
                    f"{vlr_mes:,.2f}",
                    f"{vlr_orc_mes:,.2f}",
                    f"{var_mes:,.2f}",
                    f"{vlr_acu:,.2f}",
                    f"{vlr_orcado:,.2f}",
                    f"{var_acu:,.2f}"
                ))

                # Acumula totais
                total_mes_cr += row['Vlr_Mes']
                total_mes_cr_orc += row['Vlr_Orc_Mes']
                total_acu_cr += row['Vlr_Acumulado']
                total_orc += row['Vlr_Orcado']

            # Adiciona linha de totais
            total_var_mes = (total_mes_cr + total_mes_cr_orc) if total_mes_cr_orc > 0 else (
                        total_mes_cr - total_mes_cr_orc)
            total_var_acu = (total_acu_cr + total_orc) if total_orc > 0 else (total_acu_cr - total_orc)

            self.tree.insert("", "end", values=(
                "",
                "Total",
                f"{total_mes_cr / divisor:,.2f}",
                f"{total_mes_cr_orc / divisor:,.2f}",
                f"{total_var_mes / divisor:,.2f}",
                f"{total_acu_cr / divisor:,.2f}",
                f"{total_orc / divisor:,.2f}",
                f"{total_var_acu / divisor:,.2f}"
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

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na consulta:\n{str(e)}")