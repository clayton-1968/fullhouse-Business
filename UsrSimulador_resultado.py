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
            
            if Investimento_Aporte is not None:
                if Investimento_Aporte == 'S':
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(Investimento_Area*-1))
                    
                elif Investimento_Aporte == 'N':
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(0))
                else:
                    self.entry_investimento_valor.insert(0, self.format_valor_fx(Investimento_Area*-1))
            else:
                self.entry_investimento_valor.insert(0, self.format_valor_fx(0))

            # self.entry_adto_parceiro_valor.insert(0, self.format_valor_fx(Adto_Parceiro_Valor))
            # self.entry_adto_parceiro_per_urbanizadora.insert(0, self.format_per_fx(Adto_Parceiro_Urb_Juros))
            # self.entry_adto_parceiro_per_parceiro.insert(0, self.format_per_fx(Adto_Parceiro_Per_Juros))
            # if Adto_Parceiro_Inicio == 0:
            #     self.entry_adto_parceiro_inicio_desembolso.insert(0, f"{1} º mês")
            # else:
            #     self.entry_adto_parceiro_inicio_desembolso.insert(0, f"{Adto_Parceiro_Inicio} º mês")
            
            # if Adto_Parceiro_Curva is not None:
            #     self.entry_adto_parceiro_curva_adto.insert(0, str(Adto_Parceiro_Curva))
            # else:
            #     self.entry_adto_parceiro_curva_adto.insert(0, str('Padrão 1 Mês'))

            # self.entry_vendas_preco_m2.insert(0, self.format_valor_fx(Valor_m2_sem_comissao))
            # self.entry_vendas_comissao_per.insert(0, self.format_per_fx(Vendas_comissao_per))
            # self.entry_vendas_vendas_preco_m2_com_comissao.insert(0, self.format_valor_fx(Vendas_Valor_com_comissao_m2))
            
            
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
            # self.entry_indicadores_tir_aa.insert(0, self.format_per_fx(Tir))
            # self.entry_indicadores_tir_am.insert(0, self.format_per_fx(indicadores_tir_am))
            # self.entry_indicadores_payback.insert(0, self.format_ano_fx(Payback))
            # self.entry_indicadores_multiplicador_investimento.insert(0, self.format_valor_fx(Multiplicador))
            # self.entry_indicadores_exposicaomax_caixa.insert(0, self.format_valor_fx(ExposicaoMax))
            # self.entry_indicadores_vpl_urbanizadora.insert(0, self.format_valor_fx(Vpl_Urb))
            # self.entry_indicadores_vpl_parceiro.insert(0, self.format_valor_fx(Vpl_Parceiro))
            
            # if Observacao is not None:
            #     self.text_observacoes.insert('1.0', str(Observacao))
            
            # if Http is not None:
            #     self.entry_informacoes_https.insert(0, str(Http))

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
                        ff.Multiplicador               AS Multiplicador,
                        ff.Vlr_Exposicao_Maxima        AS Exposicao_Maxima,
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
        lb_dre_vgv_bruto = customtkinter.CTkLabel(fr_dre, text="Valor Geral de Vendas - Bruto:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_vgv_bruto.place(relx=0.01, rely=0.04, relheight=0.05, relwidth=0.45)
        self.entry_dre_vgv_bruto = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_bruto.place(relx=0.50, rely=0.04, relwidth=0.49, relheight=0.05)

        # Comissão
        lb_dre_comissao = customtkinter.CTkLabel(fr_dre, text="Comissão de Vendas:", text_color="black", font=('Arial', 12), anchor=tk.W)
        lb_dre_comissao.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.25)
        lb_deducao_7.place(relx=0.43, rely=0.10, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_comissao.place(relx=0.50, rely=0.10, relwidth=0.49, relheight=0.05)

        # VGV Líquido
        lb_dre_vgv_liquido = customtkinter.CTkLabel(fr_dre, text="Valor Geral de Vendas - Líquido.:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_vgv_liquido.place(relx=0.01, rely=0.16, relheight=0.05, relwidth=0.45)
        self.entry_dre_vgv_liquido = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_liquido.place(relx=0.50, rely=0.16, relwidth=0.49, relheight=0.05)

        # Imposto
        lb_dre_impostos = customtkinter.CTkLabel(fr_dre, text="Impostos:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_impostos.place(relx=0.01, rely=0.22, relheight=0.05, relwidth=0.25)
        lb_deducao_8.place(relx=0.43, rely=0.22, relheight=0.05, relwidth=0.25)
        self.entry_dre_impostos = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_impostos.place(relx=0.50, rely=0.22, relwidth=0.49, relheight=0.05)

        # Comissão de Negócio
        lb_dre_comissao_negocio = customtkinter.CTkLabel(fr_dre, text="Itermediação do Negócio:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_comissao_negocio.place(relx=0.01, rely=0.28, relheight=0.05, relwidth=0.25)
        lb_deducao_9.place(relx=0.43, rely=0.28, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao_negocio = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_dre_comissao_negocio.place(relx=0.50, rely=0.28, relwidth=0.49, relheight=0.05)

        # Receita Líquida
        lb_dre_receita_liquida = customtkinter.CTkLabel(fr_dre, text="Receita Líquida:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_receita_liquida.place(relx=0.01, rely=0.34, relheight=0.05, relwidth=0.45)
        self.entry_dre_receita_liquida = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida.place(relx=0.50, rely=0.34, relwidth=0.49, relheight=0.05)

        # VGV Parceiro
        lb_dre_vgv_parceiro = customtkinter.CTkLabel(fr_dre, text="Receita do Parceiro:", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_dre_vgv_parceiro.place(relx=0.01, rely=0.40, relheight=0.05, relwidth=0.45)
        lb_deducao_10.place(relx=0.43, rely=0.40, relheight=0.05, relwidth=0.25)
        self.entry_dre_vgv_parceiro = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_parceiro.place(relx=0.50, rely=0.40, relwidth=0.49, relheight=0.05)

        # Receita Líquida Urbanizadora
        lb_dre_receita_liquida_urbanizadora = customtkinter.CTkLabel(fr_dre, text="Receita Urbanizaodora:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        lb_dre_receita_liquida_urbanizadora.place(relx=0.01, rely=0.46, relheight=0.05, relwidth=0.25)
        self.entry_dre_receita_liquida_urbanizadora = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida_urbanizadora.place(relx=0.50, rely=0.46, relwidth=0.49, relheight=0.05)
        
        # Custos
        lb_investimentos = customtkinter.CTkLabel(fr_dre, text="Investimento/Terreno", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_investimentos.place(relx=0.01, rely=0.52, relheight=0.05, relwidth=0.25)
        lb_deducao_11.place(relx=0.43, rely=0.52, relheight=0.05, relwidth=0.05)
        self.entry_investimento_valor = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_investimento_valor.place(relx=0.50, rely=0.52, relwidth=0.49, relheight=0.05)

        lb_projetos = customtkinter.CTkLabel(fr_dre, text="Projetos", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_projetos.place(relx=0.01, rely=0.58, relheight=0.05, relwidth=0.25)
        self.entry_projetos_per_obra = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_projetos_per_obra.place(relx=0.30, rely=0.58, relwidth=0.10, relheight=0.05)
        lb_deducao_1.place(relx=0.43, rely=0.58, relheight=0.05, relwidth=0.05)
        self.entry_projetos_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_projetos_valor_total.place(relx=0.50, rely=0.58, relwidth=0.49, relheight=0.05)

        lb_mkt_per_vgv = customtkinter.CTkLabel(fr_dre, text="MkT - % x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_mkt_per_vgv.place(relx=0.01, rely=0.64, relheight=0.05, relwidth=0.25)
        self.entry_mkt_per_vgv = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_mkt_per_vgv.place(relx=0.30, rely=0.64, relwidth=0.10, relheight=0.05)
        lb_deducao_2.place(relx=0.43, rely=0.64, relheight=0.05, relwidth=0.05)
        self.entry_mkt_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_mkt_valor_total.place(relx=0.50, rely=0.64, relwidth=0.49, relheight=0.05)

        lb_overhead_per_vgv = customtkinter.CTkLabel(fr_dre, text="Adm. - % x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_overhead_per_vgv.place(relx=0.01, rely=0.70, relheight=0.05, relwidth=0.25)
        self.entry_overhead_per_vgv = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_overhead_per_vgv.place(relx=0.30, rely=0.70, relwidth=0.10, relheight=0.05)
        lb_deducao_3.place(relx=0.43, rely=0.70, relheight=0.05, relwidth=0.25)
        self.entry_overhead_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_overhead_valor_total.place(relx=0.50, rely=0.70, relwidth=0.49, relheight=0.05)

        lb_obras_valor_m2 = customtkinter.CTkLabel(fr_dre, text="Custo $m² de Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_obras_valor_m2.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.25)
        self.entry_obras_valor_m2 = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_obras_valor_m2.place(relx=0.30, rely=0.76, relwidth=0.10, relheight=0.05)
        lb_deducao_4.place(relx=0.43, rely=0.76, relheight=0.05, relwidth=0.25)
        self.entry_obras_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_obras_valor_total.place(relx=0.50, rely=0.76, relwidth=0.49, relheight=0.05)

        lb_adm_per_obras = customtkinter.CTkLabel(fr_dre, text="Adm. - % x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_adm_per_obras.place(relx=0.01, rely=0.82, relheight=0.05, relwidth=0.25)
        self.entry_adm_per_obras = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adm_per_obras.place(relx=0.30, rely=0.82, relwidth=0.10, relheight=0.05)
        lb_deducao_5.place(relx=0.43, rely=0.82, relheight=0.05, relwidth=0.25)
        self.entry_adm_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_adm_valor_total.place(relx=0.50, rely=0.82, relwidth=0.49, relheight=0.05)

        lb_pos_obras_per_obras = customtkinter.CTkLabel(fr_dre, text="Pós Obras - % x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_pos_obras_per_obras.place(relx=0.01, rely=0.88, relheight=0.05, relwidth=0.25)
        self.entry_pos_obras_per_obras = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_pos_obras_per_obras.place(relx=0.30, rely=0.88, relwidth=0.10, relheight=0.05)
        lb_deducao_6.place(relx=0.43, rely=0.88, relheight=0.05, relwidth=0.25)
        self.entry_pos_obras_valor_total = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="red", justify=tk.RIGHT)
        self.entry_pos_obras_valor_total.place(relx=0.50, rely=0.88, relwidth=0.49, relheight=0.05)

        # Resultado Líquido Urbanizadora
        self.lb_dre_ebtda_valor = customtkinter.CTkLabel(fr_dre, text="Resultado Líquido:", text_color="black", font=('Arial', 15, 'bold'), anchor=tk.W)
        self.lb_dre_ebtda_valor.place(relx=0.01, rely=0.94, relheight=0.05, relwidth=0.45)
        self.entry_dre_ebtda_per = customtkinter.CTkEntry(fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
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
        fr_curva_gastos.place(relx=0.005, rely=0.03, relwidth=0.985, relheight=0.495)
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
                _adto = self.df_resultados['Valor_Adto'].astype(float).cumsum() / 1000
                _devolucao_adto = self.df_resultados['Valor_DevolucaoAdto'].astype(float).cumsum() / 1000
                _custo_adto = self.df_resultados['Valor_CustoAdto'].astype(float).cumsum() / 1000
                ax.plot(_adto, label='Adto')
                ax.plot(_devolucao_adto, label='Devolução Adto')
                ax.plot(_custo_adto, label='Custo Adto')
            
            
            if self.df_resultados['Projetos'].astype(float).sum() != 0.0:
                _projetos = self.df_resultados['Projetos'].astype(float).cumsum() / 1000
                ax.plot(_projetos, label='Projetos')
            
            if self.df_resultados['Obras'].astype(float).sum() != 0:
                _obras = self.df_resultados['Obras'].astype(float).cumsum() / 1000
                _adm_obras = self.df_resultados['AdmObras'].astype(float).cumsum() / 1000
                _pos_obras = self.df_resultados['PosObras'].astype(float).cumsum() / 1000
                ax.plot(_obras, label='Obras')
                ax.plot(_adm_obras, label='Adm. Obras')
                ax.plot(_pos_obras, label='Pós Obras')
            
            if self.df_resultados['Adm'].astype(float).sum() != 0:
                _adm = self.df_resultados['Adm'].astype(float).cumsum() / 1000
                ax.plot(_adm, label='Adm')
            
            if self.df_resultados['MkT'].astype(float).sum() != 0:
                _mkt = self.df_resultados['MkT'].astype(float).cumsum() / 1000
                ax.plot(_mkt, label='MkT')
            
            
            # Curva de Receitas x Gastos
            fr_curva_receitas_gastos = customtkinter.CTkFrame(fr_graficos, border_color="gray75", border_width=1, fg_color="white")
            fr_curva_receitas_gastos.place(relx=0.005, rely=0.51, relwidth=0.985, relheight=0.485)
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

                

            # ax.plot(self.df_resultados['Valor_Liberacao'], label='Liberação')
            # ax.plot(self.df_resultados['Vlr_ParcelaFinanciamento'], label='Parcela Financiamento')
            # ax.plot(self.df_resultados['Fx_Caixa'], label='Fx Caixa')
            # ax.plot(self.df_resultados['Fx_Caixa_Acumulado'], label='Fx Caixa Acumulado')

            ax.set_xlabel('Períodos')
            ax.set_ylabel('R$/1.000')
            ax_2.set_xlabel('Períodos')
            ax_2.set_ylabel('R$/1.000')
            
        # else:
        #     # ECDF manual
        #     x_sorted = np.sort(x)
        #     y_ecdf = np.arange(1, len(x_sorted)+1) / len(x_sorted)
        #     ax.plot(x_sorted, y_ecdf, marker=".", linestyle="none")
        #     ax.set_xlabel('Períodos')
        #     ax.set_ylabel('% Execução')

        ax.legend()
        ax_2.legend()
        
        
        # # Indicadores
        # fr_indicadores = customtkinter.CTkFrame(fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        # fr_indicadores.place(relx=0.005, rely=0.61, relwidth=0.985, relheight=0.385)
        # lb_indicadores = customtkinter.CTkLabel(fr_indicadores, text="Indicadores", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        # lb_indicadores.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

        # # T.I.R. a.a.
        # self.lb_indicadores_tir_aa = customtkinter.CTkLabel(fr_indicadores, text="T.I.R. a.a.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_tir_aa.place(relx=0.01, rely=0.07, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_tir_aa = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_tir_aa.place(relx=0.30, rely=0.08, relwidth=0.69, relheight=0.12)

        # # T.I.R. a.m.
        # self.lb_indicadores_tir_am = customtkinter.CTkLabel(fr_indicadores, text="T.I.R. a.m.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_tir_am.place(relx=0.01, rely=0.20, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_tir_am = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_tir_am.place(relx=0.30, rely=0.21, relwidth=0.69, relheight=0.12)

        # # PayBack
        # self.lb_indicadores_payback = customtkinter.CTkLabel(fr_indicadores, text="PayBack:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_payback.place(relx=0.01, rely=0.33, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_payback = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_payback.place(relx=0.30, rely=0.34, relwidth=0.69, relheight=0.12)

        # # Multiplicador do Investimento
        # self.lb_indicadores_multiplicador_investimento = customtkinter.CTkLabel(fr_indicadores, text="Mult.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_multiplicador_investimento.place(relx=0.01, rely=0.46, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_multiplicador_investimento = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_multiplicador_investimento.place(relx=0.30, rely=0.47, relwidth=0.69, relheight=0.12)

        # # Exposição Máxima de Caixa
        # self.lb_indicadores_exposicaomax_caixa = customtkinter.CTkLabel(fr_indicadores, text="Exp.Max.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_exposicaomax_caixa.place(relx=0.01, rely=0.59, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_exposicaomax_caixa = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_exposicaomax_caixa.place(relx=0.30, rely=0.60, relwidth=0.69, relheight=0.12)

        # # VPL Urbanizadora
        # self.lb_indicadores_vpl_urbanizadora = customtkinter.CTkLabel(fr_indicadores, text="VPL Urban.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_vpl_urbanizadora.place(relx=0.01, rely=0.72, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_vpl_urbanizadora = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_vpl_urbanizadora.place(relx=0.30, rely=0.73, relwidth=0.69, relheight=0.12)

        # # VPL Parceriro
        # self.lb_indicadores_vpl_parceiro = customtkinter.CTkLabel(fr_indicadores, text="VPV Parceiro:", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_indicadores_vpl_parceiro.place(relx=0.01, rely=0.85, relheight=0.20, relwidth=0.25)
        # self.entry_indicadores_vpl_parceiro = customtkinter.CTkEntry(fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_indicadores_vpl_parceiro.place(relx=0.30, rely=0.86, relwidth=0.69, relheight=0.12)

        # Observações do Estudo
        # fr_observacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="white")
        # fr_observacoes.place(relx=0.091, rely=0.56, relwidth=0.749, relheight=0.25)
        # lb_observacoes = customtkinter.CTkLabel(fr_observacoes, text="Observações do Negócio", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        # lb_observacoes.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.60)

        # # observações
        # self.text_observacoes = customtkinter.CTkTextbox(fr_observacoes, fg_color="black", text_color="white", width=300, height=100)
        # self.text_observacoes.place(relx=0.0, rely=0.06, relwidth=1, relheight=0.94)
        # self.text_observacoes.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_taxa_desconto))

        # informações - localização, status, anexos, data
        # self.fr_informacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="Light Yellow")
        # self.fr_informacoes.place(relx=0, rely=0.81, relwidth=0.84, relheight=0.16)
        # self.lb_informacoes = customtkinter.CTkLabel(self.fr_informacoes, text="Informações do Estudo", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        # self.lb_informacoes.place(relx=0.05, rely=0, relheight=0.10, relwidth=0.70)

        # Icon de Consulta Endereço Cadastrado
        # def selected_maps():
        #     ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get(), janela) 
        #     UF = self.entry_uf.get()
        #     Cidade = self.entry_municipio.get()
        #     Tipo_Estudo = self.entry_tpo_projeto.get()
        #     Nome_Area = self.entry_nome_cenario.get()
        #     url =self.entry_informacoes_https.get()
            
        #     if not ID_Empresa:
        #         messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     if not UF:
        #         messagebox.showinfo('Gestor Negócios', 'UF em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     if not Cidade:
        #         messagebox.showinfo('Gestor Negócios', 'Município em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     if not Tipo_Estudo:
        #         messagebox.showinfo('Gestor Negócios', 'Tipo do Estudo em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     if not Nome_Area:
        #         messagebox.showinfo('Gestor Negócios', 'Nome da Área em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     if not url:
        #         messagebox.showinfo('Gestor Negócios', 'Url da Área em Branco!!!', parent=self.janela_simulador_resultado)
        #         return
            
        #     UF = UF.upper()
        #     url = url.strip()  # Remove espaços em branco no início e no fim
        #     webbrowser.open(url)

        # coordenadas_relx = 0.915
        # coordenadas_rely = 0.55
        # coordenadas_relwidth = 0.05
        # coordenadas_relheight = 0.25
        # icon_image = self.base64_to_photoimage('lupa')
        # self.btn_consultar_maps = customtkinter.CTkButton(
        #                                             self.fr_informacoes,  
        #                                             text='',
        #                                             image=icon_image, 
        #                                             fg_color='transparent', 
        #                                             command=selected_maps
        #                                                 )
        # self.btn_consultar_maps.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        # self.btn_consultar_maps.bind("<Return>", lambda event: self.btn_consultar_maps.invoke())
        # # Adicionar o tooltip
        # ToolTip(self.btn_consultar_maps, "Consultar Endereço Cadastrado")
        
        # self.limpar_simulador_negocios()
    
Simulador_Estudos_Resultado()