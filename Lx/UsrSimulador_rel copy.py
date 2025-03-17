from imports import *
from widgets import Widgets
################# criando janela ###############
class Simulador_Estudos_Rel(Widgets):
    def simulador_estudos_rel(self):
        self.janela_simulador_rel = customtkinter.CTk()
        self.janela_simulador_rel.title('Simulador de Estudos de Negócios')
        self.janela_simulador_rel.geometry("1124x760+0+0")
        self.janela_simulador_rel.resizable(True, True)
        
        self.frame_dados_rel(self.janela_simulador_rel)
        self.frame_novosnegocios(self.janela_simulador_rel)
        self.frame_carregar_dados(self.janela_simulador_rel)

        self.janela_simulador_rel.focus_force()
        self.janela_simulador_rel.grab_set()
        self.janela_simulador_rel.mainloop()

    def frame_dados_rel(self, janela):
        # Empresa
        coordenadas_relx=0
        coordenadas_rely=0.01
        coordenadas_relwidth=0.34
        coordenadas_relheight=0.07
        self.frame_empresa(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        
        # Estado
        coordenadas_relx=0.34
        coordenadas_rely=0.01
        coordenadas_relwidth=0.06
        coordenadas_relheight=0.07
        self.frame_uf(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        
        # Municipio
        coordenadas_relx=0.40
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        self.frame_municipio(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        
        # Tipo do Projeto
        coordenadas_relx=0.60
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        self.frame_tpo_projeto(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        
        # Nome do Projeto
        coordenadas_relx=0.80
        coordenadas_rely=0.01
        coordenadas_relwidth=0.15
        coordenadas_relheight=0.07
        self.frame_nome_projeto(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)

        # Icon de Consulta
        coordenadas_relx = 0.95
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.05
        coordenadas_relheight = 0.07
        self.button_consultar(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight,'consultar')
        
        # Icon Processar
        coordenadas_relx = 0.90
        coordenadas_rely = 0.90
        coordenadas_relwidth = 0.10
        coordenadas_relheight = 0.07
        self.button_processar(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight,'processar')

    def frame_carregar_dados(self, janela):
        self.limpar_simulador_negocios()
                    
        # Carregar Variáveis
        Empresa_DS = self.lista_negocio[0].get('Pri_Descricao')
        UF = self.lista_negocio[0].get('UF')
        Cidade = self.lista_negocio[0].get('Cidade')
        Tipo = self.lista_negocio[0].get('Tipo')
        Nome_da_Area = self.lista_negocio[0].get('Nome_da_Area')
        
        Area_Total = self.lista_negocio[0].get('Area_Total')
        Per_Area_Aproveitada = self.lista_negocio[0].get('Per_Aproveitamento')
        Area_Aproveitada = self.lista_negocio[0].get('Area_Aproveitada')
        Medidas_Lote = self.lista_negocio[0].get('Medidas_Lote')
        Lote_Medio = self.lista_negocio[0].get('Area_Lote_Medio')
        Nr_Lotes = self.lista_negocio[0].get('Nr_Unidades')
        
        Participacao_Urbanizadora = self.lista_negocio[0].get('Participacao_Urbanizadora')
        Participacao_Parceiro = self.lista_negocio[0].get('Participação_Parceiro')
        Permuta_em_Lotes = self.lista_negocio[0].get('Permuta_em_Lotes')
        Per_Comissao_Negocio = self.lista_negocio[0].get('Per_Comissao_Negocio')
        Per_MkT_Cobrado = self.lista_negocio[0].get('Per_MkT_Cobrado')
        Total_Urbanizadora = self.lista_negocio[0].get('Participação_Total_Urbanizadora')
        Total_Parceiro = self.lista_negocio[0].get('Participação_Total_Parceiro')
                      
        Investimento_Area = self.lista_negocio[0].get('Investimento_Area')
        Investimento_Area_Inicio = self.lista_negocio[0].get('Investimento_Area_Inicio')
        Investimento_Area_Curva = self.lista_negocio[0].get('Investimento_Area_Curva')
        Investimento_Aporte = self.lista_negocio[0].get('Investimento_Aporte')
                  
        Adto_Parceiro_Valor = self.lista_negocio[0].get('Adto_Parceiro_Valor')
        Adto_Parceiro_Urb_Juros = self.lista_negocio[0].get('Adto_Parceiro_Urb_Juros')
        Adto_Parceiro_Per_Juros = self.lista_negocio[0].get('Adto_Parceiro_Per_Juros')
        Adto_Parceiro_Inicio = self.lista_negocio[0].get('Adto_Parceiro_Inicio')
        Adto_Parceiro_Curva = self.lista_negocio[0].get('Adto_Parceiro_Curva')

        Valor_m2_sem_comissao = self.lista_negocio[0].get('Vendas_Valor_m2')
        Vendas_comissao_per = self.lista_negocio[0].get('Vendas_comissao_per')
        Vendas_Valor_com_comissao_m2 = self.lista_negocio[0].get('Valor_m2_com_comissao')
        Vendas_Tickt_Medio = self.lista_negocio[0].get('tickt_medio')
        Vendas_prazo_financiamento = self.lista_negocio[0].get('Vendas_prazo_financiamento')
        Vendas_sistema_amortizacao = self.lista_negocio[0].get('Vendas_sistema_amortizacao')
        Vendas_juros_taxa = self.lista_negocio[0].get('Vendas_juros_taxa')
        Vendas_juros_am = self.lista_negocio[0].get('Per_Juros_am')
        Vendas_per_entrada = self.lista_negocio[0].get('Vendas_per_entrada')
        Vendas_parcela_entrada = self.lista_negocio[0].get('Vendas_parcela_entrada')
        Vendas_per_reforcos = self.lista_negocio[0].get('Vendas_per_reforcos')
        Vendas_parcela_reforcos = self.lista_negocio[0].get('Vendas_parcela_reforcos')
        Vendas_periodicidade_reforcos = self.lista_negocio[0].get('Vendas_periodicidade_reforcos')
        Vendas_per_avista = self.lista_negocio[0].get('Vendas_per_avista')
        Vendas_inicio = self.lista_negocio[0].get('Vendas_inicio')
        Vendas_curva = self.lista_negocio[0].get('Vendas_curva')
        Vendas_parcela_price = 0
        Vendas_parcela_sacoc = 0
        
        Projetos_per_obra = self.lista_negocio[0].get('Projetos_per_obra')
        Projetos_Valor = self.lista_negocio[0].get('Projetos_Valor')
        Projetos_inicio = self.lista_negocio[0].get('Projetos_inicio')
        Projetos_curva = self.lista_negocio[0].get('Projetos_curva')

        MkT_per_vgv = self.lista_negocio[0].get('MkT_per_vgv')
        MkT_Valor = self.lista_negocio[0].get('Projetos_Valor')
        MkT_inicio = self.lista_negocio[0].get('MkT_inicio')
        MkT_curva = self.lista_negocio[0].get('MkT_curva')
                            
        Adm_per_receita = self.lista_negocio[0].get('Adm_per_receita')
        Adm_Valor = self.lista_negocio[0].get('OverHead_Valor')
        Adm_Inicio = self.lista_negocio[0].get('OverHead_Inicio')
        Adm_Curva = self.lista_negocio[0].get('OverHead_Curva')

        Obras_custo_m2 = self.lista_negocio[0].get('Obras_custo_m2')
        Obra_Valor = self.lista_negocio[0].get('Obra_Valor')
        Obras_inicio = self.lista_negocio[0].get('Obras_inicio')
        Obras_curva = self.lista_negocio[0].get('Obras_curva')
        
        Pos_Obra_per_obra = self.lista_negocio[0].get('Pos_Obra_per_obra')
        Pos_Obra_Valor = self.lista_negocio[0].get('Pos_Obra_Valor')
        Pos_Obra_Inicio = self.lista_negocio[0].get('Pos_Obra_Inicio')
        Pos_Obra_curva = self.lista_negocio[0].get('Pos_Obra_Curva')
        
        AdmObra_per_obra = self.lista_negocio[0].get('AdmObra_per_obra')
        AdmObra_Valor = self.lista_negocio[0].get('AdmObras_Valor')
        AdmObra_Inicio = self.lista_negocio[0].get('AdmObras_Inicio')
        AdmObra_curva = self.lista_negocio[0].get('AdmObras_Curva')
        
        Financiamento_valor = self.lista_negocio[0].get('Financiamento_valor')
        Financiamento_sistema_amortizacao = self.lista_negocio[0].get('Financiamento_sistema_amortizacao')
        Financiamento_prazo_amortizacao = self.lista_negocio[0].get('Financiamento_prazo_amortizacao')
        Financiamento_inicio_amortizacao = self.lista_negocio[0].get('Financiamento_inicio_amortizacao')
        Financiamento_inicio_pagto_juros = self.lista_negocio[0].get('Financiamento_inicio_pagto_juros')
        Financiamento_juros = 0
        Financiamento_taxa = self.lista_negocio[0].get('Financiamento_taxa')
        Financiamento_liberacao = self.lista_negocio[0].get('Financiamento_liberacao')
        Financiamento_curva = self.lista_negocio[0].get('Financiamento_curva')
        Financiamento_financiador = self.lista_negocio[0].get('Financiamento_financiador')
                    
        Observacao = self.lista_negocio[0].get('Observacao')

        DrE_VGV_bruto = self.lista_negocio[0].get('DrE_VgV_Bruto')
        DrE_comissao =self.lista_negocio[0].get('DrE_comissao_venda')
        DrE_VGV_liquido = self.lista_negocio[0].get('DrE_VgV_Liquido')
        DrE_impostos = self.lista_negocio[0].get('DrE_impostos')
        DrE_comissao_negocios = self.lista_negocio[0].get('DrE_comissao_negocio')
        DrE_receita_liquida = self.lista_negocio[0].get('DrE_Receita_Liquida')
        DrE_VGV_parceiro = self.lista_negocio[0].get('DrE_Receita_Parceiro')
        DrE_receita_liquida_urbanizadora = self.lista_negocio[0].get('DrE_Receita_Urbanizador')
        DrE_ebtda_valor = self.lista_negocio[0].get('DrE_Ebtda_Valor')
        DrE_ebtda_per = self.lista_negocio[0].get('DrE_Ebtda_Percente')
        Tir = self.lista_negocio[0].get('Tir')
        indicadores_tir_am = self.lista_negocio[0].get('Tir_Urbanizadora_am') 
        Payback = self.lista_negocio[0].get('Payback')
        Multiplicador = self.lista_negocio[0].get('Multiplicador')
        ExposicaoMax = self.lista_negocio[0].get('ExposicaoMax')
        Vpl_Urb = self.lista_negocio[0].get('Vpl_Urb')
        Vpl_Parceiro = self.lista_negocio[0].get('Vpl_Parceiro')
        Desconto_VpL_taxa = self.lista_negocio[0].get('VpL_Taxa_Desconto')

        Status_Prospeccao = self.lista_negocio[0].get('Status_Prospeccao')
        Anexos = self.lista_negocio[0].get('Anexos')
        Dta_Contrato = self.lista_negocio[0].get('Dta_Contrato')
        Unidade = self.lista_negocio[0].get('Unidade')
        Http = self.lista_negocio[0].get('Http')
        informacoes_maps =  self.lista_negocio[0].get('Coordenadas')

        Usr = self.lista_negocio[0].get('Usr')
        Dta_Registro = self.lista_negocio[0].get('Dta_Registro')
        
        # Preenche Cabeçalho
        self.combo_empresa.set(Empresa_DS)
        self.combo_uf.set(UF)
        self.combo_municipio.set(Cidade)
        self.combo_tpo_projeto.set(Tipo)
        self.combo_nome_cenario.set(Nome_da_Area) 
        
        # Preenche os campos
        # Limpar os campos
        self.entry_area_total.delete(0, 'end')
        self.entry_area_aproveitamento.delete(0, 'end')
        self.entry_area_aproveitado.delete(0, 'end')
        self.entry_area_lote_padrao.delete(0, 'end')
        self.entry_area_lote_medio.delete(0, 'end')
        self.entry_area_nr_lotes.delete(0, 'end')
        self.entry_participacao_urbanizador.delete(0, 'end')
        self.entry_participacao_parceiro.delete(0, 'end')
        self.entry_participacao_permuta.delete(0, 'end')
        self.entry_comissao_intermediacao.delete(0, 'end')
        self.entry_admmkt_parceiro.delete(0, 'end')
        self.entry_total_urbanizadora.delete(0, 'end')
        self.entry_total_parceiro.delete(0, 'end')
        self.entry_investimento_valor.delete(0, 'end')
        self.entry_investimento_inicio_desembolso.delete(0, 'end')
        self.entry_investimento_curva_investimento.delete(0, 'end')
        self.entry_adto_parceiro_valor.delete(0, 'end')
        self.entry_adto_parceiro_per_urbanizadora.delete(0, 'end')
        self.entry_adto_parceiro_per_parceiro.delete(0, 'end')
        self.entry_adto_parceiro_inicio_desembolso.delete(0, 'end')
        self.entry_adto_parceiro_curva_adto.delete(0, 'end')
        self.entry_vendas_preco_m2.delete(0, 'end')
        self.entry_vendas_comissao_per.delete(0, 'end')
        self.entry_vendas_vendas_preco_m2_com_comissao.delete(0, 'end')
        self.entry_vendas_lote_medio.delete(0, 'end')
        self.entry_vendas_financiamento_prazo.delete(0, 'end')
        self.entry_vendas_sistema_amortizacao.delete(0, 'end')
        self.entry_vendas_juros_aa.delete(0, 'end')
        self.entry_vendas_juros_am.delete(0, 'end')
        self.entry_vendas_entrada.delete(0, 'end')
        self.entry_vendas_nr_parcelas_entrada.delete(0, 'end')
        self.entry_vendas_reforcos.delete(0, 'end')
        self.entry_vendas_nr_parcelas_reforcos.delete(0, 'end')
        self.entry_vendas_period_reforcos.delete(0, 'end')
        self.entry_vendas_per_avista.delete(0, 'end')
        self.entry_vendas_inicio.delete(0, 'end')
        self.entry_vendas_curva.delete(0, 'end')
        self.entry_vendas_parcela_price.delete(0, 'end')
        self.entry_vendas_parcela_sacoc.delete(0, 'end')
        self.entry_projetos_per_obra.delete(0, 'end')
        self.entry_projetos_valor_total.delete(0, 'end')
        self.entry_projetos_inicio_desembolso.delete(0, 'end')
        self.entry_projetos_curva_projeto.delete(0, 'end')
        self.entry_mkt_per_vgv.delete(0, 'end')
        self.entry_mkt_valor_total.delete(0, 'end')
        self.entry_mkt_inicio_desembolso.delete(0, 'end')
        self.entry_mkt_curva_mkt.delete(0, 'end')
        self.entry_overhead_per_vgv.delete(0, 'end')
        self.entry_overhead_valor_total.delete(0, 'end')
        self.entry_overhead_inicio_desembolso.delete(0, 'end')
        self.entry_overhead_curva_overhead.delete(0, 'end')
        self.entry_obras_valor_m2.delete(0, 'end')
        self.entry_obras_valor_total.delete(0, 'end')
        self.entry_obras_inicio_desembolso.delete(0, 'end')
        self.entry_obras_curva_obras.delete(0, 'end')
        self.entry_pos_obras_per_obras.delete(0, 'end')
        self.entry_pos_obras_valor_total.delete(0, 'end')
        self.entry_pos_obras_inicio_desembolso.delete(0, 'end')
        self.entry_pos_obras_curva_obras.delete(0, 'end')
        self.entry_adm_per_obras.delete(0, 'end')
        self.entry_adm_valor_total.delete(0, 'end')
        self.entry_adm_inicio_desembolso.delete(0, 'end')
        self.entry_adm_curva_obras.delete(0, 'end')
        self.entry_financiamento_valor_captacao.delete(0, 'end')
        self.entry_financiamento_sistema_amortizacao.delete(0, 'end')
        self.entry_financiamento_prazo_amortizacao.delete(0, 'end')
        self.entry_financiamento_inicio_amortizacao.delete(0, 'end')
        self.entry_financiamento_inicio_pagto_juros.delete(0, 'end')
        self.entry_financiamento_juros.delete(0, 'end')
        self.entry_financiamento_juros_aa.delete(0, 'end')
        self.entry_financiamento_inicio_liberacao.delete(0, 'end')
        self.entry_financiamento_curva_liberacao.delete(0, 'end')
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
        self.entry_indicadores_tir_aa.delete(0, 'end')
        self.entry_indicadores_tir_am.delete(0, 'end')
        self.entry_indicadores_payback.delete(0, 'end')
        self.entry_indicadores_multiplicador_investimento.delete(0, 'end')
        self.entry_indicadores_exposicaomax_caixa.delete(0, 'end')
        self.entry_indicadores_vpl_urbanizadora.delete(0, 'end')
        self.entry_indicadores_vpl_parceiro.delete(0, 'end')
        self.entry_taxa_desconto.delete(0, 'end')
        self.text_observacoes.delete('1.0', 'end')
        self.entry_informacoes_status.delete(0, 'end')
        self.entry_informacoes_anexos.delete(0, 'end')
        self.entry_informacoes_data.delete(0, 'end')
        self.entry_informacoes_unidade_negocio.delete(0, 'end')
        self.entry_informacoes_https.delete(0, 'end')
        self.entry_informacoes_maps.delete(0, 'end')
        
        # Inserir os dados
        self.entry_area_total.insert(0, self.format_m2_fx(Area_Total))  
        self.entry_area_aproveitamento.insert(0, self.format_per_fx(Per_Area_Aproveitada))
        
        self.entry_area_aproveitado.insert(0, self.format_m2_fx(Area_Aproveitada))
        self.entry_area_lote_padrao.insert(0, str(Medidas_Lote))
        self.entry_area_lote_medio.insert(0, self.format_valor_fx(float(Lote_Medio)))
        self.entry_area_nr_lotes.insert(0, self.format_valor_fx(Nr_Lotes))

        self.entry_participacao_urbanizador.insert(0, self.format_per_fx(Participacao_Urbanizadora))
        self.entry_participacao_parceiro.insert(0, self.format_per_fx(Participacao_Parceiro))
        self.entry_participacao_permuta.insert(0, self.format_per_fx(Permuta_em_Lotes))
        self.entry_comissao_intermediacao.insert(0, self.format_per_fx(Per_Comissao_Negocio))
        self.entry_admmkt_parceiro.insert(0, self.format_per_fx(Per_MkT_Cobrado))
        self.entry_total_urbanizadora.insert(0, self.format_per_fx(Total_Urbanizadora))
        self.entry_total_parceiro.insert(0, self.format_per_fx(Total_Parceiro))

        self.entry_investimento_valor.insert(0, self.format_valor_fx(Investimento_Area))
        self.entry_investimento_inicio_desembolso.insert(0, f"{Investimento_Area_Inicio} º mês")
        self.entry_investimento_curva_investimento.insert(0, str(Investimento_Area_Curva))
        if Investimento_Aporte == 'S':
            self.entry_investimento_aporte.set(str('Sim'))
        elif Investimento_Aporte == 'N':
            self.entry_investimento_aporte.set(str('Não'))
        else:
            self.entry_investimento_aporte.set(str(Investimento_Aporte))

        self.entry_adto_parceiro_valor.insert(0, self.format_valor_fx(Adto_Parceiro_Valor))
        self.entry_adto_parceiro_per_urbanizadora.insert(0, self.format_per_fx(Adto_Parceiro_Urb_Juros))
        self.entry_adto_parceiro_per_parceiro.insert(0, self.format_per_fx(Adto_Parceiro_Per_Juros))
        self.entry_adto_parceiro_inicio_desembolso.insert(0, f"{Adto_Parceiro_Inicio} º mês")
        self.entry_adto_parceiro_curva_adto.insert(0, str(Adto_Parceiro_Curva))

        self.entry_vendas_preco_m2.insert(0, self.format_valor_fx(Valor_m2_sem_comissao))
        self.entry_vendas_comissao_per.insert(0, self.format_per_fx(Vendas_comissao_per))
        self.entry_vendas_vendas_preco_m2_com_comissao.insert(0, self.format_valor_fx(Vendas_Valor_com_comissao_m2))
        self.entry_vendas_lote_medio.insert(0, self.format_valor_fx(Vendas_Tickt_Medio))
        self.entry_vendas_financiamento_prazo.insert(0, self.format_x_fx(Vendas_prazo_financiamento))
        self.entry_vendas_sistema_amortizacao.insert(0, str(Vendas_sistema_amortizacao))
        self.entry_vendas_juros_aa.insert(0, self.format_per_fx(Vendas_juros_taxa))
        self.entry_vendas_juros_am.insert(0, self.format_per_fx(Vendas_juros_am))
        self.entry_vendas_entrada.insert(0, self.format_per_fx(Vendas_per_entrada))
        self.entry_vendas_nr_parcelas_entrada.insert(0, self.format_x_fx(Vendas_parcela_entrada))
        self.entry_vendas_reforcos.insert(0, self.format_per_fx(Vendas_per_reforcos))
        self.entry_vendas_nr_parcelas_reforcos.insert(0, self.format_x_fx(Vendas_parcela_reforcos))
        self.entry_vendas_period_reforcos.insert(0, self.format_mes_fx(Vendas_periodicidade_reforcos))
        self.entry_vendas_per_avista.insert(0, self.format_per_fx(Vendas_per_avista))
        self.entry_vendas_inicio.insert(0, f"{Vendas_inicio} º mês")
        self.entry_vendas_curva.insert(0, str(Vendas_curva))
        self.entry_vendas_parcela_price.insert(0, self.format_valor_fx(Vendas_parcela_price))
        self.entry_vendas_parcela_sacoc.insert(0, self.format_valor_fx(Vendas_parcela_sacoc))
        
        self.entry_projetos_per_obra.insert(0, self.format_per_fx(Projetos_per_obra))
        self.entry_projetos_valor_total.insert(0, self.format_valor_fx(Projetos_Valor))
        self.entry_projetos_inicio_desembolso.insert(0, f"{Projetos_inicio} º mês")
        self.entry_projetos_curva_projeto.insert(0, str(Projetos_curva))

        self.entry_mkt_per_vgv.insert(0, self.format_per_fx(MkT_per_vgv))
        self.entry_mkt_valor_total.insert(0, self.format_valor_fx(MkT_Valor))
        self.entry_mkt_inicio_desembolso.insert(0, f"{MkT_inicio} º mês")
        self.entry_mkt_curva_mkt.insert(0, str(MkT_curva))

        self.entry_overhead_per_vgv.insert(0, self.format_per_fx(Adm_per_receita))
        self.entry_overhead_valor_total.insert(0, self.format_valor_fx(Adm_Valor))
        self.entry_overhead_inicio_desembolso.insert(0, f"{Adm_Inicio} º mês")
        self.entry_overhead_curva_overhead.insert(0, str(Adm_Curva))

        self.entry_obras_valor_m2.insert(0, self.format_valor_fx(Obras_custo_m2))
        self.entry_obras_valor_total.insert(0, self.format_valor_fx(Obra_Valor))
        self.entry_obras_inicio_desembolso.insert(0, f"{Obras_inicio} º mês")
        self.entry_obras_curva_obras.insert(0, str(Obras_curva))

        self.entry_pos_obras_per_obras.insert(0, self.format_per_fx(Pos_Obra_per_obra))
        self.entry_pos_obras_valor_total.insert(0, self.format_valor_fx(Pos_Obra_Valor))
        self.entry_pos_obras_inicio_desembolso.insert(0, f"{Pos_Obra_Inicio} º mês")
        self.entry_pos_obras_curva_obras.insert(0, str(Pos_Obra_curva))

        self.entry_adm_per_obras.insert(0, self.format_per_fx(AdmObra_per_obra))
        self.entry_adm_valor_total.insert(0, self.format_valor_fx(AdmObra_Valor))
        if AdmObra_Inicio == []:
            self.entry_adm_inicio_desembolso.insert(0, f"{Obras_inicio} º mês")
        else:
             self.entry_adm_inicio_desembolso.insert(0, f"{AdmObra_Inicio} º mês")
        
        if AdmObra_curva == []:
            self.entry_adm_curva_obras.insert(0, str(Obras_curva))
        else:
            self.entry_adm_curva_obras.insert(0, str(AdmObra_curva))

        self.entry_financiamento_valor_captacao.insert(0, self.format_valor_fx(Financiamento_valor))
        self.entry_financiamento_sistema_amortizacao.insert(0, str(Financiamento_sistema_amortizacao))
        self.entry_financiamento_prazo_amortizacao.insert(0, self.format_x_fx(Financiamento_prazo_amortizacao))
        self.entry_financiamento_inicio_amortizacao.insert(0, f"{Financiamento_inicio_amortizacao} º mês")
        self.entry_financiamento_inicio_pagto_juros.insert(0, f"{Financiamento_inicio_pagto_juros} º mês")
        self.entry_financiamento_juros.insert(0, self.format_valor_fx(Financiamento_juros))
        self.entry_financiamento_juros_aa.insert(0, self.format_per_fx(Financiamento_taxa))
        self.entry_financiamento_inicio_liberacao.insert(0, f"{Financiamento_liberacao} º mês")
        self.entry_financiamento_curva_liberacao.insert(0, str(Financiamento_curva))
        if Financiamento_financiador == 'S':
            self.entry_financiamento_financiador.set(str('Sim'))
        elif Financiamento_financiador == 'N':
            self.entry_financiamento_financiador.set(str('Não'))
        else:
            self.entry_financiamento_financiador.set(str(Financiamento_financiador))

        self.entry_dre_vgv_bruto.insert(0, self.format_valor_fx(DrE_VGV_bruto))
        self.entry_dre_comissao.insert(0, self.format_valor_fx(DrE_comissao))
        self.entry_dre_vgv_liquido.insert(0, self.format_valor_fx(DrE_VGV_liquido))
        self.entry_dre_impostos.insert(0, self.format_valor_fx(DrE_impostos))
        self.entry_dre_comissao_negocio.insert(0, self.format_valor_fx(DrE_comissao_negocios))
        self.entry_dre_receita_liquida.insert(0, self.format_valor_fx(DrE_receita_liquida))
        self.entry_dre_vgv_parceiro.insert(0, self.format_valor_fx(DrE_VGV_parceiro))
        self.entry_dre_receita_liquida_urbanizadora.insert(0, self.format_valor_fx(DrE_receita_liquida_urbanizadora))

        self.entry_dre_ebtda_valor.insert(0, self.format_valor_fx(DrE_ebtda_valor))
        self.entry_dre_ebtda_per.insert(0, self.format_per_fx(DrE_ebtda_per))
        self.entry_indicadores_tir_aa.insert(0, self.format_per_fx(Tir))
        self.entry_indicadores_tir_am.insert(0, self.format_per_fx(indicadores_tir_am))
        self.entry_indicadores_payback.insert(0, self.format_ano_fx(Payback))
        self.entry_indicadores_multiplicador_investimento.insert(0, self.format_valor_fx(Multiplicador))
        self.entry_indicadores_exposicaomax_caixa.insert(0, self.format_valor_fx(ExposicaoMax))
        self.entry_indicadores_vpl_urbanizadora.insert(0, self.format_valor_fx(Vpl_Urb))
        self.entry_indicadores_vpl_parceiro.insert(0, self.format_valor_fx(Vpl_Parceiro))
        self.entry_taxa_desconto.insert(0, self.format_per_fx(Desconto_VpL_taxa))

        self.text_observacoes.insert('1.0', str(Observacao))
        
        self.entry_informacoes_status.insert(0, str(Status_Prospeccao))
        self.entry_informacoes_anexos.insert(0, str(Anexos))
        self.entry_informacoes_data.insert(0, str(Dta_Contrato.strftime('%d/%m/%Y')))
        self.entry_informacoes_unidade_negocio.insert(0, str(Unidade))
        self.entry_informacoes_https.insert(0, str(Http))
        self.entry_informacoes_maps.insert(0, str(informacoes_maps))

Simulador_Estudos_Rel()