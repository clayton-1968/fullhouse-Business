from imports import *
from widgets import Widgets
from datetime import datetime
from PIL import ImageTk, Image

################# criando janela ###############
class Cronograma_Atividades(Widgets):
    def cronograma_atividades(self):
        self.window_one.title('Cronograma Atividades')
        self.clearFrame_principal()
        self.frame_cabecalho_cronograma_atividades(self.principal_frame)
        self.frame_list_cronograma_atividades(self.principal_frame)
       
################# dividindo a janela ###############
    def frame_cabecalho_cronograma_atividades(self, janela):
        # Projeto
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.25
        coordenadas_relheight = 0.07
        fr_projeto = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_projeto = customtkinter.CTkLabel(fr_projeto, text="Projetos")
        lb_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        projetos = []

        self.entry_projeto = AutocompleteCombobox(fr_projeto, width=30, font=('Times', 11), completevalues=projetos)
        self.entry_projeto.pack()
        self.entry_projeto.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_projeto.bind("<Button-1>", lambda event: self.atualizar_projetos(event, self.entry_projeto))
        self.entry_projeto.bind('<Down>', lambda event: self.atualizar_projetos(event, self.entry_projeto))

        # # Alteração
        # coordenadas_relx = 0.26
        # coordenadas_rely = 0.01
        # coordenadas_relwidth = 0.69
        # coordenadas_relheight = 0.07
        # fr_alteracao_tarefa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        # fr_alteracao_tarefa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        # lb_opcoes = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Atualização Tarefa")
        # lb_opcoes.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)
        
        # # Nr da Tarefa
        # lb_tarefa_num = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Nr.")
        # lb_tarefa_num.place(relx=0.005, rely=0.25, relheight=0.25, relwidth=0.05)
        # self.entry_tarefa_num = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_num.place(relx=0.005, rely=0.5, relwidth=0.05, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))

        # # Código da Tarefa
        # lb_tarefa_codigo = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Código")
        # lb_tarefa_codigo.place(relx=0.06, rely=0.25, relheight=0.25, relwidth=0.05)
        # self.entry_tarefa_codigo = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_codigo.place(relx=0.06, rely=0.5, relwidth=0.10, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))

        # # Responsável
        # lb_tarefa_responsavel = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Responsável")
        # lb_tarefa_responsavel.place(relx=0.175, rely=0.25, relheight=0.25, relwidth=0.10)

        # self.entry_tarefa_responsavel = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_responsavel.place(relx=0.165, rely=0.5, relwidth=0.20, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))

        # # Tempo de Espera
        # lb_tarefa_tempo_espera = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Espera")
        # lb_tarefa_tempo_espera.place(relx=0.37, rely=0.25, relheight=0.25, relwidth=0.05)
        # self.entry_tarefa_tempo_espera = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_tempo_espera.place(relx=0.37, rely=0.5, relwidth=0.05, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))

        # # Tempo Prazao de Execução
        # lb_tarefa_tempo_execucao = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Prazo")
        # lb_tarefa_tempo_execucao.place(relx=0.425, rely=0.25, relheight=0.25, relwidth=0.05)
        # self.entry_tarefa_tempo_execucao = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_tempo_execucao.place(relx=0.425, rely=0.5, relwidth=0.05, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))

        # # % de Execução
        # lb_tarefa_per_execucao = customtkinter.CTkLabel(fr_alteracao_tarefa, text="% Exc.")
        # lb_tarefa_per_execucao.place(relx=0.48, rely=0.25, relheight=0.25, relwidth=0.05)
        # self.entry_tarefa_per_execucao = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.RIGHT)
        # self.entry_tarefa_per_execucao.place(relx=0.48, rely=0.5, relwidth=0.08, relheight=0.4)
        # # self.entry_tarefa_num.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_doc_dt_emissao))
        
        # # Data Inicio Previsto
        # lb_tarefa_dta_prev_inicio = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Data Início Prev.")
        # lb_tarefa_dta_prev_inicio.place(relx=0.565, rely=0.25, relheight=0.25, relwidth=0.08)
        # self.entry_tarefa_dta_prev_inicio = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.CENTER)
        # self.entry_tarefa_dta_prev_inicio.place(relx=0.565, rely=0.5, relwidth=0.08, relheight=0.4)
        # self.entry_tarefa_dta_prev_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_tarefa_dta_prev_inicio))
        # # self.entry_doc_dt_emissao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_doc_dt_emissao, self.entry_doc_serie))
        
        # # Data Inicio Real
        # lb_tarefa_dta_real_inicio = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Data Início Real")
        # lb_tarefa_dta_real_inicio.place(relx=0.65, rely=0.25, relheight=0.25, relwidth=0.08)
        # self.entry_tarefa_dta_real_inicio = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.CENTER)
        # self.entry_tarefa_dta_real_inicio.place(relx=0.65, rely=0.5, relwidth=0.08, relheight=0.4)
        # self.entry_tarefa_dta_real_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_tarefa_dta_real_inicio))
        # # self.entry_doc_dt_emissao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_doc_dt_emissao, self.entry_doc_serie))

        # # Data Conclusão Previsto
        # lb_tarefa_dta_prev_conclusao = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Data Concl. Prev.")
        # lb_tarefa_dta_prev_conclusao.place(relx=0.735, rely=0.25, relheight=0.25, relwidth=0.08)
        # self.entry_tarefa_dta_prev_conclusao = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.CENTER)
        # self.entry_tarefa_dta_prev_conclusao.place(relx=0.735, rely=0.5, relwidth=0.08, relheight=0.4)
        # self.entry_tarefa_dta_prev_conclusao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_tarefa_dta_prev_conclusao))
        # # self.entry_doc_dt_emissao.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_doc_dt_emissao, self.entry_doc_serie))
        
        # # Data Conclusao Real
        # lb_tarefa_dta_real_conclusao = customtkinter.CTkLabel(fr_alteracao_tarefa, text="Data Concl. Real")
        # lb_tarefa_dta_real_conclusao.place(relx=0.82, rely=0.25, relheight=0.25, relwidth=0.08)
        # self.entry_tarefa_dta_real_conclusao = customtkinter.CTkEntry(fr_alteracao_tarefa, fg_color="black", text_color="white", justify=tk.CENTER)
        # self.entry_tarefa_dta_real_conclusao.place(relx=0.82, rely=0.5, relwidth=0.08, relheight=0.4)
        # self.entry_tarefa_dta_real_conclusao.bind("<Button-1>", lambda event: self.calendario(event, self.entry_tarefa_dta_real_conclusao))

        # # Botão de Gravar
        # icon_image = self.base64_to_photoimage('save')
        # self.btn_tarefa_gravar = customtkinter.CTkButton(fr_alteracao_tarefa, text='', image=icon_image, fg_color='transparent', command=[])
        # self.btn_tarefa_gravar.pack(pady=10)
        # self.btn_tarefa_gravar.place(relx=0.905, rely=0.30, relwidth=0.085, relheight=0.60)
        
        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_projeto = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=self.consulta_cronograma_atividades)
        self.btn_consultar_projeto.pack(pady=10)
        self.btn_consultar_projeto.place(relx=0.955, rely=0.02, relwidth=0.04, relheight=0.05)

    def frame_list_cronograma_atividades(self, janela):
        ## Listbox _ Cronograma de Atividades
        bg_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = janela._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
        treestyle = ttk.Style()
        # treestyle.theme_use('default')
        # treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        # treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.085, relwidth=0.99, relheight=0.91)

        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Widgets - Listar Tarefas
        self.LCronograma = ttk.Treeview(self.fr_list, height=7, column=(
                                                            'Nr',
                                                            'tarefa_id',
                                                            'tarefa_DS',
                                                            'responsavel_nome',
                                                            'tarefa_dependencia',
                                                            'tempo_espera',
                                                            'tempo_previsto',
                                                            'percentual_execucao',
                                                            'data_inicial_prevista',
                                                            'data_inicial_realizada',
                                                            'data_conclusao_prevista',
                                                            'data_conclusao_realizada',
                                                            'observacao',
                                                            )) #, show='headings'
                    
        
        self.LCronograma.heading('#0', text='Status', anchor='center')
        self.LCronograma.heading('#1', text='Nr.', anchor='center')
        self.LCronograma.heading('#2', text='Código', anchor='center')
        self.LCronograma.heading('#3', text='Descrição', anchor='center')
        self.LCronograma.heading('#4', text='Responsável', anchor='center')
        self.LCronograma.heading('#5', text='Dependência', anchor='center')
        self.LCronograma.heading('#6', text='Espera', anchor='center')
        self.LCronograma.heading('#7', text='Prazo', anchor='center')
        self.LCronograma.heading('#8', text='% Conclusão', anchor='center')
        self.LCronograma.heading('#9', text='Início Prev.', anchor='center')
        self.LCronograma.heading('#10', text='Início Real', anchor='center')
        self.LCronograma.heading('#11', text='Conclusão Prev.', anchor='center')
        self.LCronograma.heading('#12', text='Conclusão Real', anchor='center')
        self.LCronograma.heading('#13', text='Observação', anchor='center')
        
        
        Col = 50
        Col1 = 30

        self.LCronograma.column('#0', width=2, anchor='c')
        self.LCronograma.column('Nr', width=5, anchor='c')
        self.LCronograma.column('tarefa_id', width=40, anchor='w')
        self.LCronograma.column('tarefa_DS', width=400, anchor='w')
        self.LCronograma.column('responsavel_nome', width=25, anchor='w')
        self.LCronograma.column('tarefa_dependencia', width=Col, anchor='c')
        self.LCronograma.column('tempo_espera', width=Col1, anchor='c')
        self.LCronograma.column('tempo_previsto', width=Col1, anchor='c')
        self.LCronograma.column('percentual_execucao', width=Col1, anchor='e')
        self.LCronograma.column('data_inicial_prevista', width=Col, anchor='e')
        self.LCronograma.column('data_inicial_realizada', width=Col, anchor='e')
        self.LCronograma.column('data_conclusao_prevista', width=Col, anchor='e')
        self.LCronograma.column('data_conclusao_realizada', width=Col, anchor='e')
        self.LCronograma.column('observacao', width=300, anchor='w')
                
        
        self.LCronograma.pack(expand=True, fill='both')
        self.LCronograma.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)
    
    def consulta_cronograma_atividades(self):
        if self.entry_projeto.get() != '':
            projeto_id = self.obter_Projeto_ID(self.entry_projeto.get())
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher o Projeto!!")
            return
        
        # Limpa a lista atual antes de inserir novos resultados
        self.LCronograma.delete(*self.LCronograma.get_children())

        sql_query = """
                        SELECT projeto_ID, projeto_DS, tarefa_ID, tarefa_DS, responsavel_nome,
                            tarefa_dependencia, tempo_espera, tempo_previsto, percentual_execucao,
                            data_Inicial_Prevista, data_Inicial_Realizada, dias_diferenca_inicio,
                            data_conclusao_prevista, data_conclusao_realizada, prazo_fatal_dias,
                            dias_diferenca, status, observacao
                        FROM programas_atividades 
                        WHERE projeto_ID = %s
                        ORDER BY tarefa_ID
                    """
        
        self.list_tarefas = []
        self.list_tarefas = db.executar_consulta(sql_query, projeto_id)
        
        self.icon_image_azul = self.base64_to_farois('semafaro_azul') 
        self.icon_image_verde = self.base64_to_farois('semafaro_verde') 
        self.icon_image_amarelo = self.base64_to_farois('semafaro_amarelo') 
        self.icon_image_vermelho = self.base64_to_farois('semafaro_vermelho') 
        
        if not self.list_tarefas:
            # Tarefa em Branco
            tarefa_info= []
            tarefa_info = (
                            '01',
                            ' ' * round(2) + "Preencher Descrição Nova Tarefa...................!!!!",
                            '',
                            '',
                            0,
                            1,
                            '0.00%',
                            datetime.now().strftime("%d/%m/%Y"),
                            '',
                            datetime.now().strftime("%d/%m/%Y"),
                            '',
                            ''
                            )
            self.LCronograma.insert(parent="", index="end", image=self.icon_image_amarelo, values=tarefa_info)
            
            # Segunda Tarefa em Branco
            tarefa_info= []
            tarefa_info = (
                            '01.01',
                            ' ' * round(5) + "Preencher Descrição Nova Tarefa...................!!!!",
                            '',
                            '',
                            0,
                            1,
                            '0.00%',
                            datetime.now().strftime("%d/%m/%Y"),
                            '',
                            datetime.now().strftime("%d/%m/%Y"),
                            '',
                            '',
                            )
            self.LCronograma.insert(parent="", index="end", image=self.icon_image_amarelo, values=tarefa_info)

        else:
            tarefa_info= []
            nrregistros = 1
            for record in self.list_tarefas:
                nrcarat = len(record.get('tarefa_ID'))
                dta_branco = str('1899-12-30')
                data_realizada = datetime.strftime(record.get('data_Inicial_Realizada'), "%Y-%m-%d")
                data_conclusao = datetime.strftime(record.get('data_conclusao_realizada'), "%Y-%m-%d")
                data_realizada_prev = datetime.strftime(record.get('data_Inicial_Prevista'), "%Y-%m-%d")
                data_conclusao_prev = datetime.strftime(record.get('data_conclusao_prevista'), "%Y-%m-%d")
                per_conclusao = f"{record.get('percentual_execucao'):.2%}"

                semaforo = self.status_on(data_realizada_prev , data_realizada, data_conclusao_prev, data_conclusao, per_conclusao)
                
                if data_realizada_prev == str(dta_branco):
                    data_realizada_prev = ''
                else:
                    data_realizada_prev = datetime.strptime(data_realizada_prev, "%Y-%m-%d")
                    data_realizada_prev =data_realizada_prev.strftime("%d/%m/%Y")  # Formato desejado: "DD/MM/YYYY"
                
                if data_realizada == str(dta_branco):
                    data_realizada = ''
                else:
                    data_realizada = datetime.strptime(data_realizada, "%Y-%m-%d")
                    data_realizada = data_realizada.strftime("%d/%m/%Y")  # Formato desejado: "DD/MM/YYYY"

                if data_conclusao == str(dta_branco):
                    data_conclusao = ''
                else:
                    data_conclusao = datetime.strptime(data_conclusao, "%Y-%m-%d")
                    data_conclusao = data_conclusao.strftime("%d/%m/%Y")  # Formato desejado: "DD/MM/YYYY"

                if data_conclusao_prev == str(dta_branco):
                    data_conclusao_prev = ''
                else:
                    data_conclusao_prev = datetime.strptime(data_conclusao_prev, "%Y-%m-%d")
                    data_conclusao_prev = data_conclusao_prev.strftime("%d/%m/%Y")  # Formato desejado: "DD/MM/YYYY"

                if record.get('record.observacao') is None:
                    Observacao = ''
                else:
                    Observacao = record.get('record.observacao')                

                tarefa_info = (
                    nrregistros,
                    record.get('tarefa_ID'),
                    ' ' * round(nrcarat) + record.get('tarefa_DS'),
                    record.get('responsavel_nome'),
                    record.get('tarefa_dependencia'),
                    record.get('tempo_espera') if record.get('tempo_espera') is not None else 0,
                    record.get('tempo_previsto'),
                    per_conclusao,
                    data_realizada_prev,
                    data_realizada,
                    data_conclusao_prev,
                    data_conclusao,
                    Observacao,
                )
                
                self.LCronograma.insert(parent="", index="end", image=semaforo, values=tarefa_info)
                nrregistros += 1

        self.LCronograma.tag_configure('odd', background='#eee')
        self.LCronograma.tag_configure('even', background='#ddd')
        self.LCronograma.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.LCronograma.yview)

        self.atualiza_cronograma_interacao(10)
        self.ajustar_list()

        def selected_incluir():
            selected_item = self.LCronograma.selection()
            if selected_item:
                item_text = self.LCronograma.item(selected_item, 'text')
                values = self.LCronograma.item(selected_item, 'values')
                lin = self.LCronograma.index(selected_item)
                tarefa_id = values[1]
                self.incluir_tarefas(projeto_id, lin, tarefa_id, selected_item)
            else:
                messagebox.showinfo("Erro", "Selecione a posição para inclusão da Tarefa!")
                return
                # lin = 'end'

        def selected_anexar():
            selected_item = self.LCronograma.selection()
            if selected_item:
                # Texto do item selecionado
                item_text = self.LCronograma.item(self.LCronograma.selection(), 'text')
                # Obtém os valores associados (como uma tupla)
                values = self.LCronograma.item(self.LCronograma.selection(), 'values')
                
                ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
                UF = values[6]
                Cidade = values[5]
                Tipo = values[3]
                Nome_da_Area = values[4]
                
                self.lista_negocio = self.Consulta_Negocio(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
                if self.lista_negocio[0].get('Http') != '':
                    url = self.lista_negocio[0].get('Http')
                else:
                    messagebox.showwarning("Maps", "Coordenadas Não Cadastrada!!!")
                    return
                
                url = url.strip()  # Remove espaços em branco no início e no fim
                webbrowser.open(url)

        def selected_excluir():
            # self.LCronograma.delete(row_id)
            messagebox.showinfo("Informação", "Em Manutenção!!")

        
        def postPopUpMenu(event):
            row_id = self.LCronograma.identify_row(event.y)
            if row_id:  # Realiza a verificação se a linha existe.
                self.LCronograma.selection_set(row_id)
                row_values = self.LCronograma.item(row_id)['values']
                
                
                postPopUpMenu = tk.Menu(self.LCronograma, tearoff=0, font=('Verdana', 11))
                
                postPopUpMenu.add_command(label='Incluir Tarefa', accelerator='Ctrl+I', command= selected_incluir)
                postPopUpMenu.add_command(label='Alterar Tarefa', accelerator='Ctrl+A', command=selected_alterar)
                postPopUpMenu.add_command(label='Excluir Tarefa', accelerator='Delete', command=selected_excluir)
                postPopUpMenu.add_separator()
                postPopUpMenu.add_command(label='Anexar Documento', accelerator='Alt+U', command=selected_anexar)
                postPopUpMenu.post(event.x_root, event.y_root)
        # self.LCronograma.bind("<Double-1>", postPopUpMenu)  # 'Double-1' é o duplo clique do mouse
        self.LCronograma.bind("<Button-3>", postPopUpMenu)  # 'Button-3' é o clique direito do mouse
        self.LCronograma.bind('<Control-i>', lambda event: selected_incluir() if self.LCronograma.selection() else None)
        # self.LCronograma.bind('<Control-a>', lambda event: selected_alterar() if self.LCronograma.selection() else None)
        self.LCronograma.bind('<Delete>', lambda event: selected_excluir() if self.LCronograma.selection() else None)
        self.LCronograma.bind('<Control-u>', lambda event: selected_anexar() if self.LCronograma.selection() else None)

    def atualizar_dependencias(self, tarefa_id_nova):
        nr_campos = 1
        linha_base_predessessora = None

        # Primeiro loop para atualizar os números dos campos
        for i in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            self.LCronograma.item(item, text='', values=(nr_campos,) + values[1:])  
            if values[1] == tarefa_id_nova:  # Supondo que o segundo subitem é o que procuramos
                linha_base_predessessora = nr_campos
            
            nr_campos += 1

        # Segundo loop para processar as dependências
        for ii in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[ii]
            values = self.LCronograma.item(item, 'values')
            str_endereco = self.LCronograma.item(item, 'values')[4]  # Supondo que o 5º item é o subitem 4
            nr_caracteres = len(str_endereco)
                
            str_espera = self.LCronograma.item(item, 'values')[5]
            str_prazo = self.LCronograma.item(item, 'values')[6]  # Supondo que o 5º item é o subitem 4
            str_per_conclusao = self.LCronograma.item(item, 'values')[7]  # Supondo que o 5º item é o subitem 4
            str_ini_prev = self.LCronograma.item(item, 'values')[8]  # Supondo que o 5º item é o subitem 4
            str_ini_real = self.LCronograma.item(item, 'values')[9]  # Supondo que o 5º item é o subitem 4
            str_fim_prev = self.LCronograma.item(item, 'values')[10]  # Supondo que o 5º item é o subitem 4
            str_fim_real = self.LCronograma.item(item, 'values')[11]  # Supondo que o 5º item é o subitem 4
            str_obs = self.LCronograma.item(item, 'values')[12]  # Supondo que o 5º item é o subitem 4
            

            if nr_caracteres > 2:
                linha_tarefa = ""
                tarefa_dependencia = ""
                lin_dependente = ""

                for vi_contador in range(nr_caracteres):
                    char_atual = str_endereco[vi_contador]

                    if char_atual != ";":
                        lin_dependente += char_atual  # Accumula caracteres
                    if char_atual == ";" or vi_contador == nr_caracteres - 1:
                        # processa a dependência acumulada
                        dependente_num = int(lin_dependente)
                        if dependente_num > linha_base_predessessora:
                            linha_tarefa = dependente_num + 1
                        else:
                            linha_tarefa = dependente_num
                        tarefa_dependencia += str(linha_tarefa)
                        lin_dependente = ""

                        # Adiciona o delimitador se não for o último
                        if vi_contador < nr_caracteres - 1:
                            tarefa_dependencia += ";"

                # Atualiza o subitem de dependência
                self.LCronograma.item(
                                        item, 
                                        text='', 
                                        values=values[:4] + (
                                                                tarefa_dependencia, 
                                                                str_espera, 
                                                                str_prazo, 
                                                                str_per_conclusao,
                                                                str_ini_prev,
                                                                str_ini_real,
                                                                str_fim_prev,
                                                                str_fim_real,
                                                                str_obs,
                                                            )
                                        )  
            elif nr_caracteres != 0:
                dependente_num = int(str_endereco.replace("'", ""))
                if dependente_num >= linha_base_predessessora:
                    tarefa_dependencia = dependente_num + 1
                else:
                    tarefa_dependencia = dependente_num
                
                tarefa_dependencia = str(tarefa_dependencia)
                
                # Atualiza o subitem de dependência
                self.LCronograma.item(
                                        item, 
                                        text='', 
                                        values=values[:4] + (
                                                                tarefa_dependencia, 
                                                                str_espera, 
                                                                str_prazo, 
                                                                str_per_conclusao,
                                                                str_ini_prev,
                                                                str_ini_real,
                                                                str_fim_prev,
                                                                str_fim_real,
                                                                str_obs,
                                                            )
                                        ) 
            else:
                tarefa_dependencia = ""  
           
    def atualiza_cronograma_interacao(self, nr_interacao):
        calcular = True
        data_atualizacao = datetime.now()
        for _ in range(nr_interacao):
            for item_id in self.LCronograma.get_children():
                
                values = self.LCronograma.item(item_id, 'values')
                tarefa_dependencia = values[4]   
                if tarefa_dependencia:
                    self.predessessora(item_id)

        self.dta_tarefa_mae
        calcular = False

    def ajustar_list(self):
        try:
            for i in range(len(self.LCronograma.get_children())):  # Itera sobre os itens no Treeview
                item_id = self.LCronograma.get_children()[i]
                task_data = self.LCronograma.item(item_id)  # Obtém os dados do item
                tarefa_id = str(task_data['values'][1])  # Assume tarefa_ID está na posição 1
                nrcarat = len(tarefa_id.upper())
                linha = i + 1

                if linha < len(self.LCronograma.get_children()):
                    next_item_id = self.LCronograma.get_children()[linha]
                    next_task_data = self.LCronograma.item(next_item_id)
                    next_tarefa_id = str(next_task_data['values'][1])  # Assume tarefa_ID está na posição 1
                    nrcarat_seguinte = len(next_tarefa_id.upper())
                else:
                    nrcarat_seguinte = nrcarat

                # Aplica formatação baseada nos critérios
                if nrcarat_seguinte > nrcarat:
                    self.LCronograma.item(item_id, tags=('bold_blue',))  # Usar tags para aplicar estilos
                elif nrcarat_seguinte == nrcarat and nrcarat > 2:
                    self.LCronograma.item(item_id, tags=('normal_black',))
                elif nrcarat_seguinte == nrcarat and nrcarat <= 2:
                    self.LCronograma.item(item_id, tags=('bold_blue',))

                # Para última linha, verifica comparação com a linha anterior
                if i == len(self.LCronograma.get_children()) - 1:
                    tarefa_id = str(self.LCronograma.item(item_id)['values'][1])  # Assume tarefa_ID está na posição 1
                    tarefa_id_anterior = str(self.LCronograma.item(self.LCronograma.get_children()[i - 1])['values'][1])
                    if len(tarefa_id.upper()) < len(tarefa_id_anterior.upper()):
                        self.LCronograma.item(item_id, tags=('bold_blue',))

            # Configura as tags para o Treeview
            self.LCronograma.tag_configure('bold_blue', font=('Helvetica', 10, 'bold'), foreground='blue')
            self.LCronograma.tag_configure('normal_black', font=('Helvetica', 10), foreground='black')

        except Exception as e:
            messagebox.showerror("Erro!", f"Erro: {str(e)}")  # Exibe mensagem de erro        

    def status_on(self, dta_inicio_prev, dta_inicio_real, dta_conclusao_prev, dta_conclusao_real, per_conclusao):
        # try:
            if isinstance(dta_conclusao_prev, str):
                dta_conclusao_prev = datetime.strptime(dta_conclusao_prev, "%Y-%m-%d").date()
            
            today = datetime.now().date()
            if dta_inicio_real == '':
                if dta_inicio_prev < today:
                    icon_image = self.icon_image_vermelho
                else:
                    icon_image = self.icon_image_amarelo
            else:
                if dta_conclusao_real == '':
                    if dta_inicio_real != '' and dta_conclusao_prev < today:
                        icon_image = self.icon_image_vermelho
                    else:
                        icon_image = self.icon_image_azul
                elif float(per_conclusao.replace("%", "")) == 100.00:
                    icon_image = self.icon_image_verde
                elif dta_conclusao_prev >= today:
                    icon_image = self.icon_image_azul
                elif dta_conclusao_prev < today:
                    icon_image = self.icon_image_vermelho
                else:
                    icon_image = self.icon_image_amarelo

            return icon_image
           
        # except Exception as e:
            # messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def incluir_tarefas(self, projeto_id, linha, tarefa_id, selected_index):
        # Parametros Iniciais
        nrcampo = int(linha) + 2
        tarefa_id = tarefa_id.replace(".", "")
        Linha_Incluir = int(linha) + 1

        tarefa_id_nova = ''
        tarefa_ds_nova = "Preencher Descricão Nova Tarefa...................!!!!"
        responsavel_nome = ''
        tarefa_dependencia = ''
        tempo_previsto = 1
        percentual_execucao = 0
        data_inicial_prevista = datetime.now().date()
        data_conclusao_prevista = data_inicial_prevista
        dias_diferenca_inicio = ''
        
        prazo_fatal_dias = 0
        dias_diferenca_conclusao = 0
        status_projeto = ''
        observacao = ''
        
        nivel_inclusao = len(tarefa_id)
        nivel_inclusao_mae = len(tarefa_id)
        nivel_secundario = ''
        nivel_ultimo = ''
        lin = int(linha) + 1 
       
        # Checar e determinar o código novo
        for i in range(lin, len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            nivel_secundario = len(values[1].replace(".", ""))  # Supondo que o segundo subitem é o que você quer
            
            if nivel_inclusao == nivel_secundario:
                nivel_ultimo = values[1]

        # Verifica se Nivel_Ultimo está vazio
        if nivel_ultimo == '':
            nivel_ultimo = tarefa_id[:nivel_inclusao - 2] + str(int(tarefa_id[-2:]) + 1).zfill(2)  # Incrementa os últimos dois dígitos
            Linha_Incluir = 'end'
        else:
            nivel_inclusao = len(tarefa_id) + 2
            nivel_secundario = ""
            nivel_ultimo = ""
            linha += 1  # Ajusta linha para o próximo item
            # Segundo Loop
            for i in range(lin, len(self.LCronograma.get_children())):
                item = self.LCronograma.get_children()[i]
                values = self.LCronograma.item(item, 'values')
                nivel_secundario = len(values[1].replace(".", ""))
                if nivel_inclusao == nivel_secundario and values[1].replace(".", "")[:nivel_inclusao_mae] == tarefa_id.replace(".", ""):
                    nrcampo = self.LCronograma.index(item) + 2
                    Linha_Incluir = self.LCronograma.index(item) + 1
                    nivel_ultimo = values[1]
                    
            # Define Nivel_Ultimo baseado no resultado do segundo loop
            def calcular_nivel_ultimo(tarefa_id, nivel_inclusao, nivel_ultimo):
                # Extrai a parte inicial do tarefa_id
                parte_inicial = tarefa_id[:nivel_inclusao - 2]
                # Extrai os últimos dois caracteres de nivel_ultimo e incrementa
                numero_atual = int(nivel_ultimo[-2:]) + 1
                # numero_atual = '00' + numero_atual
                numero_formatado = str(numero_atual).zfill(2)  # Garante que tenha 2 dígitos
                # Concatena e retorna o novo ID
                # print(parte_inicial, numero_formatado)
                novo_nivel_ultimo = parte_inicial + numero_formatado
                return novo_nivel_ultimo
            
            if nivel_ultimo == '':
                nivel_ultimo = tarefa_id + "01"
            else:
                novo_nivel_ultimo = calcular_nivel_ultimo(tarefa_id, nivel_inclusao, nivel_ultimo)
                nivel_ultimo = novo_nivel_ultimo #tarefa_id[:nivel_inclusao - 2] + str(int(nivel_ultimo[-2:]) + 1).zfill(2)

        # Construir o Código
        tarefa_id_nova = ".".join([nivel_ultimo[i:i+2] for i in range(0, len(nivel_ultimo), 2)])
        
        # Adicionar na Lista
        nrcarat = len(tarefa_id_nova)
        per_conclusao = 0
        semaforo = self.status_on(data_inicial_prevista , '', data_inicial_prevista, '', per_conclusao)
        tarefa_info = (
                        nrcampo,
                        tarefa_id_nova,
                        ' ' * round(nrcarat) + tarefa_ds_nova,  
                        '',  # Responsável
                        '',  # Dependência
                        0,   # Tempo de espera
                        1,   # Tempo previsto
                        percentual_execucao,  
                         data_inicial_prevista.strftime("%d/%m/%Y"),  
                        '',  # Data Realizada
                        data_conclusao_prevista.strftime("%d/%m/%Y"),  
                        '',  # Data de Conclusão Realizada
                        '',  # Observação
                    )       
        # Adicionar na Tela
        self.LCronograma.insert(
                                '', 
                                Linha_Incluir,
                                iid=nrcampo,
                                image=semaforo, 
                                values=tarefa_info
                                )
        # Atualizar os indices
        self.atualizar_dependencias(tarefa_id_nova)
        # Ajustar as dependências e indice da tarefa
        # self.atualiza_cronograma_interacao(10)
        # self.adjust_list()
        
        
        messagebox.showinfo("Sucesso", "Nova tarefa incluída com sucesso!")

    
    # FALTA AJUSTAR AS OUTRAS QUESTÕES
    def excluir_programa(self, projeto_id, selected_item_index):
        
        try:
            # Check if the project is linked to any activities (programs)
            sql_query = f"SELECT * FROM programas_atividades WHERE projeto_ID={projeto_id}"
            records = db._querying(sql_query)
            
            if records:
                messagebox.showinfo("Info", "Projeto já Está Vinculado a um Programa, primeiro excluir o Programa!")
                return
            
            if messagebox.askyesno("Confirmar", "Tem Certeza que deseja Exluir?"):
                # If user confirms, delete the project
                delete_sql = f"DELETE FROM projetos_cronograma WHERE projeto_id={projeto_id}"
                db._querying(delete_sql)
                messagebox.showinfo("Success", "Projeto excluído com sucesso!")

            else:
                # If the user cancels, no action is taken
                messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")

        except Exception as e:
            messagebox.showerror("Erro", f"Um erro ocorreu: {str(e)}")
          
    def excluir_tarefas(self, projeto_id, selected_index):
        try:
            # Get the selected task information
            tarefa_id = self.LCronograma[selected_index]['tarefa_id']
            current_task_length = len(tarefa_id)
            
            # Determine if the next task exists and get its length
            if selected_index + 1 < len(self.LCronograma):
                next_task_length = len(self.LCronograma[selected_index + 1]['tarefa_id'])
            else:
                next_task_length = current_task_length
            
            # Ensure the user cannot delete a parent task that has child tasks
            if current_task_length < next_task_length:
                messagebox.showinfo("Info", "Não pode Excluir uma tarefa mãe sem excluir as tarefas filhas!")
                return
            
            # Confirm deletion with the user
            if messagebox.askyesno("Confirmar", "Tem Certeza que deseja Excluir?"):
                # SQL delete command
                delete_sql = f"DELETE FROM programas_atividades WHERE projeto_id={projeto_id} AND tarefa_id='{tarefa_id}'"
                db._querying(delete_sql)
                
                # Remove the task from the task list in memory
                self.LCronograma.pop(selected_index)
                
                # Update task indices in the remaining tasks
                for idx, task in enumerate(self.LCronograma):
                    task['task_index'] = idx + 1  # Update display index
                
                # Update dependencies
                for i in range(len(self.LCronograma)):
                    strEndereco = self.LCronograma[i]['dependencies']
                    if strEndereco:
                        dependencies = strEndereco.split(';')
                        new_dependencies = []

                        for dep in dependencies:
                            dep = int(dep.strip())
                            if dep > selected_index + 1:  # Account for removed task
                                new_dep = dep - 1
                            else:
                                new_dep = dep
                            new_dependencies.append(str(new_dep))
                        
                        self.LCronograma[i]['dependencies'] = ';'.join(new_dependencies)

                messagebox.showinfo("Success", "Tarefa excluída com sucesso!")
            else:
                messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")

        except Exception as e:
            messagebox.showerror("Erro", f"Um erro ocorreu: {str(e)}")

    def dta_tarefa_mae(self):
        dta_atualizacao = datetime.now()
        for idx in range(len(self.LCronograma.get_children())):
            values = self.LCronograma.item(idx, 'values')
            nrcarat = 0
            NrCampos = values[0]
            tarefa_id = values[1]
            nrcarat = len(tarefa_id)

            Lin = idx + 1
            if Lin > len(self.LCronograma.get_children()):
                return
            else:
                NrCaraceteres_Reg_Seg = len(values[1])

            nrcarat_seguinte = 0
            nr_tarefas_concluidas = 0
            data_inicial_prevista = None
            data_inicial_realizada = None
            data_conclusao_prevista = None
            data_conclusao_realizada = None

            values = self.LCronograma.item(Lin, 'values')
            nrregistros = len(values[1])
            linha = Lin + 1
            while values[1][:nrcarat] == tarefa_id and len(self.LCronograma.get_children()) >= linha:
                values = self.LCronograma.item(linha, 'values')
                if len(values[1]) <= nrregistros:
                    values = self.LCronograma.item(Lin, 'values')
                    if values[8]:
                        if not data_inicial_prevista:
                            data_inicial_prevista = values[8]
                        else:
                            data_inicial_prevista = min(data_inicial_prevista, values[8])
                    if values[9]:
                        if not data_inicial_realizada:
                            data_inicial_realizada = values[9]
                        else:
                            data_inicial_realizada = min(data_inicial_realizada, values[9])
                    if values[10]:
                        if not data_conclusao_prevista:
                            data_conclusao_prevista = values[10]
                        else:
                            data_conclusao_prevista = max(data_conclusao_prevista, values[10])
                    if values[11]:
                        if not data_conclusao_realizada:
                            data_conclusao_realizada = values[11]
                        else:
                            data_conclusao_realizada = max(data_conclusao_realizada, values[11])

                    # Count completed tasks
                    if values[7] == 1.0:
                        nr_tarefas_concluidas += 1
                    
                    nrcarat_seguinte += 1
        
                    # Calcular o Percentual de Execução
                    percentual_execucao = nr_tarefas_concluidas / nrcarat_seguinte if nrcarat_seguinte > 0 else 0

                    # Atualização no List
                    if idx < len(self.LCronograma.get_children()):
                        if data_inicial_prevista:
                            self.LCronograma[idx]['data_inicial_prevista'] = data_inicial_prevista
                        if data_inicial_realizada:
                            self.LCronograma[idx]['data_inicial_realizada'] = data_inicial_realizada
                        if data_conclusao_prevista:
                            self.LCronograma[idx]['data_conclusao_prevista'] = data_conclusao_prevista
                        if data_conclusao_realizada:
                            self.LCronograma[idx]['data_conclusao_realizada'] = data_conclusao_realizada
                            
                        self.LCronograma[idx]['percentual_execucao'] = percentual_execucao

                        # Optionally display success message
                        messagebox.showinfo("Success", f"Task dates and percentages updated for: {self.LCronograma[idx]['tarefa_id']}")
                Lin += 1
                values = self.LCronograma.item(Lin, 'values')
                nrregistros = len(values[1])
                linha += 1
                if Lin > len(self.LCronograma.get_children()):
                    return
                elif linha > len(self.LCronograma.get_children()):
                    return
                    
            if nr_tarefas_concluidas != 0:
                percentual_execucao = (nr_tarefas_concluidas / nrcarat_seguinte)
            else:
                percentual_execucao = 0

            if NrCaraceteres_Reg_Seg > nrcarat:
                if data_inicial_realizada and data_conclusao_realizada and percentual_execucao >= 1:
                    self.LCronograma[idx]['data_conclusao_realizada'] = data_conclusao_realizada - data_inicial_realizada
                elif data_inicial_prevista and data_conclusao_prevista:
                    self.LCronograma[idx]['data_conclusao_prevista'] = data_conclusao_prevista - data_inicial_prevista

                self.LCronograma[idx]['percentual_execucao'] = percentual_execucao

    def data_inicial_prev(self, dependency, line):
        if dependency:
            self.predessessora(line)

    def status_gantt(self, selected_index):
        
        try:
            dta_atualizacao = datetime.now()

            # Get the selected task
            task = self.LCronograma[selected_index]

            if not task['data_conclusao_realizada']:
                if datetime.strptime(task['data_inicio_prevista'], "%d/%m/%Y") < dta_atualizacao:
                    task['status'] = "Atrasado Início"
                    task['report_icon'] = 3
                else:
                    task['status'] = "Programa"
                    task['report_icon'] = 1
            else:
                if not task['data_inicio_realizada']:
                    if task['data_conclusao_prevista'] and datetime.strptime(task['data_conclusao_realizada'], "%d/%m/%Y") < dta_atualizacao:
                        task['status'] = "Atrasado Conclusão"
                        task['report_icon'] = 3
                    else:
                        task['status'] = "Em Andamento"
                        task['report_icon'] = 4
                elif float(task['percentual_execucao'].rstrip('%')) == 100:
                    task['status'] = "Concluído"
                    task['report_icon'] = 5
                elif datetime.strptime(task['data_conclusao_prevista'], "%d/%m/%Y") > dta_atualizacao:
                    task['status'] = "Em Andamento"
                    task['report_icon'] = 4
                elif datetime.strptime(task['data_conclusao_prevista'], "%d/%m/%Y") < dta_atualizacao:
                    task['status'] = "Atrasado Conclusão"
                    task['report_icon'] = 3
                else:
                    task['status'] = "Programa"
                    task['report_icon'] = 1

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}") 

    def predessessora(self, item_id):
        try:
            task_data = self.LCronograma.item(item_id)

            # Extraindo informações relevantes
            tarefa_id = task_data['values'][1]  
            tarefa_dependencia = str(task_data['values'][4]) 
            tempo_espera = float(task_data['values'][5]) 
            tempo_previsto = float(task_data['values'][6]) 

            # Inicializa a data da tarefa predecessora
            dta_precedente = None

            if tarefa_dependencia:
                # Divide as dependências por ';'
                dependencias = tarefa_dependencia.split(';')  # Exemplo: '1;2;3'
                for dep in dependencias:
                    
                    dep_index = int(dep) - 1  # Ajusta a indexação para 0 (Python)
                    item_ids = self.LCronograma.get_children()  # Obtém os IDs de todos os itens
                    # Verifica se o índice está dentro do intervalo
                    if dep_index >= len(item_ids):
                        continue  # Ignora se o índice estiver fora do intervalo
                    
                    # Obtém dados da tarefa dependente utilizando o ID do item correspondente
                    dependent_item_id = item_ids[dep_index]
                    dependent_task_data = self.LCronograma.item(dependent_item_id)
                    
                    # Processa a tarefa dependente e atualiza a data precedentemente
                    if dependent_task_data['values'][10]:  # Supondo que data_conclusao_realizada está na posição 10
                        if dta_precedente is None or dta_precedente < datetime.strptime(dependent_task_data['values'][10], "%d/%m/%Y"):
                            dta_precedente = datetime.strptime(dependent_task_data['values'][10], "%d/%m/%Y")
                    else:
                        # Se não tiver data de conclusão, usa a data de previsão
                        if dta_precedente is None or dta_precedente < datetime.strptime(dependent_task_data['values'][9], "%d/%m/%Y"):
                            dta_precedente = datetime.strptime(dependent_task_data['values'][9], "%d/%m/%Y")

            # Atualiza a data inicial prevista da tarefa atual, considerando o tempo de espera
            if dta_precedente:  # Se houver uma data precedentemente válida
                task_data['values'][7] = (dta_precedente + timedelta(days=tempo_espera)).strftime("%d/%m/%Y")  # Atualiza data_inicial_prevista

            # Atualiza a data de conclusão prevista, caso a tarefa seguinte corresponda nas dependências
            if int(tarefa_id.split('.')[0]) + 1 <= len(self.LCronograma.get_children()):  # Verifica se existe uma tarefa seguinte
                next_item_id = self.LCronograma.get_children()[int(tarefa_id.split('.')[0])]  # Ajuste de indexação
                next_task_data = self.LCronograma.item(next_item_id)

                #  Trata as datas de conclusão de acordo com a lógica da tarefa atual
                if data_inicial_realizada := task_data['values'][8]:  # Verifica se tem data inicial realizada
                    data_conclusao_prevista = datetime.strptime(data_inicial_realizada, "%d/%m/%Y") + timedelta(days=tempo_previsto)  # Adiciona o tempo previsto
                    task_data['values'][9] = data_conclusao_prevista.strftime("%d/%m/%Y")
                else:
                    task_data['values'][9] = (datetime.strptime(task_data['values'][8], "%d/%m/%Y") + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")

        except Exception as e:
            print(f"Erro na predessessora: {str(e)}")  # Exibe mensagem de erro caso ocorra uma exceção 

    def gravar_cronograma_incluir(self, projeto_id, projeto_ds, tarefa_id_nova, tarefa_ds_nova, data_inicial_prevista, data_conclusao_prevista, conexao):
        """
        Inserts a new task into the programas_atividades table.

        :param projeto_id: ID of the project to which the task belongs.
        :param projeto_ds: Description of the project.
        :param tarefa_id_nova: New task ID.
        :param tarefa_ds_nova: New task description.
        :param data_inicial_prevista: Planned start date.
        :param data_conclusao_prevista: Planned conclusion date.
        :param conexao: Database connection object.
        """
        try:
            if not projeto_id:
                print("Error: Project ID must be provided.")
                return
            
            # Determine additional variables, initializing them as required
            projeto_cr = 0
            responsavel_nome = ""
            tarefa_dependencia = ""
            tempo_espera = 0
            tempo_previsto = 0
            percentual_execucao = 0.0
            data_inicial_realizada = "1899-12-30"
            data_conclusao_realizada = "1899-12-30"
            dias_diferenca_inicio = 0
            prazo_fatal_dias = 0
            dias_diferenca_conclusao = 0
            status_projeto = ""
            observacao = ""
            anexos = ""

            # Prepare the SQL insertion command
            vsSQL = f"""
            INSERT INTO programas_atividades 
            (projeto_ID, projeto_DS, projeto_cr, tarefa_ID, tarefa_DS, responsavel_nome, tarefa_dependencia,
            tempo_espera, tempo_previsto, percentual_execucao, data_Inicial_Prevista,
            data_Inicial_Realizada, dias_diferenca_inicio, data_conclusao_prevista,
            data_conclusao_realizada, prazo_fatal_dias, dias_diferenca, status, observacao, anexos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # Convert parameters for the query
            params = (
                projeto_id,
                projeto_ds,
                projeto_cr,
                tarefa_id_nova,
                tarefa_ds_nova.replace("'", " "),  # Sanitize input
                responsavel_nome,
                tarefa_dependencia,
                round(tempo_espera, 0),
                round(tempo_previsto, 0),
                float(percentual_execucao),  # Ensure conversion
                data_inicial_prevista.strftime("%Y-%m-%d"),
                data_inicial_realizada,
                round(dias_diferenca_inicio, 0),
                data_conclusao_prevista.strftime("%Y-%m-%d"),
                data_conclusao_realizada,
                round(prazo_fatal_dias, 0),
                round(dias_diferenca_conclusao, 0),
                status_projeto,
                observacao.replace("'", " "),  # Sanitize input
                anexos
            )

            # Execute SQL command
            with conexao.cursor() as cursor:
                cursor.execute(vsSQL, params)
                conexao.commit()  # Commit the transaction

        except Exception as e:
            print(f"Error occurred: {str(e)}")
        finally:
            # Cleanup can be done here if needed (close connections)
            pass
    
    def gravar_cronograma_tarefa(self, task_data, connection): 
        pass
    
    def gravar_cronograma_total(self, projeto_id, conexao):
        pass 

    def gravar_alterar_dependencias(self, tarefa_id, tarefa_dependencia, projeto_id, conexao):
        """
        Updates the dependencies of a specified task in the programas_atividades table.

        :param tarefa_id: ID of the task whose dependencies are to be updated.
        :param tarefa_dependencia: New dependencies to set for the task.
        :param projeto_id: ID of the project the task belongs to.
        :param conexao: Database connection object.
        """
        try:
            # Prepare the SQL UPDATE statement
            sql = f"""
            UPDATE programas_atividades 
            SET tarefa_dependencia = ?
            WHERE projeto_ID = ? AND tarefa_ID = ?
            """
            
            # Execute SQL command
            with conexao.cursor() as cursor:
                cursor.execute(sql, (tarefa_dependencia, projeto_id, tarefa_id))
                conexao.commit()  # Commit the transaction

        except Exception as e:
            print(f"Error occurred while updating dependencies: {str(e)}")   

    # def abrir_anexo(self, projeto_id, tarefa_id, connection):
    #     try:
    #         sql_query = f"""
    #         SELECT 
    #             Empresa_ID AS Empresa, 
    #             Projeto_ID AS Projeto, 
    #             Tarefa_ID AS Tarefa, 
    #             ID_Anexo AS Anexo, 
    #             Doc_Num_Documento AS Doc 
    #         FROM 
    #             TB_Gedoc_Tarefas 
    #         WHERE 
    #             Projeto_ID = ? AND Tarefa_ID = ?
    #         """

    #         # Execute the SQL query
    #         with connection.cursor() as cursor:
    #             cursor.execute(sql_query, (projeto_id, tarefa_id))
    #             results = cursor.fetchall()

    #             if not results:
    #                 messagebox.showinfo("Info", "Documentos Não Cadastrado!")
    #                 return
                
    #             # Initialize the user annexes dialog
    #             user_anexos = UserAnexos()
    #             user_anexos.annex_list.delete(0, 'end')  # Clear previous items

    #             # Adding items to the annex list
    #             for row in results:
    #                 task_description, annex_id, document_number = row[2], row[3], row[4]
    #                 user_anexos.annex_list.insert('end', f"Tarefa: {task_description}, Anexo ID: {annex_id}, Documento: {document_number}")

    #             user_anexos.show()  # Simulate showing the annexes

    #     except Exception as e:
    #         messagebox.showerror("Erro", f"Erro! {str(e)}")
    
    def carrega_controle_image_list(self):
        # Clear existing images
        self.image_list_status.clear()

        # Load images
        self.add_image("img1", "lvIcons/amarelo.jpg")
        self.add_image("img2", "lvIcons/verde.jpg")
        self.add_image("img3", "lvIcons/vermelho.jpg")
        self.add_image("img4", "lvIcons/azul.jpg")
        self.add_image("img5", "lvIcons/aguardando_1.jpg")
        self.add_image("img6", "lvIcons/Anexo.jpg")

    def add_image(self, img_key, img_path):
        full_path = os.path.join(os.path.dirname(__file__), img_path)
        if os.path.exists(full_path):
            img = Image.open(full_path)
            self.image_list_status[img_key] = ImageTk.PhotoImage(img)

    def gravar_anexo_cronograma(projeto_id, tarefa_id, connection):
        try:
            # Open a file dialog to select a PDF
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            file_path = filedialog.askopenfilename(
                title="Procurar Arquivos .pdf",
                initialdir=os.getcwd(),  # Set initial directory
                filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
            )

            if not file_path:
                messagebox.showinfo("Info", "No file selected.")
                return

            # Get the details of the file
            file_name = os.path.basename(file_path)

            # Check if the document is already in the database
            sql_check = """
            SELECT ID_Anexo FROM TB_Gedoc_Tarefas 
            WHERE Projeto_ID = ? AND Tarefa_ID = ? AND Doc_Num_Documento = ? AND Empresa_ID = ?
            """
            id_empresa = "Your company ID"  # Replace with actual company ID retrieval logic
            
            with connection.cursor() as cursor:
                cursor.execute(sql_check, (projeto_id, tarefa_id, file_name, id_empresa))
                existing_record = cursor.fetchone()

                # Open and read the file in binary mode
                with open(file_path, 'rb') as file:
                    file_data = file.read()

                if existing_record is None:
                    # Insert a new record
                    sql_insert = """
                    INSERT INTO TB_Gedoc_Tarefas 
                    (Empresa_ID, Projeto_ID, Tarefa_ID, Doc_Num_Documento, BinarioPDF) 
                    VALUES (?, ?, ?, ?, ?)
                    """
                    cursor.execute(sql_insert, (id_empresa, projeto_id, tarefa_id, file_name, file_data))
                    connection.commit()
                    messagebox.showinfo("Success", "Document saved successfully.")

                else:
                    # Update the existing record
                    id_anexo = existing_record[0]
                    sql_update = """
                    UPDATE TB_Gedoc_Tarefas 
                    SET BinarioPDF = ? 
                    WHERE ID_Anexo = ?
                    """
                    cursor.execute(sql_update, (file_data, id_anexo))
                    connection.commit()
                    messagebox.showinfo("Success", "Document updated successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            if connection:
                connection.close()  # Ensure the connection is closed                           

    def upload_arquivo_cronograma(projeto_id, tarefa_id, doc_num_documento, connection):
        
        try:
            # Prepare SQL query
            sql_query = """
            SELECT * FROM TB_Gedoc_Tarefas 
            WHERE Projeto_ID = ? AND Tarefa_ID = ? AND Doc_Num_Documento = ?
            """
            
            # Execute the SQL command
            with connection.cursor() as cursor:
                cursor.execute(sql_query, (projeto_id, tarefa_id, doc_num_documento))
                record = cursor.fetchone()

                if record is None:
                    messagebox.showinfo("Info", "Documentos Não Cadastrado!")
                    return

                # Get the binary data for the document
                b64_data = record[4]  # Assuming 'BinarioPDF' is the 5th column in the result set

                if b64_data is not None:
                    # Decode and save the file
                    file_path = os.path.join(os.getcwd(), doc_num_documento)  # Save in the current directory
                    with open(file_path, 'wb') as file:
                        file.write(b64_data)  # Write the binary data to a file

                    messagebox.showinfo("Success", "Document downloaded successfully.")
                    
                    # Optionally, you can open the file or trigger additional UI dialogs
                    # In a GUI application, you might want to open this file or perform further actions
                else:
                    messagebox.showinfo("Info", "No data found for the specified document.")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")

Cronograma_Atividades()

