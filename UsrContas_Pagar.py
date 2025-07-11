from UsrCadastros import *
from widgets import Widgets

class ContasPagar(Widgets, Pessoas, Produtos, Icons):
    def contas_pagar(self, principal_frame):
        self.images_base64()

        self.window_one.title('Contas a Pagar')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets_contas_pagar()


    def create_widgets_contas_pagar(self):
        # CNPJ
        self.fr_cnpj_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cnpj_contas.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_cnpj_contas = customtkinter.CTkLabel(self.fr_cnpj_contas, text="CNPJ")
        self.lb_cnpj_contas.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_cnpj_contas = customtkinter.CTkEntry(self.fr_cnpj_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_cnpj_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)
        self.entry_cnpj_contas.configure(state='readonly')

        # Razão Social
        self.fr_razao_social_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_razao_social_contas.place(relx=0.105, rely=0, relwidth=0.25, relheight=0.07)

        self.lb_razao_social_contas = customtkinter.CTkLabel(self.fr_razao_social_contas, text='Razão Social')
        self.lb_razao_social_contas.place(relx=0.35, rely=0, relwidth=0.25, relheight=0.25)

        self.entry_razao_social_contas = customtkinter.CTkEntry(self.fr_razao_social_contas, fg_color="white", text_color="black",
                                                           justify=tk.LEFT)
        self.entry_razao_social_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # CNPJ/CPF
        self.fr_cpf_cnpj_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cpf_cnpj_contas.place(relx=0.36, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_cpf_cnpj_contas = customtkinter.CTkLabel(self.fr_cpf_cnpj_contas, text="CNPJ/CPF")
        self.lb_cpf_cnpj_contas.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.25)

        self.entry_cpf_cnpj_contas = customtkinter.CTkEntry(self.fr_cpf_cnpj_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_cpf_cnpj_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Emissão
        self.fr_dt_emissao_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_dt_emissao_contas.place(relx=0.465, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_dt_emissao_contas = customtkinter.CTkLabel(self.fr_dt_emissao_contas, text="Emissão")
        self.lb_dt_emissao_contas.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_emissao_contas = customtkinter.CTkEntry(self.fr_dt_emissao_contas, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_emissao_contas.delete(0, 'end')
        self.entry_dt_emissao_contas.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_emissao_contas.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_emissao_contas.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_emissao_contas))
        self.entry_dt_emissao_contas.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_emissao_contas, self.entry_dt_emissao_contas))

        # Registro
        self.fr_dt_registro_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_dt_registro_contas.place(relx=0.57, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_dt_registro_contas = customtkinter.CTkLabel(self.fr_dt_registro_contas, text="Registro")
        self.lb_dt_registro_contas.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_registro_contas = customtkinter.CTkEntry(self.fr_dt_registro_contas, fg_color="white",
                                                              text_color="black", justify=tk.CENTER)
        self.entry_dt_registro_contas.delete(0, 'end')
        self.entry_dt_registro_contas.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_registro_contas.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_registro_contas.bind("<Button-1>",
                                          lambda event: self.calendario(event, self.entry_dt_registro_contas))
        self.entry_dt_registro_contas.bind("<Return>",
                                          lambda event: self.muda_barrinha_dta(event, self.entry_dt_registro_contas,
                                                                               self.entry_dt_registro_contas))

        # Vencimento
        self.fr_dt_vcto_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_dt_vcto_contas.place(relx=0.675, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_dt_vcto_contas = customtkinter.CTkLabel(self.fr_dt_vcto_contas, text="Vencimento")
        self.lb_dt_vcto_contas.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_dt_vcto_contas = customtkinter.CTkEntry(self.fr_dt_vcto_contas, fg_color="white",
                                                              text_color="black", justify=tk.CENTER)
        self.entry_dt_vcto_contas.delete(0, 'end')
        self.entry_dt_vcto_contas.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_vcto_contas.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_vcto_contas.bind("<Button-1>",
                                          lambda event: self.calendario(event, self.entry_dt_vcto_contas))
        self.entry_dt_vcto_contas.bind("<Return>",
                                          lambda event: self.muda_barrinha_dta(event, self.entry_dt_vcto_contas,
                                                                               self.entry_dt_vcto_contas))

        # P. Pagamento
        self.fr_dt_prev_pag_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_dt_prev_pag_contas.place(relx=0.78, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_dt_prev_pag_contas = customtkinter.CTkLabel(self.fr_dt_prev_pag_contas, text="Previsão de Pagamento")
        self.lb_dt_prev_pag_contas.place(relx=0.075, rely=0, relheight=0.25, relwidth=0.85)

        self.entry_dt_prev_pag_contas = customtkinter.CTkEntry(self.fr_dt_prev_pag_contas, fg_color="white",
                                                              text_color="black", justify=tk.CENTER)
        self.entry_dt_prev_pag_contas.delete(0, 'end')
        self.entry_dt_prev_pag_contas.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_prev_pag_contas.place(relx=0.05, rely=0.46, relwidth=0.9, relheight=0.50)
        self.entry_dt_prev_pag_contas.bind("<Button-1>",
                                          lambda event: self.calendario(event, self.entry_dt_prev_pag_contas))
        self.entry_dt_prev_pag_contas.bind("<Return>",
                                          lambda event: self.muda_barrinha_dta(event, self.entry_dt_prev_pag_contas,
                                                                               self.entry_dt_prev_pag_contas))

        # Nota Fiscal
        self.fr_nota_fiscal_notas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_nota_fiscal_notas.place(relx=0.885, rely=0, relwidth=0.1, relheight=0.07)

        self.lb_nota_fiscal_notas = customtkinter.CTkLabel(self.fr_nota_fiscal_notas, text="Nota Fiscal")
        self.lb_nota_fiscal_notas.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.25)

        self.entry_nota_fiscal_notas = customtkinter.CTkEntry(self.fr_nota_fiscal_notas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_nota_fiscal_notas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Tipo de Documento
        self.fr_tipo_doc_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tipo_doc_contas.place(relx=0, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_tipo_doc_contas = customtkinter.CTkLabel(self.fr_tipo_doc_contas, text="Tipo de Documento")
        self.lb_tipo_doc_contas.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_tp_doc_contas = customtkinter.CTkOptionMenu(self.fr_tipo_doc_contas, values=["Boleto", "Pix"], fg_color="white",
                                                       text_color="black")
        self.combo_tp_doc_contas.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Parcela
        self.fr_parcela_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_parcela_contas.place(relx=0.105, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_parcela_contas = customtkinter.CTkLabel(self.fr_parcela_contas, text="Parcela")
        self.lb_parcela_contas.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.25)

        self.entry_parcela_contas = customtkinter.CTkEntry(self.fr_parcela_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_parcela_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Categoria (Natureza)
        self.fr_cat_nat_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cat_nat_contas.place(relx=0.21, rely=0.075, relwidth=0.15, relheight=0.07)

        self.lb_cat_nat_contas = customtkinter.CTkLabel(self.fr_cat_nat_contas, text="Categoria (Natureza)")
        self.lb_cat_nat_contas.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.combo_cat_nat_contas = customtkinter.CTkOptionMenu(self.fr_cat_nat_contas, values=["Obras", "Água e Esgoto",
                                                            "Compra de Serviços"], fg_color="white", text_color="black")
        self.combo_cat_nat_contas.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)

        # Origem
        self.fr_origem_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_origem_contas.place(relx=0.365, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_origem_contas = customtkinter.CTkLabel(self.fr_origem_contas, text="Origem")
        self.lb_origem_contas.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.25)

        self.entry_origem_contas = customtkinter.CTkEntry(self.fr_origem_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_origem_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor da Conta
        self.fr_vlr_conta_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_conta_contas.place(relx=0.47, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_vlr_conta_contas = customtkinter.CTkLabel(self.fr_vlr_conta_contas, text="Valor da Conta")
        self.lb_vlr_conta_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_conta_contas = customtkinter.CTkEntry(self.fr_vlr_conta_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_vlr_conta_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor PIS
        self.fr_vlr_pis_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_pis_contas.place(relx=0.575, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_vlr_pis_contas = customtkinter.CTkLabel(self.fr_vlr_pis_contas, text="Valor PIS")
        self.lb_vlr_pis_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_pis_contas = customtkinter.CTkEntry(self.fr_vlr_pis_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_vlr_pis_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor COFINS
        self.fr_vlr_cofins_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_cofins_contas.place(relx=0.68, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_vlr_cofins_contas = customtkinter.CTkLabel(self.fr_vlr_cofins_contas, text="Valor COFINS")
        self.lb_vlr_cofins_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_cofins_contas = customtkinter.CTkEntry(self.fr_vlr_cofins_contas, fg_color="white", text_color="black",
                                                        justify=tk.CENTER)
        self.entry_vlr_cofins_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor CSLL
        self.fr_vlr_csll_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_csll_contas.place(relx=0.785, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_vlr_csll_contas = customtkinter.CTkLabel(self.fr_vlr_csll_contas, text="Valor CSLL")
        self.lb_vlr_csll_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_csll_contas = customtkinter.CTkEntry(self.fr_vlr_csll_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_csll_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor IR
        self.fr_vlr_ir_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_ir_contas.place(relx=0.89, rely=0.075, relwidth=0.1, relheight=0.07)

        self.lb_vlr_ir_contas = customtkinter.CTkLabel(self.fr_vlr_ir_contas, text="Valor IR")
        self.lb_vlr_ir_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_ir_contas = customtkinter.CTkEntry(self.fr_vlr_ir_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_ir_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor ISS
        self.fr_vlr_iss_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_iss_contas.place(relx=0, rely=0.15, relwidth=0.1, relheight=0.07)

        self.lb_vlr_iss_contas = customtkinter.CTkLabel(self.fr_vlr_iss_contas, text="Valor ISS")
        self.lb_vlr_iss_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_iss_contas = customtkinter.CTkEntry(self.fr_vlr_iss_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_iss_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor INSS
        self.fr_vlr_inss_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_inss_contas.place(relx=0.105, rely=0.15, relwidth=0.1, relheight=0.07)

        self.lb_vlr_inss_contas = customtkinter.CTkLabel(self.fr_vlr_inss_contas, text="Valor INSS")
        self.lb_vlr_inss_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_inss_contas = customtkinter.CTkEntry(self.fr_vlr_inss_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_inss_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor Líquido
        self.fr_vlr_liquido_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_liquido_contas.place(relx=0.21, rely=0.15, relwidth=0.1, relheight=0.07)

        self.lb_vlr_liquido_contas = customtkinter.CTkLabel(self.fr_vlr_liquido_contas, text="Valor Líquido")
        self.lb_vlr_liquido_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_liquido_contas = customtkinter.CTkEntry(self.fr_vlr_liquido_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_liquido_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Valor Pago
        self.fr_vlr_pago_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_pago_contas.place(relx=0.315, rely=0.15, relwidth=0.1, relheight=0.07)

        self.lb_vlr_pago_contas = customtkinter.CTkLabel(self.fr_vlr_pago_contas, text="Valor Pago")
        self.lb_vlr_pago_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_pago_contas = customtkinter.CTkEntry(self.fr_vlr_pago_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_pago_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # A Pagar
        self.fr_vlr_a_pagar_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_vlr_a_pagar_contas.place(relx=0.42, rely=0.15, relwidth=0.1, relheight=0.07)

        self.lb_vlr_a_pagar_contas = customtkinter.CTkLabel(self.fr_vlr_a_pagar_contas, text="A Pagar")
        self.lb_vlr_a_pagar_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_vlr_a_pagar_contas = customtkinter.CTkEntry(self.fr_vlr_a_pagar_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_vlr_a_pagar_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Conta Corrente de Pagamento
        self.fr_cta_corrente_contas = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_cta_corrente_contas.place(relx=0.525, rely=0.15, relwidth=0.35, relheight=0.07)

        self.lb_cta_corrente_contas = customtkinter.CTkLabel(self.fr_cta_corrente_contas, text="Conta Corrente de Pagamento")
        self.lb_cta_corrente_contas.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)

        self.entry_cta_corrente_contas = customtkinter.CTkEntry(self.fr_cta_corrente_contas, fg_color="white",
                                                              text_color="black",
                                                              justify=tk.CENTER)
        self.entry_cta_corrente_contas.place(relx=0.01, rely=0.5, relwidth=0.96, relheight=0.4)

        # Botão de consulta
        self.fr_botoes = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_botoes.place(relx=0.88, rely=0.15, relwidth=0.075, relheight=0.07)

        # Lupa
        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.fr_botoes, image=icone_pesquisa, text='',
                                                    fg_color='transparent', command=self.consulta_contas_a_pagar)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)
        self.btn_consulta.pack(pady=10)
        self.btn_consulta.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.6)

        # Botão de salvar
        icone_salvar = self.base64_to_photoimage('save')
        self.btn_salvar = customtkinter.CTkButton(self.fr_botoes, image=icone_salvar, text='',
                                                    fg_color='transparent', command=self.salvar_conta_a_pagar)
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=2)
        self.btn_salvar.pack(pady=10)
        self.btn_salvar.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # Resultado
        self.fr_tree = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_tree.place(relx=0, rely=0.225, relwidth=1, relheight=1)

        self.tree = ttk.Treeview(self.fr_tree, columns=(
            "Minha Empresa(CNPJ)", "Razão Social", "CNPJ/CPF", "Emissão", "Registro", "Vencimento", "Previsão de Pagamento",
            "Nota Fiscal", "Tipo de Documento", "Parcela", "Categoria(Natureza)", "Origem", "Valor da Conta", "Valor PIS",
            "Valor COFINS", "Valor CSLL", "Valor IR", "Valor ISS", "Valor Líquido", "Valor Pago", "A Pagar", "Conta Corrente de Pagamento",
        ), show='headings')

        # Atualiza o layout
        self.tree.update_idletasks()

        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        col_widths = [20, 35, 20, 10, 10, 10, 10, 10, 10, 10, 10, 15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 35]
        headers = ["Minha Empresa(CNPJ)", "Razão Social", "CNPJ/CPF", "Emissão", "Registro", "Vencimento", "Previsão de Pagamento",
            "Nota Fiscal", "Tipo de Documento", "Parcela", "Categoria(Natureza)", "Origem", "Valor da Conta", "Valor PIS",
            "Valor COFINS", "Valor CSLL", "Valor IR", "Valor ISS", "Valor Líquido", "Valor Pago", "A Pagar", "Conta Corrente de Pagamento",]

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

        self.tree.bind("<Double-1>", self.lusuarios_click)

        # Scrollbar
        scrollbar_y = ttk.Scrollbar(self.fr_tree, orient="vertical", command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(self.fr_tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Posiciona a Treeview e os Scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Configura o grid do frame
        self.fr_tree.grid_rowconfigure(0, weight=1)
        self.fr_tree.grid_columnconfigure(0, weight=1)

    def consulta_contas_a_pagar(self):
        pass


    def salvar_conta_a_pagar(self):
        pass


ContasPagar()