from imports import *

class Lanc_fin():
    def images_base64(self):
        self.btsave_base64 = "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"
        self.btsave_img = PhotoImage(data=base64.b64decode(self.btsave_base64))
        self.btsave_img = self.btsave_img.subsample(3,3)
        
        self.btsavedown_base64 = "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"
        self.btsavedown_img = PhotoImage(data=base64.b64decode(self.btsavedown_base64))
        self.btsavedown_img = self.btsavedown_img.subsample(5, 5)
        
        self.bttrash_base64 = "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"
        self.bttrash_img = PhotoImage(data=base64.b64decode(self.bttrash_base64))
        self.bttrash_img = self.bttrash_img.subsample(5, 5)
    def lancamentos(self):
        self.images_base64()

        self.window_one.title('Lançamentos Financeiros')
        self.clearFrame_principal()
        self.frame_dados(self.principal_frame)
        self.frame_novosnegocios(self.principal_frame)

        # self.janela_lanc = customtkinter.CTkToplevel(self.window_one)
        # self.janela_lanc.title('Lançamentos Financeiros')
        # self.janela_lanc.geometry("1180x650")

        # self.janela_lanc.resizable(True, True)

        self.linha1_lanc(self.principal_frame)
        self.linha2_lanc(self.principal_frame)
        self.linha3_lanc(self.principal_frame)
        self.linha4_lanc(self.principal_frame)
        self.linha5_lanc(self.principal_frame)

        self.janela_lanc.focus_force()
        self.janela_lanc.grab_set()
        self.janela_lanc.mainloop()
        
    def linha1_lanc(self, janela):
        # Tipo lançamento
        fr_tipo_lcto = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_tipo_lcto.place(relx=0, rely=0.02, relwidth=0.07, relheight=0.09)

        lb_tipo_lcto = customtkinter.CTkLabel(fr_tipo_lcto, text="Tipo Lçto")
        lb_tipo_lcto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        lb_tipo_lcto_descr = customtkinter.CTkLabel(fr_tipo_lcto, text="Descrição")
        lb_tipo_lcto_descr.place(relx=0.1, rely=0.25, relheight=0.25, relwidth=0.8)

        self.opcoes = ["CPA", "CRE", "CTA"]
        self.entry_tipo_lcto_descr = customtkinter.CTkComboBox(fr_tipo_lcto, fg_color="black", text_color="white", justify=tk.RIGHT, values=self.opcoes)
        self.entry_tipo_lcto_descr.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
        self.entry_tipo_lcto_descr.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_empresa))
        # self.entry_investimento_valor.bind("<Return>", lambda event: self.format_valor(event, self.entry_investimento_valor))

        # Empresa
        coordenadas_relx = 0.08
        coordenadas_rely = 0.02
        coordenadas_relwidth = 0.38
        coordenadas_relheight = 0.09
        self.frame_empresa(self.janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))

        # Cliente
        coordenadas_relx = 0.47
        coordenadas_rely = 0.02
        coordenadas_relwidth = 0.35
        coordenadas_relheight = 0.09
        self.frame_pessoa(self.janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_pessoa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_unidade_negocio))


        # Unidade Negocios
        coordenadas_relx = 0.83
        coordenadas_rely = 0.02
        coordenadas_relwidth = 0.17
        coordenadas_relheight = 0.09
        self.frame_Unidade_Negocio(self.janela_lanc, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_unidade_negocio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_unidade_descr))
                          
        # fr_unidade = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        # fr_unidade.place(relx=0.83, rely=0.02, relwidth=0.17, relheight=0.09)

        # lb_unidade = customtkinter.CTkLabel(fr_unidade, text="Unid. Negócios")
        # lb_unidade.place(relx=0.1, rely=0, relheight=0.25)
        # lb_unidade_cod = customtkinter.CTkLabel(fr_unidade, text="Código")
        # lb_unidade_cod.place(relx=0.02, rely=0.25, relheight=0.25, relwidth=0.25)

        # self.entry_unidade_cod = customtkinter.CTkEntry(fr_unidade)
        # self.entry_unidade_cod.place(relx=0.02, rely=0.5, relwidth=0.25, relheight=0.4)

        # lb_unidade_descr = customtkinter.CTkLabel(fr_unidade, text="Descrição")
        # lb_unidade_descr.place(relx=0.28, rely=0.25, relheight=0.25, relwidth=0.7)

        # self.entry_unidade_descr = customtkinter.CTkEntry(fr_unidade)
        # self.entry_unidade_descr.place(relx=0.28, rely=0.5, relwidth=0.7, relheight=0.4)
    
    def linha2_lanc(self):
        # Estado
        fr_uf = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_uf.place(relx=0, rely=0.115, relwidth=0.06, relheight=0.09)
        lb_estado = customtkinter.CTkLabel(fr_uf, text="Estado")
        lb_estado.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        lb_uf = customtkinter.CTkLabel(fr_uf, text="UF")
        lb_uf.place(relx=0.1, rely=0.25, relheight=0.25, relwidth=0.8)
        self.entry_uf = customtkinter.CTkEntry(fr_uf)
        self.entry_uf.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)

        # Frete
        fr_frete = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_frete.place(relx=0.07, rely=0.115, relwidth=0.32, relheight=0.09)
        lb_frete = customtkinter.CTkLabel(fr_frete, text="Frete")
        lb_frete.place(relx=0.05, rely=0, relheight=0.25, relwidth=0.15)
        lb_frete_cod = customtkinter.CTkLabel(fr_frete, text="Código")
        lb_frete_cod.place(relx=0.05, rely=0.25, relheight=0.25, relwidth=0.15)
        self.entry_frete_cod = customtkinter.CTkEntry(fr_frete)
        self.entry_frete_cod.place(relx=0.05, rely=0.5, relwidth=0.15, relheight=0.4)
        lb_frete_descr = customtkinter.CTkLabel(fr_frete, text="Descrição")
        lb_frete_descr.place(relx=0.25, rely=0.25, relheight=0.25, relwidth=0.7)
        self.entry_frete_descr = customtkinter.CTkEntry(fr_frete)
        self.entry_frete_descr.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.4)

        # Documentos
        fr_doc = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_doc.place(relx=0.4, rely=0.115, relwidth=0.6, relheight=0.09)
        lb_doc = customtkinter.CTkLabel(fr_doc, text="Documento")
        lb_doc.place(relx=0.01, rely=0, relheight=0.25, relwidth=0.15)

        lb_doc_num = customtkinter.CTkLabel(fr_doc, text="Nr. Documento")
        lb_doc_num.place(relx=0.01, rely=0.25, relheight=0.25, relwidth=0.12)
        self.entry_doc_num = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_num.place(relx=0.01, rely=0.5, relwidth=0.12, relheight=0.4)

        bt_doc1 = Button(fr_doc, image=self.bttrash_img)
        bt_doc1.place(relx=0.14, rely=0.45, relwidth=0.05, relheight=0.5)
        bt_doc2 = customtkinter.CTkButton(fr_doc, text="...")
        bt_doc2.place(relx=0.2, rely=0.45, relwidth=0.05, relheight=0.5)

        lb_doc_dt_emissao = customtkinter.CTkLabel(fr_doc, text="Data Emissão")
        lb_doc_dt_emissao.place(relx=0.26, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_dt_emissao = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_dt_emissao.place(relx=0.26, rely=0.5, relwidth=0.14, relheight=0.4)

        lb_doc_serie = customtkinter.CTkLabel(fr_doc, text="Série")
        lb_doc_serie.place(relx=0.41, rely=0.25, relheight=0.25, relwidth=0.08)
        self.entry_doc_serie = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_serie.place(relx=0.41, rely=0.5, relwidth=0.08, relheight=0.4)

        lb_doc_numcontrato = customtkinter.CTkLabel(fr_doc, text="Nr. Contrato")
        lb_doc_numcontrato.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_numcontrato = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_numcontrato.place(relx=0.5, rely=0.5, relwidth=0.14, relheight=0.4)

        lb_doc_valor_total = customtkinter.CTkLabel(fr_doc, text="Valor Total Doc.")
        lb_doc_valor_total.place(relx=0.65, rely=0.25, relheight=0.25, relwidth=0.14)
        self.entry_doc_valor_total = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_valor_total.place(relx=0.65, rely=0.5, relwidth=0.14, relheight=0.4)

        bt_doc3 = customtkinter.CTkButton(fr_doc, text="...")
        bt_doc3.place(relx=0.8, rely=0.45, relwidth=0.05, relheight=0.5)

        lb_doc_parcelas = customtkinter.CTkLabel(fr_doc, text="Nr. Parcelas")
        lb_doc_parcelas.place(relx=0.86, rely=0.25, relheight=0.25, relwidth=0.13)
        self.entry_doc_parcelas = customtkinter.CTkEntry(fr_doc)
        self.entry_doc_parcelas.place(relx=0.86, rely=0.5, relwidth=0.13, relheight=0.4)
    def linha3_lanc(self):
        # Informações de Pagamento
        fr_info_pag = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_info_pag.place(relx=0, rely=0.21, relwidth=0.22, relheight=0.18)
        lb_info_pag = customtkinter.CTkLabel(fr_info_pag, text="Informações de Pagamento")
        lb_info_pag.place(relx=0.02, rely=0, relheight=0.125, relwidth=0.6)

        lb_info_pag_nr_parc = customtkinter.CTkLabel(fr_info_pag, text="Parcela Nr.")
        lb_info_pag_nr_parc.place(relx=0.02, rely=0.125, relheight=0.125, relwidth=0.27)
        self.entry_info_pag_nr_parc = customtkinter.CTkEntry(fr_info_pag)
        self.entry_info_pag_nr_parc.place(relx=0.02, rely=0.25, relwidth=0.27, relheight=0.25)

        lb_info_pag_forma_liq = customtkinter.CTkLabel(fr_info_pag, text="Forma Liquidação")
        lb_info_pag_forma_liq.place(relx=0.3, rely=0.125, relheight=0.125, relwidth=0.69)
        self.entry_info_pag_forma_liq = customtkinter.CTkEntry(fr_info_pag)
        self.entry_info_pag_forma_liq.place(relx=0.3, rely=0.25, relwidth=0.69, relheight=0.25)

        lb_info_pag_dt_venc = customtkinter.CTkLabel(fr_info_pag, text="Data Vencto")
        lb_info_pag_dt_venc.place(relx=0.02, rely=0.5, relheight=0.125, relwidth=0.35)
        self.entry_info_pag_dt_venc = customtkinter.CTkEntry(fr_info_pag)
        self.entry_info_pag_dt_venc.place(relx=0.02, rely=0.625, relwidth=0.35, relheight=0.25)

        lb_info_pag_valor_parc = customtkinter.CTkLabel(fr_info_pag, text="Valor Parcela")
        lb_info_pag_valor_parc.place(relx=0.38, rely=0.5, relheight=0.125, relwidth=0.4)
        self.entry_info_pag_valor_parc = customtkinter.CTkEntry(fr_info_pag)
        self.entry_info_pag_valor_parc.place(relx=0.38, rely=0.625, relwidth=0.4, relheight=0.25)
        bt_info_pag_salvar = Button(fr_info_pag, image=self.btsavedown_img, bg="gray55")
        bt_info_pag_salvar.place(relx=0.8, rely=0.6, relwidth=0.15, relheight=0.3)

        ## Listbox _ Informações de Pagamento
        bg_color = self.janela_lanc._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self.janela_lanc._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self.janela_lanc._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color,
                            borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        # Widgets - Listar
        self.list_g = ttk.Treeview(self.janela_lanc, height=12, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.list_g.heading("#0", text="")
        self.list_g.column("#0", width=0)
        self.list_g.heading("#1", text="Nr.")
        self.list_g.column("#1", width=10)
        self.list_g.heading("#2", text="Vencimento")
        self.list_g.column("#2", width=100)
        self.list_g.heading("#3", text="Valor")
        self.list_g.column("#3", width=70)
        self.list_g.heading("#4", text="ID...")
        self.list_g.column("#4", width=10)
        self.list_g.heading("#5", text="DS Liquidação")
        self.list_g.column("#5", width=70)
        self.list_g.heading("#6", text="")
        self.list_g.column("#6", width=70)

        self.list_g.place(relx=0.23, rely=0.22, relwidth=0.4, relheight=0.16)
        #self.list_g.bind("<Double-1>", self.OnDoubleClick)

        ## Historico
        fr_historico = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_historico.place(relx=0.64, rely=0.21, relwidth=0.31, relheight=0.18)

        lb_historico = customtkinter.CTkLabel(fr_historico, text="Histórico")
        lb_historico.place(relx=0.02, rely=0, relwidth=0.4, relheight=0.125)

        self.text_historico = customtkinter.CTkTextbox(fr_historico)
        self.text_historico.place(relx=0.02, rely=0.125, relwidth=0.96, relheight=0.825)

        bt_pag_salvar = Button(self.janela_lanc, image=self.btsave_img, bg="gray55")
        bt_pag_salvar.place(relx=0.955, rely=0.21, relwidth=0.04, relheight=0.1)

        bt2_pag_salvar = Button(self.janela_lanc, image=self.btsavedown_img, bg="gray55")
        bt2_pag_salvar.place(relx=0.955, rely=0.32, relwidth=0.04, relheight=0.06)
    def linha4_lanc(self):
        fr_itens_nota = customtkinter.CTkFrame(self.janela_lanc, border_color="gray75", border_width=1)
        fr_itens_nota.place(relx=0, rely=0.395, relwidth=1, relheight=0.12)
        lb_itens_nota = customtkinter.CTkLabel(fr_itens_nota, text="Itens da Nota")
        lb_itens_nota.place(relx=0.09, rely=0, relwidth=0.1, relheight=0.12)

        # Produto
        fr_itens_nota_prod = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_prod.place(relx=0.005, rely=0.15, relwidth=0.18, relheight=0.8)

        lb_itens_nota_prod = customtkinter.CTkLabel(fr_itens_nota_prod, text="Produto")
        lb_itens_nota_prod.place(relx=0.05, rely=0, relwidth=0.4, relheight=0.25)

        lb_itens_nota_prod_cod = customtkinter.CTkLabel(fr_itens_nota_prod, text="Código")
        lb_itens_nota_prod_cod.place(relx=0.02, rely=0.25, relwidth=0.25, relheight=0.25)
        self.lb_itens_nota_prod_cod = customtkinter.CTkEntry(fr_itens_nota_prod)
        self.lb_itens_nota_prod_cod.place(relx=0.02, rely=0.5, relwidth=0.25, relheight=0.4)

        lb_itens_nota_prod_descr = customtkinter.CTkLabel(fr_itens_nota_prod, text="Descrição")
        lb_itens_nota_prod_descr.place(relx=0.28, rely=0.25, relwidth=0.35, relheight=0.25)
        self.lb_itens_nota_prod_descr = customtkinter.CTkEntry(fr_itens_nota_prod)
        self.lb_itens_nota_prod_descr.place(relx=0.28, rely=0.5, relwidth=0.6, relheight=0.4)

        bt_itens_nota_produto = customtkinter.CTkButton(fr_itens_nota_prod, text="...")
        bt_itens_nota_produto.place(relx=0.9, rely=0.45, relwidth=0.08, relheight=0.5)

        # Centro de Resultado
        fr_itens_nota_centro_result = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_centro_result.place(relx=0.19, rely=0.15, relwidth=0.2, relheight=0.8)

        lb_itens_nota_centro = customtkinter.CTkLabel(fr_itens_nota_centro_result, text="Centro de Resultado")
        lb_itens_nota_centro.place(relx=0.05, rely=0, relwidth=0.6, relheight=0.25)

        lb_itens_nota_centro = customtkinter.CTkLabel(fr_itens_nota_centro_result, text="Código")
        lb_itens_nota_centro.place(relx=0.075, rely=0.25, relwidth=0.25, relheight=0.25)
        self.lb_itens_nota_centro = customtkinter.CTkEntry(fr_itens_nota_centro_result)
        self.lb_itens_nota_centro.place(relx=0.075, rely=0.5, relwidth=0.25, relheight=0.4)

        lb_itens_nota_centro = customtkinter.CTkLabel(fr_itens_nota_centro_result, text="Descrição")
        lb_itens_nota_centro.place(relx=0.335, rely=0.25, relwidth=0.35, relheight=0.25)
        self.lb_itens_nota_centro = customtkinter.CTkEntry(fr_itens_nota_centro_result)
        self.lb_itens_nota_centro.place(relx=0.335, rely=0.5, relwidth=0.6, relheight=0.4)

        # Natureza Financeira
        fr_itens_nota_natureza = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_natureza.place(relx=0.395, rely=0.15, relwidth=0.2, relheight=0.8)

        lb_itens_nota_natureza = customtkinter.CTkLabel(fr_itens_nota_natureza, text="Natureza Financeira")
        lb_itens_nota_natureza.place(relx=0.05, rely=0, relwidth=0.6, relheight=0.25)

        lb_itens_nota_natureza = customtkinter.CTkLabel(fr_itens_nota_natureza, text="Código")
        lb_itens_nota_natureza.place(relx=0.075, rely=0.25, relwidth=0.25, relheight=0.25)
        self.lb_itens_nota_natureza = customtkinter.CTkEntry(fr_itens_nota_natureza)
        self.lb_itens_nota_natureza.place(relx=0.075, rely=0.5, relwidth=0.25, relheight=0.4)

        lb_itens_nota_natureza = customtkinter.CTkLabel(fr_itens_nota_natureza, text="Descrição")
        lb_itens_nota_natureza.place(relx=0.335, rely=0.25, relwidth=0.35, relheight=0.25)
        self.lb_itens_nota_natureza = customtkinter.CTkEntry(fr_itens_nota_natureza)
        self.lb_itens_nota_natureza.place(relx=0.335, rely=0.5, relwidth=0.6, relheight=0.4)

        # Peso
        fr_itens_nota_peso = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_peso.place(relx=0.6, rely=0.15, relwidth=0.195, relheight=0.8)

        lb_itens_nota_peso = customtkinter.CTkLabel(fr_itens_nota_peso, text="Peso")
        lb_itens_nota_peso.place(relx=0.05, rely=0, relwidth=0.2, relheight=0.25)

        lb_itens_nota_peso_tara = customtkinter.CTkLabel(fr_itens_nota_peso, text="Tara")
        lb_itens_nota_peso_tara.place(relx=0.04, rely=0.25, relwidth=0.2, relheight=0.25)
        self.lb_itens_nota_peso_tara = customtkinter.CTkEntry(fr_itens_nota_peso)
        self.lb_itens_nota_peso_tara.place(relx=0.04, rely=0.5, relwidth=0.2, relheight=0.4)

        lb_itens_nota_peso_bruto = customtkinter.CTkLabel(fr_itens_nota_peso, text="Bruto")
        lb_itens_nota_peso_bruto.place(relx=0.28, rely=0.25, relwidth=0.2, relheight=0.25)
        self.lb_itens_nota_peso_bruto = customtkinter.CTkEntry(fr_itens_nota_peso)
        self.lb_itens_nota_peso_bruto.place(relx=0.28, rely=0.5, relwidth=0.2, relheight=0.4)

        lb_itens_nota_peso_liq = customtkinter.CTkLabel(fr_itens_nota_peso, text="Liquido")
        lb_itens_nota_peso_liq.place(relx=0.52, rely=0.25, relwidth=0.2, relheight=0.25)
        self.lb_itens_nota_peso_liq = customtkinter.CTkEntry(fr_itens_nota_peso)
        self.lb_itens_nota_peso_liq.place(relx=0.52, rely=0.5, relwidth=0.2, relheight=0.4)

        lb_itens_nota_peso_roman = customtkinter.CTkLabel(fr_itens_nota_peso, text="Roman.")
        lb_itens_nota_peso_roman.place(relx=0.76, rely=0.25, relwidth=0.2, relheight=0.25)
        self.lb_itens_nota_peso_roman = customtkinter.CTkEntry(fr_itens_nota_peso)
        self.lb_itens_nota_peso_roman.place(relx=0.76, rely=0.5, relwidth=0.2, relheight=0.4)

        # Quant/Valores
        fr_itens_nota_quant = customtkinter.CTkFrame(fr_itens_nota, border_color="gray75", border_width=1)
        fr_itens_nota_quant.place(relx=0.8, rely=0.15, relwidth=0.195, relheight=0.8)

        lb_itens_nota_quant = customtkinter.CTkLabel(fr_itens_nota_quant, text="Quant./Valores")
        lb_itens_nota_quant.place(relx=0.05, rely=0, relwidth=0.4, relheight=0.25)

        lb_itens_nota_quant2 = customtkinter.CTkLabel(fr_itens_nota_quant, text="Quant.")
        lb_itens_nota_quant2.place(relx=0.03, rely=0.25, relwidth=0.29, relheight=0.25)
        self.lb_itens_nota_quant2 = customtkinter.CTkEntry(fr_itens_nota_quant)
        self.lb_itens_nota_quant2.place(relx=0.03, rely=0.5, relwidth=0.29, relheight=0.4)

        lb_itens_nota_valor_unit = customtkinter.CTkLabel(fr_itens_nota_quant, text="Valor Unit.")
        lb_itens_nota_valor_unit.place(relx=0.35, rely=0.25, relwidth=0.29, relheight=0.25)
        self.lb_itens_nota_valor_unit = customtkinter.CTkEntry(fr_itens_nota_quant)
        self.lb_itens_nota_valor_unit.place(relx=0.35, rely=0.5, relwidth=0.29, relheight=0.4)

        lb_itens_nota_valor_total = customtkinter.CTkLabel(fr_itens_nota_quant, text="Valor Total")
        lb_itens_nota_valor_total.place(relx=0.67, rely=0.25, relwidth=0.29, relheight=0.25)
        self.lb_itens_nota_valor_total = customtkinter.CTkEntry(fr_itens_nota_quant)
        self.lb_itens_nota_valor_total.place(relx=0.67, rely=0.5, relwidth=0.29, relheight=0.4)
    def linha5_lanc(self):
        # Widgets - Listar
        self.list_g = ttk.Treeview(self.janela_lanc, height=12, column=("col1", "col2", "col3", "col4", "col5", "col6",
                "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14"))
        self.list_g.heading("#0", text="")
        self.list_g.column("#0", width=0)
        self.list_g.heading("#1", text="Item")
        self.list_g.column("#1", width=50)
        self.list_g.heading("#2", text="Código")
        self.list_g.column("#2", width=50)
        self.list_g.heading("#3", text="Descrição Produto")
        self.list_g.column("#3", width=100)
        self.list_g.heading("#4", text="Código")
        self.list_g.column("#4", width=50)
        self.list_g.heading("#5", text="Descrição Centro..")
        self.list_g.column("#5", width=100)
        self.list_g.heading("#6", text="Codigo")
        self.list_g.column("#6", width=50)
        self.list_g.heading("#7", text="Descrição Natureza")
        self.list_g.column("#7", width=100)
        self.list_g.heading("#8", text="Tara")
        self.list_g.column("#8", width=100)
        self.list_g.heading("#9", text="Bruto")
        self.list_g.column("#9", width=100)
        self.list_g.heading("#10", text="Líq.")
        self.list_g.column("#10", width=100)
        self.list_g.heading("#11", text="Roman")
        self.list_g.column("#11", width=100)
        self.list_g.heading("#12", text="Quantidade")
        self.list_g.column("#12", width=70)
        self.list_g.heading("#13", text="Valor Unit.")
        self.list_g.column("#13", width=70)
        self.list_g.heading("#14", text="Valor Total.")
        self.list_g.column("#14", width=70)

        self.list_g.place(relx=0, rely=0.52, relwidth=1, relheight=0.47)
        # self.list_g.bind("<Double-1>", self.OnDoubleClick)

Lanc_fin()