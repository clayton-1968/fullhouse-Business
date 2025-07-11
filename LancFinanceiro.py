from imports import *
from widgets import Widgets
from PIL import ImageTk, Image
from UsrCadastros import *


class Lanc_fin(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):

    def lancamentos(self):
        self.images_base64()
        
        self.window_one.title('Lançamentos Financeiros')
        self.clearFrame_principal()
        
        # Iniciar variáveis do Formulário
        self.Vlr = 0
        self.vlr_soma_itens = 0
        self.Vlr_TotalParcelas = 0
        self.Vlr_TotalItens = 0
        self.Nr_Item = 1
        self.NrCampos = 1

        self.linha1_lanc(self.principal_frame)
        self.linha2_lanc(self.principal_frame)
        self.linha3_lanc(self.principal_frame)
        self.linha4_lanc(self.principal_frame)
        self.linha5_lanc(self.principal_frame)

    def linha1_lanc(self, janela_lanc):
        # Tipo lançamento
        fr_tipo_lcto = customtkinter.CTkFrame(janela_lanc, border_color="gray75", border_width=1)
        fr_tipo_lcto.place(relx=0, rely=0, relwidth=0.07, relheight=0.07)

        lb_tipo_lcto = customtkinter.CTkLabel(fr_tipo_lcto, text="Tipo Lçto")
        lb_tipo_lcto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.opcoes = ["CPA", "CRE", "CTA"]
        self.entry_tipo_lcto_descr = customtkinter.CTkComboBox(fr_tipo_lcto, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_tipo_lcto_descr.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
        self.entry_tipo_lcto_descr.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_empresa))
        
        # Empresa
        coordenadas_relx = 0.075
        coordenadas_rely = 0
        coordenadas_relwidth = 0.38
        coordenadas_relheight = 0.07
        self.frame_empresa(janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))

        # Cliente
        coordenadas_relx = 0.46
        coordenadas_rely = 0
        coordenadas_relwidth = 0.35
        coordenadas_relheight = 0.07
        self.frame_pessoa(janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        # Botão Incluir Pessoas
        bt_cadastro_pessoas = customtkinter.CTkButton(self.fr_pessoa, text='...', font=('Arial', 30), fg_color='green', command=self.cad_pessoas)
        bt_cadastro_pessoas.place(relx=0.905, rely=0.5, relwidth=0.05, relheight=0.35)
        bt_cadastro_pessoas.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))

        # Unidade Negocios
        coordenadas_relx = 0.815
        coordenadas_rely = 0
        coordenadas_relwidth = 0.18
        coordenadas_relheight = 0.07
        self.frame_Unidade_Negocio(janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_unidade_negocio.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_uf))
                          
    def linha2_lanc(self, janela_lanc):
        # Estado
        coordenadas_relx = 0
        coordenadas_rely = 0.075
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        self.frame_uf(janela_lanc, coordenadas_relx, coordenadas_rely,coordenadas_relwidth, coordenadas_relheight)
        self.combo_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_frete))

        # Frete
        coordenadas_relx = 0.065
        coordenadas_rely = 0.075
        coordenadas_relwidth = 0.32
        coordenadas_relheight = 0.07
        self.fram_frete(janela_lanc, coordenadas_relx, coordenadas_rely,coordenadas_relwidth, coordenadas_relheight)
        self.combo_frete.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_num))

        # Documentos
        fr_doc = customtkinter.CTkFrame(janela_lanc, border_color="gray75", border_width=1)
        fr_doc.place(relx=0.39, rely=0.075, relwidth=0.6, relheight=0.09)
        lb_doc = customtkinter.CTkLabel(fr_doc, text="Documento")
        lb_doc.place(relx=0.01, rely=0, relheight=0.25, relwidth=0.15)

        lb_doc_num = customtkinter.CTkLabel(fr_doc, text="Nr. Documento")
        lb_doc_num.place(relx=0.01, rely=0.25, relheight=0.25, relwidth=0.12)
        self.entry_doc_num = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_doc_num.place(relx=0.01, rely=0.5, relwidth=0.12, relheight=0.4)
        self.entry_doc_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))
        
        # Botão Consultar
        bt_consultar = customtkinter.CTkButton(fr_doc, image=self.btconsulta_img, command=self.consulta_lcto)
        bt_consultar.place(relx=0.135, rely=0.55, relwidth=0.035, relheight=0.3)

        # Botão Excluir
        bt_excluir = customtkinter.CTkButton(fr_doc, image=self.bttrash_img, command=self.delete_document)
        bt_excluir.place(relx=0.175, rely=0.55, relwidth=0.035, relheight=0.3)

        # Botão Anexo
        bt_anexar = customtkinter.CTkButton(fr_doc, image=self.btanexar_img)
        bt_anexar.place(relx=0.215, rely=0.55, relwidth=0.035, relheight=0.3)

        lb_doc_dt_emissao = customtkinter.CTkLabel(fr_doc, text="Data Emissão")
        lb_doc_dt_emissao.place(relx=0.26, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_dt_emissao = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_doc_dt_emissao.place(relx=0.26, rely=0.5, relwidth=0.14, relheight=0.4)
        self.entry_doc_dt_emissao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_doc_dt_emissao))
        self.entry_doc_dt_emissao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_doc_dt_emissao, self.entry_doc_serie))

        lb_doc_serie = customtkinter.CTkLabel(fr_doc, text="Série")
        lb_doc_serie.place(relx=0.41, rely=0.25, relheight=0.25, relwidth=0.08)
        self.entry_doc_serie = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_doc_serie.place(relx=0.41, rely=0.5, relwidth=0.08, relheight=0.4)
        self.entry_doc_serie.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_numcontrato))

        lb_doc_numcontrato = customtkinter.CTkLabel(fr_doc, text="Nr. Contrato")
        lb_doc_numcontrato.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_numcontrato = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_doc_numcontrato.place(relx=0.5, rely=0.5, relwidth=0.14, relheight=0.4)
        self.entry_doc_numcontrato.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_valor_total))

        lb_doc_valor_total = customtkinter.CTkLabel(fr_doc, text="Valor Total Doc.")
        lb_doc_valor_total.place(relx=0.65, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_valor_total = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_doc_valor_total.place(relx=0.65, rely=0.5, relwidth=0.14, relheight=0.4)
        self.entry_doc_valor_total.bind("<Return>", lambda event: self.format_valor(event, self.entry_doc_valor_total))
        self.entry_doc_valor_total.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_parcelas))
        
        # Botão Retenções
        bt_retencoes = customtkinter.CTkButton(fr_doc, image=self.btsave_img)
        bt_retencoes.place(relx=0.8, rely=0.55, relwidth=0.035, relheight=0.3)
        
        lb_doc_parcelas = customtkinter.CTkLabel(fr_doc, text="Nr. Parcelas")
        lb_doc_parcelas.place(relx=0.86, rely=0.25, relheight=0.25, relwidth=0.13)
        self.entry_doc_parcelas = customtkinter.CTkEntry(fr_doc, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_doc_parcelas.place(relx=0.86, rely=0.5, relwidth=0.13, relheight=0.4)
        self.entry_doc_parcelas.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_info_pag_nr_parc))

    def linha3_lanc(self, janela_lanc):
        # Informações de Pagamento
        fr_info_pag = customtkinter.CTkFrame(janela_lanc, border_color="gray75", border_width=1)
        fr_info_pag.place(relx=0, rely=0.17, relwidth=0.22, relheight=0.18)
        lb_info_pag = customtkinter.CTkLabel(fr_info_pag, text="Informações de Pagamento")
        lb_info_pag.place(relx=0.02, rely=0, relheight=0.125, relwidth=0.6)

        lb_info_pag_nr_parc = customtkinter.CTkLabel(fr_info_pag, text="Parcela Nr.")
        lb_info_pag_nr_parc.place(relx=0.02, rely=0.125, relheight=0.125, relwidth=0.27)
        self.entry_info_pag_nr_parc = customtkinter.CTkEntry(fr_info_pag, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_info_pag_nr_parc.place(relx=0.02, rely=0.25, relwidth=0.27, relheight=0.25)
        self.entry_info_pag_nr_parc.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_info_pag_forma_liq))

        lb_info_pag_forma_liq = customtkinter.CTkLabel(fr_info_pag, text="Forma Liquidação")
        lb_info_pag_forma_liq.place(relx=0.3, rely=0.125, relheight=0.125, relwidth=0.69)

        self.tpo_pagto = []
        self.entry_info_pag_forma_liq = AutocompleteCombobox(fr_info_pag, foreground='black', width=30, font=('Times', 11), completevalues=self.get_tpo_pagto)
        self.entry_info_pag_forma_liq.place(relx=0.3, rely=0.25, relwidth=0.69, relheight=0.25)
        self.entry_info_pag_forma_liq.bind("<Button-1>", lambda event: self.atualizar_tpo_pagto(event, self.entry_info_pag_forma_liq))
        self.entry_info_pag_forma_liq.bind('<Down>', lambda event: self.atualizar_tpo_pagto(event, self.entry_info_pag_forma_liq))
        self.entry_info_pag_forma_liq.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_info_pag_dt_venc))

        lb_info_pag_dt_venc = customtkinter.CTkLabel(fr_info_pag, text="Data Vencto")
        lb_info_pag_dt_venc.place(relx=0.02, rely=0.5, relheight=0.125, relwidth=0.35)
        self.entry_info_pag_dt_venc = customtkinter.CTkEntry(fr_info_pag, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_info_pag_dt_venc.place(relx=0.02, rely=0.625, relwidth=0.35, relheight=0.25)
        self.entry_info_pag_dt_venc.bind("<Button-1>", lambda event: self.calendario(event, self.entry_info_pag_dt_venc))
        self.entry_info_pag_dt_venc.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_info_pag_dt_venc, self.entry_info_pag_valor_parc))

        lb_info_pag_valor_parc = customtkinter.CTkLabel(fr_info_pag, text="Valor Parcela")
        lb_info_pag_valor_parc.place(relx=0.38, rely=0.5, relheight=0.125, relwidth=0.4)
        self.entry_info_pag_valor_parc = customtkinter.CTkEntry(fr_info_pag, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_info_pag_valor_parc.place(relx=0.38, rely=0.625, relwidth=0.4, relheight=0.25)
        self.entry_info_pag_valor_parc.bind("<Return>", lambda event: self.format_valor(event, self.entry_info_pag_valor_parc))
        self.entry_info_pag_valor_parc.bind("<Return>", lambda event: self.muda_barrinha(event, bt_incluir_parcelas))
        
        # Botão Incluir Parcelas
        bt_incluir_parcelas = customtkinter.CTkButton(fr_info_pag, image=self.btsavedown_img, command=self.incluir_parcelas_click)
        bt_incluir_parcelas.place(relx=0.8, rely=0.65, relwidth=0.10, relheight=0.2)
        
        ## Listbox _ Informações de Pagamento
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background="white", foreground="black", fieldbackground="white", borderwidth=0)


        # Widgets - Listar Parcelas
        self.LParcelasFinanceiras = ttk.Treeview(janela_lanc, height=12, column=('Nr', 'Dta_Vcto', 'Valor', 'Forma_Pagto'), show='headings')
        self.LParcelasFinanceiras.heading('Nr', text='Nr.')
        self.LParcelasFinanceiras.column('Nr', width=10, anchor='center')
        self.LParcelasFinanceiras.heading('Dta_Vcto', text='Dta Vencto')
        self.LParcelasFinanceiras.column('Dta_Vcto', width=40, anchor='center')
        self.LParcelasFinanceiras.heading('Valor', text='Valor')
        self.LParcelasFinanceiras.column('Valor', width=70, anchor='e')
        self.LParcelasFinanceiras.heading('Forma_Pagto', text='Forma de Liquidação')
        self.LParcelasFinanceiras.column('Forma_Pagto', width=100, anchor='w')
        
        self.LParcelasFinanceiras.place(relx=0.23, rely=0.17, relwidth=0.4, relheight=0.16)
        #sself.LParcelasFinanceiras.bind("<Double-1>", self.OnDoubleClick)

        # Historico
        fr_historico = customtkinter.CTkFrame(janela_lanc, border_color="gray75", border_width=1)
        fr_historico.place(relx=0.64, rely=0.17, relwidth=0.31, relheight=0.18)

        lb_historico = customtkinter.CTkLabel(fr_historico, text="Histórico")
        lb_historico.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.125)

        self.text_historico = customtkinter.CTkTextbox(fr_historico, fg_color="white", text_color="black", width=300, height=100)
        self.text_historico.place(relx=0.02, rely=0.125, relwidth=0.96, relheight=0.825)
        self.text_historico.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_prod_descr))

        # Botão Salvar
        bt_pag_salvar = customtkinter.CTkButton(janela_lanc, image=self.btsave_img, text='',  command=self.gravar_lcto)
        bt_pag_salvar.place(relx=0.955, rely=0.21, relwidth=0.03, relheight=0.04)

        # Botão Incluir Itens da Nota
        bt_incluir_itens = customtkinter.CTkButton(janela_lanc, image=self.btsavedown_img, text='', command=self.incluir_itens_click)
        bt_incluir_itens.place(relx=0.955, rely=0.28, relwidth=0.03, relheight=0.04)

    def linha4_lanc(self, janela_lanc):
        fr_itens_nota = customtkinter.CTkFrame(janela_lanc, border_color="gray75", border_width=1)
        fr_itens_nota.place(relx=0, rely=0.355, relwidth=1, relheight=0.10)
        lb_itens_nota = customtkinter.CTkLabel(fr_itens_nota, text="Itens da Nota")
        lb_itens_nota.place(relx=0.02, rely=0, relwidth=0.1, relheight=0.12)

        # Produto
        fr_itens_nota_prod = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_prod.place(relx=0.005, rely=0.15, relwidth=0.18, relheight=0.7)

        lb_itens_nota_prod = customtkinter.CTkLabel(fr_itens_nota_prod, text="Produto")
        lb_itens_nota_prod.place(relx=0.2, rely=0, relwidth=0.4, relheight=0.6)

        self.produtos = []
        self.entry_itens_nota_prod_descr = AutocompleteCombobox(fr_itens_nota_prod, width=30, font=('Times', 11), completevalues=self.produtos)
        self.entry_itens_nota_prod_descr.place(relx=0.02, rely=0.5, relwidth=0.85, relheight=0.4)
        self.entry_itens_nota_prod_descr.bind("<Button-1>", lambda event: self.atualizar_produto(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_prod_descr))
        self.entry_itens_nota_prod_descr.bind('<Down>', lambda event: self.atualizar_produto(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_prod_descr))
        self.entry_itens_nota_prod_descr.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_centro))

        # Botão Cadastrar Produtos
        self.bt_itens_nota_produto = customtkinter.CTkButton(fr_itens_nota_prod, text='...', font=('Arial', 30), fg_color='green', command=self.cad_produtos)
        self.bt_itens_nota_produto.place(relx=0.88, rely=0.5, relwidth=0.09, relheight=0.35)
        self.bt_itens_nota_produto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_centro))

        # Centro de Resultado
        fr_itens_nota_centro_result = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_centro_result.place(relx=0.19, rely=0.15, relwidth=0.18, relheight=0.7)

        lb_itens_nota_centro = customtkinter.CTkLabel(fr_itens_nota_centro_result, text='Centro de Resultado')
        lb_itens_nota_centro.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.6)

        self.centro_resultado = []
        self.entry_itens_nota_centro = AutocompleteCombobox(fr_itens_nota_centro_result, width=30, font=('Times', 11), completevalues=self.centro_resultado)
        self.entry_itens_nota_centro.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_itens_nota_centro.bind("<Button-1>", lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_centro))
        self.entry_itens_nota_centro.bind('<Down>', lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_centro))
        self.entry_itens_nota_centro.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_natureza))

        # Natureza Financeira
        fr_itens_nota_natureza = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_natureza.place(relx=0.375, rely=0.15, relwidth=0.18, relheight=0.7)

        lb_itens_nota_natureza = customtkinter.CTkLabel(fr_itens_nota_natureza, text="Natureza Financeira")
        lb_itens_nota_natureza.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.6)

        self.natureza_financeira = []
        self.entry_itens_nota_natureza = AutocompleteCombobox(fr_itens_nota_natureza, width=30, font=('Times', 11), completevalues=self.natureza_financeira)
        self.entry_itens_nota_natureza.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_itens_nota_natureza.bind("<Button-1>", lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_natureza))
        self.entry_itens_nota_natureza.bind('<Down>', lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.combo_empresa.get(), janela_lanc), self.entry_itens_nota_natureza))
        self.entry_itens_nota_natureza.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_peso))

        # Peso
        fr_itens_nota_peso = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_peso.place(relx=0.56, rely=0.15, relwidth=0.10, relheight=0.7)

        lb_itens_nota_peso = customtkinter.CTkLabel(fr_itens_nota_peso, text="Peso")
        lb_itens_nota_peso.place(relx=0.15, rely=0, relwidth=0.70, relheight=0.6)

        self.entry_itens_nota_peso = customtkinter.CTkEntry(fr_itens_nota_peso, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_itens_nota_peso.place(relx=0.04, rely=0.5, relwidth=0.92, relheight=0.4)
        self.entry_itens_nota_peso.bind("<Return>", lambda event: self.format_valor(event, self.entry_itens_nota_peso))
        self.entry_itens_nota_peso.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_quant2))

        # Quant/Valores
        fr_itens_nota_quant = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_quant.place(relx=0.665, rely=0.1, relwidth=0.33, relheight=0.7)

        lb_itens_nota_quant = customtkinter.CTkLabel(fr_itens_nota_quant, text="Quant./Valores")
        lb_itens_nota_quant.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.25)

        lb_itens_nota_quant2 = customtkinter.CTkLabel(fr_itens_nota_quant, text="Quant.")
        lb_itens_nota_quant2.place(relx=0.03, rely=0.25, relwidth=0.29, relheight=0.25)
        self.entry_itens_nota_quant2 = customtkinter.CTkEntry(fr_itens_nota_quant, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_itens_nota_quant2.place(relx=0.03, rely=0.5, relwidth=0.29, relheight=0.4)
        self.entry_itens_nota_quant2.bind("<Return>", lambda event: self.format_valor(event, self.entry_itens_nota_quant2))
        self.entry_itens_nota_quant2.bind("<Return>", lambda event: self.calcular_total_itens(event, self.entry_itens_nota_valor_total))
        self.entry_itens_nota_quant2.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_valor_unit))

        lb_itens_nota_valor_unit = customtkinter.CTkLabel(fr_itens_nota_quant, text="Valor Unit.")
        lb_itens_nota_valor_unit.place(relx=0.35, rely=0.25, relwidth=0.29, relheight=0.25)
        self.entry_itens_nota_valor_unit = customtkinter.CTkEntry(fr_itens_nota_quant, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_itens_nota_valor_unit.place(relx=0.35, rely=0.5, relwidth=0.29, relheight=0.4)
        self.entry_itens_nota_valor_unit.bind("<Return>", lambda event: self.format_valor(event, self.entry_itens_nota_valor_unit))
        self.entry_itens_nota_valor_unit.bind("<Return>", lambda event: self.calcular_total_itens(event, self.entry_itens_nota_valor_total))
        self.entry_itens_nota_valor_unit.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_itens_nota_valor_unit))

        lb_itens_nota_valor_total = customtkinter.CTkLabel(fr_itens_nota_quant, text="Valor Total")
        lb_itens_nota_valor_total.place(relx=0.67, rely=0.25, relwidth=0.29, relheight=0.25)
        self.entry_itens_nota_valor_total = customtkinter.CTkEntry(fr_itens_nota_quant, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_itens_nota_valor_total.place(relx=0.67, rely=0.5, relwidth=0.29, relheight=0.4)

    def linha5_lanc(self, janela_lanc):
        
        # Widgets - Listar Itens
        self.LItens = ttk.Treeview(janela_lanc, height=12, column=('Item', 'Produto', 'Centro', 'Natureza', 'Peso', 'Quantidade', 'vlr_unitario', 'vlr_total'), show='headings')
        self.LItens.heading('Item', text="Item")
        self.LItens.column('Item', width=15, anchor='e')
        self.LItens.heading('Produto', text="Produto")
        self.LItens.column('Produto', width=300, anchor='w')
        self.LItens.heading('Centro', text="Centro Resultado")
        self.LItens.column('Centro', width=250, anchor='w')
        self.LItens.heading('Natureza', text="Natureza Financeira")
        self.LItens.column('Natureza', width=250, anchor='w')
        self.LItens.heading('Peso', text="Peso")
        self.LItens.column('Peso', width=100, anchor='e')
        self.LItens.heading('Quantidade', text="Quantidade")
        self.LItens.column('Quantidade', width=100, anchor='e')
        self.LItens.heading('vlr_unitario', text="Valor Unit.")
        self.LItens.column('vlr_unitario', width=100, anchor='e')
        self.LItens.heading('vlr_total', text="Valor Total")
        self.LItens.column('vlr_total', width=100, anchor='e')

        self.LItens.place(relx=0, rely=0.46, relwidth=1, relheight=0.47)
        # self.LItens.bind("<Double-1>", self.OnDoubleClick)
        self.entry_tipo_lcto_descr.focus()
        self.limpar_campos_lcto()

Lanc_fin()