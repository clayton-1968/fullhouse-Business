from imports import *
from widgets import Widgets
################# criando janela ###############
class Simulador_Estudos_Resultado(Widgets):

    def simulador_estudos_resultado(self, ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        self.janela_simulador_resultado = customtkinter.CTkToplevel(self.window_one)
        self.janela_simulador_resultado.title('Simulador de Estudos de Negócios')
        width = self.janela_simulador_resultado.winfo_screenwidth()
        height = self.janela_simulador_resultado.winfo_screenheight()
        self.janela_simulador_resultado.geometry(f"{width}x{height}+0+0") 
        self.janela_simulador_resultado.resizable(True, True)
        self.janela_simulador_resultado.lift()  # Traz a janela para frente   
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_simulador_resultado.protocol("WM_DELETE_WINDOW", self.on_closing_tela_resultados)

        self.consultar_fluxo_indicadores(self.janela_simulador_resultado, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
        self.frame_resumo_resultado(self.janela_simulador_resultado, ID_Empresa, DS_Empresa, UF, Cidade)
        self.frame_carregar_resultados(self.janela_simulador_resultado, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)

        self.janela_simulador_resultado.focus_force()
        self.janela_simulador_resultado.grab_set()

    def frame_carregar_resultados(self, janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        self.consultar_resultados(janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)

    def consultar_resultados(self, janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        
        if  Nome_da_Area != '':
            
            self.lista = self.Consulta_Negocio(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
            
            if self.lista == []:
                messagebox.showinfo("Informação", "Nenhum negócio encontrado.", parent=janela)
            
            
            # Carregar Variáveis
            Empresa_DS = self.lista[0].get('Pri_Descricao')
            UF = self.lista[0].get('UF')
            Cidade = self.lista[0].get('Cidade')
            Tipo = self.lista[0].get('Tipo')
            Nome_da_Area = self.lista[0].get('Nome_da_Area')
            
            Area_Total = self.lista[0].get('Area_Total')
            Per_Area_Aproveitada = self.lista[0].get('Per_Aproveitamento')
            Area_Aproveitada = self.lista[0].get('Area_Aproveitada')
            Medidas_Lote = self.lista[0].get('Medidas_Lote')
            Lote_Medio = self.lista[0].get('Area_Lote_Medio')
            Nr_Lotes = self.lista[0].get('Nr_Unidades')
            
            Participacao_Urbanizadora = self.lista[0].get('Participacao_Urbanizadora')
            Participacao_Parceiro = self.lista[0].get('Participação_Parceiro')
            Permuta_em_Lotes = self.lista[0].get('Permuta_em_Lotes')
            Per_Comissao_Negocio = self.lista[0].get('Per_Comissao_Negocio')
            Per_MkT_Cobrado = self.lista[0].get('Per_MkT_Cobrado')
            Total_Urbanizadora = self.lista[0].get('Participação_Total_Urbanizadora')
            Total_Parceiro = self.lista[0].get('Participação_Total_Parceiro')
                        
            Investimento_Area = self.lista[0].get('Investimento_Area')
            Investimento_Area_Inicio = self.lista[0].get('Investimento_Area_Inicio')
            Investimento_Area_Curva = self.lista[0].get('Investimento_Area_Curva')
            Investimento_Aporte = self.lista[0].get('Investimento_Aporte')
                    
            Adto_Parceiro_Valor = self.lista[0].get('Adto_Parceiro_Valor')
            Adto_Parceiro_Urb_Juros = self.lista[0].get('Adto_Parceiro_Urb_Juros')
            Adto_Parceiro_Per_Juros = self.lista[0].get('Adto_Parceiro_Per_Juros')
            Adto_Parceiro_Inicio = self.lista[0].get('Adto_Parceiro_Inicio')
            Adto_Parceiro_Curva = self.lista[0].get('Adto_Parceiro_Curva')

            Valor_m2_sem_comissao = self.lista[0].get('Vendas_Valor_m2')
            Vendas_comissao_per = self.lista[0].get('Vendas_comissao_per')
            Vendas_Valor_com_comissao_m2 = self.lista[0].get('Valor_m2_com_comissao')
            Vendas_Tickt_Medio = self.lista[0].get('tickt_medio')
            Vendas_prazo_financiamento = self.lista[0].get('Vendas_prazo_financiamento')
            Vendas_sistema_amortizacao = self.lista[0].get('Vendas_sistema_amortizacao')
            Vendas_juros_taxa = self.lista[0].get('Vendas_juros_taxa')
            Vendas_juros_am = self.lista[0].get('Per_Juros_am')
            Vendas_per_entrada = self.lista[0].get('Vendas_per_entrada')
            Vendas_parcela_entrada = self.lista[0].get('Vendas_parcela_entrada')
            Vendas_per_reforcos = self.lista[0].get('Vendas_per_reforcos')
            Vendas_parcela_reforcos = self.lista[0].get('Vendas_parcela_reforcos')
            Vendas_periodicidade_reforcos = self.lista[0].get('Vendas_periodicidade_reforcos')
            Vendas_per_avista = self.lista[0].get('Vendas_per_avista')
            Vendas_inicio = self.lista[0].get('Vendas_inicio')
            Vendas_curva = self.lista[0].get('Vendas_curva')
            Vendas_parcela_PRICE = self.lista[0].get('PmT_PRICE')
            Vendas_parcela_sacoc = self.lista[0].get('PmT_Sacoc')
            self.impostos = self.lista[0].get('Per_Impostos')

            Projetos_per_obra = self.lista[0].get('Projetos_per_obra')
            Projetos_Valor = self.lista[0].get('Projetos_Valor')
            Projetos_inicio = self.lista[0].get('Projetos_inicio')
            Projetos_curva = self.lista[0].get('Projetos_curva')

            MkT_per_vgv = self.lista[0].get('MkT_per_vgv')
            MkT_Valor = self.lista[0].get('Mkt_Valor')
            MkT_inicio = self.lista[0].get('MkT_inicio')
            MkT_curva = self.lista[0].get('MkT_curva')
                                
            Adm_per_receita = self.lista[0].get('Adm_per_receita')
            Adm_Valor = self.lista[0].get('OverHead_Valor')
            Adm_Inicio = self.lista[0].get('OverHead_Inicio')
            Adm_Curva = self.lista[0].get('OverHead_Curva')

            Obras_custo_m2 = self.lista[0].get('Obras_custo_m2')
            Obra_Valor = self.lista[0].get('Obra_Valor')
            Obras_inicio = self.lista[0].get('Obras_inicio')
            Obras_curva = self.lista[0].get('Obras_curva')
            
            Pos_Obra_per_obra = self.lista[0].get('Pos_Obra_per_obra')
            Pos_Obra_Valor = self.lista[0].get('Pos_Obra_Valor')
            Pos_Obra_Inicio = self.lista[0].get('Pos_Obra_Inicio')
            Pos_Obra_curva = self.lista[0].get('Pos_Obra_Curva')
            
            AdmObra_per_obra = self.lista[0].get('AdmObra_per_obra')
            AdmObra_Valor = self.lista[0].get('AdmObras_Valor')
            AdmObra_Inicio = self.lista[0].get('AdmObras_Inicio')
            AdmObra_curva = self.lista[0].get('AdmObras_Curva')
            
            Financiamento_valor = self.lista[0].get('Financiamento_valor')
            Financiamento_sistema_amortizacao = self.lista[0].get('Financiamento_sistema_amortizacao')
            Financiamento_prazo_amortizacao = self.lista[0].get('Financiamento_prazo_amortizacao')
            Financiamento_inicio_amortizacao = self.lista[0].get('Financiamento_inicio_amortizacao')
            Financiamento_inicio_pagto_juros = self.lista[0].get('Financiamento_inicio_pagto_juros')
            Financiamento_juros = 0
            Financiamento_taxa = self.lista[0].get('Financiamento_taxa')
            Financiamento_liberacao = self.lista[0].get('Financiamento_liberacao')
            Financiamento_curva = self.lista[0].get('Financiamento_curva')
            Financiamento_financiador = self.lista[0].get('Financiamento_financiador')

            Observacao = self.lista[0].get('Observacao')

            DrE_VGV_bruto = self.lista[0].get('DrE_VgV_Bruto')
            DrE_comissao =self.lista[0].get('DrE_comissao_venda')
            DrE_VGV_liquido = self.lista[0].get('DrE_VgV_Liquido')
            DrE_impostos = self.lista[0].get('DrE_impostos')
            DrE_comissao_negocios = self.lista[0].get('DrE_comissao_negocio')
            DrE_receita_liquida = self.lista[0].get('DrE_Receita_Liquida')
            DrE_VGV_parceiro = self.lista[0].get('DrE_Receita_Parceiro')
            DrE_receita_liquida_urbanizadora = self.lista[0].get('DrE_Receita_Urbanizador')
            DrE_ebtda_valor = self.lista[0].get('DrE_Ebtda_Valor')
            DrE_ebtda_per = self.lista[0].get('DrE_Ebtda_Percente')
            Tir = self.lista[0].get('Tir')
            indicadores_tir_am = self.lista[0].get('Tir_Urbanizadora_am') 
            Payback = self.lista[0].get('Payback')
            Multiplicador = self.lista[0].get('Multiplicador')
            ExposicaoMax = self.lista[0].get('ExposicaoMax')
            Vpl_Urb = self.lista[0].get('Vpl_Urb')
            Vpl_Parceiro = self.lista[0].get('Vpl_Parceiro')
            Desconto_VpL_taxa = self.lista[0].get('VpL_Taxa_Desconto')

            Status_Prospeccao = self.lista[0].get('Status_Prospeccao')
            Anexos = self.lista[0].get('Anexos')
            Dta_Contrato = self.lista[0].get('Dta_Contrato')
            Unidade = self.lista[0].get('Unidade')
            Http = self.lista[0].get('Http')
            informacoes_maps =  self.lista[0].get('Coordenadas')

            Usr = self.lista[0].get('Usr')
            Dta_Registro = self.lista[0].get('Dta_Registro')
            
            # Preenche Cabeçalho
            self.entry_tpo_projeto.insert(0, Tipo)
            self.entry_nome_cenario.insert(0, Nome_da_Area)
            
            # Limpar os campos
            self.entry_area_total.delete(0, 'end')
            self.entry_area_aproveitamento.delete(0, 'end')
            self.entry_area_aproveitado.delete(0, 'end')
            self.entry_area_lote_padrao.delete(0, 'end')
            self.entry_area_lote_medio.delete(0, 'end')
            self.entry_area_nr_lotes.delete(0, 'end')
            self.entry_projetos_per_obra.delete(0, 'end')
            self.entry_projetos_valor_total.delete(0, 'end')
            self.entry_mkt_per_vgv.delete(0, 'end')
            self.entry_mkt_valor_total.delete(0, 'end')
            self.entry_overhead_per_vgv.delete(0, 'end')
            self.entry_overhead_valor_total.delete(0, 'end')
            self.entry_obras_valor_m2.delete(0, 'end')
            self.entry_obras_valor_total.delete(0, 'end')
            self.entry_pos_obras_per_obras.delete(0, 'end')
            self.entry_pos_obras_valor_total.delete(0, 'end')
            self.entry_adm_per_obras.delete(0, 'end')
            self.entry_adm_valor_total.delete(0, 'end')
            self.entry_dre_vgv_bruto.delete(0, 'end')
            self.entry_dre_comissao.delete(0, 'end')
            self.entry_dre_vgv_liquido.delete(0, 'end')
            self.entry_dre_impostos.delete(0, 'end')
            self.entry_dre_comissao_negocio.delete(0, 'end')
            self.entry_dre_receita_liquida.delete(0, 'end')
            self.entry_dre_vgv_parceiro.delete(0, 'end')
            self.entry_dre_receita_liquida_urbanizadora.delete(0, 'end')
            self.entry_dre_ebtda_valor.delete(0, 'end')
            self.entry_dre_ebtda_per.delete(0, 'end')
            
            # # Preenche os campos Inserir os dados
            self.entry_area_total.insert(0, self.format_m2_fx(Area_Total))  
            self.entry_area_aproveitamento.insert(0, self.format_per_fx(Per_Area_Aproveitada))
            
            self.entry_area_aproveitado.insert(0, self.format_m2_fx(Area_Aproveitada))
            if Medidas_Lote is not None:
                self.entry_area_lote_padrao.insert(0, str(Medidas_Lote))
            else:
                self.entry_area_lote_padrao.insert(0, str(''))
                
            self.entry_area_lote_medio.insert(0, self.format_m2_fx(float(Lote_Medio)))
            self.entry_area_nr_lotes.insert(0, self.format_valor_fx(Nr_Lotes))
            
            self.entry_dre_comissao_per.insert(0, self.format_per_fx(Vendas_comissao_per))
            self.entry_dre_impostos_per.insert(0, self.format_per_fx(self.impostos))
            self.entry_dre_comissao_negocio_per.insert(0, self.format_per_fx(Per_Comissao_Negocio))
            self.entry_dre_vgv_parceiro_per.insert(0, self.format_per_fx(Total_Parceiro))
            self.entry_dre_receita_liquida_urbanizadora_per.insert(0, self.format_per_fx(Total_Urbanizadora))

            if Investimento_Aporte is not None:
                if Investimento_Aporte == 'S':
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(Investimento_Area*-1))
                    
                elif Investimento_Aporte == 'N':
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(0))
                else:
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(Investimento_Area*-1))
            else:
                self.entry_investimento_valor.insert(0, self.format_valor_fx(0))

            self.entry_projetos_per_obra.insert(0, self.format_per_fx(Projetos_per_obra))
            self.entry_projetos_valor_total.insert(0, self.format_valor_fx(Projetos_Valor))
            
            self.entry_mkt_per_vgv.insert(0, self.format_per_fx(MkT_per_vgv))
            self.entry_mkt_valor_total.insert(0, self.format_valor_fx(MkT_Valor))
            
            self.entry_overhead_per_vgv.insert(0, self.format_per_fx(Adm_per_receita))
            self.entry_overhead_valor_total.insert(0, self.format_valor_fx(Adm_Valor))
            
            self.entry_obras_valor_m2.insert(0, self.format_valor_fx(Obras_custo_m2))
            self.entry_obras_valor_total.insert(0, self.format_valor_fx(Obra_Valor))
            
            self.entry_pos_obras_per_obras.insert(0, self.format_per_fx(Pos_Obra_per_obra))
            self.entry_pos_obras_valor_total.insert(0, self.format_valor_fx(Pos_Obra_Valor))
            
            self.entry_adm_per_obras.insert(0, self.format_per_fx(AdmObra_per_obra))
            self.entry_adm_valor_total.insert(0, self.format_valor_fx(AdmObra_Valor))
            
            self.entry_dre_vgv_bruto.insert(0, self.format_valor_fx(DrE_VGV_bruto))
            self.entry_dre_comissao.insert(0, self.format_valor_fx(DrE_comissao*-1))
            self.entry_dre_vgv_liquido.insert(0, self.format_valor_fx(DrE_VGV_liquido))
            self.entry_dre_impostos.insert(0, self.format_valor_fx(DrE_impostos*-1))
            self.entry_dre_comissao_negocio.insert(0, self.format_valor_fx(DrE_comissao_negocios*-1))
            self.entry_dre_receita_liquida.insert(0, self.format_valor_fx(DrE_receita_liquida))
            self.entry_dre_vgv_parceiro.insert(0, self.format_valor_fx(DrE_VGV_parceiro*-1))
            self.entry_dre_receita_liquida_urbanizadora.insert(0, self.format_valor_fx(DrE_receita_liquida_urbanizadora))

            self.entry_dre_ebtda_valor.insert(0, self.format_valor_fx(DrE_ebtda_valor))
            self.entry_dre_ebtda_per.insert(0, self.format_per_fx(DrE_ebtda_per))
            
    def consultar_fluxo_indicadores(self, janela, Empresa_ID, UF, Cidade, Tipo, Nome_da_Area):
        if Empresa_ID == '': 
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.', parent=janela)
            return
        
        conditions = []  # Lista para armazenar as condições
        conditions.append("ff.Empresa_ID = %s ")
        params = [Empresa_ID]

        if Cidade != '':
            conditions.append("ff.Cidade = %s ")
            params.append(Cidade)

        if UF != '':
            conditions.append("ff.UF = %s ")
            params.append(UF)

        if Tipo!= '':
            conditions.append("ff.Tipo = %s ")
            params.append(Tipo)

        if Nome_da_Area!= '':
            conditions.append("ff.Nome_da_Area = %s ")
            params.append(Nome_da_Area)
        
        strSql = f"""SELECT 
                        df.Periodo_Nr                  AS Periodo_Nr,
                        df.Periodo_Dta                 AS Periodo_Dta,
                        ff.Tir_Urbanizadora            AS Tir_aa,
                        ff.Tir_Urbanizadora_am         AS Tir_am,
                        ff.PayBack_Urbanizadora        AS PayBack,
                        
                        ff.DrE_Ebtda_Percente              AS DrE_Ebtda_Percente,
                        ff.tickt_medio                     AS tickt_medio,
                        ff.Prazo_Financiamento             AS Vendas_prazo_financiamento,
                        ff.Sistema_Amortização_Cliente     AS Vendas_sistema_amortizacao,
                        ff.Per_Juros                       AS Vendas_juros_taxa,
                        ff.Per_Juros_am                    AS Per_Juros_am,
                        ff.Per_Entrada                     AS Vendas_per_entrada,
                        
                        ff.Multiplicador               AS Multiplicador,
                        ff.Vlr_Exposicao_Maxima*-1     AS Exposicao_Maxima,
                        ff.VpL_Urbanizadora            AS VpL,
                        ff.VpL_Taxa_Desconto           AS VpL_Taxa,
                        df.Valor_Vendas                AS Vlr_Venda, 
                        year(df.Periodo_Dta)           AS Ano,
                        month(df.Periodo_Dta)          AS Mes,
                        df.Valor_Parcelas              AS ReceitaUrb,
                        df.Valor_Parcelas_Parceiro*-1  AS ReceitaPar,
                        df.Valor_Comissao_Venda        AS ComissaoVenda,
                        df.Valor_Comissao_Negocio      AS ComissaoNegocio,
                        df.Valor_Impostos              AS Impostos,
                        df.Valor_Terreno               AS Terreno,
                        df.Valor_Projetos*-1           AS Projetos,
                        df.Valor_Obras*-1              AS Obras,
                        df.Valor_AdmObras*-1           AS AdmObras,
                        df.Valor_PosObras*-1           AS PosObras,
                        df.Valor_Adm*-1                AS Adm,
                        df.Valor_Mkt*-1                AS MkT,
                        df.Valor_Adto                  AS Valor_Adto,
                        df.Valor_AmortAdto             AS Valor_DevolucaoAdto,
                        df.Valor_CustoAdtoPar          AS Valor_CustoAdto,
                        df.Valor_Liberacao             AS Valor_Liberacao,
                        df.Vlr_ParcelaFinanciamento    AS Vlr_ParcelaFinanciamento,
                        df.Valor_Fx                    AS Fx_Caixa,
                        df.Valor_Fx_Acumulado          AS Fx_Caixa_Acumulado       

                    FROM Dados_Prospeccao ff
                    LEFT JOIN Dados_Fluxo AS df ON df.Empresa_ID=ff.Empresa_ID AND df.UF=ff.UF AND df.Cidade=ff.Cidade AND df.Nome_da_Area=ff.Nome_da_Area AND df.Tipo=ff.Tipo
                    WHERE {' AND '.join(conditions)} ORDER BY Ano, Mes, Periodo_Nr
                """
        results = db.executar_consulta(strSql, params)
        
        self.df_resultados = pd.DataFrame(results)
        
    def frame_resumo_resultado(self, janela, ID_Empresa, DS_Empresa, UF, Cidade):
        municipio = Cidade + ' - ' + UF.upper()
        
        # Cabeçalho
        coordenadas_relx=0.01
        coordenadas_rely=0.01
        coordenadas_relwidth=0.98
        coordenadas_relheight=0.07
        fr_cabecalho = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_cabecalho.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_cabelho = customtkinter.CTkLabel(fr_cabecalho, text="Identificação do Estudo")
        lb_cabelho.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)
        
        entry_empresa = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.LEFT)
        entry_empresa.place(relx=0.001, rely=0.5, relwidth=0.20, relheight=0.4)
        entry_empresa.insert(0, DS_Empresa)

        entry_municipio = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.LEFT)
        entry_municipio.place(relx=0.205, rely=0.5, relwidth=0.10, relheight=0.4)
        entry_municipio.insert(0, municipio)

        self.entry_tpo_projeto = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_tpo_projeto.place(relx=0.31, rely=0.5, relwidth=0.10, relheight=0.4)
        
        self.entry_nome_cenario = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_nome_cenario.place(relx=0.415, rely=0.50, relwidth=0.10, relheight=0.4)
        
        lb_area_total = customtkinter.CTkLabel(fr_cabecalho, text="Área Total", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_area_total.place(relx=0.525, rely=0.20,relheight=0.30, relwidth=0.10)
        self.entry_area_total = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_total.place(relx=0.52, rely=0.50, relwidth=0.10, relheight=0.40)

        lb_area_aproveitamento = customtkinter.CTkLabel(fr_cabecalho, text="% Aproveitamento", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_area_aproveitamento.place(relx=0.63, rely=0.20, relheight=0.30, relwidth=0.10)
        self.entry_area_aproveitamento = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_aproveitamento.place(relx=0.625, rely=0.50, relwidth=0.10, relheight=0.40)

        lb_area_aproveitado = customtkinter.CTkLabel(fr_cabecalho, text="m² Aproveitado", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_area_aproveitado.place(relx=0.735, rely=0.20, relheight=0.30, relwidth=0.10)
        self.entry_area_aproveitado = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_aproveitado.place(relx=0.73, rely=0.50, relwidth=0.10, relheight=0.40)
        
        lb_area_aproveitado = customtkinter.CTkLabel(fr_cabecalho, text="Lote Médio", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_area_aproveitado.place(relx=0.84, rely=0.20, relheight=0.30, relwidth=0.05)
        self.entry_area_lote_padrao = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_lote_padrao.place(relx=0.835, rely=0.50, relwidth=0.05, relheight=0.40)

        self.lb_area_lote_medio = customtkinter.CTkLabel(fr_cabecalho, text="m² Lote Médio", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_area_lote_medio.place(relx=0.89, rely=0.20, relheight=0.30, relwidth=0.05)
        self.entry_area_lote_medio = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_lote_medio.place(relx=0.885, rely=0.50, relwidth=0.05, relheight=0.40)
        
        lb_area_nr_lotes = customtkinter.CTkLabel(fr_cabecalho, text="Nr. Lotes", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_area_nr_lotes.place(relx=0.945, rely=0.20, relheight=0.30, relwidth=0.05)
        self.entry_area_nr_lotes = customtkinter.CTkEntry(fr_cabecalho, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_nr_lotes.place(relx=0.94, rely=0.50, relwidth=0.05, relheight=0.40)

        # Demonstrativo - Estudo
        fr_resultados = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="white")
        fr_resultados.place(relx=0.01, rely=0.08, relwidth=0.98, relheight=0.98)
        lb_resultados = customtkinter.CTkLabel(fr_resultados, text="Indicadores", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_resultados.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.90)
        
        # DRE
        fr_dre = customtkinter.CTkFrame(fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        fr_dre.place(relx=0.005, rely=0.03,relwidth=0.295, relheight=0.90)
        lb_dre = customtkinter.CTkLabel(fr_dre, text="Demonstração do Resultado", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_dre.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        lb_deducao_1 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_2 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_3 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_4 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_5 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_6 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_7 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_8 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_9 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_10 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_deducao_11 = customtkinter.CTkLabel(fr_dre, text="( - )", text_color="red", font=('Arial', 15, 'bold'), anchor=tk.W)
        
        # VGV Bruto
        lb_dre_vgv_bruto = customtkinter.CTkLabel(fr_dre, text="VGV - Bruto:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_vgv_bruto.place(relx=0.01, rely=0.04, relheight=0.05, relwidth=0.45)
        self.entry_dre_vgv_bruto = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_bruto.place(relx=0.50, rely=0.04, relwidth=0.49, relheight=0.05)

        # Comissão
        lb_dre_comissao = customtkinter.CTkLabel(fr_dre, text="Comissão:", text_color="black", font=('Arial', 12), anchor=tk.W)
        lb_dre_comissao.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_comissao_per.place(relx=0.30, rely=0.10, relwidth=0.10, relheight=0.05)
        lb_deducao_7.place(relx=0.43, rely=0.10, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_comissao.place(relx=0.50, rely=0.10, relwidth=0.49, relheight=0.05)

        # VGV Líquido
        lb_dre_vgv_liquido = customtkinter.CTkLabel(fr_dre, text="VGV - Líquido:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_vgv_liquido.place(relx=0.01, rely=0.16, relheight=0.05, relwidth=0.45)
        self.entry_dre_vgv_liquido = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_liquido.place(relx=0.50, rely=0.16, relwidth=0.49, relheight=0.05)

        # Imposto
        lb_dre_impostos = customtkinter.CTkLabel(fr_dre, text="Impostos:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_impostos.place(relx=0.01, rely=0.22, relheight=0.05, relwidth=0.25)
        self.entry_dre_impostos_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_impostos_per.place(relx=0.30, rely=0.22, relwidth=0.10, relheight=0.05)
        lb_deducao_8.place(relx=0.43, rely=0.22, relheight=0.05, relwidth=0.25)
        self.entry_dre_impostos = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_impostos.place(relx=0.50, rely=0.22, relwidth=0.49, relheight=0.05)

        # Comissão de Negócio
        lb_dre_comissao_negocio = customtkinter.CTkLabel(fr_dre, text="Itermediação:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_comissao_negocio.place(relx=0.01, rely=0.28, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao_negocio_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_comissao_negocio_per.place(relx=0.30, rely=0.28, relwidth=0.10, relheight=0.05)
        lb_deducao_9.place(relx=0.43, rely=0.28, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao_negocio = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_comissao_negocio.place(relx=0.50, rely=0.28, relwidth=0.49, relheight=0.05)

        # Receita Líquida
        lb_dre_receita_liquida = customtkinter.CTkLabel(fr_dre, text="Receita Líquida:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_receita_liquida.place(relx=0.01, rely=0.34, relheight=0.05, relwidth=0.45)
        self.entry_dre_receita_liquida = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida.place(relx=0.50, rely=0.34, relwidth=0.49, relheight=0.05)

        # VGV Parceiro
        lb_dre_vgv_parceiro = customtkinter.CTkLabel(fr_dre, text="Receita Parceiro:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_vgv_parceiro.place(relx=0.01, rely=0.40, relheight=0.05, relwidth=0.25)
        self.entry_dre_vgv_parceiro_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_vgv_parceiro_per.place(relx=0.30, rely=0.40, relwidth=0.10, relheight=0.05)
        lb_deducao_10.place(relx=0.43, rely=0.40, relheight=0.05, relwidth=0.05)
        self.entry_dre_vgv_parceiro = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_vgv_parceiro.place(relx=0.50, rely=0.40, relwidth=0.49, relheight=0.05)

        # Receita Líquida Urbanizadora
        lb_dre_receita_liquida_urbanizadora = customtkinter.CTkLabel(fr_dre, text="Receita UrbanVix:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_receita_liquida_urbanizadora.place(relx=0.01, rely=0.46, relheight=0.05, relwidth=0.45)
        self.entry_dre_receita_liquida_urbanizadora_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_receita_liquida_urbanizadora_per.place(relx=0.30, rely=0.46, relwidth=0.10, relheight=0.05)
        self.entry_dre_receita_liquida_urbanizadora = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida_urbanizadora.place(relx=0.50, rely=0.46, relwidth=0.49, relheight=0.05)
        
        # Custos
        lb_investimentos = customtkinter.CTkLabel(fr_dre, text="Investimento/Terreno", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_investimentos.place(relx=0.01, rely=0.52, relheight=0.05, relwidth=0.25)
        lb_deducao_11.place(relx=0.43, rely=0.52, relheight=0.05, relwidth=0.05)
        self.entry_investimento_valor = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_investimento_valor.place(relx=0.50, rely=0.52, relwidth=0.49, relheight=0.05)

        lb_projetos = customtkinter.CTkLabel(fr_dre, text="Projetos - % x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_projetos.place(relx=0.01, rely=0.58, relheight=0.05, relwidth=0.25)
        self.entry_projetos_per_obra = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_projetos_per_obra.place(relx=0.30, rely=0.58, relwidth=0.10, relheight=0.05)
        lb_deducao_1.place(relx=0.43, rely=0.58, relheight=0.05, relwidth=0.05)
        self.entry_projetos_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_projetos_valor_total.place(relx=0.50, rely=0.58, relwidth=0.49, relheight=0.05)

        lb_mkt_per_vgv = customtkinter.CTkLabel(fr_dre, text="MkT - % x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_mkt_per_vgv.place(relx=0.01, rely=0.64, relheight=0.05, relwidth=0.25)
        self.entry_mkt_per_vgv = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_mkt_per_vgv.place(relx=0.30, rely=0.64, relwidth=0.10, relheight=0.05)
        lb_deducao_2.place(relx=0.43, rely=0.64, relheight=0.05, relwidth=0.05)
        self.entry_mkt_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_mkt_valor_total.place(relx=0.50, rely=0.64, relwidth=0.49, relheight=0.05)

        lb_overhead_per_vgv = customtkinter.CTkLabel(fr_dre, text="Adm. - % x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_overhead_per_vgv.place(relx=0.01, rely=0.70, relheight=0.05, relwidth=0.25)
        self.entry_overhead_per_vgv = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_overhead_per_vgv.place(relx=0.30, rely=0.70, relwidth=0.10, relheight=0.05)
        lb_deducao_3.place(relx=0.43, rely=0.70, relheight=0.05, relwidth=0.25)
        self.entry_overhead_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_overhead_valor_total.place(relx=0.50, rely=0.70, relwidth=0.49, relheight=0.05)

        lb_obras_valor_m2 = customtkinter.CTkLabel(fr_dre, text="Custo $m² de Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_obras_valor_m2.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.25)
        self.entry_obras_valor_m2 = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_obras_valor_m2.place(relx=0.30, rely=0.76, relwidth=0.10, relheight=0.05)
        lb_deducao_4.place(relx=0.43, rely=0.76, relheight=0.05, relwidth=0.25)
        self.entry_obras_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_obras_valor_total.place(relx=0.50, rely=0.76, relwidth=0.49, relheight=0.05)

        lb_adm_per_obras = customtkinter.CTkLabel(fr_dre, text="Adm. - % x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_adm_per_obras.place(relx=0.01, rely=0.82, relheight=0.05, relwidth=0.25)
        self.entry_adm_per_obras = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_adm_per_obras.place(relx=0.30, rely=0.82, relwidth=0.10, relheight=0.05)
        lb_deducao_5.place(relx=0.43, rely=0.82, relheight=0.05, relwidth=0.25)
        self.entry_adm_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_adm_valor_total.place(relx=0.50, rely=0.82, relwidth=0.49, relheight=0.05)

        lb_pos_obras_per_obras = customtkinter.CTkLabel(fr_dre, text="Pós Obras - % x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_pos_obras_per_obras.place(relx=0.01, rely=0.88, relheight=0.05, relwidth=0.25)
        self.entry_pos_obras_per_obras = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_pos_obras_per_obras.place(relx=0.30, rely=0.88, relwidth=0.10, relheight=0.05)
        lb_deducao_6.place(relx=0.43, rely=0.88, relheight=0.05, relwidth=0.25)
        self.entry_pos_obras_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_pos_obras_valor_total.place(relx=0.50, rely=0.88, relwidth=0.49, relheight=0.05)

        # Resultado Líquido Urbanizadora
        self.lb_dre_ebtda_valor = customtkinter.CTkLabel(fr_dre, text="Resultado Líquido:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        self.lb_dre_ebtda_valor.place(relx=0.01, rely=0.94, relheight=0.05, relwidth=0.45)
        self.entry_dre_ebtda_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", font=('Arial', 10), justify=tk.RIGHT)
        self.entry_dre_ebtda_per.place(relx=0.30, rely=0.94, relwidth=0.10, relheight=0.05)
        self.entry_dre_ebtda_valor = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_ebtda_valor.place(relx=0.50, rely=0.94, relwidth=0.49, relheight=0.05)

        # GRAFICOS
        fr_graficos = customtkinter.CTkFrame(fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        fr_graficos.place(relx=0.305, rely=0.03,relwidth=0.69, relheight=0.90)
        lb_graficos = customtkinter.CTkLabel(fr_graficos, text="Gráficos", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_graficos.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        # Curva de Gastos
        fr_curva_gastos = customtkinter.CTkFrame(fr_graficos, border_color="gray75", border_width=1, fg_color="white")
        fr_curva_gastos.place(relx=0.005, rely=0.03, relwidth=0.495, relheight=0.455)
        lb_curva_gastos = customtkinter.CTkLabel(fr_curva_gastos, text="Curvas de Gastos", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_curva_gastos.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

        # Criando figura nova
        figura = plt.Figure(figsize=(8, 4), dpi=100)
        ax = figura.add_subplot(111)
        canva = FigureCanvasTkAgg(figura, master=fr_curva_gastos)
        canva.get_tk_widget().place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.90)
        canva.draw()
        
        # Verifica se ax.ecdf existe
        if hasattr(ax, "ecdf"):
            if self.df_resultados['Terreno'].astype(float).sum() != 0:
                _terreno = self.df_resultados['Terreno'].astype(float).cumsum() / 1000
                ax.plot(_terreno, label='Investimento Terreno')

            if self.df_resultados['Valor_Adto'].astype(float).sum() != 0:
                _adto           = self.df_resultados['Valor_Adto'].astype(float).cumsum() / 1000
                _devolucao_adto = self.df_resultados['Valor_DevolucaoAdto'].astype(float).cumsum() / 1000
                _custo_adto     = self.df_resultados['Valor_CustoAdto'].astype(float).cumsum() / 1000
                ax.plot(_adto, label='Adto')
                ax.plot(_devolucao_adto, label='Devolução Adto')
                ax.plot(_custo_adto, label='Custo Adto')
            
            
            if self.df_resultados['Projetos'].astype(float).sum() != 0.0:
                _projetos = self.df_resultados['Projetos'].astype(float).cumsum() / 1000
                
                idx_inicio  = 0
                idx_fim     = 0
                for i in range(1, len(_projetos)):
                    if idx_inicio == 0 and _projetos[i] > 0:
                        idx_inicio = i

                    if _projetos[i] == _projetos[i-1]:
                        idx_fim = i
                        break
                ax.plot(_projetos[idx_inicio:idx_fim], label='Projetos')
            
            if self.df_resultados['Obras'].astype(float).sum() != 0:
                _obras     = self.df_resultados['Obras'].astype(float).cumsum() / 1000
                _adm_obras = self.df_resultados['AdmObras'].astype(float).cumsum() / 1000
                # _pos_obras = self.df_resultados['PosObras'].astype(float).cumsum() / 1000

                idx_inicio  = 0
                idx_fim     = 0
                for i in range(1, len(_obras)):
                    if idx_inicio == 0 and _obras[i] > 0:
                        idx_inicio = i
                        
                    if _obras[i] == _obras.max():
                        idx_fim = i
                        break
                
                ax.plot(_obras[idx_inicio:idx_fim], label='Obras')

                idx_inicio = 0
                idx_fim    = 0
                for i in range(1, len(_adm_obras)):
                    if idx_inicio == 0 and _adm_obras[i] > 0:
                        idx_inicio = i

                    if _adm_obras[i] == _adm_obras.max():
                        idx_fim = i
                        break
                ax.plot(_adm_obras[idx_inicio:idx_fim], label='Adm. Obras')

                # idx_inicio = 0
                # idx_fim    = 0
                # for i in range(1, len(_pos_obras)):
                #     if idx_inicio == 0 and _pos_obras[i] > 0:
                #         idx_inicio = i

                #     if _pos_obras[i] == _pos_obras.max():
                #         idx_fim = i
                #         break
                # ax.plot(_pos_obras[idx_inicio:idx_fim], label='Pós Obras')
                
            # if self.df_resultados['Adm'].astype(float).sum() != 0:
            #     _adm = self.df_resultados['Adm'].astype(float).cumsum() / 1000
                
            #     idx_inicio = 0
            #     idx_fim    = 0
            #     for i in range(1, len(_adm)):
            #         if idx_inicio == 0 and _adm[i] > 0:
            #             idx_inicio = i

            #         if _adm[i] == _adm.max():
            #             idx_fim = i
            #             break
            #     ax.plot(_adm[idx_inicio:idx_fim], label='Adm')
                
            
            if self.df_resultados['MkT'].astype(float).sum() != 0:
                _mkt = self.df_resultados['MkT'].astype(float).cumsum() / 1000
                
                idx_inicio = 0
                idx_fim    = 0
                for i in range(1, len(_mkt)):
                    if idx_inicio == 0 and _mkt[i] > 0:
                        idx_inicio = i

                    if _mkt[i] == _mkt.max():
                        idx_fim = i
                        break
                ax.plot(_mkt[idx_inicio:idx_fim], label='MkT')
            
            # Curva de Receitas x Gastos
            fr_curva_receitas_gastos = customtkinter.CTkFrame(fr_graficos, border_color="gray75", border_width=1, fg_color="white")
            fr_curva_receitas_gastos.place(relx=0.005, rely=0.51, relwidth=0.495, relheight=0.455)
            lb_curva_receitas_gastos = customtkinter.CTkLabel(fr_curva_receitas_gastos, text="Curvas de Receitas x Total Gastos", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
            lb_curva_receitas_gastos.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

            # Criando figura nova
            figura_2 = plt.Figure(figsize=(8, 4), dpi=100)
            ax_2 = figura_2.add_subplot(111)
            canva = FigureCanvasTkAgg(figura_2, master=fr_curva_receitas_gastos)
            canva.get_tk_widget().place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.90)
            canva.draw()
            
            # Verifica se ax.ecdf existe
            if hasattr(ax_2, "ecdf"):
                _total_gastos = (
                    self.df_resultados['Terreno'].astype(float) + 
                    self.df_resultados['Valor_Adto'].astype(float) +
                    self.df_resultados['Valor_DevolucaoAdto'].astype(float) +
                    self.df_resultados['Valor_CustoAdto'].astype(float) +
                    self.df_resultados['Projetos'].astype(float) + 
                    self.df_resultados['Obras'].astype(float) +
                    self.df_resultados['AdmObras'].astype(float) +
                    self.df_resultados['PosObras'].astype(float) +
                    self.df_resultados['Adm'].astype(float) + 
                    self.df_resultados['MkT'].astype(float)
                ).cumsum() / 1000
                ax_2.plot(_total_gastos, label='Total de Gastos')

                _vendas_receitas = self.df_resultados['ReceitaUrb'].astype(float).cumsum() / 1000
                ax_2.plot(_vendas_receitas, label='Receitas')

                # Encontrar o ponto de interseção
                idx_intersecao = None
                for i in range(min(len(_total_gastos), len(_vendas_receitas))):
                    if _vendas_receitas[i] >= _total_gastos[i]:
                        idx_intersecao = i
                        break
                if idx_intersecao is not None:
                    ax_2.axvline(idx_intersecao, color='purple', linestyle='--', label='Ponto de Equilíbrio')
                    valor_intersecao = _total_gastos[idx_intersecao]
                    ax_2.text(idx_intersecao, valor_intersecao, f'{idx_intersecao} º mês', color='purple', fontsize=10, va='bottom', ha='right')
            
            ax.set_xlabel('Períodos')
            ax.set_ylabel('R$/1.000')
            ax_2.set_xlabel('Períodos')
            ax_2.set_ylabel('R$/1.000')
            
        ax.legend()
        ax_2.legend()
        
        # DEMONSTRAÇÃO DE TAXAS
        fr_grafico_taxas = customtkinter.CTkFrame(fr_graficos, border_color="gray75", border_width=1, fg_color="white")
        fr_grafico_taxas.place(relx=0.505, rely=0.03, relwidth=0.49, relheight=0.455)
        lb_grafico_taxas = customtkinter.CTkLabel(fr_grafico_taxas, text="Taxas", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_grafico_taxas.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)
        
        # Criando figura nova
        figura_3 = plt.Figure(figsize=(8, 4), dpi=100)
        ax_3 = figura_3.add_subplot(111)
        canva = FigureCanvasTkAgg(figura_3, master=fr_grafico_taxas)
        canva.get_tk_widget().place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.90)
        canva.draw()
        
        
        # make data:
        _juros_vendas_aa  = self.df_resultados['Vendas_juros_taxa'].max()
        _vpl_taxa         = self.df_resultados['VpL_Taxa'].max()
        _tir_aa           = self.df_resultados['Tir_aa'].max()
        _tir_am           = self.df_resultados['Tir_am'].max()
        _ebitda          = self.df_resultados['DrE_Ebtda_Percente'].max()
        
        y = [_juros_vendas_aa, _vpl_taxa, _tir_aa, _tir_am, _ebitda]
        x = np.arange(len(y))  # x agora tem tamanho 4

        ax_3.bar(x, y, width=0.7, edgecolor="white", linewidth=1)
        # Adiciona o valor dentro de cada barra
        for i, valor in enumerate(y):
            percentual = valor * 100  # transforma em percentual
            ax_3.text(i, valor/2, f'{percentual:.2f}%', color='white', ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Adiciona o nome do indicador acima da barra
        labels = ['Juros \n Vendas', 'Desconto \n VpL', 'TiR \n % aa', 'TiR \n% am', 'EBITDA']
        for i, label in enumerate(labels):
            ax_3.text(i, y[i] + (max(y)*0.03), label, ha='center', va='bottom', fontsize=7, color='black', fontweight='bold')

        ax_3.set(xlim=(-0.5, len(y)-0.5), xticks=x, ylim=(0, max(y)*1.1), yticks=np.linspace(0, max(y)*1.1, 5))
        
        # OUTROS INDICADORES
        fr_grafico_outros = customtkinter.CTkFrame(fr_graficos, border_color="gray75", border_width=1, fg_color="white")
        fr_grafico_outros.place(relx=0.505, rely=0.51, relwidth=0.49, relheight=0.455)
        lb_grafico_outros = customtkinter.CTkLabel(fr_grafico_outros, text="Outros Indicadores", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_grafico_outros.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

        # Criando figura nova
        figura_4 = plt.Figure(figsize=(8, 4), dpi=100)
        ax_4 = figura_4.add_subplot(111)
        canva = FigureCanvasTkAgg(figura_4, master=fr_grafico_outros)
        canva.get_tk_widget().place(relx=0.01, rely=0.05, relwidth=0.49, relheight=0.90)
        canva.draw()
        
        _payback          = self.df_resultados['PayBack'].max()
        _multiplicador    = self.df_resultados['Multiplicador'].max()
                
        y = [_payback, _multiplicador]
        x = np.arange(len(y)) 

        ax_4.bar(x, y, width=0.7, color='red', edgecolor="white", linewidth=1)
        # Adiciona o valor dentro de cada barra
        for i, valor in enumerate(y):
            ax_4.text(i, valor/2, f'{valor:.2f}', color='white', ha='center', va='center', fontsize=8, fontweight='bold')
        
        labels_1 = ['PayBack \n anos', 'Multiplicador']
        for i, label in enumerate(labels_1):
            ax_4.text(i, y[i] + (max(y)*0.03), label, ha='center', va='bottom', fontsize=7, color='black', fontweight='bold')

        ax_4.set(xlim=(-0.5, len(y)-0.5), xticks=x, ylim=(0, max(y)*1.1), yticks=np.linspace(0, max(y)*1.1, 5))
        # ax_4.set_xticklabels(['PayBack', 'Multiplicador'], rotation=45, ha='right', fontsize=7)

        # Criando figura nova
        figura_5 = plt.Figure(figsize=(8, 4), dpi=100)
        ax_5 = figura_5.add_subplot(111)
        canva = FigureCanvasTkAgg(figura_5, master=fr_grafico_outros)
        canva.get_tk_widget().place(relx=0.505, rely=0.05, relwidth=0.49, relheight=0.90)
        canva.draw()
        
        _exposicao_maxima = self.df_resultados['Exposicao_Maxima'].max() / 1000
        _vpl              = self.df_resultados['VpL'].max() / 1000

        # make data
        x = [_exposicao_maxima, _vpl]
        labels = ['Exposição Máxima', 'VpL']
        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
        
        def mostrar_valor_absoluto(val):
            total = sum(x)
            valor = total * val / 100
            return f'{valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            
        
        ax_5.pie(
            x, 
            labels=labels, 
            colors=colors, 
            radius=3, 
            center=(4, 4), 
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, 
            frame=True, 
            autopct=mostrar_valor_absoluto)
        ax_5.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

Simulador_Estudos_Resultado()