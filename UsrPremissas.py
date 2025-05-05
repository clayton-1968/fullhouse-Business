from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Premissas_Orcamento(Widgets):
    def premissas_orcamento(self, ID_Empresa, DS_Empresa, ID_Orc, DS_Orc, ID_Lcto):
        self.janela_premissas = customtkinter.CTkToplevel(self.window_one)
        self.janela_premissas.title('Cadastro de Premissas Orçamentárias')
        width = self.janela_premissas.winfo_screenwidth()
        height = self.janela_premissas.winfo_screenheight()
        self.janela_premissas.geometry(f"{width}x{height}+0+0") 
        self.janela_premissas.resizable(True, True)
        self.janela_premissas.lift()  # Traz a janela para frente   
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_premissas.protocol("WM_DELETE_WINDOW", self.on_closing_tela_premissas)

        self.frame_linha_1(self.janela_premissas)
        self.frame_linha_2(self.janela_premissas)
        self.frame_linha_3(self.janela_premissas)
        self.frame_linha_4(self.janela_premissas)
        self.frame_linha_5(self.janela_premissas)
        self.frame_linha_6(self.janela_premissas)
        self.limpar_campos_premissas()
        self.frame_premissa_dados(
                                  ID_Empresa, 
                                  DS_Empresa, 
                                  ID_Orc,
                                  DS_Orc, 
                                  ID_Lcto)
        
        self.janela_premissas.focus_force()
        self.janela_premissas.grab_set()
       
################# dividindo a janela ###############
    def frame_linha_1(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.375
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa", anchor='w')
        lb_empresa.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_orcamento))

        # Orçamento
        coordenadas_relx = 0.385
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_orcamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_orcamento.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_orcamento = customtkinter.CTkLabel(fr_orcamento, text="Orçamento", anchor='w')
        lb_orcamento.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        orcamentos = []

        self.entry_orcamento = AutocompleteCombobox(fr_orcamento, width=30, font=('Times', 11), completevalues=orcamentos)
        self.entry_orcamento.pack()
        self.entry_orcamento.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_orcamento.bind("<Button-1>", lambda event: self.atualizar_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_orcamento))
        self.entry_orcamento.bind("<KeyRelease>", lambda event: self.atualizar_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_orcamento))
        self.entry_orcamento.bind('<Down>', lambda event: self.atualizar_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_orcamento))
        self.entry_orcamento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tipo_lcto_descr))
        
        # Tipo Lançamento
        fr_tpo_lancamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tpo_lancamento.place(relx=0.64, rely=0.01,relwidth=0.10, relheight=0.07)
        lb_tpo_lancamento = customtkinter.CTkLabel(fr_tpo_lancamento, text="Tipo Lçto", anchor='w')
        lb_tpo_lancamento.place(relx=0.009, rely=0.01, relheight=0.30, relwidth=0.55)

        self.opcoes_lcto = ["CPA", "CRE", "CTA"]
        self.entry_tipo_lcto_descr = customtkinter.CTkComboBox(fr_tpo_lancamento, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes_lcto)
        self.entry_tipo_lcto_descr.place(relx=0.005, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_tipo_lcto_descr.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_status_lcto))

        # Status
        fr_status_lancamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_status_lancamento.place(relx=0.745, rely=0.01,relwidth=0.10, relheight=0.07)
        lb_status_lancamento = customtkinter.CTkLabel(fr_status_lancamento, text="Status", anchor='w')
        lb_status_lancamento.place(relx=0.009, rely=0.01, relheight=0.30, relwidth=0.55)

        self.opcoes = ["Ativo", "Excluído"]
        self.entry_status_lcto = customtkinter.CTkComboBox(fr_status_lancamento, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_status_lcto.place(relx=0.005, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_status_lcto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_centro_debito))

        # ID do Lançamento
        fr_id_lancamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_id_lancamento.place(relx=0.85, rely=0.01,relwidth=0.10, relheight=0.07)
        lb_id_lancamento = customtkinter.CTkLabel(fr_id_lancamento, text="ID Lançamento", anchor='w')
        lb_id_lancamento.place(relx=0.009, rely=0.01, relheight=0.30, relwidth=0.55)

        self.entry_id_lcto = customtkinter.CTkEntry(fr_id_lancamento, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_id_lcto.place(relx=0.005, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_id_lcto.configure(state='disabled')
        
        # Botão de Gravar
        icon_image = self.base64_to_photoimage('save')
        self.btn_gravar_premissas = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=self.gravar_premissas)
        self.btn_gravar_premissas.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)

    def frame_linha_2(self, janela):
        # Débito
        coordenadas_relx = 0.005
        coordenadas_rely = 0.085
        coordenadas_relwidth = 0.99
        coordenadas_relheight = 0.10
        fr_lacto_debito = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_lacto_debito.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_lacto_debito = customtkinter.CTkLabel(fr_lacto_debito, text="a Débito", anchor='w', font=("Arial", 16, "bold"))
        lb_lacto_debito.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.99)

        # Centro de Resultado Débito
        fr_centro_debito = customtkinter.CTkFrame(fr_lacto_debito, border_color="gray75", border_width=1)
        fr_centro_debito.place(relx=0.005, rely=0.40,relwidth=0.4925, relheight=0.55)
        lb_centro_debito = customtkinter.CTkLabel(fr_centro_debito, text="Centro de Resultado", anchor='w')
        lb_centro_debito.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        centro_debito = []
        self.entry_centro_debito = AutocompleteCombobox(fr_centro_debito, width=30, font=('Times', 11), completevalues=centro_debito)
        self.entry_centro_debito.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_centro_debito.bind("<Button-1>", lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_debito))
        self.entry_centro_debito.bind("<KeyRelease>", lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_debito))
        self.entry_centro_debito.bind('<Down>', lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_debito))
        self.entry_centro_debito.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_natureza_debito))
        
        
        # Natureza Débito
        fr_natureza_debito = customtkinter.CTkFrame(fr_lacto_debito, border_color="gray75", border_width=1)
        fr_natureza_debito.place(relx=0.5025, rely=0.40,relwidth=0.4925, relheight=0.55)
        lb_natureza_debito = customtkinter.CTkLabel(fr_natureza_debito, text="Natureza Financeira", anchor='w')
        lb_natureza_debito.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        natureza_debito = []
        self.entry_natureza_debito = AutocompleteCombobox(fr_natureza_debito, width=30, font=('Times', 11), completevalues=natureza_debito)
        self.entry_natureza_debito.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_natureza_debito.bind("<Button-1>", lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_debito))
        self.entry_natureza_debito.bind("<KeyRelease>", lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_debito))
        self.entry_natureza_debito.bind('<Down>', lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_debito))
        self.entry_natureza_debito.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_centro_credito))

    def frame_linha_3(self, janela):
        # Crédito
        coordenadas_relx = 0.005
        coordenadas_rely = 0.19
        coordenadas_relwidth = 0.99
        coordenadas_relheight = 0.10
        fr_lacto_credito = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_lacto_credito.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_lacto_debito = customtkinter.CTkLabel(fr_lacto_credito, text="a Crédito", anchor='w', font=("Arial", 16, "bold"))
        lb_lacto_debito.place(relx=0.005, rely=0.01, relheight=0.25, relwidth=0.99)

        # Centro de Resultado Crédito
        fr_centro_credito = customtkinter.CTkFrame(fr_lacto_credito, border_color="gray75", border_width=1)
        fr_centro_credito.place(relx=0.005, rely=0.40,relwidth=0.4925, relheight=0.55)
        lb_centro_credito = customtkinter.CTkLabel(fr_centro_credito, text="Centro de Resultado", anchor='w')
        lb_centro_credito.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        centro_credito = []
        self.entry_centro_credito = AutocompleteCombobox(fr_centro_credito, width=30, font=('Times', 11), completevalues=centro_credito)
        self.entry_centro_credito.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_centro_credito.bind("<Button-1>", lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_credito))
        self.entry_centro_credito.bind("<KeyRelease>", lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_credito))
        self.entry_centro_credito.bind('<Down>', lambda event: self.atualizar_centro_resultado(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_centro_credito))
        self.entry_centro_credito.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_natureza_credito))
        
        # Natureza Crédito
        fr_natureza_credito = customtkinter.CTkFrame(fr_lacto_credito, border_color="gray75", border_width=1)
        fr_natureza_credito.place(relx=0.5025, rely=0.40,relwidth=0.4925, relheight=0.55)
        lb_natureza_credito = customtkinter.CTkLabel(fr_natureza_credito, text="Natureza Financeira", anchor='w')
        lb_natureza_credito.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        natureza_credito = []
        self.entry_natureza_credito = AutocompleteCombobox(fr_natureza_credito, width=30, font=('Times', 11), completevalues=natureza_credito)
        self.entry_natureza_credito.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_natureza_credito.bind("<Button-1>", lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_credito))
        self.entry_natureza_credito.bind("<KeyRelease>", lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_credito))
        self.entry_natureza_credito.bind('<Down>', lambda event: self.atualizar_natureza_financeira(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_natureza_credito))
        self.entry_natureza_credito.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_item_preco))
    
    def frame_linha_4(self, janela):
        # Item
        coordenadas_relx = 0.005
        coordenadas_rely = 0.295
        coordenadas_relwidth = 0.99
        coordenadas_relheight = 0.10
        fr_lacto_item = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_lacto_item.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_lacto_item = customtkinter.CTkLabel(fr_lacto_item, text="Item", anchor='w', font=("Arial", 16, "bold"))
        lb_lacto_item.place(relx=0.005, rely=0.01, relheight=0.25, relwidth=0.99)

        # Item
        fr_item = customtkinter.CTkFrame(fr_lacto_item, border_color="gray75", border_width=1)
        fr_item.place(relx=0.005, rely=0.40,relwidth=0.4925, relheight=0.55)
        lb_item = customtkinter.CTkLabel(fr_item, text="Item", anchor='w')
        lb_item.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        item_preco = []

        self.entry_item_preco = AutocompleteCombobox(fr_item, width=30, font=('Times', 11), completevalues=item_preco)
        self.entry_item_preco.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_item_preco.bind("<Button-1>", lambda event: self.atualizar_item_precos_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.obter_Orc_ID(self.entry_orcamento.get(), janela), self.entry_item_preco))
        self.entry_item_preco.bind("<KeyRelease>", lambda event: self.atualizar_item_precos_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.obter_Orc_ID(self.entry_orcamento.get(), janela), self.entry_item_preco))
        self.entry_item_preco.bind('<Down>', lambda event: self.atualizar_item_precos_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.obter_Orc_ID(self.entry_orcamento.get(), janela), self.entry_item_preco))
        self.entry_item_preco.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_volume_valor))
        
        # Volume
        fr_volume = customtkinter.CTkFrame(fr_lacto_item, border_color="gray75", border_width=1)
        fr_volume.place(relx=0.5025, rely=0.40,relwidth=0.10, relheight=0.55)
        lb_volume = customtkinter.CTkLabel(fr_volume, text=" Volume", anchor='w')
        lb_volume.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        self.entry_volume_valor = customtkinter.CTkEntry(fr_volume, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_volume_valor.place(relx=0.005, rely=0.40, relwidth=0.985, relheight=0.55)
        self.entry_volume_valor.bind("<Return>", lambda event: self.format_valor(event, self.entry_volume_valor))
        self.entry_volume_valor.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_natureza_gerencial))

        # Tipo da Natureza Gerencial
        fr_natureza_gerencial = customtkinter.CTkFrame(fr_lacto_item, border_color="gray75", border_width=1)
        fr_natureza_gerencial.place(relx=0.6075, rely=0.40,relwidth=0.3875, relheight=0.55)
        lb_natureza_gerencial = customtkinter.CTkLabel(fr_natureza_gerencial, text="Natureza Gerencial", anchor='w')
        lb_natureza_gerencial.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        natureza_gerencial = []

        self.entry_natureza_gerencial = AutocompleteCombobox(fr_natureza_gerencial, width=30, font=('Times', 11), completevalues=natureza_gerencial)
        self.entry_natureza_gerencial.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_natureza_gerencial.bind("<Button-1>", lambda event: self.atualizar_natureza_gerencial(event, self.entry_natureza_gerencial))
        self.entry_natureza_gerencial.bind("<KeyRelease>", lambda event: self.atualizar_natureza_gerencial(event, self.entry_natureza_gerencial))
        self.entry_natureza_gerencial.bind('<Down>', lambda event: self.atualizar_natureza_gerencial(event, self.entry_natureza_gerencial))
        self.entry_natureza_gerencial.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_periodicidade))
    
    def frame_linha_5(self, janela):
        # Períodos e Indices
        coordenadas_relx = 0.005
        coordenadas_rely = 0.40
        coordenadas_relwidth = 0.99
        coordenadas_relheight = 0.10
        fr_lacto_periodos = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_lacto_periodos.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_lacto_periodos = customtkinter.CTkLabel(fr_lacto_periodos, text="Períodos e Indices", anchor='w', font=("Arial", 16, "bold"))
        lb_lacto_periodos.place(relx=0.005, rely=0.01, relheight=0.25, relwidth=0.99)

        # Periodicidade
        fr_periodicidade = customtkinter.CTkFrame(fr_lacto_periodos, border_color="gray75", border_width=1)
        fr_periodicidade.place(relx=0.005, rely=0.40,relwidth=0.20, relheight=0.55)
        lb_periodicidade = customtkinter.CTkLabel(fr_periodicidade, text="Periodicidade", anchor='w')
        lb_periodicidade.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        periodicidade = []

        self.entry_periodicidade = AutocompleteCombobox(fr_periodicidade, width=30, font=('Times', 11), completevalues=periodicidade)
        self.entry_periodicidade.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_periodicidade.bind("<Button-1>", lambda event: self.atualizar_periodicidade(event, self.entry_periodicidade))
        self.entry_periodicidade.bind("<KeyRelease>", lambda event: self.atualizar_periodicidade(event, self.entry_periodicidade))
        self.entry_periodicidade.bind('<Down>', lambda event: self.atualizar_periodicidade(event, self.entry_periodicidade))
        self.entry_periodicidade.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_indices_reajuste))
        
        # Indices de Reajuste
        fr_indices_reajuste = customtkinter.CTkFrame(fr_lacto_periodos, border_color="gray75", border_width=1)
        fr_indices_reajuste.place(relx=0.21, rely=0.40,relwidth=0.20, relheight=0.55)
        lb_indices_reajuste = customtkinter.CTkLabel(fr_indices_reajuste, text="Indice de Reajuste", anchor='w')
        lb_indices_reajuste.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        indices_reajuste = []

        self.entry_indices_reajuste = AutocompleteCombobox(fr_indices_reajuste, width=30, font=('Times', 11), completevalues=indices_reajuste)
        self.entry_indices_reajuste.place(relx=0.005, rely=0.5, relwidth=0.7275, relheight=0.4)
        self.entry_indices_reajuste.bind("<Button-1>", lambda event: self.atualizar_idx(event, self.entry_indices_reajuste))
        self.entry_indices_reajuste.bind("<KeyRelease>", lambda event: self.atualizar_idx(event, self.entry_indices_reajuste))
        self.entry_indices_reajuste.bind('<Down>', lambda event: self.atualizar_idx(event, self.entry_indices_reajuste))
        self.entry_indices_reajuste.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_dt_reajuste))

        Dta_Reajuste = datetime.now() # ajustar para final do mês

        lb_dt_reajuste = customtkinter.CTkLabel(fr_indices_reajuste, text="Data Reajuste", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_dt_reajuste.place(relx=0.7475, rely=0.30, relheight=0.125, relwidth=0.20)
        self.entry_dt_reajuste = customtkinter.CTkEntry(fr_indices_reajuste, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_dt_reajuste.delete(0, 'end')
        self.entry_dt_reajuste.insert(0, Dta_Reajuste.strftime("%d/%m/%Y"))
        self.entry_dt_reajuste.place(relx=0.7425, rely=0.46, relwidth=0.2425, relheight=0.50)
        self.entry_dt_reajuste.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_reajuste))
        self.entry_dt_reajuste.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_reajuste, self.entry_dt_inicio))

        # Periodo de Previsão
        fr_periodo_previsao = customtkinter.CTkFrame(fr_lacto_periodos, border_color="gray75", border_width=1)
        fr_periodo_previsao.place(relx=0.415, rely=0.25,relwidth=0.15, relheight=0.70)
        lb_periodo_previsao = customtkinter.CTkLabel(fr_periodo_previsao, text="Período Orçamento", anchor='w')
        lb_periodo_previsao.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        TDta_Inicio = datetime.strptime("01/01/2000", "%d/%m/%Y")
        TDta_Fim = datetime.now()
        
        lb_dt_venc_inicio = customtkinter.CTkLabel(fr_periodo_previsao, text="Data Início", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_dt_venc_inicio.place(relx=0.01, rely=0.30, relheight=0.125, relwidth=0.20)
        self.entry_dt_inicio = customtkinter.CTkEntry(fr_periodo_previsao, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, TDta_Inicio.strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_inicio, self.entry_dt_fim))

        lb_dt_venc_fim = customtkinter.CTkLabel(fr_periodo_previsao, text="Data Fim", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_dt_venc_fim.place(relx=0.47, rely=0.30, relheight=0.125, relwidth=0.35)
        self.entry_dt_fim = customtkinter.CTkEntry(fr_periodo_previsao, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_dt_fim.delete(0, 'end')
        self.entry_dt_fim.insert(0, TDta_Fim.strftime("%d/%m/%Y"))
        self.entry_dt_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_fim))
        self.entry_dt_fim.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_fim, self.entry_despesa_dedutivel))

        # Informações Financeiras e Fiscais
        fr_informacoes_financeiras_fiscais = customtkinter.CTkFrame(fr_lacto_periodos, border_color="gray75", border_width=1)
        fr_informacoes_financeiras_fiscais.place(relx=0.57, rely=0.25,relwidth=0.425, relheight=0.70)
        lb_informacoes_financeiras_fiscais = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Informações Financeiras e Fiscais", anchor='w')
        lb_informacoes_financeiras_fiscais.place(relx=0.005, rely=0.01, relheight=0.30, relwidth=0.55)
        
        # Dedutível Sim/Não
        self.lb_despesa_dedutivel = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Dedutível?", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_despesa_dedutivel.place(relx=0.01, rely=0.30, relheight=0.125, relwidth=0.10)
        self.opcoes = ["Sim", "Não"]
        self.entry_despesa_dedutivel = customtkinter.CTkComboBox(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT, values=self.opcoes)
        self.entry_despesa_dedutivel.place(relx=0.005, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_despesa_dedutivel.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_pis_cofins))

        # Pis/Cofins
        lb_pis_cofins = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Pis/Cofins", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_pis_cofins.place(relx=0.115, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_pis_cofins = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_pis_cofins.place(relx=0.11, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_pis_cofins.bind("<Return>", lambda event: self.format_per(event, self.entry_pis_cofins, self.entry_pis_cofins))
        self.entry_pis_cofins.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_icms))

        # ICMS
        lb_icms = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="ICMS", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_icms.place(relx=0.22, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_icms = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_icms.place(relx=0.215, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_icms.bind("<Return>", lambda event: self.format_per(event, self.entry_icms, self.entry_icms))
        self.entry_icms.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_gera_pagto))

        # Gera Pagto?
        self.lb_gera_pagto = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Gera Pagto?", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_gera_pagto.place(relx=0.325, rely=0.30, relheight=0.125, relwidth=0.10)
        self.opcoes_gera_pagto = ["Sim", "Não"]
        self.entry_gera_pagto = customtkinter.CTkComboBox(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT, values=self.opcoes_gera_pagto)
        self.entry_gera_pagto.place(relx=0.32, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_gera_pagto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_per_avista))

        # % A vista
        lb_per_avista = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="% À Vista", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_per_avista.place(relx=0.435, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_per_avista = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_per_avista.place(relx=0.43, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_per_avista.bind("<Return>", lambda event: self.format_per_dif_aprazo(event))
        
        # % A Prazo
        lb_per_aprazo = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="% A Prazo", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_per_aprazo.place(relx=0.54, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_per_aprazo = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_per_aprazo.place(relx=0.535, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_per_aprazo.bind("<Return>", lambda event: self.format_per(event, self.entry_per_aprazo, self.entry_per_aprazo))
        self.entry_per_aprazo.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_nr_parcelas))

        # Nr. Parcelas
        lb_nr_parcelas = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Nr. Parcelas", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_nr_parcelas.place(relx=0.645, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_nr_parcelas = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_nr_parcelas.place(relx=0.64, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_nr_parcelas.bind("<Return>", lambda event: self.format_x(event, self.entry_nr_parcelas))
        self.entry_nr_parcelas.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_prazo_pagto))

        # Prazo (0/n)
        lb_prazo_pagto = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Prazo(0/n)", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_prazo_pagto.place(relx=0.75, rely=0.30, relheight=0.125, relwidth=0.20)

        self.entry_prazo_pagto = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_prazo_pagto.place(relx=0.745, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_prazo_pagto.bind("<Return>", lambda event: self.format_x(event, self.entry_prazo_pagto))
        self.entry_prazo_pagto.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_per_tx_juros))

         # Taxa Juros(% a.m.)
        lb_per_tx_juros = customtkinter.CTkLabel(fr_informacoes_financeiras_fiscais, text="Juros(% a.m.)", text_color="white", font=('Arial', 10), anchor=tk.W)
        lb_per_tx_juros.place(relx=0.855, rely=0.30, relheight=0.125, relwidth=0.10)

        self.entry_per_tx_juros = customtkinter.CTkEntry(fr_informacoes_financeiras_fiscais, fg_color="black", text_color="white", justify=tk.RIGHT)
        self.entry_per_tx_juros.place(relx=0.85, rely=0.50, relwidth=0.10, relheight=0.40)
        self.entry_per_tx_juros.bind("<Return>", lambda event: self.format_per(event, self.entry_per_tx_juros, self.entry_per_tx_juros))
        self.entry_per_tx_juros.bind("<Return>", lambda event: self.muda_barrinha(event, self.text_historico))
        
    def frame_linha_6(self, janela):
        # Histórico do Lançamento
        coordenadas_relx = 0.005
        coordenadas_rely = 0.505
        coordenadas_relwidth = 0.99
        coordenadas_relheight = 0.49
        fr_lacto_historico = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_lacto_historico.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_lacto_historico = customtkinter.CTkLabel(fr_lacto_historico, text="Histórico do Lançamento", anchor='w', font=("Arial", 16, "bold"))
        lb_lacto_historico.place(relx=0.005, rely=0.005, relheight=0.09, relwidth=0.99)

        # observações
        self.text_historico = customtkinter.CTkTextbox(fr_lacto_historico, fg_color="black", text_color="white", width=300, height=100)
        self.text_historico.place(relx=0.005, rely=0.10, relwidth=0.99, relheight=0.88)
        # self.text_historico.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_taxa_desconto))

    def frame_premissa_dados(       
                                self,
                                ID_Empresa,
                                DS_Empresa, 
                                ID_Orc, 
                                DS_Orc,
                                ID_Lcto
                            ):
        def Consulta_Premissa(ID_Empresa, ID_Orc, ID_Lcto):
            conditions = []  # Lista para armazenar as condições
            # Condições iniciais
            conditions.append("pp.Pri_ID = %s")
            params = [ID_Empresa]
            conditions.append("pp.Orc_ID = %s")
            params.append(ID_Orc)
            conditions.append("pp.Prem_ID = %s")
            params.append(ID_Lcto)
            
            # print(ID_Empresa, ID_Orc, ID_Lcto)
            
            vsSQL = f"""SELECT 
                            pp.Orc_ID, 
                            pp.Prem_ID, 
                            pp.Cen_ID_Debito,  
                            cc2.Cen_Descricao as CenDebito, 
                            pp.Con_ID_Debito,  
                            cc.Nat_Descricao as ConDebito, 
                            pp.Cen_ID_Credito, 
                            cc3.Cen_Descricao as CenCredito, 
                            pp.Con_ID_Credito, 
                            cc1.Nat_Descricao as ConCredito, 
                            pp.Prem_Historico, 
                            pp.Preco_ID, 
                            cc4.Preco_Descricao, 
                            cc4.Preco_Valor, 
                            pp.Prem_Quantidade, 
                            cc6.TipodeMedida_Diminutivo, 
                            Tipo_Lcto, 
                            pp.Prem_Dedutivel, 
                            pp.Prem_Financeiro, 
                            pp.Prem_PrazoPgto, 
                            pp.Prem_aVista, 
                            pp.Prem_aPrazo, 
                            pp.Prem_nrParc, 
                            pp.Prem_txJuros, 
                            pp.Prem_ICMS, 
                            pp.Prem_PISCofins, 
                            pp.Nat_ID, 
                            cc5.Nat_Desc, 
                            pp.Nat_Tipo, 
                            pp.Idx_ID, 
                            cc7.Idx_DS, 
                            cc6.TipodeMedida_Diminutivo, 
                            pp.Idx_Data, 
                            pp.Periodi_ID, 
                            cc8.Periodi_Descricao, 
                            pp.Prem_DtaInicio, 
                            pp.Prem_DtaFim, 
                            pp.Status_ID 
                        FROM orc_premissas pp 
                        Inner Join TB_Natureza       cc  on cc.Nat_ID=pp.Con_ID_Debito and cc.Empresa_ID=pp.Pri_ID
                        Inner Join TB_Natureza       cc1 on cc1.Nat_ID=pp.Con_ID_Credito and cc1.Empresa_ID=pp.Pri_ID 
                        Inner Join centrocusto       cc2 on cc2.Cen_ID=pp.Cen_ID_Debito and cc2.Empresa_ID=pp.Pri_ID
                        Inner Join centrocusto       cc3 on cc3.Cen_ID=pp.Cen_ID_Credito and cc3.Empresa_ID=pp.Pri_ID
                        Inner Join orc_precos        cc4 on cc4.Preco_ID=pp.Preco_ID and cc4.Orc_ID=pp.Orc_ID and cc4.Empresa_ID=pp.Pri_ID
                        Inner Join naturezas         cc5 on cc5.Nat_ID=pp.Nat_ID 
                        Inner Join TB_TiposdeMedida  cc6 on cc6.TipodeMedida_ID=cc4.Unidade_ID 
                        Inner Join Orc_idx           cc7 on cc7.Idx_ID=pp.Idx_ID
                        Inner Join orc_periodicidade cc8 on cc8.Periodi_ID=pp.Periodi_ID 
                        WHERE {' AND '.join(conditions)}
                    """
            
            myresult = db.executar_consulta(vsSQL, params)
            consulta = [(consulta) for consulta in myresult]
            return consulta

        if  ID_Lcto != '':
            self.lista = Consulta_Premissa(ID_Empresa, ID_Orc, ID_Lcto)
            if self.lista == []:
                messagebox.showinfo("Informação", "Nenhuma Premissa encontrada!!!.")
            
            self.limpar_campos_premissas()
            
            # Carregar Variáveis
            Orc_Tpo = self.lista[0].get('Tipo_Lcto')
            DS_Status = self.lista[0].get('Status_ID')
            if DS_Status =='A':
                DS_Status = 'Ativo'
            else:
                DS_Status = 'Excluído'

            ID_Lcto = self.lista[0].get('Prem_ID')
            Cen_DS_Debito = self.lista[0].get('CenDebito')
            Nat_DS_Debito  = self.lista[0].get('ConDebito')
            Cen_DS_Credito  = self.lista[0].get('CenCredito')
            Nat_DS_Credito  = self.lista[0].get('ConCredito')
            DS_Item  = self.lista[0].get('Preco_Descricao')
            Volume = self.lista[0].get('Prem_Quantidade')
            DS_Nat_Gerencial = self.lista[0].get('Nat_Desc')
            DS_Periodicidade = self.lista[0].get('Periodi_Descricao')
            DS_Indice = self.lista[0].get('Idx_DS')
            Dta_Reajuste = self.lista[0].get('Idx_Data')
            Dta_Inicio = self.lista[0].get('Prem_DtaInicio')
            Dta_Fim = self.lista[0].get('Prem_DtaFim')
            Dedutivel = self.lista[0].get('Prem_Dedutivel')
            Per_Pis_Cofins = self.lista[0].get('Prem_PISCofins')/100
            Per_Icms = self.lista[0].get('Prem_ICMS')/100
            GeraPgto = self.lista[0].get('Prem_Financeiro')
            Per_Avista = self.lista[0].get('Prem_aVista')/100
            Per_APrazo = self.lista[0].get('Prem_aPrazo')/100
            Nr_Parcelas = self.lista[0].get('Prem_nrParc')
            Prazo = self.lista[0].get('Prem_aPrazo')
            Per_Juros  = self.lista[0].get('Prem_txJuros')/100
            DS_Historico = self.lista[0].get('Prem_Historico')

            # Limpar Campos
            self.entry_id_lcto.delete(0, 'end')
            self.entry_centro_debito.delete(0, 'end')
            self.entry_natureza_debito.delete(0, 'end')
            self.entry_centro_credito.delete(0, 'end')
            self.entry_natureza_credito.delete(0, 'end')
            self.entry_item_preco.delete(0, 'end')
            self.entry_volume_valor.delete(0, 'end')
            self.entry_natureza_gerencial.delete(0, 'end')
            self.entry_periodicidade.delete(0, 'end')
            self.entry_indices_reajuste.delete(0, 'end')
            self.entry_dt_reajuste.delete(0, 'end')
            self.entry_dt_inicio.delete(0, 'end')
            self.entry_dt_fim.delete(0, 'end')
            self.entry_pis_cofins.delete(0, 'end')
            self.entry_icms.delete(0, 'end')
            self.entry_per_avista.delete(0, 'end')
            self.entry_per_aprazo.delete(0, 'end')
            self.entry_nr_parcelas.delete(0, 'end')
            self.entry_prazo_pagto.delete(0, 'end')
            self.entry_per_tx_juros.delete(0, 'end')
            self.text_historico.delete('1.0', 'end')

            # Preenche Cabeçalho
            self.entry_empresa.set(DS_Empresa)
            self.entry_orcamento.set(DS_Orc)
            self.entry_tipo_lcto_descr.set(Orc_Tpo)
            self.entry_status_lcto.set(DS_Status)

            # Preenche os campos Inserir os dados
            self.entry_id_lcto.configure(state='normal')
            self.entry_id_lcto.insert(0, ID_Lcto)
            self.entry_id_lcto.configure(state='disabled')

            self.entry_centro_debito.insert(0, str(Cen_DS_Debito))
            self.entry_natureza_debito.insert(0, str(Nat_DS_Debito))
            self.entry_centro_credito.insert(0, str(Cen_DS_Credito))
            self.entry_natureza_credito.insert(0, str(Nat_DS_Credito))
            self.entry_item_preco.insert(0, str(DS_Item))
            
            self.entry_volume_valor.insert(0, self.format_valor_fx(float(Volume)))
            
            self.entry_natureza_gerencial.insert(0, str(DS_Nat_Gerencial))
            self.entry_periodicidade.insert(0, str(DS_Periodicidade))
            self.entry_indices_reajuste.insert(0, str(DS_Indice))
            
            if Dta_Reajuste is not None:
                self.entry_dt_reajuste.insert(0, str(Dta_Reajuste.strftime('%d/%m/%Y')))
            else:
                Dta_Reajuste = datetime.now()
                self.entry_dt_reajuste.insert(0, str(Dta_Reajuste.strftime('%d/%m/%Y')))

            if Dta_Inicio is not None:
                self.entry_dt_inicio.insert(0, str(Dta_Inicio.strftime('%d/%m/%Y')))
            else:
                Dta_Inicio = datetime.now()
                self.entry_dt_inicio.insert(0, str(Dta_Inicio.strftime('%d/%m/%Y')))

            if Dta_Fim is not None:
                self.entry_dt_fim.insert(0, str(Dta_Fim.strftime('%d/%m/%Y')))
            else:
                Dta_Fim = datetime.now()
                self.entry_dt_fim.insert(0, str(Dta_Fim.strftime('%d/%m/%Y')))

            if Dedutivel == 'S':
                 self.entry_despesa_dedutivel.set('Sim')
            else:
                self.entry_despesa_dedutivel.set('Não')
            
            self.entry_pis_cofins.insert(0, self.format_per_fx(Per_Pis_Cofins))
            self.entry_icms.insert(0, self.format_per_fx(Per_Icms))
            
            if GeraPgto == 'S':
                self.entry_gera_pagto.set('Sim')
            else:
                self.entry_gera_pagto.set('Não')
            
            self.entry_per_avista.insert(0, self.format_per_fx(Per_Avista))
            self.entry_per_aprazo.insert(0, self.format_per_fx(Per_APrazo))
            self.entry_nr_parcelas.insert(0, self.format_x_fx(Nr_Parcelas))
            self.entry_prazo_pagto.insert(0, self.format_x_fx(Prazo))
            self.entry_per_tx_juros.insert(0, self.format_per_fx(Per_Juros))
            if DS_Historico is not None:
                self.text_historico.insert('1.0', str(DS_Historico))
        else:
            self.entry_empresa.set(DS_Empresa)
            self.entry_orcamento.set(DS_Orc)
    
        self.atualizar_empresas(Event, self.entry_empresa)
        self.atualizar_orcamentos(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.entry_orcamento)
        self.atualizar_centro_resultado(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.entry_centro_debito)
        self.atualizar_natureza_financeira(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.entry_natureza_debito)
        self.atualizar_centro_resultado(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.entry_centro_credito)
        self.atualizar_natureza_financeira(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.entry_natureza_credito)
        self.atualizar_item_precos_orcamentos(Event, self.obter_Empresa_ID(self.entry_empresa.get(), self.janela_premissas), self.obter_Orc_ID(self.entry_orcamento.get(), self.janela_premissas), self.entry_item_preco)
        self.atualizar_natureza_gerencial(Event, self.entry_natureza_gerencial)
        self.atualizar_periodicidade(Event, self.entry_periodicidade)
        self.atualizar_idx(Event, self.entry_indices_reajuste)

    def gravar_premissas(self):
        
        Empresa_DS = self.entry_empresa.get()
        Orc_DS  = self.entry_orcamento.get()
        Orc_Tpo = self.entry_tipo_lcto_descr.get()
        DS_Status = self.entry_status_lcto.get()
        
        if DS_Status == 'Ativo':
            DS_Status = 'A'
        else:
            DS_Status = 'E'

        ID_Lcto = self.entry_id_lcto.get()
        
        Cen_DS_Debito = self.entry_centro_debito.get()
        Nat_DS_Debito  = self.entry_natureza_debito.get()

        Cen_DS_Credito  = self.entry_centro_credito.get()
        Nat_DS_Credito  = self.entry_natureza_credito.get()

        DS_Item  = self.entry_item_preco.get()
        Volume = float(self.entry_volume_valor.get().replace('.', '').replace(',', '.')[:15])

        DS_Nat_Gerencial = self.entry_natureza_gerencial.get()
        DS_Periodicidade = self.entry_periodicidade.get()
        DS_Indice = self.entry_indices_reajuste.get()
        Dta_Reajuste = datetime.strptime(self.entry_dt_reajuste.get(), "%d/%m/%Y")
        Dta_Reajuste = Dta_Reajuste.strftime("%Y-%m-%d")
        
        Dta_Inicio = datetime.strptime(self.entry_dt_inicio.get(), "%d/%m/%Y")
        Dta_Fim = datetime.strptime(self.entry_dt_fim.get(), "%d/%m/%Y")

        Dedutivel = self.entry_despesa_dedutivel.get()
        if Dedutivel == 'Sim':
            Dedutivel = 'S'
        else:
            Dedutivel = 'N'

        Per_Pis_Cofins = float(self.entry_pis_cofins.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_Icms = float(self.entry_icms.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        GeraPgto = self.entry_gera_pagto.get()
        if GeraPgto == 'Sim':
            GeraPgto = 'S'
        else:
            GeraPgto = 'N'

        Per_Avista = float(self.entry_per_avista.get().replace("%", "").replace(",", ".")[:7]) 
        Per_APrazo = float(self.entry_per_aprazo.get().replace("%", "").replace(",", ".")[:7]) 
        Nr_Parcelas = float(self.entry_nr_parcelas.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        Prazo = float(self.entry_prazo_pagto.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        Per_Juros  = float(self.entry_per_tx_juros.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        DS_Historico = self.text_historico.get("1.0", "end")
        
        if Empresa_DS != '':
            ID_Empresa = self.obter_Empresa_ID(Empresa_DS, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!", parent=self.janela_premissas)
            return
        
        if Orc_DS != '':
            ID_Orc = self.obter_Orc_ID(Orc_DS, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!", parent=self.janela_premissas)
            return
          
        if Cen_DS_Debito != '':
            ID_Cen_Debito = self.obter_Centro_ID(Cen_DS_Debito, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Centro de Custos à Débito!!", parent=self.janela_premissas)
            return

        if Cen_DS_Credito != '':
            ID_Cen_Credito = self.obter_Centro_ID(Cen_DS_Credito, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Centro de Custos à Crédito!!", parent=self.janela_premissas)
            return

        if Nat_DS_Debito != '':
            ID_Nat_Debito = self.obter_Natureza_ID(Nat_DS_Debito, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Natureza à Débito!!", parent=self.janela_premissas)
            return

        if Nat_DS_Credito != '':
            ID_Nat_Credito = self.obter_Natureza_ID(Nat_DS_Credito, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Natureza à Crédito!!", parent=self.janela_premissas)
            return
        
        if DS_Item != '':
            ID_Item = self.obter_Orc_Item_ID(DS_Item, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Natureza à Crédito!!", parent=self.janela_premissas)
            return
        
        if DS_Indice != '':
            ID_Indice = self.obter_Indice_ID(DS_Indice, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Ìndice de Reajuste!!", parent=self.janela_premissas)
            return
        
        if DS_Periodicidade != '':
            ID_Periodicidade = self.obter_Periodicidade_ID(DS_Periodicidade, self.janela_premissas)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Periodicidade!!", parent=self.janela_premissas)
            return
        
        if DS_Nat_Gerencial != '':
            ID_Nat_Gerencial = self.obter_Nat_Gerencial_ID(DS_Nat_Gerencial, self.janela_premissas)
            Nat_Tipo = 'R'
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher Periodicidade!!", parent=self.janela_premissas)
            return
        
        if DS_Status != '':
            if DS_Status != "A" and DS_Status != "E":
                messagebox.showinfo("Gestor de Negócios", "Erro: Status de Gravação tem que ser A: Ativo ou E: Excluído!!", parent=self.janela_premissas)
                return
        else:
            messagebox.showinfo("Gestor de Negócios", "Erro: Status de Gravação tem que ser A: Ativo ou E: Excluído!!", parent=self.janela_premissas)
            return

        if not DS_Historico:
            messagebox.showinfo("Gestor de Negócios", "Historico não Cadastrado!!", parent=self.janela_premissas)
            return
        elif len(DS_Historico) > 200:
            resposta = messagebox.askyesno("Tamanho Histórico", "Historico Muito Grande, Máximo 200 Caracteres, Alterar Automaticamente?")
            if not resposta:
                return
            
            self.text_historico = self.text_historico[:200]
        
        resposta = messagebox.askyesno("Gravar Premissa", "Confirmar?", parent=self.janela_premissas)
        if not resposta:
           return
        
        if ID_Lcto:
            # Update statement
            vsSQL = """
                        UPDATE orc_premissas SET 
                            Cen_ID_Debito=%s, 
                            Con_ID_Debito=%s, 
                            Cen_ID_Credito=%s, 
                            Con_ID_Credito=%s,
                            Prem_Historico=%s, 
                            Preco_ID=%s, 
                            Prem_Quantidade=%s, 
                            Tipo_Lcto=%s,
                            Prem_Dedutivel=%s, 
                            Prem_Financeiro=%s, 
                            Prem_PrazoPgto=%s, 
                            Prem_aVista=%s, 
                            Prem_aPrazo=%s, 
                            Prem_nrParc=%s, 
                            Prem_txJuros=%s, 
                            Prem_ICMS=%s, 
                            Prem_PISCofins=%s, 
                            Nat_ID=%s, 
                            Idx_ID=%s, 
                            Idx_Data=%s, 
                            Periodi_ID=%s, 
                            Prem_DtaInicio=%s, 
                            Prem_DtaFim=%s, 
                            Status_ID=%s,
                            Nat_Tipo=%s
                        WHERE 
                            Pri_ID=%s AND 
                            Orc_ID=%s AND 
                            Prem_ID=%s AND 
                            Prem_Tipo='PRM'
                    """
            params = (
                        ID_Cen_Debito,
                        ID_Nat_Debito,
                        ID_Cen_Credito,
                        ID_Nat_Credito,
                        DS_Historico,
                        ID_Item,
                        Volume,
                        Orc_Tpo,
                        Dedutivel,
                        GeraPgto,
                        Prazo,
                        Per_Avista,
                        Per_APrazo,
                        Nr_Parcelas,
                        Per_Juros,
                        Per_Icms,
                        Per_Pis_Cofins,
                        ID_Nat_Gerencial,
                        ID_Indice,
                        Dta_Reajuste,
                        ID_Periodicidade ,
                        Dta_Inicio,
                        Dta_Fim,
                        DS_Status,
                        Nat_Tipo,
                        ID_Empresa, 
                        ID_Orc,
                        ID_Lcto
                    )

        else:
            vsSQL = """
                        INSERT INTO orc_premissas 
                        (
                            Pri_ID, 
                            Orc_ID, 
                            Cen_ID_Debito, 
                            Cen_ID_Credito, 
                            Prem_Tipo,
                            Con_ID_Debito, 
                            Con_ID_Credito, 
                            Prem_Historico, 
                            Preco_ID, 
                            Prem_Quantidade,
                            Tipo_Lcto, 
                            Prem_Dedutivel, 
                            Prem_Financeiro, 
                            Prem_PrazoPgto,
                            Prem_aVista, 
                            Prem_aPrazo, 
                            Prem_nrParc, 
                            Prem_txJuros,
                            Prem_ICMS, 
                            Prem_PISCofins, 
                            Nat_ID, 
                            Idx_ID, 
                            Idx_Data, 
                            Periodi_ID, 
                            Prem_DtaInicio, 
                            Prem_DtaFim, 
                            Status_ID,
                            Nat_Tipo
                        )
                        VALUES (%s, %s, %s, %s, 'PRM', %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            params = (
                        ID_Empresa, 
                        ID_Orc,
                        ID_Cen_Debito,
                        ID_Cen_Credito,
                        ID_Nat_Debito,
                        ID_Nat_Credito,
                        DS_Historico,
                        ID_Item,
                        Volume,
                        Orc_Tpo,
                        Dedutivel,
                        GeraPgto,
                        Prazo,
                        Per_Avista,
                        Per_APrazo,
                        Nr_Parcelas,
                        Per_Juros,
                        Per_Icms,
                        Per_Pis_Cofins,
                        ID_Nat_Gerencial,
                        ID_Indice,
                        Dta_Reajuste,
                        ID_Periodicidade ,
                        Dta_Inicio,
                        Dta_Fim,
                        DS_Status,
                        Nat_Tipo
                    )
                                
        db.executar_consulta(vsSQL, params)
        self.limpar_campos_premissas()
    
    def limpar_campos_premissas(self):
        valor_decimal = '0,00'
        valor_percente = '0,00 %'
        prazo = '1 x'
        sim_nao = 'Sim'

        # Limpa a entrada
        self.entry_tipo_lcto_descr.set('CPA')
        self.entry_status_lcto.set('Ativo')
        
        self.entry_id_lcto.configure(state='normal')
        self.entry_id_lcto.delete(0, 'end')
        self.entry_id_lcto.configure(state='disabled')
        
        self.entry_centro_debito.delete(0, 'end')
        self.entry_natureza_debito.delete(0, 'end')
        self.entry_centro_credito.delete(0, 'end')
        self.entry_natureza_credito.delete(0, 'end')
        self.entry_item_preco.delete(0, 'end')

        self.entry_volume_valor.delete(0, 'end')
        self.entry_volume_valor.insert(0, valor_decimal.strip())
        
        self.entry_natureza_gerencial.delete(0, 'end')
        self.entry_periodicidade.delete(0, 'end')
        self.entry_indices_reajuste.delete(0, 'end')
        
        self.entry_despesa_dedutivel.set(sim_nao.strip())

        self.entry_pis_cofins.delete(0, 'end')
        self.entry_pis_cofins.insert(0, valor_percente.strip())
        
        self.entry_icms.delete(0, 'end')
        self.entry_icms.insert(0, valor_percente.strip())
        
        self.entry_gera_pagto.set(sim_nao.strip())
        
        self.entry_per_avista.delete(0, 'end')
        self.entry_per_avista.insert(0, valor_percente.strip())
        
        self.entry_per_aprazo.delete(0, 'end')
        self.entry_per_aprazo.insert(0, valor_percente.strip())
        
        self.entry_nr_parcelas.delete(0, 'end')
        self.entry_nr_parcelas.insert(0, prazo.strip())

        self.entry_prazo_pagto.delete(0, 'end')
        self.entry_prazo_pagto.insert(0, prazo.strip())
        

        self.entry_per_tx_juros.delete(0, 'end')
        self.entry_per_tx_juros.insert(0, valor_percente.strip())
        
        self.text_historico.delete('1.0', 'end')

Premissas_Orcamento()
