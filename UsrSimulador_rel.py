from imports import *
from widgets import Widgets
################# criando janela ###############
class Simulador_Estudos_Rel(Widgets):

    def simulador_estudos_rel(self, ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        self.janela_simulador_rel = customtkinter.CTkToplevel(self.window_one)
        self.janela_simulador_rel.title('Simulador de Estudos de Negócios')
        width = self.janela_simulador_rel.winfo_screenwidth()
        height = self.janela_simulador_rel.winfo_screenheight()
        self.janela_simulador_rel.geometry(f"{width}x{height}+0+0") 
        self.janela_simulador_rel.resizable(True, True)
        self.janela_simulador_rel.lift()  # Traz a janela para frente   
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_simulador_rel.protocol("WM_DELETE_WINDOW", self.on_closing_tela_negocios)

        self.frame_dados_rel(self.janela_simulador_rel)
        self.frame_novosnegocios(self.janela_simulador_rel, ID_Empresa, DS_Empresa, UF, Cidade)
        self.frame_carregar_dados(self.janela_simulador_rel, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)

        self.janela_simulador_rel.focus_force()
        self.janela_simulador_rel.grab_set()

    def frame_dados_rel(self, janela):
        # Empresa
        coordenadas_relx=0
        coordenadas_rely=0.01
        coordenadas_relwidth=0.34
        coordenadas_relheight=0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []
        
        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_uf))
        
       
        # Estado
        coordenadas_relx=0.34
        coordenadas_rely=0.01
        coordenadas_relwidth=0.06
        coordenadas_relheight=0.07
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
        coordenadas_relx=0.40
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        fr_municipio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_municipio.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_municipio = customtkinter.CTkLabel(fr_municipio, text="Município")
        lb_municipio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        municipios = self.get_municipios( self.entry_uf.get())
        
        self.entry_municipio = AutocompleteCombobox(fr_municipio, width=30, font=('Times', 11), completevalues=municipios)
        self.entry_municipio.pack()
        self.entry_municipio.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_municipio.bind("<Button-1>", lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind('<Down>', lambda event: self.atualizar_municipio(event, self.entry_uf.get(), self.entry_municipio))
        self.entry_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tpo_projeto))

        # Tipo do Projeto
        coordenadas_relx=0.60
        coordenadas_rely=0.01
        coordenadas_relwidth=0.20
        coordenadas_relheight=0.07
        fr_tpo_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_tpo_projeto = customtkinter.CTkLabel(fr_tpo_projeto, text="Tipo do Projeto")
        lb_tpo_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        tpo_projeto = self.get_tpo_projetos()
        tpo_projeto = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in tpo_projeto]

        self.entry_tpo_projeto = AutocompleteCombobox(fr_tpo_projeto, width=30, font=('Times', 11), completevalues=tpo_projeto)
        self.entry_tpo_projeto.pack()
        self.entry_tpo_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_tpo_projeto.bind("<Button-1>", lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind('<Down>', lambda event: self.atualizar_tpo_projeto(self, self.entry_tpo_projeto))
        self.entry_tpo_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nome_cenario))
        
        
        # Nome do Projeto
        coordenadas_relx=0.80
        coordenadas_rely=0.01
        coordenadas_relwidth=0.15
        coordenadas_relheight=0.07
        fr_nome_cenario = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_nome_cenario.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_nome_cenario = customtkinter.CTkLabel(fr_nome_cenario, text="Nome do Cenário")
        lb_nome_cenario.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        nome_cenario = []
        self.entry_nome_cenario = AutocompleteCombobox(fr_nome_cenario, width=30, font=('Times', 11), completevalues=nome_cenario)
        self.entry_nome_cenario.pack()
        self.entry_nome_cenario.place(relx=0.01, rely=0.5, relwidth=0.95, relheight=0.4)
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
        self.entry_nome_cenario.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_area_total))

        # Icon de Consulta
        coordenadas_relx = 0.95
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.05
        coordenadas_relheight = 0.07
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar = customtkinter.CTkButton(
                                                    janela,  
                                                    text='',
                                                    image=icon_image, 
                                                    fg_color='transparent', 
                                                    command=lambda: [self.consultar_simulacao(janela)]
                                                        )
        
        self.btn_consultar.pack()
        self.btn_consultar.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.btn_consultar.bind("<Return>", lambda event: self.btn_consultar.invoke())
        
        # Icon Processar
        coordenadas_relx = 0.90
        coordenadas_rely = 0.90
        coordenadas_relwidth = 0.10
        coordenadas_relheight = 0.07
        icon_image = self.base64_to_photoimage('save')
        self.btn_processar = customtkinter.CTkButton(
                                                    janela, 
                                                    text='',
                                                    image=icon_image, 
                                                    fg_color='transparent', 
                                                    command=lambda: [self.Fluxo_Caixa(
                                                                                    self.obter_Empresa_ID(self.entry_empresa.get()), 
                                                                                    self.entry_uf.get(), 
                                                                                    self.entry_municipio.get(), 
                                                                                    self.entry_tpo_projeto.get(),
                                                                                    self.entry_nome_cenario.get(),
                                                                                    self.janela_simulador_rel
                                                                                    )
                                                                    ]
                                                    ) 
        self.btn_processar.pack()
        self.btn_processar.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.btn_processar.bind("<Return>", lambda event: self.btn_processar.invoke())

    def frame_carregar_dados(self, janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        self.consultar_simulacao(janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)

    def consultar_simulacao(self, janela, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        
        if  Nome_da_Area != '':
            self.lista = self.Consulta_Negocio(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
            if self.lista == []:
                messagebox.showinfo("Informação", "Nenhum negócio encontrado.", parent=janela)
            
            self.limpar_simulador_negocios()
            
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
            self.entry_empresa.set(Empresa_DS)
            self.entry_uf.set(UF.upper())
            self.entry_municipio.set(Cidade)
            self.entry_tpo_projeto.set(Tipo)
            self.entry_nome_cenario.set(Nome_da_Area) 
            
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
            
            # # Preenche os campos Inserir os dados
            self.entry_area_total.insert(0, self.format_m2_fx(Area_Total))  
            self.entry_area_aproveitamento.insert(0, self.format_per_fx(Per_Area_Aproveitada))
            
            self.entry_area_aproveitado.insert(0, self.format_m2_fx(Area_Aproveitada))
            if Medidas_Lote is not None:
                self.entry_area_lote_padrao.insert(0, str(Medidas_Lote))
            else:
                self.entry_area_lote_padrao.insert(0, str(''))
                
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
            if Investimento_Area_Inicio == 0:
                self.entry_investimento_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_investimento_inicio_desembolso.insert(0, f"{Investimento_Area_Inicio} º mês")
            
            if Investimento_Area_Curva is not None:
                self.entry_investimento_curva_investimento.insert(0, str(Investimento_Area_Curva))
            else:
                self.entry_investimento_curva_investimento.insert(0, str('Padrão 1 Mês'))
            
            if Investimento_Aporte is not None:
                if Investimento_Aporte == 'S':
                    self.entry_investimento_aporte.set(str('Sim'))
                elif Investimento_Aporte == 'N':
                    self.entry_investimento_aporte.set(str('Não'))
                else:
                    self.entry_investimento_aporte.set(str(Investimento_Aporte))
            else:
                self.entry_investimento_aporte.set(str('Não'))

            self.entry_adto_parceiro_valor.insert(0, self.format_valor_fx(Adto_Parceiro_Valor))
            self.entry_adto_parceiro_per_urbanizadora.insert(0, self.format_per_fx(Adto_Parceiro_Urb_Juros))
            self.entry_adto_parceiro_per_parceiro.insert(0, self.format_per_fx(Adto_Parceiro_Per_Juros))
            if Adto_Parceiro_Inicio == 0:
                self.entry_adto_parceiro_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_adto_parceiro_inicio_desembolso.insert(0, f"{Adto_Parceiro_Inicio} º mês")
            
            if Adto_Parceiro_Curva is not None:
                self.entry_adto_parceiro_curva_adto.insert(0, str(Adto_Parceiro_Curva))
            else:
                self.entry_adto_parceiro_curva_adto.insert(0, str('Padrão 1 Mês'))

            self.entry_vendas_preco_m2.insert(0, self.format_valor_fx(Valor_m2_sem_comissao))
            self.entry_vendas_comissao_per.insert(0, self.format_per_fx(Vendas_comissao_per))
            self.entry_vendas_vendas_preco_m2_com_comissao.insert(0, self.format_valor_fx(Vendas_Valor_com_comissao_m2))
            self.entry_vendas_lote_medio.insert(0, self.format_valor_fx(Vendas_Tickt_Medio))
            if not Vendas_prazo_financiamento:
                self.entry_vendas_financiamento_prazo.insert(0, self.format_x_fx(1))
            else:
                self.entry_vendas_financiamento_prazo.insert(0, self.format_x_fx(Vendas_prazo_financiamento))

            if Vendas_sistema_amortizacao is not None:
                self.entry_vendas_sistema_amortizacao.insert(0, str(Vendas_sistema_amortizacao))
            else:
                self.entry_vendas_sistema_amortizacao.insert(0, str('PRICE'))

            self.entry_vendas_juros_aa.insert(0, self.format_per_fx(Vendas_juros_taxa))
            self.entry_vendas_juros_am.insert(0, self.format_per_fx(Vendas_juros_am))
            self.entry_vendas_entrada.insert(0, self.format_per_fx(Vendas_per_entrada))
            if Vendas_parcela_entrada == 0:
                self.entry_vendas_nr_parcelas_entrada.insert(0, self.format_x_fx(1))
            else:
                self.entry_vendas_nr_parcelas_entrada.insert(0, self.format_x_fx(Vendas_parcela_entrada))

            self.entry_vendas_reforcos.insert(0, self.format_per_fx(Vendas_per_reforcos))
            if Vendas_parcela_reforcos == 0:
                self.entry_vendas_nr_parcelas_reforcos.insert(0, self.format_x_fx(1))
            else:
                self.entry_vendas_nr_parcelas_reforcos.insert(0, self.format_x_fx(Vendas_parcela_reforcos))

            if Vendas_periodicidade_reforcos == 0:
                self.entry_vendas_period_reforcos.insert(0, f"{12} º mês")
            else:
                self.entry_vendas_period_reforcos.insert(0, self.format_mes_fx(Vendas_periodicidade_reforcos))

            self.entry_vendas_per_avista.insert(0, self.format_per_fx(Vendas_per_avista))
            if Vendas_inicio == 0:
                self.entry_vendas_inicio.insert(0, f"{1} º mês")
            else:
                self.entry_vendas_inicio.insert(0, f"{Vendas_inicio} º mês")
            
            if Vendas_curva is not None:
                self.entry_vendas_curva.insert(0, str(Vendas_curva))
            else:
                self.entry_vendas_curva.insert(0, str('Padrão 1 Mês'))
            self.entry_vendas_parcela_price.insert(0, self.format_valor_fx(Vendas_parcela_PRICE))
            self.entry_vendas_parcela_sacoc.insert(0, self.format_valor_fx(Vendas_parcela_sacoc))
            
            self.entry_projetos_per_obra.insert(0, self.format_per_fx(Projetos_per_obra))
            self.entry_projetos_valor_total.insert(0, self.format_valor_fx(Projetos_Valor))
            if Projetos_inicio == 0:
                self.entry_projetos_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_projetos_inicio_desembolso.insert(0, f"{Projetos_inicio} º mês")

            if Projetos_curva is not None:
                self.entry_projetos_curva_projeto.insert(0, str(Projetos_curva))
            else:
                self.entry_projetos_curva_projeto.insert(0, str('Padrão 1 Mês'))

            self.entry_mkt_per_vgv.insert(0, self.format_per_fx(MkT_per_vgv))
            self.entry_mkt_valor_total.insert(0, self.format_valor_fx(MkT_Valor))
            if MkT_inicio == 0:
                self.entry_mkt_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_mkt_inicio_desembolso.insert(0, f"{MkT_inicio} º mês")
            
            if MkT_curva is not None:
                self.entry_mkt_curva_mkt.insert(0, str(MkT_curva))
            else:
                self.entry_mkt_curva_mkt.insert(0, str('Padrão 1 Mês'))
 
            self.entry_overhead_per_vgv.insert(0, self.format_per_fx(Adm_per_receita))
            self.entry_overhead_valor_total.insert(0, self.format_valor_fx(Adm_Valor))
            if Adm_Inicio == 0:
                self.entry_overhead_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_overhead_inicio_desembolso.insert(0, f"{Adm_Inicio} º mês")
            
            if Adm_Curva is not None:
                self.entry_overhead_curva_overhead.insert(0, str(Adm_Curva))
            else:
                self.entry_overhead_curva_overhead.insert(0, str('Padrão 1 Mês'))
   
            self.entry_obras_valor_m2.insert(0, self.format_valor_fx(Obras_custo_m2))
            self.entry_obras_valor_total.insert(0, self.format_valor_fx(Obra_Valor))
            if Obras_inicio == 0:
                self.entry_obras_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_obras_inicio_desembolso.insert(0, f"{Obras_inicio} º mês")

            if Obras_curva is not None:
                self.entry_obras_curva_obras.insert(0, str(Obras_curva))
            else:
                self.entry_obras_curva_obras.insert(0, str('Padrão 1 Mês'))
         
            self.entry_pos_obras_per_obras.insert(0, self.format_per_fx(Pos_Obra_per_obra))
            self.entry_pos_obras_valor_total.insert(0, self.format_valor_fx(Pos_Obra_Valor))
            if Pos_Obra_Inicio == 0:
                self.entry_pos_obras_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                self.entry_pos_obras_inicio_desembolso.insert(0, f"{Pos_Obra_Inicio} º mês")
            
            if Pos_Obra_curva is not None:
                self.entry_pos_obras_curva_obras.insert(0, str(Pos_Obra_curva))
            else:
                self.entry_pos_obras_curva_obras.insert(0, str('Padrão 1 Mês'))
            

            self.entry_adm_per_obras.insert(0, self.format_per_fx(AdmObra_per_obra))
            self.entry_adm_valor_total.insert(0, self.format_valor_fx(AdmObra_Valor))
            if AdmObra_Inicio == 0:
                self.entry_adm_inicio_desembolso.insert(0, f"{1} º mês")
            else:
                if AdmObra_Inicio == []:
                    self.entry_adm_inicio_desembolso.insert(0, f"{Obras_inicio} º mês")
                else:
                    self.entry_adm_inicio_desembolso.insert(0, f"{AdmObra_Inicio} º mês")
            
            if AdmObra_curva == []:
                self.entry_adm_curva_obras.insert(0, str(Obras_curva))
            else:
                self.entry_adm_curva_obras.insert(0, str(AdmObra_curva))

            self.entry_financiamento_valor_captacao.insert(0, self.format_valor_fx(Financiamento_valor))
            
            if Financiamento_sistema_amortizacao is not None:
                self.entry_financiamento_sistema_amortizacao.insert(0, str(Financiamento_sistema_amortizacao))
            else:
                self.entry_financiamento_sistema_amortizacao.insert(0, str('PRICE'))
            
            if not Financiamento_prazo_amortizacao:
                self.entry_financiamento_prazo_amortizacao.insert(0, self.format_x_fx(1))
            else:
                self.entry_financiamento_prazo_amortizacao.insert(0, self.format_x_fx(Financiamento_prazo_amortizacao))
            
            if Financiamento_inicio_amortizacao == 0:
                self.entry_financiamento_inicio_amortizacao.insert(0, f"{1} º mês")
            else:
                self.entry_financiamento_inicio_amortizacao.insert(0, f"{Financiamento_inicio_amortizacao} º mês")
            
            if Financiamento_inicio_pagto_juros == 0:
                self.entry_financiamento_inicio_pagto_juros.insert(0, f"{1} º mês")
            else:
                self.entry_financiamento_inicio_pagto_juros.insert(0, f"{Financiamento_inicio_pagto_juros} º mês")
            
            self.entry_financiamento_juros.insert(0, self.format_valor_fx(Financiamento_juros))
            self.entry_financiamento_juros_aa.insert(0, self.format_per_fx(Financiamento_taxa))
            
            if Financiamento_liberacao == 0:
                self.entry_financiamento_inicio_liberacao.insert(0, f"{1} º mês")
            else:
                self.entry_financiamento_inicio_liberacao.insert(0, f"{Financiamento_liberacao} º mês")
            
            if Financiamento_curva is not None:
                self.entry_financiamento_curva_liberacao.insert(0, str(Financiamento_curva))
            else:
                self.entry_financiamento_curva_liberacao.insert(0, str('Padrão 1 Mês'))
            
            if Financiamento_financiador is not None:
                if Financiamento_financiador == 'S':
                    self.entry_financiamento_financiador.set(str('Sim'))
                elif Financiamento_financiador == 'N':
                    self.entry_financiamento_financiador.set(str('Não'))
                else:
                    self.entry_financiamento_financiador.set(str(Financiamento_financiador))
            else:
                self.entry_financiamento_financiador.set(str('Não'))

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
            
            if Desconto_VpL_taxa == 0:
                self.entry_taxa_desconto.insert(0, self.format_per_fx(.12))
            else:
                self.entry_taxa_desconto.insert(0, self.format_per_fx(Desconto_VpL_taxa))
            
            if Observacao is not None:
                self.text_observacoes.insert('1.0', str(Observacao))
            
            if Status_Prospeccao is not None:
                self.entry_informacoes_status.insert(0, str(Status_Prospeccao))
            else:
                self.entry_informacoes_status.insert(0, '')

            if Anexos is not None:
                self.entry_informacoes_anexos.insert(0, str(Anexos))

            if Dta_Contrato is not None:
                self.entry_informacoes_data.insert(0, str(Dta_Contrato.strftime('%d/%m/%Y')))
            else:
                Dta_Contrato = datetime.now()
                self.entry_informacoes_data.insert(0, str(Dta_Contrato.strftime('%d/%m/%Y')))
                        
            self.entry_informacoes_unidade_negocio.insert(0, str(Unidade))
            
            if Http is not None:
                self.entry_informacoes_https.insert(0, str(Http))
            
            if informacoes_maps is not None:
                self.entry_informacoes_maps.insert(0, str(informacoes_maps))

    def frame_novosnegocios(self, janela, ID_Empresa, DS_Empresa, UF, Cidade):
        # Preenche Cabeçalho
        self.entry_empresa.set( DS_Empresa)
        self.entry_uf.set(UF.upper())
        self.entry_municipio.set(Cidade)
        
        # Área m2
        self.fr_area_m2 = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="yellow")
        self.fr_area_m2.place(relx=0, rely=0.08, relwidth=0.09, relheight=0.30)
        self.lb_area_m2 = customtkinter.CTkLabel(self.fr_area_m2, text="Área m²", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_area_m2.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.50)

        # Área Total
        self.lb_area_total = customtkinter.CTkLabel(self.fr_area_m2, text="Área Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_total.place(relx=0.01, rely=0.06,relheight=0.03, relwidth=0.97)
        self.entry_area_total = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_total.place(relx=0.01, rely=0.10, relwidth=0.97, relheight=0.1)

        self.entry_area_total.bind("<Return>", lambda event: self.format_m2(event, self.entry_area_total))
        self.entry_area_total.bind("<Return>", lambda event: self.format_dre)
        self.entry_area_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_area_aproveitamento))

        # Percentual Aproveitamento da Área
        self.lb_area_aproveitamento = customtkinter.CTkLabel(self.fr_area_m2, text="% Aproveitamento", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_aproveitamento.place(relx=0.01, rely=0.21, relheight=0.03, relwidth=0.97)
        self.entry_area_aproveitamento = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_aproveitamento.place( relx=0.01, rely=0.25, relwidth=0.97, relheight=0.1)

        self.entry_area_aproveitamento.bind("<Return>", lambda event: self.format_area_aproveitada(event))
        self.entry_area_aproveitamento.bind("<Return>", lambda event: self.format_dre(event))
        
        # Área Aproveitada
        self.lb_area_aproveitado = customtkinter.CTkLabel(self.fr_area_m2, text="m² Aproveitado", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_aproveitado.place(relx=0.01, rely=0.36, relheight=0.03, relwidth=0.97)
        self.entry_area_aproveitado = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_aproveitado.place(relx=0.01, rely=0.40, relwidth=0.97, relheight=0.1)
        # self.entry_area_aproveitado.configure(state="disabled")

        # Medidas do Lote Médio
        self.lb_area_lote_medio = customtkinter.CTkLabel(self.fr_area_m2, text="Lote Médio", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_lote_medio.place(relx=0.01, rely=0.66, relheight=0.03, relwidth=0.97)
        self.entry_area_lote_medio = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_lote_medio.place(relx=0.01, rely=0.70, relwidth=0.97, relheight=0.1)

        self.entry_area_lote_medio.bind("<KeyRelease>", lambda event: self.format_m2(event, self.entry_area_lote_medio))

        # Área do Lote Médio
        self.lb_area_aproveitado = customtkinter.CTkLabel(self.fr_area_m2, text="m² Lote Médio", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_aproveitado.place(relx=0.01, rely=0.51, relheight=0.03, relwidth=0.97)
        self.entry_area_lote_padrao = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_lote_padrao.place(relx=0.01, rely=0.55, relwidth=0.97, relheight=0.1)

        self.entry_area_lote_padrao.bind("<KeyRelease>", lambda event: self.format_medida_lote(event))
        self.entry_area_lote_padrao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_participacao_urbanizador))

        # Nr de Lotes
        self.lb_area_nr_lotes = customtkinter.CTkLabel(self.fr_area_m2, text="Nr. Lotes", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_area_nr_lotes.place(relx=0.01, rely=0.81, relheight=0.03, relwidth=0.97)
        self.entry_area_nr_lotes = customtkinter.CTkEntry(self.fr_area_m2, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_area_nr_lotes.place(relx=0.01, rely=0.85, relwidth=0.97, relheight=0.1)

        # Participação
        self.fr_participacao = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="yellow")
        self.fr_participacao.place(relx=0, rely=0.38, relwidth=0.09, relheight=0.43)
        self.lb_participacao = customtkinter.CTkLabel(self.fr_participacao, text="Participação", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_participacao.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.70)

        # % Urbanizador
        self.lb_participacao_urbanizador = customtkinter.CTkLabel(
            self.fr_participacao, text="% Urbanizador", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_participacao_urbanizador.place(
            relx=0.01, rely=0.06, relheight=0.03, relwidth=0.97)
        self.entry_participacao_urbanizador = customtkinter.CTkEntry(
            self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_participacao_urbanizador.place(
            relx=0.01, rely=0.10, relwidth=0.97, relheight=0.08)

        self.entry_participacao_urbanizador.bind("<Return>", lambda event: self.format_per_terreneiro(event))
        self.entry_participacao_urbanizador.bind("<Return>", lambda event: self.format_dre(event))

        # % Terreneiro
        self.lb_participacao_parceiro = customtkinter.CTkLabel(
            self.fr_participacao, text="% Parceiro", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_participacao_parceiro.place(
            relx=0.01, rely=0.19, relheight=0.03, relwidth=0.97)
        self.entry_participacao_parceiro = customtkinter.CTkEntry(
            self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_participacao_parceiro.place(
            relx=0.01, rely=0.23, relwidth=0.97, relheight=0.08)

        # % Permuta
        self.lb_participacao_permuta = customtkinter.CTkLabel(
            self.fr_participacao, text="% Permuta Física", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_participacao_permuta.place(relx=0.01, rely=0.32, relheight=0.03, relwidth=0.97)
        self.entry_participacao_permuta = customtkinter.CTkEntry(self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_participacao_permuta.place(relx=0.01, rely=0.36, relwidth=0.97, relheight=0.08)
        self.entry_participacao_permuta.bind("<Return>", lambda event: self.format_per(event, self.entry_participacao_permuta, self.entry_comissao_intermediacao))
        self.entry_participacao_permuta.bind("<Return>", lambda event: self.format_per_total_participacao(event))
        self.entry_participacao_permuta.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_participacao_permuta.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_comissao_intermediacao))

        # % Comissão
        self.lb_comissao_intermediacao = customtkinter.CTkLabel(
            self.fr_participacao, text="% Comissão", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_comissao_intermediacao.place(
            relx=0.01, rely=0.45, relheight=0.03, relwidth=0.97)
        self.entry_comissao_intermediacao = customtkinter.CTkEntry(
            self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_comissao_intermediacao.place(
            relx=0.01, rely=0.49, relwidth=0.97, relheight=0.08)
        self.entry_comissao_intermediacao.bind("<Return>", lambda event: self.format_per(event, self.entry_comissao_intermediacao, self.entry_admmkt_parceiro))
        self.entry_comissao_intermediacao.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_comissao_intermediacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_admmkt_parceiro))

        # % Adm./MkT
        self.lb_admmkt_parceiro = customtkinter.CTkLabel(self.fr_participacao, text="% Adm. MkT", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_admmkt_parceiro.place(relx=0.01, rely=0.58, relheight=0.03, relwidth=0.97)
        self.entry_admmkt_parceiro = customtkinter.CTkEntry(self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_admmkt_parceiro.place(relx=0.01, rely=0.62, relwidth=0.97, relheight=0.08)
        self.entry_admmkt_parceiro.bind("<Return>", lambda event: self.format_per_total_participacao(event))
        self.entry_admmkt_parceiro.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_admmkt_parceiro.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_investimento_valor))

        # % Total Urbanizadora
        self.lb_total_urbanizadora = customtkinter.CTkLabel(
            self.fr_participacao, text="% Total Urban.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_total_urbanizadora.place(
            relx=0.01, rely=0.71, relheight=0.03, relwidth=0.97)
        self.entry_total_urbanizadora = customtkinter.CTkEntry(
            self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_total_urbanizadora.place(
            relx=0.01, rely=0.75, relwidth=0.97, relheight=0.08)

        # Total Parceiro
        # % Total Parceiro
        self.lb_total_parceiro = customtkinter.CTkLabel(self.fr_participacao, text="% Total Parceiro", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_total_parceiro.place(relx=0.01, rely=0.84, relheight=0.03, relwidth=0.97)
        self.entry_total_parceiro = customtkinter.CTkEntry(self.fr_participacao, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_total_parceiro.place(relx=0.01, rely=0.88, relwidth=0.97, relheight=0.08)

        # Investimento
        self.fr_investimento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="orange")
        self.fr_investimento.place(relx=0.091, rely=0.08, relwidth=0.09, relheight=0.20)
        self.lb_investimento = customtkinter.CTkLabel(self.fr_investimento, text="Investimento", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_investimento.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.70)

        self.lb_investimento_valor = customtkinter.CTkLabel(
            self.fr_investimento, text="Valor", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_investimento_valor.place(
            relx=0.01, rely=0.09, relheight=0.05, relwidth=0.97)
        self.entry_investimento_valor = customtkinter.CTkEntry(
            self.fr_investimento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_investimento_valor.place(
            relx=0.005, rely=0.15, relwidth=0.97, relheight=0.15)
        self.entry_investimento_valor.bind("<Return>", lambda event: self.format_valor(event, self.entry_investimento_valor))
        self.entry_investimento_valor.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_investimento_valor.bind("<Return>", lambda event: self.muda_barrinha(
            event, self.entry_investimento_inicio_desembolso))

        self.lb_investimento_inicio_desembolso = customtkinter.CTkLabel(self.fr_investimento, text="Início Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_investimento_inicio_desembolso.place(relx=0.01, rely=0.315, relheight=0.05, relwidth=0.97)
        self.entry_investimento_inicio_desembolso = customtkinter.CTkEntry(self.fr_investimento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_investimento_inicio_desembolso.place(relx=0.005, rely=0.375, relwidth=0.97, relheight=0.15)
        self.entry_investimento_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_investimento_inicio_desembolso))
        self.entry_investimento_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_investimento_curva_investimento))
        
        self.lb_investimento_curva_investimento = customtkinter.CTkLabel(self.fr_investimento, text="Curva de Investimento", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_investimento_curva_investimento.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.97)
        self.nome_curva = []
        self.entry_investimento_curva_investimento = AutocompleteCombobox(self.fr_investimento, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_investimento_curva_investimento.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_investimento_curva_investimento.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_investimento_curva_investimento))
        self.entry_investimento_curva_investimento.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_investimento_curva_investimento))
        self.entry_investimento_curva_investimento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_investimento_aporte))

        self.lb_investimento_aporte = customtkinter.CTkLabel(self.fr_investimento, text="Aporte?", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_investimento_aporte.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.97)
        self.opcoes = ["Não", "Sim"]
        self.entry_investimento_aporte = customtkinter.CTkComboBox(self.fr_investimento, fg_color="black", text_color="white", justify=tk.RIGHT, values=self.opcoes)
        self.entry_investimento_aporte.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_investimento_aporte.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adto_parceiro_valor))

        # Adto Parceiro
        self.fr_adto_parceiro = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="orange")
        self.fr_adto_parceiro.place(relx=0.091, rely=0.28, relwidth=0.09, relheight=0.28)
        self.lb_adto_parceiro = customtkinter.CTkLabel(self.fr_adto_parceiro, text="Adto Parceiro", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_adto_parceiro.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

        self.lb_adto_parceiro_valor = customtkinter.CTkLabel(self.fr_adto_parceiro, text="Valor", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adto_parceiro_valor.place(relx=0.01, rely=0.06, relheight=0.05, relwidth=0.97)
        self.entry_adto_parceiro_valor = customtkinter.CTkEntry(self.fr_adto_parceiro, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adto_parceiro_valor.place(relx=0.005, rely=0.12, relwidth=0.97, relheight=0.114)
        self.entry_adto_parceiro_valor.bind("<Return>", lambda event: self.format_valor(event, self.entry_adto_parceiro_valor))
        self.entry_adto_parceiro_valor.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adto_parceiro_per_urbanizadora))
        
        self.lb_adto_parceiro_per_urbanizadora = customtkinter.CTkLabel(self.fr_adto_parceiro, text="% Amort.(Repasse)", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adto_parceiro_per_urbanizadora.place(relx=0.01, rely=0.25, relheight=0.05, relwidth=0.97)
        self.entry_adto_parceiro_per_urbanizadora = customtkinter.CTkEntry(self.fr_adto_parceiro, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adto_parceiro_per_urbanizadora.place(relx=0.005, rely=0.31, relwidth=0.97, relheight=0.114)
        self.entry_adto_parceiro_per_urbanizadora.bind("<Return>", lambda event: self.format_per(event, self.entry_adto_parceiro_per_urbanizadora, self.entry_adto_parceiro_per_parceiro))

        self.lb_adto_parceiro_per_parceiro = customtkinter.CTkLabel(self.fr_adto_parceiro, text="% a.a. (Par.)", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adto_parceiro_per_parceiro.place(relx=0.01, rely=0.44, relheight=0.05, relwidth=0.97)
        self.entry_adto_parceiro_per_parceiro = customtkinter.CTkEntry(self.fr_adto_parceiro, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adto_parceiro_per_parceiro.place(relx=0.005, rely=0.50, relwidth=0.97, relheight=0.114)
        self.entry_adto_parceiro_per_parceiro.bind("<Return>", lambda event: self.format_per(event, self.entry_adto_parceiro_per_parceiro, self.entry_adto_parceiro_inicio_desembolso))
        
        self.lb_adto_parceiro_inicio_desembolso = customtkinter.CTkLabel(self.fr_adto_parceiro, text="Início Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adto_parceiro_inicio_desembolso.place(relx=0.01, rely=0.63, relheight=0.05, relwidth=0.97)
        self.entry_adto_parceiro_inicio_desembolso = customtkinter.CTkEntry(self.fr_adto_parceiro, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adto_parceiro_inicio_desembolso.place(relx=0.005, rely=0.69, relwidth=0.97, relheight=0.114)
        self.entry_adto_parceiro_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_adto_parceiro_inicio_desembolso))
        self.entry_adto_parceiro_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adto_parceiro_curva_adto))

        self.lb_adto_parceiro_curva_adto = customtkinter.CTkLabel(self.fr_adto_parceiro, text="Curva Adto", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adto_parceiro_curva_adto.place(relx=0.01, rely=0.82, relheight=0.05, relwidth=0.97)
        self.nome_curva = []
        self.entry_adto_parceiro_curva_adto = AutocompleteCombobox(self.fr_adto_parceiro, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_adto_parceiro_curva_adto.place(relx=0.005, rely=0.88, relwidth=0.97, relheight=0.114)
        self.entry_adto_parceiro_curva_adto.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_adto_parceiro_curva_adto))
        self.entry_adto_parceiro_curva_adto.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_adto_parceiro_curva_adto))
        self.entry_adto_parceiro_curva_adto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_preco_m2))

        # Preço de Venda m2
        self.fr_vendas = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="#006400")
        self.fr_vendas.place(relx=0.181, rely=0.08,relwidth=0.18, relheight=0.48)
        self.lb_vendas = customtkinter.CTkLabel(self.fr_vendas, text="Vendas", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_vendas.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.50)

        # Preços e Comissões
        self.fr_precos_comissoes = customtkinter.CTkFrame(self.fr_vendas, border_color="gray75", border_width=1, fg_color="#006400")
        self.fr_precos_comissoes.place(relx=0.005, rely=0.03, relwidth=0.495, relheight=0.47)
        self.lb_precos_comissoes = customtkinter.CTkLabel(self.fr_precos_comissoes, text="Preços e Comissões", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_precos_comissoes.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.70)

        self.lb_vendas_preco_m2 = customtkinter.CTkLabel(self.fr_precos_comissoes, text="Valor m²", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_preco_m2.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_vendas_preco_m2 = customtkinter.CTkEntry(self.fr_precos_comissoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_preco_m2.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_vendas_preco_m2.bind("<Return>", lambda event: self.format_valor(event, self.entry_vendas_preco_m2))
        self.entry_vendas_preco_m2.bind("<Return>", lambda event: self.format_preco_comissao(event))
        self.entry_vendas_preco_m2.bind("<Return>", lambda event: self.format_pmt(event))
        
        self.entry_vendas_preco_m2.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_vendas_preco_m2.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_comissao_per))

        self.lb_vendas_comissao_per = customtkinter.CTkLabel(self.fr_precos_comissoes, text="% Comissão", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_comissao_per.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.97)
        self.entry_vendas_comissao_per = customtkinter.CTkEntry(self.fr_precos_comissoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_comissao_per.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_vendas_comissao_per.bind("<Return>", lambda event: self.format_per(event, self.entry_vendas_comissao_per, self.entry_vendas_financiamento_prazo))
        self.entry_vendas_comissao_per.bind("<Return>", lambda event: self.format_preco_comissao(event))
        self.entry_vendas_comissao_per.bind("<Return>", lambda event: self.format_pmt(event))
        self.entry_vendas_comissao_per.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_vendas_vendas_preco_m2_com_comissao = customtkinter.CTkLabel(self.fr_precos_comissoes, text="$ m² c/com.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_vendas_preco_m2_com_comissao.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.97)
        self.entry_vendas_vendas_preco_m2_com_comissao = customtkinter.CTkEntry(self.fr_precos_comissoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_vendas_preco_m2_com_comissao.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        
        self.lb_vendas_lote_medio = customtkinter.CTkLabel(self.fr_precos_comissoes, text="$ Lote Médio", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_lote_medio.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.97)
        self.entry_vendas_lote_medio = customtkinter.CTkEntry(self.fr_precos_comissoes, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_lote_medio.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)

        # Financiamento
        self.fr_financiamento = customtkinter.CTkFrame(self.fr_vendas, border_color="gray75", border_width=1, fg_color="#006400")
        self.fr_financiamento.place(relx=0.505, rely=0.03, relwidth=0.495, relheight=0.47)
        self.lb_financiamento = customtkinter.CTkLabel(self.fr_financiamento, text="Financiamento", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_financiamento.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_vendas_financiamento_prazo = customtkinter.CTkLabel(self.fr_financiamento, text="Prazo Financiamento", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_financiamento_prazo.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_vendas_financiamento_prazo = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_financiamento_prazo.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_vendas_financiamento_prazo.bind("<Return>", lambda event: self.format_x(event, self.entry_vendas_financiamento_prazo))
        self.entry_vendas_financiamento_prazo.bind("<Return>", lambda event: self.format_pmt(event))
        self.entry_vendas_financiamento_prazo.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_sistema_amortizacao))

        self.lb_vendas_sistema_amortizacao = customtkinter.CTkLabel(self.fr_financiamento, text="Sistema Amort.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_sistema_amortizacao.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.70)
        self.nome_sistema_amortizacao = []
        self.entry_vendas_sistema_amortizacao = AutocompleteCombobox(self.fr_financiamento, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_sistema_amortizacao)
        self.entry_vendas_sistema_amortizacao.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_vendas_sistema_amortizacao.bind("<Button-1>", lambda event: self.atualizar_sistema_amortizacao(event, self.entry_vendas_sistema_amortizacao))
        self.entry_vendas_sistema_amortizacao.bind("<Return>", lambda event: self.muda_barrinha(event,  self.entry_vendas_juros_aa))

        self.lb_vendas_juros_aa = customtkinter.CTkLabel(self.fr_financiamento, text="% a.a.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_juros_aa.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.30)
        self.entry_vendas_juros_aa = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_juros_aa.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_vendas_juros_aa.bind("<Return>", lambda event: self.format_per(event, self.entry_vendas_juros_aa, self.entry_vendas_entrada))
        self.entry_vendas_juros_aa.bind("<Return>", lambda event: self.format_juros_am(event, self.entry_vendas_juros_am, self.entry_vendas_juros_aa))
        self.entry_vendas_juros_aa.bind("<Return>", lambda event: self.format_pmt(event))

        self.lb_vendas_juros_am = customtkinter.CTkLabel(self.fr_financiamento, text="% a.m.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_juros_am.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.30)
        self.entry_vendas_juros_am = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_juros_am.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)

        # Política de Vendas
        self.fr_politica_vendas = customtkinter.CTkFrame(
            self.fr_vendas, border_color="gray75", border_width=1, fg_color="#006400")
        self.fr_politica_vendas.place(
            relx=0.005, rely=0.505, relwidth=0.99, relheight=0.49)
        self.lb_politica_vendas = customtkinter.CTkLabel(
            self.fr_politica_vendas, text="Política de Vendas", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_politica_vendas.place(
            relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_vendas_entrada = customtkinter.CTkLabel(self.fr_politica_vendas, text="% Entrada", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_entrada.place(relx=0.01, rely=0.06, relheight=0.05, relwidth=0.47)
        self.entry_vendas_entrada = customtkinter.CTkEntry(self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_entrada.place(relx=0.005, rely=0.12, relwidth=0.49, relheight=0.114)
        self.entry_vendas_entrada.bind("<Return>", lambda event: self.format_per(event, self.entry_vendas_entrada, self.entry_vendas_nr_parcelas_entrada))
        self.entry_vendas_entrada.bind("<Return>", lambda event: self.format_pmt(event))
        
        self.lb_vendas_nr_parcelas_entrada = customtkinter.CTkLabel(self.fr_politica_vendas, text="Nr. Parcelas", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_nr_parcelas_entrada.place(relx=0.51, rely=0.06, relheight=0.05, relwidth=0.47)
        self.entry_vendas_nr_parcelas_entrada = customtkinter.CTkEntry(self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_nr_parcelas_entrada.place(relx=0.505, rely=0.12, relwidth=0.49, relheight=0.114)
        self.entry_vendas_nr_parcelas_entrada.bind("<Return>", lambda event: self.format_x(event, self.entry_vendas_nr_parcelas_entrada))
        self.entry_vendas_nr_parcelas_entrada.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_reforcos))

        self.lb_vendas_reforcos = customtkinter.CTkLabel(self.fr_politica_vendas, text="% Reforços", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_reforcos.place(relx=0.01, rely=0.2440, relheight=0.05, relwidth=0.47)
        self.entry_vendas_reforcos = customtkinter.CTkEntry(self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_reforcos.place(relx=0.005, rely=0.3040, relwidth=0.49, relheight=0.114)
        self.entry_vendas_reforcos.bind("<Return>", lambda event: self.format_per(event, self.entry_vendas_reforcos, self.entry_vendas_nr_parcelas_reforcos))
        self.entry_vendas_reforcos.bind("<Return>", lambda event: self.format_pmt(event))
        
        self.lb_vendas_nr_parcelas_reforcos = customtkinter.CTkLabel(self.fr_politica_vendas, text="Nr. Reforços", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_nr_parcelas_reforcos.place(relx=0.51, rely=0.2440, relheight=0.05, relwidth=0.47)
        self.entry_vendas_nr_parcelas_reforcos = customtkinter.CTkEntry(self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_nr_parcelas_reforcos.place(relx=0.505, rely=0.3040, relwidth=0.49, relheight=0.114)
        self.entry_vendas_nr_parcelas_reforcos.bind("<Return>", lambda event: self.format_x(event, self.entry_vendas_nr_parcelas_reforcos))
        self.entry_vendas_nr_parcelas_reforcos.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_period_reforcos))

        self.lb_vendas_period_reforcos = customtkinter.CTkLabel(self.fr_politica_vendas, text="Period. Reforços", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_period_reforcos.place(relx=0.01, rely=0.4280, relheight=0.05, relwidth=0.97)
        self.entry_vendas_period_reforcos = customtkinter.CTkEntry(self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_period_reforcos.place(relx=0.005, rely=0.4880, relwidth=0.49, relheight=0.114)
        self.entry_vendas_period_reforcos.bind("<Return>", lambda event: self.format_mes(event, self.entry_vendas_period_reforcos))
        self.entry_vendas_period_reforcos.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_per_avista))

        self.lb_vendas_per_avista = customtkinter.CTkLabel(
            self.fr_politica_vendas, text="% Venda aVista", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_per_avista.place(
            relx=0.51, rely=0.4280, relheight=0.05, relwidth=0.30)
        self.entry_vendas_per_avista = customtkinter.CTkEntry(
            self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_per_avista.place(
            relx=0.505, rely=0.4880, relwidth=0.49, relheight=0.114)
        self.entry_vendas_per_avista.bind("<Return>", lambda event: self.format_per(event, self.entry_vendas_per_avista, self.entry_vendas_inicio))
        
        self.lb_vendas_inicio = customtkinter.CTkLabel(
            self.fr_politica_vendas, text="Início Vendas", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_inicio.place(
            relx=0.01, rely=0.6120, relheight=0.05, relwidth=0.97)
        self.entry_vendas_inicio = customtkinter.CTkEntry(
            self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_inicio.place(
            relx=0.005, rely=0.6720, relwidth=0.49, relheight=0.114)
        self.entry_vendas_inicio.bind("<Return>", lambda event: self.format_mes(event, self.entry_vendas_inicio))
        self.entry_vendas_inicio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_vendas_curva))

        self.lb_vendas_curva = customtkinter.CTkLabel(self.fr_politica_vendas, text="Curva de Vendas", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_curva.place(relx=0.51, rely=0.6120, relheight=0.05, relwidth=0.30)
        self.nome_curva = []
        self.entry_vendas_curva = AutocompleteCombobox(self.fr_politica_vendas, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_vendas_curva.place(relx=0.505, rely=0.6720, relwidth=0.49, relheight=0.114)
        self.entry_vendas_curva.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_vendas_curva))
        self.entry_vendas_curva.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_vendas_curva))
        self.entry_vendas_curva.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_projetos_per_obra))


        self.lb_vendas_parcela_price = customtkinter.CTkLabel(
            self.fr_politica_vendas, text="PRICE", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_parcela_price.place(
            relx=0.01, rely=0.7960, relheight=0.05, relwidth=0.97)
        self.entry_vendas_parcela_price = customtkinter.CTkEntry(
            self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_parcela_price.place(
            relx=0.005, rely=0.8560, relwidth=0.49, relheight=0.114)

        self.lb_vendas_parcela_sacoc = customtkinter.CTkLabel(
            self.fr_politica_vendas, text="SACOC", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas_parcela_sacoc.place(
            relx=0.51, rely=0.7960, relheight=0.05, relwidth=0.30)
        self.entry_vendas_parcela_sacoc = customtkinter.CTkEntry(
            self.fr_politica_vendas, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_vendas_parcela_sacoc.place(
            relx=0.505, rely=0.8560, relwidth=0.49, relheight=0.114)

        # Custos
        self.fr_custos = customtkinter.CTkFrame(
            janela, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_custos.place(relx=0.361, rely=0.08,
                             relwidth=0.359, relheight=0.48)
        self.lb_custos = customtkinter.CTkLabel(
            self.fr_custos, text="Custos", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_custos.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.50)

        # Projetos
        self.fr_projetos = customtkinter.CTkFrame(
            self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_projetos.place(relx=0.005, rely=0.03,
                               relwidth=0.33, relheight=0.47)
        self.lb_projetos = customtkinter.CTkLabel(
            self.fr_projetos, text="Projetos", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_projetos.place(
            relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_projetos_per_obra = customtkinter.CTkLabel(self.fr_projetos, text="% x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_projetos_per_obra.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_projetos_per_obra = customtkinter.CTkEntry(self.fr_projetos, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_projetos_per_obra.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_projetos_per_obra.bind("<Return>", lambda event: self.format_per(event, self.entry_projetos_per_obra, self.entry_projetos_inicio_desembolso))
        self.entry_projetos_per_obra.bind("<Return>", lambda event: self.format_custo_projetos(event))
        self.entry_projetos_per_obra.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_projetos_valor_total = customtkinter.CTkLabel(self.fr_projetos, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_projetos_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.70)
        self.entry_projetos_valor_total = customtkinter.CTkEntry(self.fr_projetos, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_projetos_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_projetos_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_projetos_valor_total))
        self.entry_projetos_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_projetos_inicio_desembolso))

        self.lb_projetos_inicio_desembolso = customtkinter.CTkLabel(self.fr_projetos, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_projetos_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.70)
        self.entry_projetos_inicio_desembolso = customtkinter.CTkEntry(self.fr_projetos, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_projetos_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_projetos_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_projetos_inicio_desembolso))
        self.entry_projetos_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_projetos_curva_projeto))

        self.lb_projetos_curva_projeto = customtkinter.CTkLabel(self.fr_projetos, text="Curva Projetos", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_projetos_curva_projeto.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.30)
        self.nome_curva = []
        self.entry_projetos_curva_projeto = AutocompleteCombobox(self.fr_projetos, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_projetos_curva_projeto.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_projetos_curva_projeto.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_projetos_curva_projeto))
        self.entry_projetos_curva_projeto.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_projetos_curva_projeto))
        self.entry_projetos_curva_projeto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_mkt_per_vgv))

        # Marketing
        self.fr_mkt = customtkinter.CTkFrame(
            self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_mkt.place(relx=0.335, rely=0.03, relwidth=0.33, relheight=0.47)
        self.lb_mkt = customtkinter.CTkLabel(
            self.fr_mkt, text="Marketing", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_mkt.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_mkt_per_vgv = customtkinter.CTkLabel(self.fr_mkt, text="% x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_mkt_per_vgv.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_mkt_per_vgv = customtkinter.CTkEntry(self.fr_mkt, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_mkt_per_vgv.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_mkt_per_vgv.bind("<Return>", lambda event: self.format_per(event, self.entry_mkt_per_vgv, self.entry_mkt_inicio_desembolso))
        self.entry_mkt_per_vgv.bind("<Return>", lambda event: self.format_custo_mkt(event))
        self.entry_mkt_per_vgv.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_mkt_valor_total = customtkinter.CTkLabel(self.fr_mkt, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_mkt_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.70)
        self.entry_mkt_valor_total = customtkinter.CTkEntry(self.fr_mkt, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_mkt_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_mkt_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_mkt_valor_total))
        self.entry_mkt_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_mkt_inicio_desembolso))

        self.lb_mkt_inicio_desembolso = customtkinter.CTkLabel(self.fr_mkt, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_mkt_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.70)
        self.entry_mkt_inicio_desembolso = customtkinter.CTkEntry(self.fr_mkt, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_mkt_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_mkt_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_mkt_inicio_desembolso))
        self.entry_mkt_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_mkt_curva_mkt))

        self.lb_mkt_curva_mkt = customtkinter.CTkLabel(self.fr_mkt, text="Curva MkT", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_mkt_curva_mkt.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.30)
        self.nome_curva = []
        self.entry_mkt_curva_mkt = AutocompleteCombobox(self.fr_mkt, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_mkt_curva_mkt.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_mkt_curva_mkt.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_mkt_curva_mkt))
        self.entry_mkt_curva_mkt.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_mkt_curva_mkt))
        self.entry_mkt_curva_mkt.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_overhead_per_vgv))

        # OverHead
        self.fr_overhead = customtkinter.CTkFrame(self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_overhead.place(relx=0.665, rely=0.03, relwidth=0.33, relheight=0.47)
        self.lb_overhead = customtkinter.CTkLabel(self.fr_overhead, text="Over Head", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_overhead.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_overhead_per_vgv = customtkinter.CTkLabel(self.fr_overhead, text="% x VGV Bruto", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_overhead_per_vgv.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_overhead_per_vgv = customtkinter.CTkEntry(self.fr_overhead, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_overhead_per_vgv.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_overhead_per_vgv.bind("<Return>", lambda event: self.format_per(event, self.entry_overhead_per_vgv, self.entry_overhead_inicio_desembolso))
        self.entry_overhead_per_vgv.bind("<Return>", lambda event: self.format_custo_overhead(event))
        self.entry_overhead_per_vgv.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_overhead_valor_total = customtkinter.CTkLabel(self.fr_overhead, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_overhead_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.70)
        self.entry_overhead_valor_total = customtkinter.CTkEntry(self.fr_overhead, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_overhead_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_overhead_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_overhead_valor_total))
        self.entry_overhead_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event,  self.entry_overhead_inicio_desembolso))

        self.lb_overhead_inicio_desembolso = customtkinter.CTkLabel(self.fr_overhead, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_overhead_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.70)
        self.entry_overhead_inicio_desembolso = customtkinter.CTkEntry(self.fr_overhead, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_overhead_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_overhead_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_overhead_inicio_desembolso))
        self.entry_overhead_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event,  self.entry_overhead_curva_overhead))

        self.lb_overhead_curva_overhead = customtkinter.CTkLabel(self.fr_overhead, text="Curva Adm.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_overhead_curva_overhead.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.30)
        self.nome_curva = []
        self.entry_overhead_curva_overhead = AutocompleteCombobox(self.fr_overhead, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_overhead_curva_overhead.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_overhead_curva_overhead.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_overhead_curva_overhead))
        self.entry_overhead_curva_overhead.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_overhead_curva_overhead))
        self.entry_overhead_curva_overhead.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_obras_valor_m2))

        # Obras
        self.fr_obras = customtkinter.CTkFrame(
            self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_obras.place(relx=0.005, rely=0.505,
                            relwidth=0.33, relheight=0.49)
        self.lb_obras = customtkinter.CTkLabel(
            self.fr_obras, text="Obras", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_obras.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_obras_valor_m2 = customtkinter.CTkLabel(self.fr_obras, text="Custo $m² de Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_obras_valor_m2.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_obras_valor_m2 = customtkinter.CTkEntry(self.fr_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_obras_valor_m2.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_valor(event, self.entry_obras_valor_m2))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_custo_obras(event))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_custo_projetos(event))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_custo_posobras(event))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_custo_admobras(event))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_obras_valor_m2.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_obras_inicio_desembolso))

        self.lb_obras_valor_total = customtkinter.CTkLabel(self.fr_obras, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_obras_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.97)
        self.entry_obras_valor_total = customtkinter.CTkEntry(self.fr_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_obras_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_obras_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_obras_valor_total))
        self.entry_obras_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_obras_inicio_desembolso))

        self.lb_obras_inicio_desembolso = customtkinter.CTkLabel(self.fr_obras, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_obras_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.97)
        self.entry_obras_inicio_desembolso = customtkinter.CTkEntry(self.fr_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_obras_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_obras_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_obras_inicio_desembolso))
        self.entry_obras_inicio_desembolso.bind("<Return>", lambda event: self.format_custo_admobras(event))
        self.entry_obras_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_obras_curva_obras))

        self.lb_obras_curva_obras = customtkinter.CTkLabel(self.fr_obras, text="Curva Obras", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_obras_curva_obras.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.97)
        self.nome_curva = []
        self.entry_obras_curva_obras = AutocompleteCombobox(self.fr_obras, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_obras_curva_obras.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_obras_curva_obras.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_obras_curva_obras))
        self.entry_obras_curva_obras.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_obras_curva_obras))
        self.entry_obras_curva_obras.bind("<Return>", lambda event: self.format_custo_admobras(event))
        self.entry_obras_curva_obras.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_pos_obras_per_obras))

        # Pós Obras
        self.fr_pos_obras = customtkinter.CTkFrame(
            self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_pos_obras.place(relx=0.335, rely=0.505,
                                relwidth=0.33, relheight=0.49)
        self.lb_pos_obras = customtkinter.CTkLabel(
            self.fr_pos_obras, text="Pós Obras", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_pos_obras.place(
            relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_pos_obras_per_obras = customtkinter.CTkLabel(self.fr_pos_obras, text="% x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_pos_obras_per_obras.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_pos_obras_per_obras = customtkinter.CTkEntry(self.fr_pos_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_pos_obras_per_obras.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_pos_obras_per_obras.bind("<Return>", lambda event: self.format_per(event, self.entry_pos_obras_per_obras, self.entry_adm_per_obras))
        self.entry_pos_obras_per_obras.bind("<Return>", lambda event: self.format_custo_posobras(event))
        self.entry_pos_obras_per_obras.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_pos_obras_valor_total = customtkinter.CTkLabel(self.fr_pos_obras, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_pos_obras_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.97)
        self.entry_pos_obras_valor_total = customtkinter.CTkEntry(self.fr_pos_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_pos_obras_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_pos_obras_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_pos_obras_valor_total))
        self.entry_pos_obras_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_pos_obras_inicio_desembolso))

        self.lb_pos_obras_inicio_desembolso = customtkinter.CTkLabel(self.fr_pos_obras, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_pos_obras_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.97)
        self.entry_pos_obras_inicio_desembolso = customtkinter.CTkEntry(self.fr_pos_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_pos_obras_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_pos_obras_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_pos_obras_inicio_desembolso))
        self.entry_pos_obras_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_pos_obras_curva_obras))

        self.lb_pos_obras_curva_obras = customtkinter.CTkLabel(self.fr_pos_obras, text="Curva Pós Obras", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_pos_obras_curva_obras.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.97)
        self.nome_curva = []
        self.entry_pos_obras_curva_obras = AutocompleteCombobox(self.fr_pos_obras, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_pos_obras_curva_obras.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_pos_obras_curva_obras.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_pos_obras_curva_obras))
        self.entry_pos_obras_curva_obras.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_pos_obras_curva_obras))
        self.entry_pos_obras_curva_obras.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adm_per_obras))

        # Adm Obras
        self.fr_adm_obras = customtkinter.CTkFrame(
            self.fr_custos, border_color="gray75", border_width=1, fg_color="#8B0000")
        self.fr_adm_obras.place(relx=0.665, rely=0.505,
                                relwidth=0.33, relheight=0.49)
        self.lb_adm_obras = customtkinter.CTkLabel(
            self.fr_adm_obras, text="Adm. Obras", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_adm_obras.place(
            relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        self.lb_adm_per_obras = customtkinter.CTkLabel(self.fr_adm_obras, text="% x Obra", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adm_per_obras.place(relx=0.01, rely=0.10, relheight=0.05, relwidth=0.97)
        self.entry_adm_per_obras = customtkinter.CTkEntry(self.fr_adm_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adm_per_obras.place(relx=0.005, rely=0.16, relwidth=0.97, relheight=0.15)
        self.entry_adm_per_obras.bind("<Return>", lambda event: self.format_per(event, self.entry_adm_per_obras, self.entry_financiamento_valor_captacao))
        self.entry_adm_per_obras.bind("<Return>", lambda event: self.format_custo_admobras(event))
        self.entry_adm_per_obras.bind("<Return>", lambda event: self.format_dre(event))
        
        self.lb_adm_valor_total = customtkinter.CTkLabel(self.fr_adm_obras, text="$ Total", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adm_valor_total.place(relx=0.01, rely=0.32, relheight=0.05, relwidth=0.97)
        self.entry_adm_valor_total = customtkinter.CTkEntry(self.fr_adm_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adm_valor_total.place(relx=0.005, rely=0.38, relwidth=0.97, relheight=0.15)
        self.entry_adm_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_adm_valor_total))
        self.entry_adm_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adm_inicio_desembolso))

        self.lb_adm_inicio_desembolso = customtkinter.CTkLabel(self.fr_adm_obras, text="Inicio Desembolso", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adm_inicio_desembolso.place(relx=0.01, rely=0.54, relheight=0.05, relwidth=0.97)
        self.entry_adm_inicio_desembolso = customtkinter.CTkEntry(self.fr_adm_obras, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_adm_inicio_desembolso.place(relx=0.005, rely=0.60, relwidth=0.97, relheight=0.15)
        self.entry_adm_inicio_desembolso.bind("<Return>", lambda event: self.format_mes(event, self.entry_adm_inicio_desembolso))
        self.entry_adm_inicio_desembolso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_adm_curva_obras))

        self.lb_adm_curva_obras = customtkinter.CTkLabel(self.fr_adm_obras, text="Curva Adm. Obras", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_adm_curva_obras.place(relx=0.01, rely=0.76, relheight=0.05, relwidth=0.97)
        self.nome_curva = []
        self.entry_adm_curva_obras = AutocompleteCombobox(self.fr_adm_obras, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_adm_curva_obras.place(relx=0.005, rely=0.82, relwidth=0.97, relheight=0.15)
        self.entry_adm_curva_obras.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_adm_curva_obras))
        self.entry_adm_curva_obras.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_adm_curva_obras))
        self.entry_adm_curva_obras.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_valor_captacao))

        # financiamento
        self.fr_financiamento = customtkinter.CTkFrame(
            janela, border_color="gray75", border_width=1, fg_color="Light blue")
        self.fr_financiamento.place(
            relx=0.721, rely=0.08, relwidth=0.119, relheight=0.48)
        self.lb_financiamento = customtkinter.CTkLabel(
            self.fr_financiamento, text="Financiamento", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_financiamento.place(
            relx=0.05, rely=0, relheight=0.03, relwidth=0.50)

        # Valor Captação
        self.lb_financiamento_valor_captacao = customtkinter.CTkLabel(self.fr_financiamento, text="Valor Captação", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_valor_captacao.place(relx=0.01, rely=0.04, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_valor_captacao = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_valor_captacao.place(relx=0.01, rely=0.07, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_valor_captacao.bind("<Return>", lambda event: self.format_valor(event, self.entry_financiamento_valor_captacao))
        self.entry_financiamento_valor_captacao.bind("<Return>", lambda event: self.format_dre(event))
        self.entry_financiamento_valor_captacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_sistema_amortizacao))

        # Sistema Amortização
        self.lb_financiamento_sistema_amortizacao = customtkinter.CTkLabel(self.fr_financiamento, text="Sistema de Amortização", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_sistema_amortizacao.place(relx=0.01, rely=0.135, relheight=0.02, relwidth=0.97)
        self.nome_sistema_amortizacao = []
        self.entry_financiamento_sistema_amortizacao = AutocompleteCombobox(self.fr_financiamento, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_sistema_amortizacao)
        self.entry_financiamento_sistema_amortizacao.place(relx=0.01, rely=0.165, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_sistema_amortizacao.bind("<Button-1>", lambda event: self.atualizar_sistema_amortizacao(event, self.entry_financiamento_sistema_amortizacao))
        self.entry_financiamento_sistema_amortizacao.bind("<Return>", lambda event: self.muda_barrinha(event,  self.entry_financiamento_prazo_amortizacao))

        # Prazo Amortização
        self.lb_financiamento_prazo_amortizacao = customtkinter.CTkLabel(self.fr_financiamento, text="Prazo Amortização", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_prazo_amortizacao.place(relx=0.01, rely=0.23, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_prazo_amortizacao = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_prazo_amortizacao.place(relx=0.01, rely=0.26, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_prazo_amortizacao.bind("<Return>", lambda event: self.format_x(event, self.entry_financiamento_prazo_amortizacao))
        self.entry_financiamento_prazo_amortizacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_inicio_amortizacao))

        # Inicio Amortização
        self.lb_financiamento_inicio_amortizacao = customtkinter.CTkLabel(
            self.fr_financiamento, text="Início Amortização", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_inicio_amortizacao.place(
            relx=0.01, rely=0.325, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_inicio_amortizacao = customtkinter.CTkEntry(
            self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_inicio_amortizacao.place(
            relx=0.01, rely=0.355, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_inicio_amortizacao.bind("<Return>", lambda event: self.format_mes(event, self.entry_financiamento_inicio_amortizacao))
        self.entry_financiamento_inicio_amortizacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_inicio_pagto_juros))

        # Inicio Pagto Juros
        self.lb_financiamento_inicio_pagto_juros = customtkinter.CTkLabel(
            self.fr_financiamento, text="Início Pagto Juros", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_inicio_pagto_juros.place(
            relx=0.01, rely=0.42, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_inicio_pagto_juros = customtkinter.CTkEntry(
            self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_inicio_pagto_juros.place(
            relx=0.01, rely=0.45, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_inicio_pagto_juros.bind("<Return>", lambda event: self.format_mes(event, self.entry_financiamento_inicio_pagto_juros))
        self.entry_financiamento_inicio_pagto_juros.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_juros))

        # Juros
        self.lb_financiamento_juros = customtkinter.CTkLabel(self.fr_financiamento, text="Valor Juros", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_juros.place(relx=0.01, rely=0.515, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_juros = customtkinter.CTkEntry(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_juros.place(relx=0.01, rely=0.545, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_juros.bind("<Return>", lambda event: self.format_valor(event, self.entry_financiamento_juros))
        self.entry_financiamento_juros.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_juros_aa))

        # Juros % a.a.
        self.lb_financiamento_juros_aa = customtkinter.CTkLabel(
            self.fr_financiamento, text="% a.a.", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_juros_aa.place(
            relx=0.01, rely=0.61, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_juros_aa = customtkinter.CTkEntry(
            self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_juros_aa.place(
            relx=0.01, rely=0.64, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_juros_aa.bind("<Return>", lambda event: self.format_per(event, self.entry_financiamento_juros_aa, self.entry_financiamento_inicio_liberacao))

        # Inicio Liberação
        self.lb_financiamento_inicio_liberacao = customtkinter.CTkLabel(
            self.fr_financiamento, text="Início Liberação", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_inicio_liberacao.place(
            relx=0.01, rely=0.705, relheight=0.02, relwidth=0.97)
        self.entry_financiamento_inicio_liberacao = customtkinter.CTkEntry(
            self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_financiamento_inicio_liberacao.place(
            relx=0.01, rely=0.735, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_inicio_liberacao.bind("<Return>", lambda event: self.format_mes(event, self.entry_financiamento_inicio_liberacao))
        self.entry_financiamento_inicio_liberacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_curva_liberacao))

        # Curva de Liberação
        self.lb_financiamento_curva_liberacao = customtkinter.CTkLabel(self.fr_financiamento, text="Curva Liberação", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_curva_liberacao.place(relx=0.01, rely=0.80, relheight=0.02, relwidth=0.97)
        self.nome_curva = []
        self.entry_financiamento_curva_liberacao = AutocompleteCombobox(self.fr_financiamento, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_financiamento_curva_liberacao.place(relx=0.01, rely=0.83, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_curva_liberacao.bind("<Button-1>", lambda event: self.atualizar_curvas(event, self.entry_financiamento_curva_liberacao))
        self.entry_financiamento_curva_liberacao.bind('<Down>', lambda event: self.atualizar_curvas(event, self.entry_financiamento_curva_liberacao))
        self.entry_financiamento_curva_liberacao.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_financiamento_financiador))

        # Financiador é o Parceiro?
        self.lb_financiamento_financiador = customtkinter.CTkLabel(self.fr_financiamento, text="Financiador é o Parceiro", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_financiamento_financiador.place(relx=0.01, rely=0.895, relheight=0.02, relwidth=0.97)
        self.opcoes = ["Não", "Sim"]
        self.entry_financiamento_financiador = customtkinter.CTkComboBox(self.fr_financiamento, fg_color="black", text_color="white", justify=tk.RIGHT, values=self.opcoes)
        self.entry_financiamento_financiador.place(relx=0.01, rely=0.925, relwidth=0.97, relheight=0.055)
        self.entry_financiamento_financiador.bind("<Return>", lambda event: self.muda_barrinha(event, self.text_observacoes ))

        # Resultados
        self.fr_resultados = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="white")
        self.fr_resultados.place(relx=0.841, rely=0.08, relwidth=0.159, relheight=0.73)
        self.lb_resultados = customtkinter.CTkLabel(self.fr_resultados, text="Resultados", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_resultados.place(relx=0.05, rely=0, relheight=0.03, relwidth=0.50)

        # DRE
        self.fr_dre = customtkinter.CTkFrame(self.fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        self.fr_dre.place(relx=0.005, rely=0.03,relwidth=0.985, relheight=0.47)
        self.lb_dre = customtkinter.CTkLabel(self.fr_dre, text="DRE", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_dre.place(relx=0.05, rely=0, relheight=0.04, relwidth=0.50)

        # VGV Bruto
        self.lb_dre_vgv_bruto = customtkinter.CTkLabel(self.fr_dre, text="VGV Bruto:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_vgv_bruto.place(relx=0.01, rely=0.12, relheight=0.05, relwidth=0.25)
        self.entry_dre_vgv_bruto = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_bruto.place(relx=0.30, rely=0.10, relwidth=0.69, relheight=0.10)

        # Comissão
        self.lb_dre_comissao = customtkinter.CTkLabel(self.fr_dre, text="Comissão:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_comissao.place(relx=0.01, rely=0.23, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_comissao.place(relx=0.30, rely=0.21, relwidth=0.69, relheight=0.10)

        # VGV Líquido
        self.lb_dre_vgv_liquido = customtkinter.CTkLabel(self.fr_dre, text="VGV Líq.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_vgv_liquido.place(relx=0.01, rely=0.34, relheight=0.05, relwidth=0.25)
        self.entry_dre_vgv_liquido = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_liquido.place(relx=0.30, rely=0.32, relwidth=0.69, relheight=0.10)

        # Imposto
        self.lb_dre_impostos = customtkinter.CTkLabel(self.fr_dre, text="Impostos:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_impostos.place(relx=0.01, rely=0.45, relheight=0.05, relwidth=0.25)
        self.entry_dre_impostos = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_impostos.place(relx=0.30, rely=0.43, relwidth=0.69, relheight=0.10)

        # Comissão de Negócio
        self.lb_dre_comissao_negocio = customtkinter.CTkLabel(self.fr_dre, text="Com.Negócio:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_comissao_negocio.place(relx=0.01, rely=0.56, relheight=0.05, relwidth=0.25)
        self.entry_dre_comissao_negocio = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_comissao_negocio.place(relx=0.30, rely=0.54, relwidth=0.69, relheight=0.10)

        # Receita Líquida
        self.lb_dre_receita_liquida = customtkinter.CTkLabel(self.fr_dre, text="Receita Líq.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_receita_liquida.place(relx=0.01, rely=0.67, relheight=0.05, relwidth=0.25)
        self.entry_dre_receita_liquida = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida.place(relx=0.30, rely=0.65, relwidth=0.69, relheight=0.10)

        # VGV Parceiro
        self.lb_dre_vgv_parceiro = customtkinter.CTkLabel(self.fr_dre, text="VGV Parc.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_vgv_parceiro.place(relx=0.01, rely=0.78, relheight=0.05, relwidth=0.25)
        self.entry_dre_vgv_parceiro = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_vgv_parceiro.place(relx=0.30, rely=0.76, relwidth=0.69, relheight=0.10)

        # Receita Líquida Urbanizadora
        self.lb_dre_receita_liquida_urbanizadora = customtkinter.CTkLabel(self.fr_dre, text="Receita Urban.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_receita_liquida_urbanizadora.place(relx=0.01, rely=0.89, relheight=0.05, relwidth=0.25)
        self.entry_dre_receita_liquida_urbanizadora = customtkinter.CTkEntry(self.fr_dre, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_receita_liquida_urbanizadora.place(relx=0.30, rely=0.87, relwidth=0.69, relheight=0.10)

        # Ebtda
        self.fr_ebtda = customtkinter.CTkFrame(self.fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        self.fr_ebtda.place(relx=0.005, rely=0.50,relwidth=0.985, relheight=0.11)
        self.lb_ebtda = customtkinter.CTkLabel(self.fr_ebtda, text="Ebtda", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_ebtda.place(relx=0.05, rely=0, relheight=0.20, relwidth=0.50)

        # Valor
        self.lb_dre_ebtda_valor = customtkinter.CTkLabel(self.fr_ebtda, text="Valor:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_ebtda_valor.place(relx=0.01, rely=0.30, relheight=0.20, relwidth=0.25)
        self.entry_dre_ebtda_valor = customtkinter.CTkEntry(self.fr_ebtda, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_ebtda_valor.place(relx=0.30, rely=0.03, relwidth=0.69, relheight=0.47)

        # %
        self.lb_dre_ebtda_per = customtkinter.CTkLabel(self.fr_ebtda, text="%:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_dre_ebtda_per.place(relx=0.01, rely=0.75, relheight=0.20, relwidth=0.25)
        self.entry_dre_ebtda_per = customtkinter.CTkEntry(self.fr_ebtda, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_dre_ebtda_per.place(relx=0.30, rely=0.50, relwidth=0.69, relheight=0.47)

        # Indicadores
        self.fr_indicadores = customtkinter.CTkFrame(self.fr_resultados, border_color="gray75", border_width=1, fg_color="white")
        self.fr_indicadores.place(relx=0.005, rely=0.61, relwidth=0.985, relheight=0.385)
        self.lb_indicadores = customtkinter.CTkLabel(self.fr_indicadores, text="Indicadores", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_indicadores.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.50)

        # T.I.R. a.a.
        self.lb_indicadores_tir_aa = customtkinter.CTkLabel(self.fr_indicadores, text="T.I.R. a.a.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_tir_aa.place(relx=0.01, rely=0.07, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_tir_aa = customtkinter.CTkEntry(self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_tir_aa.place(relx=0.30, rely=0.08, relwidth=0.69, relheight=0.12)

        # T.I.R. a.m.
        self.lb_indicadores_tir_am = customtkinter.CTkLabel(
            self.fr_indicadores, text="T.I.R. a.m.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_tir_am.place(
            relx=0.01, rely=0.20, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_tir_am = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_tir_am.place(
            relx=0.30, rely=0.21, relwidth=0.69, relheight=0.12)

        # PayBack
        self.lb_indicadores_payback = customtkinter.CTkLabel(
            self.fr_indicadores, text="PayBack:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_payback.place(
            relx=0.01, rely=0.33, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_payback = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_payback.place(
            relx=0.30, rely=0.34, relwidth=0.69, relheight=0.12)

        # Multiplicador do Investimento
        self.lb_indicadores_multiplicador_investimento = customtkinter.CTkLabel(
            self.fr_indicadores, text="Mult.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_multiplicador_investimento.place(
            relx=0.01, rely=0.46, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_multiplicador_investimento = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_multiplicador_investimento.place(
            relx=0.30, rely=0.47, relwidth=0.69, relheight=0.12)

        # Exposição Máxima de Caixa
        self.lb_indicadores_exposicaomax_caixa = customtkinter.CTkLabel(
            self.fr_indicadores, text="Exp.Max.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_exposicaomax_caixa.place(
            relx=0.01, rely=0.59, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_exposicaomax_caixa = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_exposicaomax_caixa.place(
            relx=0.30, rely=0.60, relwidth=0.69, relheight=0.12)

        # VPL Urbanizadora
        self.lb_indicadores_vpl_urbanizadora = customtkinter.CTkLabel(
            self.fr_indicadores, text="VPL Urban.:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_vpl_urbanizadora.place(
            relx=0.01, rely=0.72, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_vpl_urbanizadora = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_vpl_urbanizadora.place(
            relx=0.30, rely=0.73, relwidth=0.69, relheight=0.12)

        # VPL Parceriro
        self.lb_indicadores_vpl_parceiro = customtkinter.CTkLabel(
            self.fr_indicadores, text="VPV Parceiro:", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_indicadores_vpl_parceiro.place(
            relx=0.01, rely=0.85, relheight=0.20, relwidth=0.25)
        self.entry_indicadores_vpl_parceiro = customtkinter.CTkEntry(
            self.fr_indicadores, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_indicadores_vpl_parceiro.place(
            relx=0.30, rely=0.86, relwidth=0.69, relheight=0.12)

        # Taxa Desconto
        self.fr_taxa_desconto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="white")
        self.fr_taxa_desconto.place(relx=0.841, rely=0.81, relwidth=0.159, relheight=0.08)
        self.lb_taxa_desconto = customtkinter.CTkLabel(self.fr_taxa_desconto, text="Taxa Desconto - VpL", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_taxa_desconto.place(relx=0.05, rely=0, relheight=0.15, relwidth=0.97)

        self.entry_taxa_desconto = customtkinter.CTkEntry(self.fr_taxa_desconto, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_taxa_desconto.place(relx=0.01, rely=0.20, relwidth=0.97, relheight=0.50)
        self.entry_taxa_desconto.bind("<Return>", lambda event: self.format_per(event, self.entry_taxa_desconto, self.entry_informacoes_status))
        self.entry_taxa_desconto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_status))
        
        # Observações do Estudo
        self.fr_observacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="white")
        self.fr_observacoes.place(relx=0.091, rely=0.56, relwidth=0.749, relheight=0.25)
        self.lb_observacoes = customtkinter.CTkLabel(self.fr_observacoes, text="Observações do Negócio", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_observacoes.place(relx=0.05, rely=0, relheight=0.05, relwidth=0.60)

        # observações
        self.text_observacoes = customtkinter.CTkTextbox(self.fr_observacoes, fg_color="black", text_color="white", width=300, height=100)
        self.text_observacoes.place(relx=0.0, rely=0.06, relwidth=1, relheight=0.94)
        self.text_observacoes.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_taxa_desconto))

        # informações - localização, status, anexos, data
        self.fr_informacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1, fg_color="Light Yellow")
        self.fr_informacoes.place(relx=0, rely=0.81, relwidth=0.84, relheight=0.16)
        self.lb_informacoes = customtkinter.CTkLabel(self.fr_informacoes, text="Informações do Estudo", text_color="black", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_informacoes.place(relx=0.05, rely=0, relheight=0.10, relwidth=0.70)

        # Status
        self.lb_informacoes_status = customtkinter.CTkLabel(self.fr_informacoes, text="Status", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_informacoes_status.place(relx=0.01, rely=0.11, relheight=0.07, relwidth=0.70)
        status = []
        self.entry_informacoes_status = AutocompleteCombobox(self.fr_informacoes, width=30, font=('Times', 11), completevalues=status)
        self.entry_informacoes_status.pack()
        self.entry_informacoes_status.place(relx=0.01, rely=0.19, relwidth=0.30, relheight=0.25)
        self.entry_informacoes_status.bind("<Button-1>", lambda event: self.atualizar_status(event, self.entry_empresa.get(), self.entry_informacoes_status))
        self.entry_informacoes_status.bind('<Down>', lambda event: self.atualizar_status(event, self.entry_empresa.get(), self.entry_informacoes_status))
        self.entry_informacoes_status.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_anexos))

        # Anexos
        self.lb_informacoes_anexos = customtkinter.CTkLabel(self.fr_informacoes, text="Anexos", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_informacoes_anexos.place(relx=0.315, rely=0.11, relheight=0.07, relwidth=0.70)
        self.entry_informacoes_anexos = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_informacoes_anexos.place(relx=0.315, rely=0.19, relwidth=0.465, relheight=0.25)
        self.entry_informacoes_anexos.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_data))

        # Data do cadastro
        self.lb_informacoes_data = customtkinter.CTkLabel(self.fr_informacoes, text="Data Cadastro", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_informacoes_data.place(relx=0.785, rely=0.11, relheight=0.07, relwidth=0.97)
        self.entry_informacoes_data = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_informacoes_data.place(relx=0.785, rely=0.19, relwidth=0.10, relheight=0.25)
        self.entry_informacoes_data.bind("<Button-1>", lambda event: self.calendario(event, self.entry_informacoes_data))
        self.entry_informacoes_data.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_informacoes_data, self.entry_informacoes_unidade_negocio))
        
        # Unidade Negócio
        self.lb_informacoes_unidade_negocio = customtkinter.CTkLabel(self.fr_informacoes, text="Unidade Negócio", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_informacoes_unidade_negocio.place(relx=0.895, rely=0.11, relheight=0.07, relwidth=0.97)
        self.unidade_negocio = []
        self.entry_informacoes_unidade_negocio = AutocompleteCombobox(self.fr_informacoes, width=30, justify=tk.LEFT, font=('Times', 8), completevalues=self.nome_curva)
        self.entry_informacoes_unidade_negocio.place(relx=0.895, rely=0.19, relwidth=0.10, relheight=0.25)
        self.entry_informacoes_unidade_negocio.bind("<Button-1>", lambda event: self.atualizar_unidade_negocios(event, self.entry_informacoes_unidade_negocio))
        self.entry_informacoes_unidade_negocio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_https))

        # Https://
        self.lb_informacoes_https = customtkinter.CTkLabel(self.fr_informacoes, text="Https://", text_color="black", font=('Arial', 10), anchor=tk.W)
        self.lb_informacoes_https.place(relx=0.01, rely=0.45, relheight=0.08, relwidth=0.25)
        self.entry_informacoes_https = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_informacoes_https.place(relx=0.01, rely=0.55, relwidth=0.85, relheight=0.25)
        
        # Coordenadas Maps - Desativado gravando em branco o campo
        self.lb_informacoes_maps = customtkinter.CTkLabel(self.fr_informacoes, text="Coordenadas Maps", text_color="black", font=('Arial', 10), anchor=tk.W)
        # self.lb_informacoes_maps.place(relx=0.01, rely=0.45, relheight=0.08, relwidth=0.25)
        self.entry_informacoes_maps = customtkinter.CTkEntry(self.fr_informacoes, fg_color="black", text_color="white", justify=tk.LEFT)
        # self.entry_informacoes_maps.place(relx=0.01, rely=0.55, relwidth=0.85, relheight=0.25)
        # self.entry_informacoes_maps.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_informacoes_maps))

        # Icon Adicionar endereço no maps
        coordenadas_relx = 0.86
        coordenadas_rely = 0.55
        coordenadas_relwidth = 0.05
        coordenadas_relheight = 0.25
        icon_image = self.base64_to_photoimage('savedown')
        self.btn_gravar_maps = customtkinter.CTkButton(
                                                    self.fr_informacoes,  
                                                    text='',
                                                    image=icon_image, 
                                                    fg_color='transparent', 
                                                    command=self.Acessar_Maps
                                                        )
        self.btn_gravar_maps.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.btn_gravar_maps.bind("<Return>", lambda event: self.btn_gravar_maps.invoke())
        
        # Icon de Consulta Endereço Cadastrado
        def selected_maps():
            ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get()) 
            UF = self.entry_uf.get()
            Cidade = self.entry_municipio.get()
            Tipo_Estudo = self.entry_tpo_projeto.get()
            Nome_Area = self.entry_nome_cenario.get()
            url =self.entry_informacoes_https.get()
            
            if not ID_Empresa:
                messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            if not UF:
                messagebox.showinfo('Gestor Negócios', 'UF em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            if not Cidade:
                messagebox.showinfo('Gestor Negócios', 'Município em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            if not Tipo_Estudo:
                messagebox.showinfo('Gestor Negócios', 'Tipo do Estudo em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            if not Nome_Area:
                messagebox.showinfo('Gestor Negócios', 'Nome da Área em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            if not url:
                messagebox.showinfo('Gestor Negócios', 'Url da Área em Branco!!!', parent=self.janela_simulador_rel)
                return
            
            UF = UF.upper()
            url = url.strip()  # Remove espaços em branco no início e no fim
            webbrowser.open(url)

        coordenadas_relx = 0.915
        coordenadas_rely = 0.55
        coordenadas_relwidth = 0.05
        coordenadas_relheight = 0.25
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_maps = customtkinter.CTkButton(
                                                    self.fr_informacoes,  
                                                    text='',
                                                    image=icon_image, 
                                                    fg_color='transparent', 
                                                    command=selected_maps
                                                        )
        self.btn_consultar_maps.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        self.btn_consultar_maps.bind("<Return>", lambda event: self.btn_consultar_maps.invoke())
        
        self.limpar_simulador_negocios()

Simulador_Estudos_Rel()