from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Fluxo_Projetado(Widgets):
    def fluxo_projetado(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        self.janela_fluxo_projetado = customtkinter.CTkToplevel(self.window_one)
        self.janela_fluxo_projetado.title('Fluxo de Caixa Projetado - ' + Empresa_DS + ' - ' + Cidade + '/' + UF + ' - ' + Tipo + ' - ' + Nome_da_Area)
        width = self.janela_fluxo_projetado.winfo_screenwidth()
        height = self.janela_fluxo_projetado.winfo_screenheight()
        self.janela_fluxo_projetado.geometry(f"{width}x{height}+0+0") 
        self.janela_fluxo_projetado.resizable(True, True)
        self.janela_fluxo_projetado.lift()  # Traz a janela para frente   
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_fluxo_projetado.protocol("WM_DELETE_WINDOW", self.on_closing_tela_fluxo_projetado)

        self.frame_cabecalho_fluxo_projetado(self.janela_fluxo_projetado)
        self.frame_list_fluxo_projetado(self.janela_fluxo_projetado, Nome_da_Area)
        self.frame_carregar_dados_fluxo_projetado(Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area)
        
        # style = ttkthemes.ThemedStyle(self.janela_fluxo_projetado)
        # style.theme_use('clam')
        # style.configure('Treeview', font=('Verdana', 8), foreground='#2b2b2b', cellpadding=19)
        # style.configure('Treeview.Heading', font=('Verdana', 10, 'bold'), foreground='#444', background='silver')
        # style.map('Treeview', background=[('selected', 'darkgreen')], foreground=[('selected', 'orange')])

        self.janela_fluxo_projetado.focus_force()
        self.janela_fluxo_projetado.grab_set()    
        
################# dividindo a janela ###############
    def frame_cabecalho_fluxo_projetado(self, janela):
        # Indicadores
        # Informações Indicadores
        self.fr_informacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_informacoes.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.07)
        self.lb_informacoes = customtkinter.CTkLabel(self.fr_informacoes, text="Indicadores", text_color="white", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_informacoes.place(relx=0.05, rely=0, relheight=0.15, relwidth=0.50)

        # T.I.R. (a.m.) do Empreendimento
        self.lb_tir_am = customtkinter.CTkLabel(self.fr_informacoes, text="T.I.R. (% a.m.)", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_tir_am.place(relx=0.005, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_tir_am = customtkinter.CTkEntry(
                                                    self.fr_informacoes, 
                                                    fg_color="darkblue", 
                                                    font=("Helvetica", 12, "bold"),
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda 
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_tir_am.place(relx=0.005, rely=0.30, relwidth=0.08, relheight=0.6)
               
       # T.I.R. (a.a.) do Empreendimento
        self.lb_tir_aa = customtkinter.CTkLabel(self.fr_informacoes, text="T.I.R. (% a.a.)", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_tir_aa.place(relx=0.09, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_tir_aa = customtkinter.CTkEntry(
                                                    self.fr_informacoes, 
                                                    fg_color="darkblue", 
                                                    font=("Helvetica", 12, "bold"), 
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_tir_aa.place(relx=0.09, rely=0.30, relwidth=0.08, relheight=0.6)

        # PayBack do Empreendimento
        self.lb_payback = customtkinter.CTkLabel(self.fr_informacoes, text="PayBack", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_payback.place(relx=0.175, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_payback = customtkinter.CTkEntry(
                                                    self.fr_informacoes, 
                                                    fg_color="darkblue", 
                                                    font=("Helvetica", 12, "bold"), 
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_payback.place(relx=0.175, rely=0.30, relwidth=0.08, relheight=0.6)

        # VpL do Empreendimento
        self.lb_vpl = customtkinter.CTkLabel(self.fr_informacoes, text="VpL", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_vpl.place(relx=0.26, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_vpl = customtkinter.CTkEntry(
                                                self.fr_informacoes, 
                                                fg_color="darkblue", 
                                                font=("Helvetica", 12, "bold"), 
                                                border_color="darkblue",  # Cor da borda
                                                border_width=2,  # Largura da borda
                                                text_color="white", 
                                                justify=tk.RIGHT)
        self.entry_vpl.place(relx=0.26, rely=0.30, relwidth=0.08, relheight=0.6)

        # Taxa VpL do Empreendimento
        self.lb_vpl_taxa = customtkinter.CTkLabel(self.fr_informacoes, text="Taxa Desconto VpL", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_vpl_taxa.place(relx=0.345, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_vpl_taxa = customtkinter.CTkEntry(
                                                    self.fr_informacoes, 
                                                    fg_color="darkblue", 
                                                    font=("Helvetica", 12, "bold"), 
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_vpl_taxa.place(relx=0.345, rely=0.30, relwidth=0.08, relheight=0.6)
        
        # Valor Exposição Máxima de Caixa
        self.lb_exposicao_caixa = customtkinter.CTkLabel(self.fr_informacoes, text="Exposição Máxima", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_exposicao_caixa.place(relx=0.43, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_exposicao_caixa = customtkinter.CTkEntry(
                                                            self.fr_informacoes, 
                                                            fg_color="darkred", 
                                                            font=("Helvetica", 12, "bold"), 
                                                            border_color="darkred",  # Cor da borda
                                                            border_width=2,  # Largura da borda
                                                            text_color="white", 
                                                            justify=tk.RIGHT)
        self.entry_exposicao_caixa.place(relx=0.43, rely=0.30, relwidth=0.08, relheight=0.6)

        #----------------------------------------------------------------------------------
        
        # Totais
        self.fr_totais = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_totais.place(relx=0.005, rely=0.085, relwidth=0.985, relheight=0.07)
        self.lb_totais = customtkinter.CTkLabel(self.fr_totais, text="Totais", text_color="white", font=('Arial', 12, 'bold'), anchor=tk.W)
        self.lb_totais.place(relx=0.05, rely=0, relheight=0.15, relwidth=0.50)

        # Vendas
        self.lb_vendas = customtkinter.CTkLabel(self.fr_totais, text="Total Vendas", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_vendas.place(relx=0.005, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_vendas = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkblue", 
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_vendas.place(relx=0.005, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Recebimentos Totais
        self.lb_recbtos = customtkinter.CTkLabel(self.fr_totais, text="Total Recebimento", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_recbtos.place(relx=0.062948, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_recbtos = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkblue", 
                                                    border_color="darkblue",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_recbtos.place(relx=0.062948, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Repasses Parceiro
        self.lb_repasses = customtkinter.CTkLabel(self.fr_totais, text="Total Repassar", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_repasses.place(relx=0.120896, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_repasses = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_repasses.place(relx=0.120896, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Comissão de Vendas
        self.lb_comissao = customtkinter.CTkLabel(self.fr_totais, text="Total Comissão", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_comissao.place(relx=0.178844, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_comissao = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_comissao.place(relx=0.178844, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Comissão Intermediação
        self.lb_intermediacao = customtkinter.CTkLabel(self.fr_totais, text="Total Itermediação", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_intermediacao.place(relx=0.236792, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_intermediacao = customtkinter.CTkEntry(
                                                        self.fr_totais, 
                                                        fg_color="darkred", 
                                                        border_color="darkred",  # Cor da borda
                                                        border_width=2,  # Largura da borda
                                                        text_color="white", 
                                                        justify=tk.RIGHT)
        self.entry_intermediacao.place(relx=0.236792, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Impostos
        self.lb_impostos = customtkinter.CTkLabel(self.fr_totais, text="Total Impostos", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_impostos.place(relx=0.294740, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_impostos = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_impostos.place(relx=0.294740, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Recuros para Aquisição e/ou Torna
        self.lb_aportes = customtkinter.CTkLabel(self.fr_totais, text="Total Terreno/Torna", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_aportes.place(relx=0.352688, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_aportes = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_aportes.place(relx=0.352688, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Projetos
        self.lb_projetos = customtkinter.CTkLabel(self.fr_totais, text="Total Projetos", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_projetos.place(relx=0.410636, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_projetos = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_projetos.place(relx=0.410636, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Obras  
        self.lb_obras = customtkinter.CTkLabel(self.fr_totais, text="Total Obras", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_obras.place(relx=0.468584, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_obras = customtkinter.CTkEntry(
                                                self.fr_totais, 
                                                fg_color="darkred", 
                                                border_color="darkred",  # Cor da borda
                                                border_width=2,  # Largura da borda
                                                text_color="white", 
                                                justify=tk.RIGHT)
        self.entry_obras.place(relx=0.468584, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Administração de Obras
        self.lb_admobras = customtkinter.CTkLabel(self.fr_totais, text="Total Adm. Obras", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_admobras.place(relx=0.526532, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_admobras = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_admobras.place(relx=0.526532, rely=0.30, relwidth=0.052948, relheight=0.6)

        # MkT
        self.lb_mkt = customtkinter.CTkLabel(self.fr_totais, text="Total MkT", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_mkt.place(relx=0.584480, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_mkt = customtkinter.CTkEntry(
                                                self.fr_totais, 
                                                fg_color="darkred", 
                                                border_color="darkred",  # Cor da borda
                                                border_width=2,  # Largura da borda
                                                text_color="white", 
                                                justify=tk.RIGHT)
        self.entry_mkt.place(relx=0.584480, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Pós Obras
        self.lb_posobras = customtkinter.CTkLabel(self.fr_totais, text="Total Pós Obras", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_posobras.place(relx=0.642428, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_posobras = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_posobras.place(relx=0.642428, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Over Head
        self.lb_overhead = customtkinter.CTkLabel(self.fr_totais, text="Total Over Head", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_overhead.place(relx=0.700376, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_overhead = customtkinter.CTkEntry(
                                                    self.fr_totais, 
                                                    fg_color="darkred", 
                                                    border_color="darkred",  # Cor da borda
                                                    border_width=2,  # Largura da borda
                                                    text_color="white", 
                                                    justify=tk.RIGHT)
        self.entry_overhead.place(relx=0.700376, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Adto para o Parceiro
        self.lb_adto = customtkinter.CTkLabel(self.fr_totais, text="Total Adiantado", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_adto.place(relx=0.758324, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_adto = customtkinter.CTkEntry(
                                                self.fr_totais, 
                                                fg_color="darkred", 
                                                border_color="darkred",  # Cor da borda
                                                border_width=2,  # Largura da borda
                                                text_color="white", 
                                                justify=tk.RIGHT)
        self.entry_adto.place(relx=0.758324, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Devolução de Adto para o Parceiro
        self.lb_devolucaoadto = customtkinter.CTkLabel(self.fr_totais, text="Total Devolvido", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_devolucaoadto.place(relx=0.816272, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_devolucaoadto = customtkinter.CTkEntry(
                                                          self.fr_totais, 
                                                          fg_color="darkblue", 
                                                          border_color="darkblue",  # Cor da borda
                                                          border_width=2,  # Largura da borda
                                                          text_color="white", 
                                                          justify=tk.RIGHT)
        self.entry_devolucaoadto.place(relx=0.816272, rely=0.30, relwidth=0.052948, relheight=0.6)

        # Liberação de Emprestimo para o Projeto
        self.lb_emprestimoliberacao = customtkinter.CTkLabel(self.fr_totais, text="Total Liberado", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_emprestimoliberacao.place(relx=0.874220, rely=0.15,relheight=0.15, relwidth=0.5)
        self.entry_emprestimoliberacao = customtkinter.CTkEntry(
                                                                self.fr_totais, 
                                                                fg_color="darkblue", 
                                                                border_color="darkblue",  # Cor da borda
                                                                border_width=2,  # Largura da borda
                                                                text_color="white", 
                                                                justify=tk.RIGHT)
        self.entry_emprestimoliberacao.place(relx=0.874220, rely=0.30, relwidth=0.0529488, relheight=0.6)

        # Liquidação do Financiamento do Projeto
        self.lb_emprestimoliquidacao = customtkinter.CTkLabel(self.fr_totais, text="Total Liquidado", text_color="white", font=('Arial', 10), anchor=tk.W)
        self.lb_emprestimoliquidacao.place(relx=0.932168, rely=0.15,relheight=0.15, relwidth=0.052948)
        self.entry_emprestimoliquidacao = customtkinter.CTkEntry(
                                                                self.fr_totais, 
                                                                fg_color="darkred", 
                                                                border_color="darkred",  # Cor da borda
                                                                border_width=2,  # Largura da borda
                                                                text_color="white", 
                                                                justify=tk.RIGHT)
        self.entry_emprestimoliquidacao.place(relx=0.932168, rely=0.30, relwidth=0.052948, relheight=0.6)
        
    def frame_list_fluxo_projetado(self, janela, estudo_ds):
        ## Listbox _ Informações Pesquisa
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.165, relwidth=0.985, relheight=0.85)

        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Widgets - Listar Parcelas
        self.Lfluxo_projetado = ttk.Treeview(self.fr_list, height=7, column=(
                                                            'Periodo', 
                                                            'Data', 
                                                            'Vlr_Venda', 
                                                            'Vlr_Rcbtos', 
                                                            'Vlr_RepasseParceiro', 
                                                            'Vlr_ComissaoVendas',
                                                            'Vlr_ComissaoNegocio',
                                                            'Vlr_Impostos',
                                                            'Vlr_TerrenoAporte',
                                                            'Vlr_Projetos',
                                                            'Vlr_Obra',
                                                            'Vlr_AdmObra',
                                                            'Vlr_MkT',
                                                            'Vlr_PosObra',
                                                            'Vlr_OverHead',
                                                            'Vlr_Adto',
                                                            'Vlr_DevolucaoAdto',
                                                            'Vlr_LiberacaoFinanciamento',
                                                            'Vlr_PagtoFinanciamento',
                                                            'Vlr_FCaixa',
                                                            'Vlr_FCaixaAcumulado'
                                                            ), show='headings') # , show='headings'
        
        self.Lfluxo_projetado.heading('#0', text='#', anchor='center')
        self.Lfluxo_projetado.heading('#1', text='Periodo', anchor='center')
        self.Lfluxo_projetado.heading('#2', text='Data', anchor='center')
        self.Lfluxo_projetado.heading('#3', text='Vendas', anchor='center')
        self.Lfluxo_projetado.heading('#4', text='Recebíveis', anchor='center')
        self.Lfluxo_projetado.heading('#5', text='Repasse', anchor='center')
        self.Lfluxo_projetado.heading('#6', text='Comissao', anchor='center')
        self.Lfluxo_projetado.heading('#7', text='Intermediação', anchor='center')
        self.Lfluxo_projetado.heading('#8', text='Impostos', anchor='center')
        self.Lfluxo_projetado.heading('#9', text='Terreno/Torna', anchor='center')
        self.Lfluxo_projetado.heading('#10', text='Projetos', anchor='center')
        self.Lfluxo_projetado.heading('#11', text='Obra', anchor='center')
        self.Lfluxo_projetado.heading('#12', text='Adm Obra', anchor='center')
        self.Lfluxo_projetado.heading('#13', text='MkT', anchor='center')
        self.Lfluxo_projetado.heading('#14', text='Pós Obra', anchor='center')
        self.Lfluxo_projetado.heading('#15', text='Over Head', anchor='center')
        self.Lfluxo_projetado.heading('#16', text='Adto', anchor='center')
        self.Lfluxo_projetado.heading('#17', text='Devolucao Adto', anchor='center')
        self.Lfluxo_projetado.heading('#18', text='Liberacao Financiamento', anchor='center')
        self.Lfluxo_projetado.heading('#19', text='Pagto Financiamento', anchor='center')
        self.Lfluxo_projetado.heading('#20', text='Fcx', anchor='center')
        self.Lfluxo_projetado.heading('#21', text='Fcx Acumulado', anchor='center')
        
        Col = 30

        self.Lfluxo_projetado.column('#0', width=2, anchor='w')
        self.Lfluxo_projetado.column('Periodo', width=10, anchor='c')
        self.Lfluxo_projetado.column('Data', width=Col, anchor='c')
        self.Lfluxo_projetado.column('Vlr_Venda', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_Rcbtos', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_RepasseParceiro', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_ComissaoVendas', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_ComissaoNegocio', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_Impostos', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_TerrenoAporte', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_Projetos', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_Obra', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_AdmObra', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_MkT', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_PosObra', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_OverHead', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_Adto', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_DevolucaoAdto', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_LiberacaoFinanciamento', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_PagtoFinanciamento', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_FCaixa', width=Col, anchor='e')
        self.Lfluxo_projetado.column('Vlr_FCaixaAcumulado', width=Col, anchor='e')
        
        self.Lfluxo_projetado.pack(expand=True, fill='both')
        self.Lfluxo_projetado.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)

    def frame_carregar_dados_fluxo_projetado(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        # self.limpar_campos_fluxo_projetado()
        self.consultar_fluxo_projetado(Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area)
    
    def consultar_fluxo_projetado(self, Empresa_ID, Empresa_DS, UF, Cidade, Tipo, Nome_da_Area):
        if Empresa_DS == '': 
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        # Limpa a lista atual antes de inserir novos resultados
        self.Lfluxo_projetado.delete(*self.Lfluxo_projetado.get_children())

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
                        df.Periodo_Nr                                   AS Periodo_Nr,
                        df.Periodo_Dta                                  AS Periodo_Dta,
                        ff.Tir_Urbanizadora                             AS Tir_aa,
                        ff.Tir_Urbanizadora_am                          AS Tir_am,
                        ff.PayBack_Urbanizadora                         AS PayBack,
                        ff.Multiplicador                                AS Multiplicador,
                        FORMAT(ff.Vlr_Exposicao_Maxima, 2, 'de_DE')     AS Exposicao_Maxima,
                        FORMAT(ff.VpL_Urbanizadora, 2, 'de_DE')         AS VpL,
                        ff.VpL_Taxa_Desconto                            AS VpL_Taxa,
                        FORMAT(df.Valor_Vendas, 2, 'de_DE')             AS Vlr_Venda, 
                        year(df.Periodo_Dta)                            AS Ano,
                        month(df.Periodo_Dta)                           AS Mes,
                        FORMAT(df.Valor_Parcelas, 2, 'de_DE')           AS ReceitaUrb,
                        FORMAT(df.Valor_Parcelas_Parceiro*-1, 2, 'de_DE')  AS ReceitaPar,
                        FORMAT(df.Valor_Comissao_Venda, 2, 'de_DE')     AS ComissaoVenda,
                        FORMAT(df.Valor_Comissao_Negocio, 2, 'de_DE')   AS ComissaoNegocio,
                        FORMAT(df.Valor_Impostos, 2, 'de_DE')           AS Impostos,
                        FORMAT(df.Valor_Terreno, 2, 'de_DE')            AS Terreno,
                        FORMAT(df.Valor_Projetos, 2, 'de_DE')           AS Projetos,
                        FORMAT(df.Valor_Obras, 2, 'de_DE')              AS Obras,
                        FORMAT(df.Valor_AdmObras, 2, 'de_DE')           AS AdmObras,
                        FORMAT(df.Valor_PosObras, 2, 'de_DE')           AS PosObras,
                        FORMAT(df.Valor_Adm, 2, 'de_DE')                AS Adm,
                        FORMAT(df.Valor_Mkt, 2, 'de_DE')                AS MkT,
                        FORMAT(df.Valor_Adto, 2, 'de_DE')               AS Valor_Adto,
                        FORMAT(df.Valor_AmortAdto, 2, 'de_DE')          AS Valor_DevolucaoAdto,
                        FORMAT(df.Valor_CustoAdtoPar, 2, 'de_DE')       AS Valor_CustoAdto,
                        FORMAT(df.Valor_Liberacao, 2, 'de_DE')          AS Valor_Liberacao,
                        FORMAT(df.Vlr_ParcelaFinanciamento, 2, 'de_DE') AS Vlr_ParcelaFinanciamento,
                        FORMAT(df.Valor_Fx, 2, 'de_DE')                 AS Fx_Caixa,
                        FORMAT(df.Valor_Fx_Acumulado, 2, 'de_DE')       AS Fx_Caixa_Acumulado       

                    FROM Dados_Prospeccao ff
                    LEFT JOIN Dados_Fluxo AS df ON df.Empresa_ID=ff.Empresa_ID AND df.UF=ff.UF AND df.Cidade=ff.Cidade AND df.Nome_da_Area=ff.Nome_da_Area AND df.Tipo=ff.Tipo
                    WHERE {' AND '.join(conditions)} ORDER BY Ano, Mes, Periodo_Nr
                """
        results = db.executar_consulta(strSql, params)
        
        # Carregar Lista
        icon_image = self.base64_to_photoimage('lupa')
        _vendas = 0
        _recbtos = 0
        _repasses = 0
        _comissao = 0
        _intermediacao = 0
        _impostos = 0
        _aportes = 0
        _projetos = 0
        _obras = 0
        _admobras = 0
        _mkt = 0
        _posobras = 0
        _overhead = 0
        _adto = 0
        _devolucaoadto = 0
        _emprestimoliberacao = 0
        _emprestimoliquidacao = 0
        
        # Configura as tags para o Treeview
        self.Lfluxo_projetado.tag_configure('vermelho', foreground='red')  # Define a tag 'vermelho' para texto vermelho
        self.Lfluxo_projetado.tag_configure('preto', foreground='black')  # Define a tag 'preto' para texto preto
        tags = []

        for row in results:
            _vendas += float(row['Vlr_Venda'].replace('.', '').replace(',', '.')[:15])
            _recbtos += float(row['ReceitaUrb'].replace('.', '').replace(',', '.')[:15])
            _repasses += float(row['ReceitaPar'].replace('.', '').replace(',', '.')[:15])
            _comissao += float(row['ComissaoVenda'].replace('.', '').replace(',', '.')[:15])
            _intermediacao += float(row['ComissaoNegocio'].replace('.', '').replace(',', '.')[:15])
            _impostos += float(row['Impostos'].replace('.', '').replace(',', '.')[:15])
            _aportes += float(row['Terreno'].replace('.', '').replace(',', '.')[:15])
            _projetos += float(row['Projetos'].replace('.', '').replace(',', '.')[:15])
            _obras += float(row['Obras'].replace('.', '').replace(',', '.')[:15])
            _admobras += float(row['AdmObras'].replace('.', '').replace(',', '.')[:15])
            _mkt += float(row['MkT'].replace('.', '').replace(',', '.')[:15])
            _posobras += float(row['PosObras'].replace('.', '').replace(',', '.')[:15])
            _overhead += float(row['Adm'].replace('.', '').replace(',', '.')[:15])
            _adto += float(row['Valor_Adto'].replace('.', '').replace(',', '.')[:15])
            _devolucaoadto += float(row['Valor_DevolucaoAdto'].replace('.', '').replace(',', '.')[:15])
            _emprestimoliberacao += float(row['Valor_Liberacao'].replace('.', '').replace(',', '.')[:15])
            _emprestimoliquidacao += float(row['Vlr_ParcelaFinanciamento'].replace('.', '').replace(',', '.')[:15])
            _tir_am = row['Tir_am']
            _tir_aa = row['Tir_aa']
            _payback = row['PayBack']
            _vpl = float(row['VpL'].replace('.', '').replace(',', '.')[:15])
            _vpl_taxa = row['VpL_Taxa']
            _exposicao_caixa = float(row['Exposicao_Maxima'].replace('.', '').replace(',', '.')[:15])

            self.Lfluxo_projetado.insert('', 'end', 
                               values=(
                                    row['Periodo_Nr'],
                                    row['Periodo_Dta'],
                                    row['Vlr_Venda'],
                                    row['ReceitaUrb'],
                                    row['ReceitaPar'],
                                    row['ComissaoVenda'],
                                    row['ComissaoNegocio'],
                                    row['Impostos'],
                                    row['Terreno'],
                                    row['Projetos'],
                                    row['Obras'],
                                    row['AdmObras'],
                                    row['MkT'],
                                    row['PosObras'],
                                    row['Adm'],
                                    row['Valor_Adto'],
                                    row['Valor_DevolucaoAdto'],
                                    row['Valor_Liberacao'],
                                    row['Vlr_ParcelaFinanciamento'],
                                    row['Fx_Caixa'],
                                    row['Fx_Caixa_Acumulado']
                                    ))
            
        self.entry_vendas.insert(0, self.format_valor_fx(float(_vendas)))
        self.entry_vendas.configure(state='disabled')
        self.entry_recbtos.insert(0, self.format_valor_fx(float(_recbtos)))
        self.entry_recbtos.configure(state='disabled')
        self.entry_repasses.insert(0, self.format_valor_fx(float(_repasses)))
        self.entry_repasses.configure(state='disabled')
        self.entry_comissao.insert(0, self.format_valor_fx(float(_comissao)))
        self.entry_comissao.configure(state='disabled')
        self.entry_intermediacao.insert(0, self.format_valor_fx(float(_intermediacao)))
        self.entry_intermediacao.configure(state='disabled')
        self.entry_impostos.insert(0, self.format_valor_fx(float(_impostos)))
        self.entry_impostos.configure(state='disabled')
        self.entry_aportes.insert(0, self.format_valor_fx(float(_aportes)))
        self.entry_aportes.configure(state='disabled')
        self.entry_projetos.insert(0, self.format_valor_fx(float(_projetos)))
        self.entry_projetos.configure(state='disabled')
        self.entry_obras.insert(0, self.format_valor_fx(float(_obras)))
        self.entry_obras.configure(state='disabled')
        self.entry_admobras.insert(0, self.format_valor_fx(float(_admobras)))
        self.entry_admobras.configure(state='disabled')
        self.entry_mkt.insert(0, self.format_valor_fx(float(_mkt)))
        self.entry_mkt.configure(state='disabled')
        self.entry_posobras.insert(0, self.format_valor_fx(float(_posobras)))
        self.entry_posobras.configure(state='disabled')
        self.entry_overhead.insert(0, self.format_valor_fx(float(_overhead)))
        self.entry_overhead.configure(state='disabled')
        self.entry_adto.insert(0, self.format_valor_fx(float(_adto)))
        self.entry_adto.configure(state='disabled')
        self.entry_devolucaoadto.insert(0, self.format_valor_fx(float(_devolucaoadto)))
        self.entry_devolucaoadto.configure(state='disabled')
        self.entry_emprestimoliberacao.insert(0, self.format_valor_fx(float(_emprestimoliberacao)))
        self.entry_emprestimoliberacao.configure(state='disabled')
        self.entry_emprestimoliquidacao.insert(0, self.format_valor_fx(float(_emprestimoliquidacao)))
        self.entry_emprestimoliquidacao.configure(state='disabled')
        
        self.entry_tir_am.insert(0, self.format_per_fx(float(_tir_am)))
        self.entry_tir_am.configure(state='disabled')
        self.entry_tir_aa.insert(0, self.format_per_fx(float(_tir_aa)))
        self.entry_tir_aa.configure(state='disabled')
        self.entry_payback.insert(0, self.format_ano_fx(float(_payback)))
        self.entry_payback.configure(state='disabled')
        self.entry_vpl.insert(0, self.format_valor_fx(float(_vpl)))
        self.entry_vpl.configure(state='disabled')
        self.entry_vpl_taxa.insert(0, self.format_per_fx(float(_vpl_taxa)))
        self.entry_vpl_taxa.configure(state='disabled')
        self.entry_exposicao_caixa.insert(0, self.format_valor_fx(float(_exposicao_caixa)))
        self.entry_exposicao_caixa.configure(state='disabled')

        self.Lfluxo_projetado.tag_configure('odd', background='#eee')
        self.Lfluxo_projetado.tag_configure('even', background='#ddd')
        self.Lfluxo_projetado.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.Lfluxo_projetado.yview)

Fluxo_Projetado()
