from imports import *
from widgets import Widgets
from datetime import datetime

################# criando janela ###############
class Relatorio_Orcamento(Widgets):
    def relatorio_orcamento(self):
        self.window_one.title('Relatório Orcamento')
        self.clearFrame_principal()
        self.frame_cabecalho_relatorio_orcamento(self.principal_frame)
        # self.frame_list_relatorio_orcamento(self.principal_frame)
       
################# dividindo a janela ###############
    def frame_cabecalho_relatorio_orcamento(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa")
        lb_empresa.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_orcamento))

        # Orçamento
        coordenadas_relx = 0.26
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.17
        coordenadas_relheight = 0.07
        fr_orcamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_orcamento.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_orcamento = customtkinter.CTkLabel(fr_orcamento, text="Orçamento")
        lb_orcamento.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        orcamentos = []

        self.entry_orcamento = AutocompleteCombobox(fr_orcamento, width=30, font=('Times', 11), completevalues=orcamentos)
        self.entry_orcamento.pack()
        self.entry_orcamento.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_orcamento.bind("<Button-1>", lambda event: self.atualizar_orcamentos(event, self.entry_empresa.get(), self.entry_orcamento))
        self.entry_orcamento.bind('<Down>', lambda event: self.atualizar_orcamentos(event, self.entry_empresa.get(), self.entry_orcamento))
        self.entry_orcamento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_dt_inicio))

        # Data Início da Projeção Orçamentária
        dta = self.ult_dia_mes(datetime.now())
        TDta_Inicio =  datetime.strptime(dta, "%Y-%m-%d")
        
        coordenadas_relx = 0.435
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.08
        coordenadas_relheight = 0.07
        fr_dta_inicio = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_dta_inicio.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_dta_inicio = customtkinter.CTkLabel(fr_dta_inicio, text="Data Início")
        lb_dta_inicio.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        self.entry_dt_inicio = customtkinter.CTkEntry(fr_dta_inicio, fg_color="black", text_color="white", justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, TDta_Inicio.strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.985, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_centro_resultado))
        
        
        # Centro Resultado
        coordenadas_relx = 0.52
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.17
        coordenadas_relheight = 0.07
        fr_centro_resultado = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_centro_resultado.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_centro_resultado = customtkinter.CTkLabel(fr_centro_resultado, text="Centro Resultado")
        lb_centro_resultado.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        centro_resultados = []
        
        self.entry_centro_resultado = AutocompleteCombobox(fr_centro_resultado, width=30, font=('Times', 11), completevalues=centro_resultados)
        self.entry_centro_resultado.pack()
        self.entry_centro_resultado.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_centro_resultado.bind("<Button-1>", lambda event:  self.atualizar_centro_resultado(event, self.entry_empresa.get(), self.entry_centro_resultado))
        self.entry_centro_resultado.bind('<Down>', lambda event:  self.atualizar_centro_resultado(event, self.entry_empresa.get(), self.entry_centro_resultado))
        self.entry_centro_resultado.bind("<Return>", lambda event: self.muda_barrinha(event, self.opcoes_relatorio_menu))
        
        # Opções
        coordenadas_relx = 0.695
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.255
        coordenadas_relheight = 0.07
        fr_opcoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_opcoes.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_opcoes = customtkinter.CTkLabel(fr_opcoes, text="Opções")
        lb_opcoes.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        # Opções Tipo do Relatório
        opcoes_relatorio = ['Natureza Financeira', 'Centro Resultado']
        self.opcoes_relatorio_menu = ctk.CTkOptionMenu(fr_opcoes, values=opcoes_relatorio)
        self.opcoes_relatorio_menu.set(opcoes_relatorio[0])
        self.opcoes_relatorio_menu.place(relx=0.005, rely=0.50, relheight=0.25, relwidth=0.40)

        # Opções Extras
        self.check_var_premissas = customtkinter.StringVar(value="off")
        self.check_var_excel = customtkinter.StringVar(value="off")
        self.check_var_reais_mil = customtkinter.StringVar(value="off")
        
        self.checkbox_excel = customtkinter.CTkCheckBox(fr_opcoes, text='Gerar Excel?', variable=self.check_var_excel, onvalue="on", offvalue="off")
        self.checkbox_excel.place(relx=0.42, rely=0.50, relheight=0.35, relwidth=0.40)

        self.checkbox_reais_mil = customtkinter.CTkCheckBox(fr_opcoes, text='Em R$/1.000', variable=self.check_var_reais_mil, onvalue="on", offvalue="off")
        self.checkbox_reais_mil.place(relx=0.73, rely=0.50, relheight=0.35, relwidth=0.265)

        # Botão de Consultar
        def consultar():
            Empresa_DS = self.entry_empresa.get()
            Orc_DS = self.entry_orcamento.get()

            if self.entry_empresa.get() != '':
                ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            if self.entry_orcamento.get() != '':
                ID_Orcamento = self.obter_Orc_ID(self.entry_orcamento.get())
            else:
                ID_Orcamento = self.entry_orcamento.get()
                
            if self.entry_centro_resultado.get() != '':
                ID_Centro_Resultado = self.obter_Centro_ID(self.entry_centro_resultado.get())
            else:
                ID_Centro_Resultado = self.entry_centro_resultado.get()
                    
            if self.opcoes_relatorio_menu.get() == 'Natureza Financeira':
                strClassificacao = 'Natureza Financeira'
            else:
                strClassificacao = 'Centro Resultado'

            if self.checkbox_excel.get() == 'on':
                chk_excel = 'S' 
            else:
                chk_excel = 'N'

            if self.checkbox_reais_mil.get() == 'on':
                intDiv = 1000
                chk_reais_mil = 1000         
            else:
                intDiv = 1
                chk_reais_mil = 1
            
            Dta_Inicio = self.entry_dt_inicio.get()
            Dta_Inicio_str = datetime.strptime(Dta_Inicio, "%d/%m/%Y")

            dtaIni_obj = datetime.strptime(Dta_Inicio, "%d/%m/%Y")
            dtaFim_obj = dtaIni_obj.replace(year=dtaIni_obj.year + 4)
            Dta_Fim = dtaFim_obj.strftime("%d/%m/%Y")

            Ano_Inicial = dtaIni_obj.year
            Ano_Final = dtaFim_obj.year

            Ano_1 = Ano_Inicial
            Ano_2 = Ano_1 + 1
            Ano_3 = Ano_2 + 1
            Ano_4 = Ano_3 + 1
            Ano_5 = Ano_4 + 1
            Ano_6 = Ano_5 + 1

            lista = self.consulta_relatorio_orcamento(ID_Empresa, ID_Orcamento, ID_Centro_Resultado, Dta_Inicio_str, Dta_Fim, strClassificacao)
            if lista == []:
                # Limpa a lista atual antes de inserir novos resultados
                self.LOrcamento.delete(*self.LOrcamento.get_children())
                messagebox.showinfo("Informação", "Nenhum orçamento encontrado.", parent=janela)
                return
            
            ## Listbox _ Informações Pesquisa
            bg_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
            text_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
            selected_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
            treestyle = ttk.Style()
            treestyle.theme_use('default')
            treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
            treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
            
            self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
            self.fr_list.place(relx=0.005, rely=0.085, relwidth=0.99, relheight=0.91)

            self.scrollbar_orcamento = ttk.Scrollbar(self.fr_list, orient='vertical')
            self.scrollbar_orcamento.pack(side='right', fill='y')

            # Widgets - Listar Valores
            self.LOrcamento = ttk.Treeview(self.fr_list, height=7, column=(
                                                                'Codigo', 
                                                                'Descricao', 
                                                                'Jan', 
                                                                'Fev', 
                                                                'Mar', 
                                                                'Abr',
                                                                'Mai',
                                                                'Jun',
                                                                'Jul',
                                                                'Ago',
                                                                'Set',
                                                                'Out',
                                                                'Nov',
                                                                'Dez',
                                                                'Total-Ano1',
                                                                'Total-Ano2',
                                                                'Total-Ano3',
                                                                'Total-Ano4',
                                                                'Total-Ano5',
                                                                'Total-Ano6'
                                                                ), show='headings')
            
            # self.LOrcamento.heading('#0', text='#', anchor='center')
            self.LOrcamento.heading('#1', text='Código', anchor='center')
            self.LOrcamento.heading('#2', text='Descrição', anchor='center')
            self.LOrcamento.heading('#3', text='Jan', anchor='center')
            self.LOrcamento.heading('#4', text='Fev', anchor='center')
            self.LOrcamento.heading('#5', text='Mar', anchor='center')
            self.LOrcamento.heading('#6', text='Abr', anchor='center')
            self.LOrcamento.heading('#7', text='Mai', anchor='center')
            self.LOrcamento.heading('#8', text='Jun', anchor='center')
            self.LOrcamento.heading('#9', text='Jul', anchor='center')
            self.LOrcamento.heading('#10', text='Ago', anchor='center')
            self.LOrcamento.heading('#11', text='Set', anchor='center')
            self.LOrcamento.heading('#12', text='Out', anchor='center')
            self.LOrcamento.heading('#13', text='Nov', anchor='center')
            self.LOrcamento.heading('#14', text='Dez', anchor='center')
            self.LOrcamento.heading('#15', text=Ano_1, anchor='center')
            self.LOrcamento.heading('#16', text=Ano_2, anchor='center')
            self.LOrcamento.heading('#17', text=Ano_3, anchor='center')
            self.LOrcamento.heading('#18', text=Ano_4, anchor='center')
            self.LOrcamento.heading('#19', text=Ano_5, anchor='center')
            self.LOrcamento.heading('#20', text=Ano_6, anchor='center')

            Col = 50

            # self.LOrcamento.column('#0', width=2, anchor='w')
            self.LOrcamento.column('Codigo', width=50, anchor='w')
            self.LOrcamento.column('Descricao', width=100, anchor='w')
            self.LOrcamento.column('Jan', width=Col, anchor='e')
            self.LOrcamento.column('Fev', width=Col, anchor='e')
            self.LOrcamento.column('Mar', width=Col, anchor='e')
            self.LOrcamento.column('Abr', width=Col, anchor='e')
            self.LOrcamento.column('Mai', width=Col, anchor='e')
            self.LOrcamento.column('Jun', width=Col, anchor='e')
            self.LOrcamento.column('Jul', width=Col, anchor='e')
            self.LOrcamento.column('Ago', width=Col, anchor='e')
            self.LOrcamento.column('Set', width=Col, anchor='e')
            self.LOrcamento.column('Out', width=Col, anchor='e')
            self.LOrcamento.column('Nov', width=Col, anchor='e')
            self.LOrcamento.column('Dez', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano1', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano2', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano3', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano4', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano5', width=Col, anchor='e')
            self.LOrcamento.column('Total-Ano6', width=Col, anchor='e')
            
            
            self.LOrcamento.pack(expand=True, fill='both')
            self.LOrcamento.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)
            
            # Limpa a lista atual antes de inserir novos resultados
            self.LOrcamento.delete(*self.LOrcamento.get_children())

            ano_inicial = Dta_Inicio_str.year
            # Iniciando as variáveis totais
            valor_mes = [0] * 12  # Holds monthly totals
            total_geral = [0] * 19
            total_ano = [0] * 6  # Holds monthly totals
            
            result_list = []
            i = 0
            if strClassificacao == 'Centro Resultado':
                ult_centro = lista[i]['Centro']
                str_desc_centro = lista['Cen_Descricao']
                item = {
                    'Centro': ult_centro,
                    'DescSecundario': str_desc_centro,
                    'SubItems': []  
                }
                
                result_list.append(item)

                while i < len(lista) and lista[i]['Centro'] == ult_centro:
                    dta_ref_calculo = Dta_Inicio 

                    for coluna in range(1, 13):  # Loop through 1 to 12 for each month
                        if lista:
                            dta_lcto = lista[i]['DtaLcto']

                            if dta_lcto.year == ano_inicial and lista[i]['Centro'] == ult_centro:
                                if dta_lcto >= dta_ref_calculo:  # Compare date
                                    if coluna == dta_lcto.month:
                                        valor = lista[i]['Vlr'] / intDiv  # Assuming intDiv is a defined variable
                                        item['SubItems'].append(f"{valor:,.0f}")  # Format value
                                        total_ano[0] += valor  # Total for the current year
                                        total_geral[coluna - 1] += valor  # Update corresponding monthly total

                            # Update reference date for the next comparison
                            dta_ref_calculo = (dta_ref_calculo.replace(day=1) + timedelta(days=32)).replace(day=1)

                            # Move to the next record (in the actual data processing flow)
                            i += 1

                # After processing, prepare to add monthly totals to subitems
                for i in range(5):
                    if total_ano[i] == 0:
                        item['SubItems'].append("-")
                    else:
                        item['SubItems'].append(f"{total_ano[i]:,.0f}")

                    total_geral[i] += total_ano[i]
                    total_ano[i] = 0  # Reset for the next iteration

            elif strClassificacao == 'Natureza Financeira':
                ult_centro = lista[i]['Centro']
                nr_registros = (len(lista))
                
                while (i + 1) <= nr_registros and lista[i]['Centro'] == ult_centro:
                    ult_conta = lista[i]['Conta']
                    NroDigitos = len(ult_conta)
                    str_desc_conta = lista[i]['DescSecundario']
                    item = {
                            'Conta': ult_conta,
                            'Descricao': str_desc_conta,
                            'Jan': [],
                            'Fev': [],  
                            'Mar': [],  
                            'Abr': [],  
                            'Mai': [],  
                            'Jun': [],  
                            'Jul': [],  
                            'Ago': [],  
                            'Set': [],  
                            'Out': [],  
                            'Nov': [],  
                            'Dez': [],  
                            'Total_1': [],  
                            'Total_2': [],  
                            'Total_3': [],  
                            'Total_4': [],  
                            'Total_5': [],
                            'Total_6': []    
                            }
                    
                    while (i + 1) <= nr_registros  and lista[i]['Centro'] == ult_centro and lista[i]['Conta'] == ult_conta:
                        dta_ref_calculo = datetime.strptime(Dta_Inicio, "%d/%m/%Y").date()
                        
                        for coluna in range(1, 13):
                            if (i + 1) <= nr_registros: 
                                dta_lcto = lista[i]['DtaLcto']
                                
                                if dta_lcto.year == ano_inicial and lista[i]['Conta'] == ult_conta:
                                    if dta_lcto >= dta_ref_calculo:  
                                        if coluna == dta_lcto.month:
                                            valor = lista[i]['Vlr'] / intDiv  
                                            valor_mes[coluna - 1] += valor
                                            NroDigitos = len(ult_conta)
                                            total_ano[0] += valor  
                                            if NroDigitos == 9:
                                                total_geral[coluna - 1] += valor
                                            
                                            if (i + 1) <= nr_registros:
                                                i += 1
                                        else:
                                            valor_mes[coluna - 1] += 0
                                    else:
                                        valor_mes[coluna - 1] += 0
                                    
                                    # dta_ref_calculo = dta_ref_calculo + relativedelta(months=1)
                                    # dta_ref_calculo = self.ult_dia_mes(dta_ref_calculo)
                                    # dta_ref_calculo = datetime.strptime(dta_ref_calculo, "%Y-%m-%d").date()
                                else:
                                    valor_mes[coluna - 1] += 0
                            else:
                                valor_mes[coluna - 1] += 0
                        
                        item['Jan'].append(self.format_valor_fx(valor_mes[0]))  
                        item['Fev'].append(self.format_valor_fx(valor_mes[1]))  
                        item['Mar'].append(self.format_valor_fx(valor_mes[2]))  
                        item['Abr'].append(self.format_valor_fx(valor_mes[3]))  
                        item['Mai'].append(self.format_valor_fx(valor_mes[4]))  
                        item['Jun'].append(self.format_valor_fx(valor_mes[5]))  
                        item['Jul'].append(self.format_valor_fx(valor_mes[6]))  
                        item['Ago'].append(self.format_valor_fx(valor_mes[7]))  
                        item['Set'].append(self.format_valor_fx(valor_mes[8]))  
                        item['Out'].append(self.format_valor_fx(valor_mes[9]))  
                        item['Nov'].append(self.format_valor_fx(valor_mes[10]))  
                        item['Dez'].append(self.format_valor_fx(valor_mes[11]))
                        item['Total_1'].append(self.format_valor_fx(total_ano[0]))    


                        while (i < nr_registros and lista[i]['Centro'] == ult_centro and lista[i]['Conta'] == ult_conta):
                            dta_lcto = lista[i]['DtaLcto']
                            if dta_lcto.year == ano_inicial:  
                                for year_offset in range(1, 6):
                                    if dta_lcto.year == ano_inicial + year_offset:
                                        total_ano[year_offset] += lista[i]['Vlr'] / intDiv
                                        
                            i += 1
                            
                        item['Total_2'].append(self.format_valor_fx(total_ano[1]))
                        item['Total_3'].append(self.format_valor_fx(total_ano[2]))
                        item['Total_4'].append(self.format_valor_fx(total_ano[3]))
                        item['Total_5'].append(self.format_valor_fx(total_ano[4]))
                        item['Total_6'].append(self.format_valor_fx(total_ano[5]))

                        total_ano[0] = 0
                        total_ano[1] = 0
                        total_ano[2] = 0
                        total_ano[3] = 0
                        total_ano[4] = 0
                        total_ano[5] = 0
                        
                    for ii in range(5):
                        if len(ult_conta) == 9:
                            total_geral[ii + 13] += total_ano[ii]  
                    
                            
                    self.LOrcamento.insert("", "end", text=ult_conta, values=(
                                                                            item['Conta'], 
                                                                            item['Descricao'],  
                                                                            item['Jan'], 
                                                                            item['Fev'], 
                                                                            item['Mar'], 
                                                                            item['Abr'], 
                                                                            item['Mai'], 
                                                                            item['Jun'],
                                                                            item['Jul'],
                                                                            item['Ago'],
                                                                            item['Set'],
                                                                            item['Out'],
                                                                            item['Nov'],
                                                                            item['Dez'],
                                                                            item['Total_1'],
                                                                            item['Total_2'],
                                                                            item['Total_3'],
                                                                            item['Total_4'],
                                                                            item['Total_5'],
                                                                            item['Total_6'])
                                                                            )
                    for coluna in range(1, 13):  
                        valor_mes[coluna - 1] = 0
                    
                    for year_offset in range(1, 6):
                        total_ano[year_offset] = 0
                        

            self.LOrcamento.tag_configure('odd', background='#eee')
            self.LOrcamento.tag_configure('even', background='#ddd')
            self.LOrcamento.configure(yscrollcommand=self.scrollbar_orcamento.set)
            self.scrollbar_orcamento.configure(command=self.LOrcamento.yview)

            def selected_premissas():
                selected_item = self.LOrcamento.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.LOrcamento.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.LOrcamento.item(selected_item, 'values')
                    
                    ID_Lcto = ''
                    if Empresa_DS != '':
                        ID_Empresa = self.obter_Empresa_ID(Empresa_DS)
                    else:
                        messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                        return
                    
                    if Orc_DS != '':
                        ID_Orc = self.obter_Orc_ID(Orc_DS)
                    else:
                        messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!")
                        return
                    
                    ID_Lcto = values[0]
                    self.premissas_orcamento(ID_Empresa, Empresa_DS, ID_Orc, Orc_DS, ID_Lcto)
                
            def postPopUpMenu(event):
                row_id = self.LOrcamento.identify_row(event.y)
                if row_id:  # Realiza a verificação se a linha existe.
                    self.LOrcamento.selection_set(row_id)
                    row_values = self.LOrcamento.item(row_id)['values']
                    # print(row_values)
                    postPopUpMenu = tk.Menu(self.LOrcamento, tearoff=0, font=('Verdana', 11))
                    postPopUpMenu.add_command(label='Consultar Premissas', accelerator='Ctrl+S', command= selected_premissas)
                    postPopUpMenu.post(event.x_root, event.y_root)
            
            self.LOrcamento.bind("<Double-1>", postPopUpMenu)  # 'Double-1' é o duplo clique do mouse
            self.LOrcamento.bind("<Button-3>", postPopUpMenu)  # 'Button-3' é o clique direito do mouse
            self.LOrcamento.bind('<Control-s>', lambda event: selected_premissas() if self.LOrcamento.selection() else None)
            
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_orcamento = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=consultar)
        self.btn_consultar_orcamento.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)

    def consulta_relatorio_orcamento(self, ID_Empresa, ID_Orcamento, ID_Centro_Resultado, Dta_Inicio, Dta_Fim, strClassificacao):
        # Lista para armazenar as condições
        
        if isinstance(Dta_Inicio, str):
            Dta_Inicio = datetime.strptime(Dta_Inicio, "%d/%m/%Y")
        elif not isinstance(Dta_Inicio, datetime):
            raise ValueError("Dta_Inicio must be a string or a datetime object")

        if isinstance(Dta_Fim, str):
            Dta_Fim = datetime.strptime(Dta_Fim, "%d/%m/%Y")
        elif not isinstance(Dta_Fim, datetime):
            raise ValueError("Dta_Fim must be a string or a datetime object")

        Dta_Inicio = Dta_Inicio.strftime("%Y-%m-%d")
        Dta_Fim = Dta_Fim.strftime("%Y-%m-%d")

        conditions_1 = []
        conditions_2 = []

        conditions_1.append("oo.Prem_Tipo='PRM'")
        conditions_1.append(f"oo.Pri_ID = '{ID_Empresa}'")
        conditions_1.append(f"oo.Orc_ID = '{ID_Orcamento}'")
        
        if ID_Centro_Resultado != '':
            conditions_1.append(f"oo.Cen_IDDebito = '{ID_Centro_Resultado}'")
            
        conditions_1.append(f"oo.Orc_Data BETWEEN '{Dta_Inicio}' AND '{Dta_Fim}'")
        
        conditions_2.append("oo.Prem_Tipo='PRM'")
        conditions_2.append(f"oo.Pri_ID = '{ID_Empresa}'")
        conditions_2.append(f"oo.Orc_ID = '{ID_Orcamento}'")
        
        if ID_Centro_Resultado != '':
            conditions_2.append(f"oo.Cen_IDCredito = '{ID_Centro_Resultado}'")
        conditions_2.append(f"oo.Orc_Data BETWEEN '{Dta_Inicio}' AND '{Dta_Fim}'")
        
        if strClassificacao == 'Centro Resultado':
            str_sql = f"""
                        SELECT 
                        Centro        AS Centro, 
                        Cen_Descricao AS Cen_Descricao, 
                        DtaLcto       AS DtaLcto, 
                        SUM(Vlr)      AS Vlr 
                        FROM (
                            SELECT 
                                oo.Cen_IDDebito        AS Centro, 
                                cc.Cen_Descricao       AS Cen_Descricao, 
                                oo.Orc_Data            AS DtaLcto, 
                                SUM(oo.Orc_Valor * -1) AS Vlr
                            FROM orc_orcado oo
                            INNER JOIN centrocusto cc ON cc.Cen_ID = oo.Cen_IDDebito AND cc.Empresa_ID = oo.Pri_ID
                            WHERE {' AND '.join(conditions_1)}
                            GROUP BY Centro, Cen_Descricao, DtaLcto
                        UNION ALL 
                            SELECT 
                                oo.Cen_IDCredito      AS Centro, 
                                cc.Cen_Descricao      AS Cen_Descricao, 
                                oo.Orc_Data           AS DtaLcto, 
                                SUM(oo.Orc_Valor * 1) AS Vlr
                            FROM orc_orcado oo
                            INNER JOIN centrocusto cc ON cc.Cen_ID = oo.Cen_IDCredito AND cc.Empresa_ID = oo.Pri_ID
                            WHERE {' AND '.join(conditions_2)}
                            GROUP BY Centro, Cen_Descricao, DtaLcto
                        ) AS COMPLETO
                        GROUP BY Centro, Cen_Descricao, DtaLcto
                        ORDER BY LEFT(Centro, 7), DtaLcto
                    """
        elif strClassificacao == 'Natureza Financeira':
            NrCampos = 1
            str_sql = ''
            for viContNivel in range(1, 6):
                str_sql += f"""
                            SELECT 
                                oo.Cen_IDDebito        AS Centro, 
                                ct1.Nat_ID             AS Conta,
                                ct1.Nat_Descricao      AS DescSecundario, 
                                oo.Orc_Data            AS DtaLcto,
                                SUM(oo.Orc_Valor * -1) AS Vlr
                            FROM orc_orcado oo
                            INNER JOIN TB_Natureza ct ON ct.Nat_ID = oo.Con_IDDebito AND ct.Empresa_ID = oo.Pri_ID
                            INNER JOIN (SELECT Nat_ID, Nat_Descricao FROM TB_Natureza WHERE Empresa_ID = '{ID_Empresa}' GROUP BY Nat_ID, Nat_Descricao) ct1 ON ct1.Nat_ID = LEFT(ct.Nat_ID, {NrCampos})
                            INNER JOIN centrocusto cc ON cc.Cen_ID = oo.Cen_IDDebito AND cc.Empresa_ID = oo.Pri_ID
                            WHERE {' AND '.join(conditions_1)}
                            GROUP BY Centro, Conta, DescSecundario, DtaLcto
                            UNION ALL
                            SELECT 
                                oo.Cen_IDCredito      AS Centro, 
                                ct1.Nat_ID            AS Conta,
                                ct1.Nat_Descricao     AS DescSecundario, 
                                oo.Orc_Data           AS DtaLcto,
                                SUM(oo.Orc_Valor * 1) AS Vlr
                            FROM orc_orcado oo
                            INNER JOIN TB_Natureza ct ON ct.Nat_ID = oo.Con_IDCredito AND ct.Empresa_ID = oo.Pri_ID
                            INNER JOIN (SELECT Nat_ID, Nat_Descricao FROM TB_Natureza WHERE Empresa_ID = '{ID_Empresa}' GROUP BY Nat_ID, Nat_Descricao) ct1 ON ct1.Nat_ID = LEFT(ct.Nat_ID, {NrCampos})
                            INNER JOIN centrocusto cc ON cc.Cen_ID = oo.Cen_IDCredito AND cc.Empresa_ID = oo.Pri_ID
                            WHERE {' AND '.join(conditions_2)}
                            GROUP BY Centro, Conta, DescSecundario, DtaLcto
                        """

                if viContNivel != 5:
                    str_sql += " UNION ALL "
                if NrCampos == 1:
                    NrCampos = 2
                elif NrCampos == 2:
                    NrCampos = 4
                elif NrCampos == 4:
                    NrCampos = 6
                elif NrCampos == 6:
                    NrCampos = 9

            str_sql += " ORDER BY Centro, LEFT(Conta, 9), DtaLcto"
        
        myresult = db._querying(str_sql)
        consulta = [(consulta) for consulta in myresult]

        return consulta       
    
Relatorio_Orcamento()