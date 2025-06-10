from imports import *
from widgets import Widgets
from datetime import datetime
from PIL import ImageTk, Image
from UsrCadastros import Projetos
from UsrCadastros import Cronograma_Atividades_Copiar


################# criando janela ###############
class Cronograma_Atividades_Hierarquico(Widgets, Projetos, Cronograma_Atividades_Copiar):
    def cronograma_atividades_hierarquico(self):
        self.window_one.title('Cronograma Atividades - Hierarquia')
        self.images = {}
        self.clearFrame_principal()
        self.frame_cabecalho_cronograma_atividades_hierarquico(self.principal_frame)

################# dividindo a janela ###############
    
    def frame_cabecalho_cronograma_atividades_hierarquico(self, janela):
        # Projeto
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.50
        coordenadas_relheight = 0.07
        fr_projeto = customtkinter.CTkFrame(
            janela, border_color="gray75", border_width=1)
        fr_projeto.place(relx=coordenadas_relx, rely=coordenadas_rely,
                         relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_projeto = customtkinter.CTkLabel(fr_projeto, text="Projetos")
        lb_projeto.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.55)

        projetos = []

        self.entry_projeto = AutocompleteCombobox(
            fr_projeto, width=30, font=('Times', 11), completevalues=projetos)
        self.entry_projeto.pack()
        self.entry_projeto.place(
            relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_projeto.bind(
            "<Button-1>", lambda event: self.atualizar_projetos(event, self.entry_projeto))
        self.entry_projeto.bind(
            '<Down>', lambda event: self.atualizar_projetos(event, self.entry_projeto))

        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar_projeto = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=lambda: self.consulta_cronograma_atividades_hierarquico(janela))
        self.btn_consultar_projeto.pack(pady=10)
        self.btn_consultar_projeto.place(relx=0.51, rely=0.02, relwidth=0.04, relheight=0.05)
        # Adicionar o tooltip
        ToolTip(self.btn_consultar_projeto, "Consultar Cronograma de Atividades")

        # Opções Aberto ou Fechado
        self.check_var_aberto_fechado = customtkinter.StringVar(value="off")
        self.checkbox_aberto_fechado = customtkinter.CTkCheckBox(janela, text='Resumido', variable=self.check_var_aberto_fechado, onvalue="on", offvalue="off")        
        self.checkbox_aberto_fechado.place(relx=0.555, rely=0.02, relwidth=0.10, relheight=0.05)

        # Botão de Salvar Cronograma
        icon_image = self.base64_to_photoimage('save')
        self.btn_salvar_projeto = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=lambda: self.gravar_cronograma_total_hierarquico(janela))
        self.btn_salvar_projeto.pack(pady=10)
        self.btn_salvar_projeto.place(relx=0.66, rely=0.02, relwidth=0.04, relheight=0.05)
        # Adicionar o tooltip
        ToolTip(self.btn_salvar_projeto, "Salvar Cronograma de Atividades")

        # Botão Copiar Template Cronograma
        icon_image = self.base64_to_photoimage('copia')
        self.btn_copiar_atividades = customtkinter.CTkButton(janela, text='Copiar', image=icon_image, fg_color='transparent', command=self.cad_cronograma_atividades_copiar)
        self.btn_copiar_atividades.pack(pady=10)
        self.btn_copiar_atividades.place(relx=0.705, rely=0.02, relwidth=0.055, relheight=0.05)
        # Adicionar o tooltip
        ToolTip(self.btn_copiar_atividades, "Copiar Atividades de um Template para um Novo Programa de Atividades")

        # Botão Incluir Cronograma
        icon_image = self.base64_to_photoimage('open_book')
        self.btn_novo_projeto = customtkinter.CTkButton(janela, text='Novo', image=icon_image, fg_color='transparent', command=self.cad_projetos)
        self.btn_novo_projeto.pack(pady=10)
        self.btn_novo_projeto.place(relx=0.765, rely=0.02, relwidth=0.08, relheight=0.05)
        # Adicionar o tooltip
        ToolTip(self.btn_novo_projeto, "Incluir Novo Programa Atividades")
         
        # Botão Sair Cronograma
        icon_image = self.base64_to_photoimage('sair')
        self.btn_sair_projeto = customtkinter.CTkButton(janela, text='Sair', image=icon_image, fg_color='transparent', command=self.tela_principal)
        self.btn_sair_projeto.pack(pady=10)
        self.btn_sair_projeto.place(relx=0.955, rely=0.02, relwidth=0.04, relheight=0.05)
        # Adicionar o tooltip
        ToolTip(self.btn_sair_projeto, "Sair do Cronograma")
      
    def consulta_cronograma_atividades_hierarquico(self, janela):
        projeto_ds = self.entry_projeto.get()
        if self.entry_projeto.get() != '':
            projeto_id = self.obter_Projeto_ID(self.entry_projeto.get(), janela)
        else:
            messagebox.showinfo("Gestor de Negócios", "Preencher o Projeto!!")
            return

        # Listbox _ Cronograma de Atividades
        # Definindo cores
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", 
                            background='#FFFFFF',
                            foreground="black",
                            rowheight=25,
                            fieldbackground="#D3D3D3")
        # Configura o estilo para a linha selecionada
        treestyle.map('Treeview', 
                    background=[('selected', '#4A6984')],  # Cor de fundo quando selecionado
                    foreground=[('selected', 'white')])  # Cor do texto quando selecionado
        
        # Adicione estas linhas para criar as linhas de grade
        treestyle.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        treestyle.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))  # Modify the font of the body
        treestyle.configure("Treeview.Heading",  font=('Calibri', 13,'bold'))  # Modify the font of the headings
        treestyle.configure("Treeview", rowheight=30)  # Adjust row height

        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.085, relwidth=0.99, relheight=0.91)

        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Widgets - Listar Tarefas
        self.LCronograma = TreeviewEdit(self.fr_list, projeto_id, projeto_ds, height=7, column=(
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
        ))  # , show='headings tree'

        # Configuração opcional para linhas alternadas (zebra striping)
        self.LCronograma.tag_configure('oddrow', background='white')
        self.LCronograma.tag_configure('evenrow', background='#F0F0F0')
        
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

        self.LCronograma.column('#0', width=100, anchor='c')
        self.LCronograma.column('Nr', width=3, anchor='c')
        self.LCronograma.column('tarefa_id', width=100, anchor='w')
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

        # Limpa a lista atual antes de inserir novos resultados
        self.LCronograma.delete(*self.LCronograma.get_children())

        sql_query = """
                        SELECT 
                            pc.projeto_empresa          AS projeto_empresa,
                            pa.projeto_ID               AS projeto_ID, 
                            pa.projeto_DS               AS projeto_DS, 
                            pa.tarefa_ID                AS tarefa_ID, 
                            pa.tarefa_DS                AS tarefa_DS, 
                            pa.parent_id                AS parent_id,
                            pa.responsavel_nome         AS responsavel_nome,
                            pa.tarefa_dependencia       AS tarefa_dependencia, 
                            pa.tempo_espera             AS tempo_espera, 
                            pa.tempo_previsto           AS tempo_previsto, 
                            pa.percentual_execucao      AS percentual_execucao,
                            pa.data_Inicial_Prevista    AS data_Inicial_Prevista, 
                            pa.data_Inicial_Realizada   AS data_Inicial_Realizada, 
                            pa.dias_diferenca_inicio    AS dias_diferenca_inicio,
                            pa.data_conclusao_prevista  AS data_conclusao_prevista, 
                            pa.data_conclusao_realizada AS data_conclusao_realizada, 
                            pa.prazo_fatal_dias         AS prazo_fatal_dias,
                            pa.dias_diferenca           AS dias_diferenca, 
                            pa.status                   AS status, 
                            pa.observacao               AS observacao
                        FROM programas_atividades pa
                        INNER JOIN projetos_cronograma pc ON pc.projeto_id=pa.projeto_id 
                        WHERE pa.projeto_ID = %s
                        ORDER BY tarefa_ID
                    """

        self.list_tarefas = []
        self.list_tarefas = db.executar_consulta(sql_query, projeto_id)
        
        self.icon_image_azul = self.base64_to_farois('semafaro_azul')
        self.icon_image_verde = self.base64_to_farois('semafaro_verde')
        self.icon_image_amarelo = self.base64_to_farois('semafaro_amarelo')
        self.icon_image_vermelho = self.base64_to_farois('semafaro_vermelho')
        
        # Criar um dicionário para armazenar os itens da TreeView
        self.tree_items = {}    
    
        if not self.list_tarefas:
            messagebox.showinfo("Gestor de Negócios", "Projeto sem tarefas!!")
            return
        else:
            tarefa_info = []
            nrregistros = 1
            for record in self.list_tarefas:
                empresa_projeto_id = record.get('projeto_empresa')
                tarefa_id = str(record.get('tarefa_ID')).zfill(2)
                parent_id = record.get('parent_id')

                nrcarat = len(record.get('tarefa_ID'))
                dta_branco = str('1899-12-30')
                data_realizada = datetime.strftime(record.get('data_Inicial_Realizada'), "%Y-%m-%d")
                data_conclusao = datetime.strftime(record.get('data_conclusao_realizada'), "%Y-%m-%d")
                data_realizada_prev = datetime.strftime(record.get('data_Inicial_Prevista'), "%Y-%m-%d")
                data_conclusao_prev = datetime.strftime(record.get('data_conclusao_prevista'), "%Y-%m-%d")
                per_conclusao = f"{record.get('percentual_execucao'):.2%}"
                
                if data_realizada_prev == str(dta_branco):
                    data_realizada_prev = ''
                else:
                    data_realizada_prev = datetime.strptime(data_realizada_prev, "%Y-%m-%d")
                    data_realizada_prev = data_realizada_prev.strftime("%d/%m/%Y")  # Formato desejado: "DD/MM/YYYY"

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

                if record.get('observacao') is None:

                    Observacao = ''
                else:
                    Observacao = record.get('observacao')
                
                tarefa_info = (
                    nrregistros,
                    tarefa_id,
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
                # Inserir o item na TreeView
                if parent_id:
                    parent_item = self.tree_items.get(parent_id)
                    item_id = self.LCronograma.insert(parent_item, 'end', values=tarefa_info, tags=('evenrow' if nrregistros % 2 == 0 else 'oddrow',))
                else:
                    item_id = self.LCronograma.insert('', 'end', values=tarefa_info, tags=('evenrow' if nrregistros % 2 == 0 else 'oddrow',))

                # Armazenar o item no dicionário
                self.tree_items[tarefa_id] = item_id

                # Configurar o semáforo
                semaforo = []
                per_conclusao = float(per_conclusao.replace("%", ""))
                semaforo = self.status_on(item_id, data_realizada_prev, data_realizada, data_conclusao_prev, data_conclusao, per_conclusao)
                self.LCronograma.item(item_id, image=semaforo)

                nrregistros += 1

        def expand_all(tree, item=""):
            tree.item(item, open=True)
            for child in tree.get_children(item):
                expand_all(tree, child)

        # Após o loop de inserção das tarefas, chame a função para expandir todos os itens
        if self.checkbox_aberto_fechado.get() == 'off':
            expand_all(self.LCronograma)

        self.LCronograma.tag_configure('odd', background='#eee')
        self.LCronograma.tag_configure('even', background='#ddd')
        self.LCronograma.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.LCronograma.yview)

        self.ajustar_list_hierarquico()

        def selected_incluir():
            selected_item = self.LCronograma.selection()
            if selected_item:
                item_text = self.LCronograma.item(selected_item, 'text')
                values = self.LCronograma.item(selected_item, 'values')
                lin = self.LCronograma.index(selected_item)
                tarefa_id = values[1]
                
                self.incluir_tarefas(projeto_id, projeto_ds, lin, tarefa_id, selected_item)
            else:
                messagebox.showinfo(
                    "Erro", "Selecione a posição para inclusão da Tarefa!")
                return
                # lin = 'end'

        def selected_anexar():
            selected_item = self.LCronograma.selection()
            if selected_item:
                item_text = self.LCronograma.item(selected_item, 'text')
                values = self.LCronograma.item(selected_item, 'values')
                lin = self.LCronograma.index(selected_item)
                tarefa_id = values[1]
                self.tarefa_anexo(lin, empresa_projeto_id, projeto_id, tarefa_id)
            else:
                messagebox.showinfo("Erro", "Selecione a posição para inclusão do Anexo!", janela)
                return

        def selected_pesquisar():
            selected_item = self.LCronograma.selection()
            if selected_item:
                item_text = self.LCronograma.item(selected_item, 'text')
                values = self.LCronograma.item(selected_item, 'values')
                lin = self.LCronograma.index(selected_item)
                tarefa_id = values[1]
                self.pesquisa_anexos(projeto_id, tarefa_id)
                
            else:
                messagebox.showinfo("Erro", "Selecione a posição para Pesquisar Existência de Anexos!", janela)
                return
            
        def selected_excluir():
            if self.entry_projeto.get() != '':
                projeto_id = self.obter_Projeto_ID(self.entry_projeto.get(), janela)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher o Projeto!!")
                return

            selected_item = self.LCronograma.selection()
            if selected_item:
                if self.LCronograma.get_children(selected_item):
                    messagebox.showwarning("Aviso", "Não é possível excluir uma tarefa que possui subtarefas.")
                    return
                
                values = self.LCronograma.item(selected_item, 'values')
                lin = self.LCronograma.index(selected_item)
                tarefa_id = str(values[1]).zfill(2)
                
                # Identificar a tarefa mãe
                parent_item = self.LCronograma.parent(selected_item)
                parent_values = self.LCronograma.item(parent_item, 'values')
                parent_lin = self.LCronograma.index(parent_item)
                parent_tarefa_id = str(parent_values[1]).zfill(2)
                    
  
                # Identificar os filhos
                children = self.LCronograma.get_children(selected_item)
                for child in children:
                    child_values = self.LCronograma.item(child, 'values')
                    child_lin = self.LCronograma.index(child)
                    child_tarefa_id = str(child_values[1]).zfill(2)
                
                if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir esta tarefa?"):
                    try:
                        self.excluir_tarefas(projeto_id, tarefa_id)
                        self.LCronograma.delete(selected_item)
                        self.atualizar_dependencias_exclusao(lin)
                        self.atualiza_cronograma_interacao(10)
                        self.ajustar_list()

                        messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
                    except Exception as e:
                        messagebox.showerror("Erro", f"Não foi possível excluir a tarefa: {str(e)}")
            else:
                messagebox.showinfo("Erro", "Selecione a posição para Exclusão da Tarefa!")

        def postPopUpMenu(event):
            row_id = self.LCronograma.identify_row(event.y)
            if row_id:  # Realiza a verificação se a linha existe.
                self.LCronograma.selection_set(row_id)
                row_values = self.LCronograma.item(row_id)['values']

                postPopUpMenu = tk.Menu(self.LCronograma, tearoff=0, font=('Verdana', 11))

                # postPopUpMenu.add_command(label='Incluir Tarefa', accelerator='Ctrl+I', command= selected_incluir)
                postPopUpMenu.add_command(label='Incluir Tarefa', accelerator='Insert', command=selected_incluir)
                postPopUpMenu.add_command(label='Excluir Tarefa', accelerator='Delete', command=selected_excluir)
                postPopUpMenu.add_separator()
                postPopUpMenu.add_command(label='Anexar Documento', accelerator='Alt+U', command=selected_anexar)
                postPopUpMenu.add_command(label='Pesquisar Documentos', accelerator='Alt+P', command=selected_pesquisar)
                postPopUpMenu.post(event.x_root, event.y_root)

        # Uso:
        all_numbers = self.get_all_items_numbers()
        print("Informações de todos os itens (pais e filhos):")
        for number, campo1, campo2, position, level in all_numbers:
            print(f"Linha: {number}, Tarefa: {campo1}, Descrição: {campo2}, Tarefa Pai: {position}, Tarefa Filho: {level}")

        # 'Button-3' é o clique direito do mouse
        self.LCronograma.bind("<Button-3>", postPopUpMenu)
        self.LCronograma.bind('<Insert>', lambda event: selected_incluir() if self.LCronograma.selection() else None)
        self.LCronograma.bind('<Delete>', lambda event: selected_excluir() if self.LCronograma.selection() else None)
        self.LCronograma.bind('<Control-u>', lambda event: selected_anexar() if self.LCronograma.selection() else None)
        self.LCronograma.bind('<Control-p>', lambda event: selected_pesquisar() if self.LCronograma.selection() else None)

    def atualizar_dependencias_exclusao_hierarquico(self, linha_base_predessessora):
        # Reassigning the numbers

        nr_campos = 1
        for i in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            self.LCronograma.item(
                item, text='', values=(nr_campos,) + values[1:])
            nr_campos += 1

        # Reassign dependencies based on remaining items
        for ii in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[ii]
            values = self.LCronograma.item(item, 'values')
            # Supondo que o 5º item é o subitem 4
            str_endereco = self.LCronograma.item(item, 'values')[4]
            nr_caracteres = len(str_endereco)
            str_espera = self.LCronograma.item(item, 'values')[5]
            # Supondo que o 5º item é o subitem 4
            str_prazo = self.LCronograma.item(item, 'values')[6]
            str_per_conclusao = self.LCronograma.item(
                item, 'values')[7]  # Supondo que o 5º item é o subitem 4
            # Supondo que o 5º item é o subitem 4
            str_ini_prev = self.LCronograma.item(item, 'values')[8]
            # Supondo que o 5º item é o subitem 4
            str_ini_real = self.LCronograma.item(item, 'values')[9]
            # Supondo que o 5º item é o subitem 4
            str_fim_prev = self.LCronograma.item(item, 'values')[10]
            # Supondo que o 5º item é o subitem 4
            str_fim_real = self.LCronograma.item(item, 'values')[11]
            str_obs = self.LCronograma.item(item, 'values')[12]

            if nr_caracteres != 0 and nr_caracteres > 2:
                lin_dependente = ""
                tarefa_dependencia = ""

                for vi_contador in range(nr_caracteres):
                    char = str_endereco[vi_contador]

                    if char != ";":
                        lin_dependente += char
                    if char == ";" or vi_contador == nr_caracteres - 1:
                        linha_tarefa = int(lin_dependente) - 1 if int(
                            lin_dependente) > linha_base_predessessora else int(lin_dependente)
                        tarefa_dependencia += str(linha_tarefa) + ";"
                        lin_dependente = ""

                # Remove the last semicolon if it exists
                tarefa_dependencia = tarefa_dependencia.rstrip(';')

                # Update the task dependency
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
                linha_tarefa = int(
                    str_endereco) - 1 if int(str_endereco) > linha_base_predessessora else int(str_endereco)
                self.LCronograma.item(
                    item,
                    text='',
                    values=values[:4] + (
                        linha_tarefa,
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

    def atualizar_dependencias_hierarquico(self, tarefa_id_nova):
        nr_campos = 1
        linha_base_predessessora = None

        # Primeiro loop para atualizar os números dos campos
        for i in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            self.LCronograma.item(
                item, text='', values=(nr_campos,) + values[1:])
            if values[1] == tarefa_id_nova:  # Supondo que o segundo subitem é o que procuramos
                linha_base_predessessora = nr_campos

            nr_campos += 1

        # Segundo loop para processar as dependências
        for ii in range(len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[ii]
            values = self.LCronograma.item(item, 'values')
            # Supondo que o 5º item é o subitem 4
            str_endereco = self.LCronograma.item(item, 'values')[4]
            nr_caracteres = len(str_endereco)

            str_espera = self.LCronograma.item(item, 'values')[5]
            # Supondo que o 5º item é o subitem 4
            str_prazo = self.LCronograma.item(item, 'values')[6]
            str_per_conclusao = self.LCronograma.item(
                item, 'values')[7]  # Supondo que o 5º item é o subitem 4
            # Supondo que o 5º item é o subitem 4
            str_ini_prev = self.LCronograma.item(item, 'values')[8]
            # Supondo que o 5º item é o subitem 4
            str_ini_real = self.LCronograma.item(item, 'values')[9]
            # Supondo que o 5º item é o subitem 4
            str_fim_prev = self.LCronograma.item(item, 'values')[10]
            # Supondo que o 5º item é o subitem 4
            str_fim_real = self.LCronograma.item(item, 'values')[11]
            # Supondo que o 5º item é o subitem 4
            str_obs = self.LCronograma.item(item, 'values')[12]

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

    def atualiza_cronograma_interacao_hierarquico(self, nr_interacao):
        for _ in range(nr_interacao):
            for item_id in self.LCronograma.get_children():
                values = self.LCronograma.item(item_id, 'values')
                tarefa_dependencia = values[4]
                self.predessessora(item_id)

        self.dta_tarefa_mae
        
    def is_valid_date_hierarquico(self, date_str):
        try:
            self.parse_date(date_str)
            return True
        except ValueError:
            return False

    def parse_date_hierarquico(self, date_str, fallback_date=None):
        if isinstance(date_str, datetime):
            return date_str  # Retorna se já for um objeto datetime

        if date_str:  # Verifica se date_str não é vazio
            try:
                # Tenta analisar o formato com hora
                # Formato para data com hora
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                pass

            try:
                # Se necessário, tenta o formato sem hora
                # Formato sem hora
                return datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError as e:
                pass

        if fallback_date:
            if isinstance(fallback_date, datetime):
                return fallback_date  # Retorne se já é um objeto datetime
            try:
                # Formato do fallback
                return datetime.strptime(fallback_date, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                pass

        return None  # Retorna None se não conseguiu analisar

    def predessessora_hierarquico(self, item_id):
        # try:
            current_values = self.LCronograma.item(item_id).get('values')
            tasks_ids = self.LCronograma.get_children()
            task = self.LCronograma.item(item_id)
            lin = task['values'][0]
            strEndereco = task['values'][4] if task['values'][4] else ""

            tarefa_check = None
            tarefa_check = '01.02.01'
            semaforo = []
            
            tarefa_id = str(task['values'][1]).zfill(2)
            current_values[1] = tarefa_id
            tarefa_dependencia = str(task['values'][4])
            tempo_espera = float(task['values'][5])
            tempo_previsto = float(task['values'][6])

            per_conclusao = float(task['values'][7].replace("%", ""))
            data_inicial_prevista = self.parse_date(task['values'][8])
            data_inicial_realizada = self.parse_date(task['values'][9])
            data_conclusao_prevista = self.parse_date(task['values'][10])
            data_conclusao_realizada = self.parse_date(task['values'][11])

            nr_caracteres = len(str(strEndereco))
            dta_precedente = None
            lin_dependente = ''
            if nr_caracteres != 0:
                for viContador in range(nr_caracteres):
                    char = str(strEndereco)[viContador]
                    if char != ';':
                        lin_dependente += char
                    else:
                        if int(lin_dependente) >= len(self.LCronograma.get_children()):
                            return

                        index = int(lin_dependente)
                        dep_task_id = tasks_ids[index]
                        dep_sub_items = self.LCronograma.item(dep_task_id, 'values')
                        
                        data_inicial_realizada = self.parse_date(dep_sub_items[9])
                        data_conclusao_prevista = self.parse_date(dep_sub_items[10])
                        data_conclusao_realizada = self.parse_date(dep_sub_items[11])
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            if data_conclusao_realizada and self.is_valid_date(data_conclusao_realizada):
                                if dta_precedente is not None and dta_precedente < data_conclusao_realizada:
                                    dta_precedente = data_conclusao_realizada
                                else:
                                    dta_precedente = data_conclusao_prevista
                            else:
                                dta_precedente = data_conclusao_prevista
                        else:
                            if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                                dta_precedente = data_conclusao_prevista

                        lin_dependente = ''

                if lin_dependente and int(lin_dependente) <= len(self.LCronograma.get_children()):
                    index = int(lin_dependente) - 1
                    dep_task_id = tasks_ids[index]
                    dep_task = self.LCronograma.item(dep_task_id, 'values')
                    dep_sub_items = self.LCronograma.item(dep_task_id, 'values')

                    data_inicial_realizada = self.parse_date(dep_sub_items[9])
                    data_conclusao_prevista = self.parse_date(dep_sub_items[10])
                    data_conclusao_realizada = self.parse_date(dep_sub_items[11])

                    if data_conclusao_realizada and self.is_valid_date(data_conclusao_realizada):
                        if dta_precedente is None or dta_precedente < data_conclusao_realizada:
                            dta_precedente = data_conclusao_realizada
                    else:
                        if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                            dta_precedente = data_conclusao_prevista
                else:
                    if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                        dta_precedente = data_conclusao_prevista

                if dta_precedente or dta_precedente is not None:
                    current_values[8] = (
                        dta_precedente + timedelta(days=tempo_espera)).strftime("%d/%m/%Y")
                
                nr_caracteres = int(len(tarefa_id))
                if lin + 1 < len(self.LCronograma.get_children()):
                    index = int(lin + 1)
                    next_task_id = tasks_ids[index]
                    next_task = self.LCronograma.item(next_task_id, 'values')
                    nr_caracteres_seguintes = int(len(next_task[1]))

                    if nr_caracteres_seguintes <= nr_caracteres:
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            current_values[10] = (self.parse_date(data_inicial_realizada) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
                        else:
                            current_values[10] = (self.parse_date(data_inicial_prevista) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
            else:
                nr_caracteres = int(len(tarefa_id))
                if lin + 1 < len(self.LCronograma.get_children()):
                    index = int(lin + 1)
                    next_task_id = tasks_ids[index]
                    next_task = self.LCronograma.item(next_task_id, 'values')
                    nr_caracteres_seguintes = int(len(next_task[1]))

                    if nr_caracteres_seguintes <= nr_caracteres:
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            current_values[10] = (self.parse_date(
                                data_inicial_realizada) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
                        else:
                            current_values[10] = (self.parse_date(
                                data_inicial_prevista) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
            # print(current_values)
            # breakpoint()
            self.LCronograma.item(item_id, values=current_values)

        # except Exception as e:
        #     messagebox.showerror("Error", f"Error in calculate_predecessor: {str(e)}")
            
    def ajustar_list_hierarquico(self):
        try:
            total_items = len(self.LCronograma.get_children())
            
            def process_item(item_id, level=0):
                task_data = self.LCronograma.item(item_id)
                tarefa_id = str(task_data['values'][1]).zfill(2)
                nrcarat = len(tarefa_id.upper())

                children = self.LCronograma.get_children(item_id)
                is_last = (len(children) == 0)

                if not is_last:
                    next_item_id = children[0]
                    next_task_data = self.LCronograma.item(next_item_id)
                    next_tarefa_id = str(next_task_data['values'][1])
                    nrcarat_seguinte = len(next_tarefa_id.upper())
                else:
                    nrcarat_seguinte = 0

                # Aplica formatação baseada nos critérios
                if nrcarat_seguinte > nrcarat or (is_last and nrcarat <= 2):
                    self.LCronograma.item(item_id, tags=('bold_blue',))
                elif nrcarat_seguinte == nrcarat and nrcarat > 2:
                    self.LCronograma.item(item_id, tags=('normal_black',))
                elif nrcarat_seguinte == nrcarat and nrcarat <= 2:
                    self.LCronograma.item(item_id, tags=('bold_blue',))
                else:
                    self.LCronograma.item(item_id, tags=('normal_black',))

                per_conclusao = float(task_data['values'][7].replace("%", ""))
                data_inicial_prevista = self.parse_date(task_data['values'][8])
                data_inicial_realizada = self.parse_date(task_data['values'][9])
                data_conclusao_prevista = self.parse_date(task_data['values'][10])
                data_conclusao_realizada = self.parse_date(task_data['values'][11])
                
                semaforo = self.status_on(
                    item_id, 
                    data_inicial_prevista, 
                    data_inicial_realizada,
                    data_conclusao_prevista, 
                    data_conclusao_realizada, 
                    per_conclusao
                )
                
                self.LCronograma.item(item_id, image=semaforo)

                # Processa recursivamente as tarefas filhas
                for child in children:
                    process_item(child, level + 1)

            # Processa todos os itens de nível superior
            for item_id in self.LCronograma.get_children():
                process_item(item_id)

            # Configura as tags para o Treeview
            self.LCronograma.tag_configure('bold_blue', font=('Helvetica', 10, 'bold'), foreground='blue')
            self.LCronograma.tag_configure('normal_black', font=('Helvetica', 10), foreground='black')

        except Exception as e:
            messagebox.showerror("Erro!", f"Erro: {str(e)}")

    def status_on_hierarquico(self, selected_iid, dta_inicio_prev, dta_inicio_real, dta_conclusao_prev, dta_conclusao_real, per_conclusao):
        try:
            # Carrega os farois
            icon_image_azul = self.base64_to_farois('semafaro_azul')
            icon_image_verde = self.base64_to_farois('semafaro_verde')
            icon_image_amarelo = self.base64_to_farois('semafaro_amarelo')
            icon_image_vermelho = self.base64_to_farois('semafaro_vermelho')

            # Remova a hora e o minuto
            if isinstance(dta_inicio_prev, datetime):
                dta_inicio_prev = dta_inicio_prev.date()  # Converte para date

            if isinstance(dta_inicio_real, datetime):
                dta_inicio_real = dta_inicio_real.date()  # Converte para date

            if isinstance(dta_conclusao_prev, datetime):
                dta_conclusao_prev = dta_conclusao_prev.date()  # Converte para date

            if isinstance(dta_conclusao_real, datetime):
                dta_conclusao_real = dta_conclusao_real.date()  # Converte para date

            if isinstance(dta_inicio_real, str):
                try:
                    dta_inicio_real = datetime.strptime(dta_inicio_real, "%d/%m/%Y").date()
                except ValueError:
                    dta_inicio_real = None  # ou use uma data padrão, como datetime.now().date()

            if isinstance(dta_inicio_prev, str):
                try:
                    dta_inicio_prev = datetime.strptime(dta_inicio_prev, "%d/%m/%Y").date()
                except ValueError:
                    dta_inicio_prev = None  # ou use uma data padrão, como datetime.now().date()

            if isinstance(dta_conclusao_prev, str):
                try:
                    dta_conclusao_prev = datetime.strptime(dta_conclusao_prev, "%d/%m/%Y").date()
                except ValueError:
                    dta_conclusao_prev = None  # ou use uma data padrão, como datetime.now().date()

            if isinstance(dta_conclusao_real, str):
                try:
                    dta_conclusao_real = datetime.strptime(dta_conclusao_real, "%d/%m/%Y").date()
                except ValueError:
                    dta_conclusao_real = None  # ou use uma data padrão, como datetime.now().date()


            today = datetime.now().date()
            if dta_inicio_real == '' or dta_inicio_real is None:
                if dta_inicio_prev < today:
                    icon_image = icon_image_vermelho
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                else:
                    icon_image = icon_image_amarelo
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
            else:
                if dta_conclusao_real == '' or dta_conclusao_real is None:
                    if dta_inicio_real != '' or dta_inicio_real is not None and dta_conclusao_prev < today:
                        icon_image = icon_image_vermelho
                        # Armazenar referência
                        self.images[selected_iid] = icon_image
                    else:
                        icon_image = icon_image_azul
                        # Armazenar referência
                        self.images[selected_iid] = icon_image
                elif float(per_conclusao) == 100.00:
                    icon_image = icon_image_verde
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                elif dta_conclusao_prev >= today:
                    icon_image = icon_image_azul
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                elif dta_conclusao_prev < today:
                    icon_image = icon_image_vermelho
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                else:
                    icon_image = icon_image_amarelo
                    # Armazenar referência
                    self.images[selected_iid] = icon_image

            return icon_image

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # def incluir_tarefas(self, projeto_id, projeto_ds, linha, tarefa_id, selected_index):
    #     # Parametros Iniciais
    #     nrcampo = int(linha) + 2
    #     tarefa_id = tarefa_id.replace(".", "")
    #     Linha_Incluir = int(linha) + 1

    #     tarefa_id_nova = ''
    #     tarefa_ds_nova = "Preencher Descricão Nova Tarefa...................!!!!"
    #     responsavel_nome = ''
    #     tarefa_dependencia = ''
    #     tempo_previsto = 1
    #     percentual_execucao = '0.00%'
    #     data_inicial_prevista = datetime.now().date()
    #     data_conclusao_prevista = data_inicial_prevista
    #     dias_diferenca_inicio = ''

    #     prazo_fatal_dias = 0
    #     dias_diferenca_conclusao = 0
    #     status_projeto = ''
    #     observacao = ''

    #     nivel_inclusao = len(tarefa_id)
    #     nivel_inclusao_mae = len(tarefa_id)
    #     nivel_secundario = ''
    #     nivel_ultimo = ''
    #     lin = int(linha) + 1
    #     # Checar e determinar o código novo
    #     for i in range(lin, len(self.LCronograma.get_children())):
    #         item = self.LCronograma.get_children()[i]
    #         values = self.LCronograma.item(item, 'values')
    #         # Supondo que o segundo subitem é o que você quer
    #         nivel_secundario = len(values[1].replace(".", ""))
    #         if nivel_inclusao == nivel_secundario:
    #             nivel_ultimo = values[1]
        
    #     # Verifica se Nivel_Ultimo está vazio
    #     if nivel_ultimo == '':
    #         # Incrementa os últimos dois dígitos
    #         tarefa_mae_id = tarefa_id
    #         nivel_ultimo = tarefa_id[:nivel_inclusao - 2] + str(int(tarefa_id[-2:]) + 1).zfill(2)
    #         Linha_Incluir = 'end'
    #     else:
    #         tarefa_mae_id = tarefa_id[:-3] if len(tarefa_id) > 3 else ''
    #         nivel_inclusao = len(tarefa_id) + 2
    #         nivel_secundario = ""
    #         nivel_ultimo = ""
    #         linha += 1  # Ajusta linha para o próximo item
    #         # Segundo Loop
    #         for i in range(lin, len(self.LCronograma.get_children())):
    #             item = self.LCronograma.get_children()[i]
    #             values = self.LCronograma.item(item, 'values')
    #             nivel_secundario = len(values[1].replace(".", ""))
    #             if nivel_inclusao == nivel_secundario and values[1].replace(".", "")[:nivel_inclusao_mae] == tarefa_id.replace(".", ""):
    #                 nrcampo = self.LCronograma.index(item) + 2
    #                 Linha_Incluir = self.LCronograma.index(item) + 1
    #                 nivel_ultimo = values[1]

    #         # Define Nivel_Ultimo baseado no resultado do segundo loop
    #         def calcular_nivel_ultimo(tarefa_id, nivel_inclusao, nivel_ultimo):
    #             # Extrai a parte inicial do tarefa_id
    #             parte_inicial = tarefa_id[:nivel_inclusao - 2]
    #             # Extrai os últimos dois caracteres de nivel_ultimo e incrementa
    #             numero_atual = int(nivel_ultimo[-2:]) + 1
    #             # numero_atual = '00' + numero_atual
    #             numero_formatado = str(numero_atual).zfill(2)  # Garante que tenha 2 dígitos
    #             # Concatena e retorna o novo ID
    #             # print(parte_inicial, numero_formatado)
    #             novo_nivel_ultimo = parte_inicial + numero_formatado
    #             return novo_nivel_ultimo

    #         if nivel_ultimo == '':
    #             nivel_ultimo = tarefa_id + "01"
    #         else:
    #             novo_nivel_ultimo = calcular_nivel_ultimo(
    #                 tarefa_id, nivel_inclusao, nivel_ultimo)
    #             # tarefa_id[:nivel_inclusao - 2] + str(int(nivel_ultimo[-2:]) + 1).zfill(2)
    #             nivel_ultimo = novo_nivel_ultimo

    #     # Construir o Código
    #     tarefa_id_nova = ".".join([nivel_ultimo[i:i+2]
    #                               for i in range(0, len(nivel_ultimo), 2)])

    #     # Adicionar na Lista
    #     nrcarat = len(tarefa_id_nova)
    #     tarefa_info = (
    #         nrcampo,
    #         str(tarefa_id_nova).zfill(2),
    #         ' ' * round(nrcarat) + tarefa_ds_nova,
    #         '',  # Responsável
    #         '',  # Dependência
    #         0,   # Tempo de espera
    #         1,   # Tempo previsto
    #         percentual_execucao,
    #         data_inicial_prevista.strftime("%d/%m/%Y"),
    #         '',  # Data Realizada
    #         data_conclusao_prevista.strftime("%d/%m/%Y"),
    #         '',  # Data de Conclusão Realizada
    #         '',  # Observação
    #     )
    #     # Adicionar na Tela
    #     # identificador_unico = f"item_{len(self.LCronograma.get_children()) + 1}"
    #     identificador_unico = f"item_{uuid.uuid4().hex}"
    #     per_conclusao = 0
    #     semaforo = self.status_on(identificador_unico, data_inicial_prevista, '', data_inicial_prevista, '', per_conclusao)

    #     self.LCronograma.insert(
    #         '',
    #         Linha_Incluir,
    #         iid=identificador_unico,
    #         image=semaforo,
    #         values=tarefa_info
    #     )
    #     # Gravar no Banco de Dados
    #     # self.gravar_cronograma_incluir(projeto_id, projeto_ds, tarefa_id_nova,
    #     #                                tarefa_ds_nova, tarefa_mae_id, data_inicial_prevista, data_conclusao_prevista)
    #     # Atualizar os indices
    #     self.atualizar_dependencias(tarefa_id_nova)
    #     self.atualiza_cronograma_interacao(10)
    #     self.ajustar_list()
    
    def incluir_tarefas_hierarquico(self, projeto_id, projeto_ds, linha, tarefa_id, selected_item):
        # Parametros Iniciais
        nrcampo = int(linha) + 2
        tarefa_id = tarefa_id.replace(".", "")
        tarefa_ds_nova = "Preencher Descricão Nova Tarefa...................!!!!"
        
        percentual_execucao = '0.00%'
        data_inicial_prevista = datetime.now().date()
        data_conclusao_prevista = data_inicial_prevista
        
        nivel_inclusao = len(tarefa_id)
        nivel_inclusao_mae = len(tarefa_id)
        nivel_ultimo = ''
        lin = int(linha) + 1
        
        nivel_ultimo = self.determinar_novo_codigo(tarefa_id, selected_item)
      
        # Verificar se é uma tarefa filha ou uma nova tarefa principal
        if nivel_ultimo == '':
            # Incrementa os últimos dois dígitos
            nivel_ultimo = tarefa_id[:nivel_inclusao - 2] + str(int(tarefa_id[-2:]) + 1).zfill(2)
            Linha_Incluir = 'end'

        else:  # É uma nova tarefa principal
            nivel_inclusao = len(tarefa_id) + 2
            nivel_secundario = ""
            nivel_ultimo = ""
            linha += 1  # Ajusta linha para o próximo item

            selected_index = self.LCronograma.index(selected_item)

            # Segundo Loop
            # print(selected_index, len(self.LCronograma.get_children()))
            # for i in range(selected_index, len(self.LCronograma.get_children())):
            #     item = self.LCronograma.get_children()[i]
            #     values = self.LCronograma.item(item, 'values')
            #     nivel_secundario = len(values[1].replace(".", ""))
            #     if nivel_inclusao == nivel_secundario and values[1].replace(".", "")[:nivel_inclusao_mae] == tarefa_id.replace(".", ""):
            #         nrcampo = self.LCronograma.index(item) + 2
            #         Linha_Incluir = self.LCronograma.index(item) + 1
            #         nivel_ultimo = values[1]

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
                nivel_ultimo = novo_nivel_ultimo






            # # Incrementar o número da tarefa principal
            # if nivel_ultimo:
            #     nivel_ultimo = nivel_ultimo[:nivel_inclusao - 2] + str(int(nivel_ultimo[-2:]) + 1).zfill(2)
            # else:
            #     nivel_ultimo = ".01"
            
            Linha_Incluir = 'end'

        # Construir o Código
        tarefa_id_nova = ".".join([nivel_ultimo[i:i+2] for i in range(0, len(nivel_ultimo), 2)])
        tarefa_mae_id = tarefa_id_nova[:-3] if len(tarefa_id_nova) > 3 else ''
        
        # Adicionar na Lista
        nrcarat = len(tarefa_id_nova)
        tarefa_info = self.criar_tarefa_info(nrcampo, tarefa_id_nova, tarefa_ds_nova, nrcarat, percentual_execucao, data_inicial_prevista, data_conclusao_prevista)

        # Adicionar na Tela
        identificador_unico = f"item_{uuid.uuid4().hex}"
        per_conclusao = 0
        semaforo = self.status_on(identificador_unico, data_inicial_prevista, '', data_inicial_prevista, '', per_conclusao)

        self.LCronograma.insert(
            '',
            Linha_Incluir,
            iid=identificador_unico,
            image=semaforo,
            values=tarefa_info
        )

        print('Gravando tarefa...')
        breakpoint()
        # Gravar no Banco de Dados
        # self.gravar_cronograma_incluir(projeto_id, projeto_ds, tarefa_id_nova,
        #                             tarefa_ds_nova, tarefa_mae_id, data_inicial_prevista, data_conclusao_prevista)
        
        # self.consulta_cronograma_atividades(self.principal_frame)

        # Atualizar os indices
        self.atualizar_dependencias(tarefa_id_nova)
        self.atualiza_cronograma_interacao(10)
        self.ajustar_list()

    def encontrar_ultima_subtarefa_hierarquico(self, tarefa_mae_id):
        nivel_ultimo = tarefa_mae_id  # Inicializa com a tarefa mãe
        tarefa_mae_id_sem_pontos = tarefa_mae_id.replace(".", "")
        
        for item in self.LCronograma.get_children():
            values = self.LCronograma.item(item, 'values')
            item_id = values[1]
            item_id_sem_pontos = item_id.replace(".", "")
            
            print(f'Analisando: {item_id}, Tarefa mãe: {tarefa_mae_id}')
            
            if item_id_sem_pontos.startswith(tarefa_mae_id_sem_pontos) and item_id != tarefa_mae_id:
                if len(item_id_sem_pontos) == len(tarefa_mae_id_sem_pontos) + 2:
                    nivel_ultimo = item_id
                # Não precisamos do 'else' aqui, pois queremos continuar procurando
        
        # Se não encontrou nenhuma subtarefa, adiciona "01" à tarefa mãe
        if nivel_ultimo == tarefa_mae_id:
            nivel_ultimo += ".01"
        else:
            # Incrementa o último número da subtarefa
            partes = nivel_ultimo.split(".")
            ultimo_numero = int(partes[-1])
            partes[-1] = f"{ultimo_numero + 1:02d}"
            nivel_ultimo = ".".join(partes)
        
        print(f"Última subtarefa encontrada: {nivel_ultimo}")
        return nivel_ultimo

    def encontrar_posicao_insercao_hierarquico(self, linha, tarefa_base_id):
        ultima_posicao = linha
        nivel_base = len(tarefa_base_id)
        
        print(f"Buscando posição de inserção para tarefa base: {tarefa_base_id}")
        
        for i in range(linha + 1, len(self.LCronograma.get_children())):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            tarefa_atual = values[1].replace(".", "")
            
            print(f"Analisando tarefa: {tarefa_atual}")
            
            if tarefa_atual.startswith(tarefa_base_id):
                ultima_posicao = i
                print(f"Subtarefa encontrada, atualizando última posição para: {ultima_posicao}")
            elif len(tarefa_atual) <= nivel_base:
                print(f"Tarefa de nível superior ou igual encontrada: {tarefa_atual}")
                break
        
        posicao_final = ultima_posicao + 1
        print(f"Posição de inserção final: {posicao_final}")
        return posicao_final
    
    def encontrar_ultima_tarefa_principal_hierarquico(self):
        for i in range(len(self.LCronograma.get_children()) - 1, -1, -1):
            item = self.LCronograma.get_children()[i]
            values = self.LCronograma.item(item, 'values')
            if len(values[1]) == 2:
                return values[1]
        return ''

    def determinar_novo_codigo_hierarquico(self, tarefa_id, item_selecionado):
        nivel_inclusao = len(tarefa_id.replace(".", ""))
        nivel_ultimo = ''
        
        # Encontrar o índice do item selecionado
        todos_itens = self.LCronograma.get_children()
        try:
            indice_inicio = todos_itens.index(item_selecionado)
        except ValueError:
            # Se o item selecionado não for encontrado, começamos do início
            indice_inicio = 0
        
        def processar_item(item, nivel_atual):
            nonlocal nivel_ultimo
            values = self.LCronograma.item(item, 'values')
            item_id = values[1].replace(".", "")
            
            if len(item_id) == nivel_inclusao:
                nivel_ultimo = item_id
            elif len(item_id) > nivel_inclusao:
                # Processa os filhos
                for child in self.LCronograma.get_children(item):
                    processar_item(child, len(item_id))
            elif len(item_id) < nivel_inclusao:
                # Encontramos um item de nível superior, paramos a busca
                return False
            
            return True

        # Processa todos os itens a partir do item selecionado
        for item in todos_itens[indice_inicio:]:
            if not processar_item(item, nivel_inclusao):
                break

        # Determinar o novo código
        if nivel_ultimo == '':
            # É uma nova tarefa principal
            novo_codigo = tarefa_id[:nivel_inclusao - 2] + str(int(tarefa_id[-2:]) + 1).zfill(2)
        else:
            # É uma subtarefa
            parte_inicial = tarefa_id[:nivel_inclusao - 2]
            numero_atual = int(nivel_ultimo[-2:]) + 1
            novo_codigo = parte_inicial + str(numero_atual).zfill(2)

        return ".".join([novo_codigo[i:i+2] for i in range(0, len(novo_codigo), 2)])
    
    def criar_tarefa_info_hierarquico(self, nrcampo, tarefa_id_nova, tarefa_ds_nova, nrcarat, 
                        percentual_execucao, data_inicial_prevista, data_conclusao_prevista):
        return (
            nrcampo,
            str(tarefa_id_nova).zfill(2),
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

    def get_all_items_numbers(self):
        def traverse(item='', level=0):
            numbers = []
            children = self.LCronograma.get_children(item)
            for index, child in enumerate(children):
                values = self.LCronograma.item(child, 'values')
                if values:
                    position = self.LCronograma.index(child)
                    number = values[0]  # Número do item (campo 0)
                    campo1 = values[1]  # Campo 1
                    campo2 = values[2]  # Campo 2
                    numbers.append((number, campo1, campo2, position, level))  # Número, campo1, campo2, posição e nível
                numbers.extend(traverse(child, level + 1))
            return numbers

        return traverse()
           

    ##----------------------------------------------------------------------------##
    def gravar_cronograma_incluir_hierarquico(self, projeto_id, projeto_ds, tarefa_id_nova, tarefa_ds_nova, tarefa_mae_id, data_inicial_prevista, data_conclusao_prevista):
        try:
            if not projeto_id:
                messagebox.showinfo("Gestor de Negócios", "Preencher o Projeto!!")
                return
            
            self.atualiza_cronograma_interacao(10)
            projeto_cr = 0
            responsavel_nome = ""
            tarefa_dependencia = ""
            tempo_espera = 0
            tempo_previsto = 0
            percentual_execucao = 0.0
            data_inicial_realizada = str('1899-12-30')
            data_conclusao_realizada = str('1899-12-30')
            dias_diferenca_inicio = 0
            prazo_fatal_dias = 0
            dias_diferenca_conclusao = 0
            status_projeto = ""
            observacao = ""
            anexos = ""

            # Prepare the SQL insertion command
            vsSQL = """
                        INSERT INTO programas_atividades (
                                                            projeto_ID, 
                                                            projeto_DS, 
                                                            projeto_cr, 
                                                            tarefa_ID, 
                                                            tarefa_DS, 
                                                            parent_ID,
                                                            responsavel_nome, 
                                                            tarefa_dependencia,
                                                            tempo_espera, 
                                                            tempo_previsto, 
                                                            percentual_execucao, 
                                                            data_Inicial_Prevista,
                                                            data_Inicial_Realizada, 
                                                            dias_diferenca_inicio, 
                                                            data_conclusao_prevista,
                                                            data_conclusao_realizada, 
                                                            prazo_fatal_dias, 
                                                            dias_diferenca, 
                                                            status, 
                                                            observacao, 
                                                            anexos)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            params = (
                projeto_id,
                projeto_ds,
                projeto_cr,
                tarefa_id_nova,
                tarefa_ds_nova.replace("'", " "),
                tarefa_mae_id,
                responsavel_nome,
                tarefa_dependencia,
                round(tempo_espera, 0),
                round(tempo_previsto, 0),
                float(percentual_execucao),
                data_inicial_prevista.strftime("%Y-%m-%d"),
                data_inicial_realizada,
                round(dias_diferenca_inicio, 0),
                data_conclusao_prevista.strftime("%Y-%m-%d"),
                data_conclusao_realizada,
                round(prazo_fatal_dias, 0),
                round(dias_diferenca_conclusao, 0),
                status_projeto,
                observacao.replace("'", " "),
                anexos
            )

            # Execute SQL command
            myresult = db.executar_consulta(vsSQL, params)
            
        except Exception as e:
            messagebox.showinfo(f"Error occurred: {str(e)}")
        finally:
            pass

    def gravar_cronograma_total_hierarquico(self, janela):
        try:
            projeto_ds = self.entry_projeto.get()
            if self.entry_projeto.get() != '':
                projeto_id = self.obter_Projeto_ID(self.entry_projeto.get(), self.window_one)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher o Projeto!!", parent=janela)
                return
            if len(self.LCronograma.get_children()) == 0:
                messagebox.showinfo("Gestor de Negócios", "Projeto sem tarefas para salvar!!", parent=janela)
                return

            # Cria uma nova janela (tela de carregamento)
            coordenadas_relx = 0.20
            coordenadas_rely = 0.30
            coordenadas_relwidth = 0.50
            coordenadas_relheight = 0.05
            self.frm_barra_progresso = customtkinter.CTkFrame(janela, border_color="gray75", border_width=0, fg_color='transparent', corner_radius=10)
            self.frm_barra_progresso.pack(fill='x')
            self.frm_barra_progresso.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
            
            # Cria a Barra de Progresso
            self.progress_bar = ctk.CTkProgressBar(
                                                    self.frm_barra_progresso,
                                                    width=400,
                                                    height=30,
                                                    corner_radius=30,
                                                    fg_color='#003',
                                                    progress_color='#060',
                                                )
            self.progress_bar.pack(fill='x', pady=10, padx=10)
            # Cria um label para mostrar o texto na barra de progresso
            self.label_progresso = ctk.CTkLabel(self.frm_barra_progresso, text="Aguarde Gravando...: 0%", anchor='center', text_color='white')
            self.label_progresso.pack(pady=(0, 10))  # Adiciona espaço abaixo da label

            self.progress_bar.set(1)  # Reseta a barra de progresso para 0
            self.total_records = len(self.LCronograma.get_children())  # Total records to process
            self.current_index = 0

            for i in range(len(self.LCronograma.get_children())):
                self.process_records()
                item = self.LCronograma.get_children()[i]
                values = self.LCronograma.item(item, 'values')
                # Assign values from the selected item (simulating UsrCronograma)
                projeto_ID = projeto_id
                projeto_DS = projeto_ds
                projeto_cr = 0
                tarefa_id = str(values[1]).zfill(2)  # '01' manter como string
                tarefa_DS = values[2].strip()
                nivel_atual = len(tarefa_id)
                if nivel_atual == 2:
                    tarefa_mae_id = ''
                else:
                    tarefa_mae_id = tarefa_id[:-3] if len(tarefa_id) > 3 else ''
                responsavel_nome = values[3]
                tarefa_dependencia = values[4]
                Tempo_Espera = values[5]
                Tempo_Previsto = values[6]
                percentual_execucao = values[7]
                data_inicial_Prevista = datetime.strptime(values[8], "%d/%m/%Y")
                data_inicial_Realizada = datetime.strptime(values[9], "%d/%m/%Y") if values[9] else None
                data_Conclusao_Prevista = datetime.strptime(values[10], "%d/%m/%Y")
                data_Conclusao_Realizada = datetime.strptime(values[11], "%d/%m/%Y") if values[11] else None
                prazo_fatal_dias = 0
                dias_diferenca_Conclusao = 0
                status_projeto = ""
                observacao = values[12]
                Anexos = ''

                # Calculate date differences
                dias_diferenca_inicio = (data_inicial_Realizada - data_inicial_Prevista).days if data_inicial_Realizada else 0
                prazo_fatal_dias = (datetime.now() - data_Conclusao_Prevista).days
                dias_diferenca_Conclusao = (data_Conclusao_Prevista - data_Conclusao_Realizada).days if data_Conclusao_Realizada else 0

                sql = """
                        UPDATE programas_atividades SET
                            projeto_DS               = %s,
                            projeto_cr               = %s,
                            tarefa_DS                = %s,
                            parent_ID                = %s,
                            responsavel_nome         = %s,
                            tarefa_dependencia       = %s,
                            tempo_espera             = %s,
                            tempo_previsto           = %s,
                            percentual_execucao      = %s,
                            Data_inicial_prevista    = %s,
                            Data_inicial_Realizada   = %s,
                            dias_diferenca_inicio    = %s,
                            data_conclusao_prevista  = %s,
                            data_conclusao_realizada = %s,
                            prazo_fatal_dias         = %s,
                            dias_diferenca           = %s,
                            status                   = %s,
                            observacao               = %s,
                            anexos                   = %s
                        WHERE projeto_ID    = %s 
                              AND tarefa_ID = %s
                    """

                parameters = (
                                projeto_DS,
                                projeto_cr,
                                tarefa_DS.replace("'", " "),
                                tarefa_mae_id,
                                responsavel_nome,
                                tarefa_dependencia,
                                Tempo_Espera,
                                Tempo_Previsto,
                                float(percentual_execucao.strip('%')) / 100,
                                data_inicial_Prevista.strftime('%Y-%m-%d'),
                                data_inicial_Realizada.strftime('%Y-%m-%d') if data_inicial_Realizada else '1899-12-30',
                                dias_diferenca_inicio,
                                data_Conclusao_Prevista.strftime('%Y-%m-%d'),
                                data_Conclusao_Realizada.strftime('%Y-%m-%d') if data_Conclusao_Realizada else '1899-12-30',
                                prazo_fatal_dias,
                                dias_diferenca_Conclusao,
                                status_projeto,
                                observacao.replace("'", " "),
                                Anexos,
                                projeto_ID,
                                tarefa_id
                            )
                # Execute the SQL command
                db.executar_consulta(sql, parameters)
                # messagebox.showinfo("Sucesso", "Tarefa Alterada com sucesso!")

        except Exception as e:
            messagebox.showinfo("Gestor de Negócios", f"Erro: {e}", parent=janela)
            return
        finally:
            pass

    def excluir_tarefas_hierarquico(self, projeto_id, tarefa_id):
        try:
            db.begin_transaction()
            try:
                delete_sql = f"DELETE FROM programas_atividades WHERE projeto_id={projeto_id} AND tarefa_id='{tarefa_id}'"
                db._querying(delete_sql)
                db.commit_transaction()
            except Exception as e:
                db.rollback_transaction()
                messagebox.showerror("Erro", f"Um erro ocorreu ao excluir a tarefa: {str(e)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Um erro ocorreu ao processar a exclusão: {str(e)}")
        finally:
            try:
                db.closing()
            except:
                pass

    def dta_tarefa_mae_hierarquico(self):
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
                            data_inicial_prevista = min(
                                data_inicial_prevista, values[8])
                    if values[9]:
                        if not data_inicial_realizada:
                            data_inicial_realizada = values[9]
                        else:
                            data_inicial_realizada = min(
                                data_inicial_realizada, values[9])
                    if values[10]:
                        if not data_conclusao_prevista:
                            data_conclusao_prevista = values[10]
                        else:
                            data_conclusao_prevista = max(
                                data_conclusao_prevista, values[10])
                    if values[11]:
                        if not data_conclusao_realizada:
                            data_conclusao_realizada = values[11]
                        else:
                            data_conclusao_realizada = max(
                                data_conclusao_realizada, values[11])

                    # Count completed tasks
                    if values[7] == 1.0:
                        nr_tarefas_concluidas += 1

                    nrcarat_seguinte += 1

                    # Calcular o Percentual de Execução
                    percentual_execucao = nr_tarefas_concluidas / \
                        nrcarat_seguinte if nrcarat_seguinte > 0 else 0

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
                        messagebox.showinfo(
                            "Success", f"Task dates and percentages updated for: {self.LCronograma[idx]['tarefa_id']}")
                Lin += 1
                values = self.LCronograma.item(Lin, 'values')
                nrregistros = len(values[1])
                linha += 1
                if Lin > len(self.LCronograma.get_children()):
                    return
                elif linha > len(self.LCronograma.get_children()):
                    return

            if nr_tarefas_concluidas != 0:
                percentual_execucao = (
                    nr_tarefas_concluidas / nrcarat_seguinte)
            else:
                percentual_execucao = 0

            if NrCaraceteres_Reg_Seg > nrcarat:
                if data_inicial_realizada and data_conclusao_realizada and percentual_execucao >= 1:
                    self.LCronograma[idx]['data_conclusao_realizada'] = data_conclusao_realizada - \
                        data_inicial_realizada
                elif data_inicial_prevista and data_conclusao_prevista:
                    self.LCronograma[idx]['data_conclusao_prevista'] = data_conclusao_prevista - \
                        data_inicial_prevista

                self.LCronograma[idx]['percentual_execucao'] = percentual_execucao

    def process_records_hierarquico(self):
        if self.current_index < self.total_records:
            self.current_index += 1 
            progress_value = self.current_index / self.total_records
            self.progress_bar.set(progress_value)
            self.label_progresso.configure(text=f"Aguarde Gravando...: {progress_value * 100:.0f}%")
            self.window_one.after(1000, self.process_records)
            self.window_one.update_idletasks()  # Atualiza a interface gráfica
        else:
            # Finaliza o processamento
            self.progress_bar.stop()  # Para a barra de progresso
            self.label_progresso.configure(text="Gravação concluída!")  # Mensagem de conclusão
            # Opcional: pode destruir o frame após alguns segundos ou manter uma interface de resultado
            self.window_one.after(2000, self.frm_barra_progresso.destroy)  # Espera 2 segundos antes de destruir o frame
            # self.progress_bar.stop()  # Para a barra de progresso
            # self.frm_barra_progresso.destroy()

    def tarefa_anexo_hierarquico(self, lin, empresa_id, projeto_id, tarefa_id):
        # Define o caminho do diretório
        sPath = os.path.join(os.getcwd(), '')  # Usa o diretório atual do script
        
        # Verifica se o diretório existe
        if os.path.exists(sPath):
            # Chama a função para gravar o anexo
            self.gravar_anexo_cronograma(lin, empresa_id, projeto_id, tarefa_id)
        else:
            # Mostra uma mensagem se o diretório não existir
            messagebox.showinfo("Gestor de Negócios", f"Erro - Arquivo Não Encontrado no caminho: {sPath}", parent=self.principal_frame)
    
    def gravar_anexo_cronograma_hierarquico(self, lin, empresa_id, projeto_id, tarefa_id):
        try:
            # Abrir a pasta e selecionar o PDF
            root = tk.Tk()
            root.withdraw()  # Esconder sua Janela
            file_path = filedialog.askopenfilename(
                title="Procurar Arquivos .pdf",
                initialdir=os.getcwd(),  # Setar o Diretório
                filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
            )
            
            if not file_path:
                messagebox.showinfo("Gestor de Negócios", "Informação nenhum arquivo selecionado!!!", parent=self.principal_frame)
                return

            # Pegar detalhes do arquivo
            file_name = os.path.basename(file_path)
            documento_ds = file_name

            conditions = []  
            conditions.append('Empresa_ID = %s')
            params = [empresa_id]
            conditions.append('Projeto_ID = %s')
            params.append(projeto_id)
            conditions.append('Tarefa_ID = %s')
            params.append(tarefa_id)
            conditions.append('Doc_Num_Documento = %s')
            params.append(documento_ds)
            
            # Checar se a tarefa existe
            sql_check = f"""
                            SELECT ID_Anexo FROM TB_Gedoc_Tarefas 
                            WHERE {' AND '.join(conditions)} 
                        """
            
            record = db.executar_consulta(sql_check, params)
            # Abir e ler o arquivo em modo binário
            with open(file_path, 'rb') as file:
                file_data = file.read()
            
            if record:
                existing_record = record
                id_anexo = existing_record[0]['ID_Anexo']
                sql_update = """
                                UPDATE TB_Gedoc_Tarefas 
                                SET BinarioPDF = %s 
                                WHERE ID_Anexo = %s
                            """
                db.executar_consulta(sql_update, (file_data, id_anexo))
                messagebox.showinfo("Gestor de Negócios", "Documento Alterado com sucesso!!!", parent=self.principal_frame)
            else:
                # Inserir um Novo Registro
                sql_insert = """
                                INSERT INTO TB_Gedoc_Tarefas 
                                (
                                    Empresa_ID, 
                                    Projeto_ID, 
                                    Tarefa_ID, 
                                    Doc_Num_Documento, 
                                    BinarioPDF) 
                                VALUES (%s, %s, %s, %s, %s)
                            """
                db.executar_consulta(sql_insert, (empresa_id, projeto_id, tarefa_id, file_name, file_data))
                messagebox.showinfo("Gestor de Negócios", "Documento salvo com sucesso!!!", parent=self.principal_frame)

        except Exception as e:
            messagebox.showerror("Gestor de Negócios", f"Erro - ocorrência: {str(e)}", parent=self.principal_frame)
        finally:
            pass


Cronograma_Atividades_Hierarquico()

# ***********************************************************************************************************************************************************#
#                                          CLASSE PARA INTERAGIR COM O LIST
# ***********************************************************************************************************************************************************#

class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, projeto_id, projeto_ds, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.tree = ttk.Treeview(self)
        self.images = {}
        self.projeto_id = projeto_id
        self.projeto_ds = projeto_ds

        self.bind('<Double-1>', self.on_double_click)

    def on_double_click(self, event):
        region_clicked = self.identify_region(event.x, event.y)
        if region_clicked not in ('tree', 'cell'):
            return

        col_id = self.identify_column(event.x)
        self.column_index = int(col_id[1:]) - 1
        if self.column_index < 2:
            messagebox.showinfo("Gestor de Negócios", "Campo Não Permite Alteração!!")
            return

        selected_iid = self.focus()  # O numero da linha tbem é o iid
        selected_values = self.item(selected_iid)
        if col_id == '#0':
            selected_text = selected_values.get('text')
        else:
            selected_text = selected_values.get('values')[self.column_index]

        self.entry_descricao = selected_values.get('values')[2]
        self.entry_responsavel = selected_values.get('values')[3]
        self.entry_dependencia = selected_values.get('values')[4]
        self.entry_tempo_espera = selected_values.get('values')[5]
        self.entry_tempo_previsto = selected_values.get('values')[6]
        self.entry_per_execucao = selected_values.get('values')[7]
        self.entry_data_inicial_prevista = selected_values.get('values')[8]
        self.entry_data_inicial_realizada = selected_values.get('values')[9]
        self.entry_data_conclusao_prevista = selected_values.get('values')[10]
        self.entry_data_conclusao_realizada = selected_values.get('values')[11]
        self.entry_observacao = selected_values.get('values')[12]

        column_box = self.bbox(selected_iid, col_id)
        self.entry_edit = tk.Entry(self.master, width=column_box[2])

        if self.column_index == 8 or self.column_index == 9 or self.column_index == 10 or self.column_index == 11:
            self.entry_edit.bind("<Double-1>", self.calendario)
            self.entry_edit.bind('<KeyRelease>', self.update_date_format)

        # Carregar os dados para os devidos Calculos
        self.entry_id = str(selected_values.get('values')[1])
        self.entry_id = str(self.entry_id).zfill(2)  # '01' manter como string
        self.entry_descricao = selected_values.get('values')[2]
        self.entry_responsavel = selected_values.get('values')[3]
        self.entry_dependencia = selected_values.get('values')[4]
        self.entry_tempo_espera = selected_values.get('values')[5]
        self.entry_tempo_previsto = selected_values.get('values')[6]
        self.entry_per_execucao = selected_values.get('values')[7]
        self.entry_data_inicial_prevista = selected_values.get('values')[8]
        self.entry_data_inicial_realizada = selected_values.get('values')[9]
        self.entry_data_conclusao_prevista = selected_values.get('values')[10]
        self.entry_data_conclusao_realizada = selected_values.get('values')[11]
        self.entry_observacao = selected_values.get('values')[12]

        self.entry_edit.editing_column_index = self.column_index
        self.entry_edit.editing_item_iid = selected_iid
        self.entry_edit.insert(0, selected_text)
        self.entry_edit.select_range(0, tk.END)
        self.entry_edit.focus_set()
        if self.column_index != 8 and self.column_index != 9 and self.column_index != 10 and self.column_index != 11:
            self.entry_edit.bind('<FocusOut>', self.on_focus_out)

        self.entry_edit.bind('<Return>', self.on_enter_pressed)

        # localização do entry no TreeView
        self.entry_edit.place(x=column_box[0],
                              y=column_box[1],
                              width=column_box[2],
                              height=column_box[3])

    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        # Obtém o valor editado
        new_value = event.widget.get()

        selected_iid = event.widget.editing_item_iid
        self.column_index = event.widget.editing_column_index

        if self.column_index == 2:
            # Descrição da Tarefa
            nrcarat = len(self.entry_id)
            new_value = ' ' * round(nrcarat) + new_value.strip()

        elif self.column_index == 4:
            # Dependência
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo('Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar a dependência!!!')
                event.widget.destroy()
                return
            
        elif self.column_index == 5:
            # Espera
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo('Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar o tempo de espera!!!')
                event.widget.destroy()
                return
        
        elif self.column_index == 6:
            # Prazo
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo('Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar o prazo de execução da tarefa!!!')
                event.widget.destroy()
                return
            
        elif self.column_index == 7:
            # Percentual de Execução
            if self.entry_data_conclusao_realizada != '':
                messagebox.showinfo('Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar o percentual executado!!!')
                event.widget.destroy()
                return
            elif new_value == '100':
                new_value = f"{float(new_value)/100:.2%}"
                self.entry_data_conclusao_realizada = datetime.now().date().strftime("%d/%m/%Y")
            else:
                new_value = f"{float(new_value)/100:.2%}"

        elif self.column_index == 8:
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo(
                    "Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar a data inicial.")
                event.widget.destroy()
                return
            else:
                self.entry_data_conclusao_prevista = (self.parse_date(new_value) + timedelta(days=float(self.entry_tempo_previsto))).strftime("%d/%m/%Y")
                
        elif self.column_index == 9:
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo("Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar a data inicial.")
                event.widget.destroy()
                return
            

        elif self.column_index == 10:
            if self.entry_per_execucao == '100.00%':
                messagebox.showinfo(
                    "Gestor de Negócios", "A tarefa já foi concluída, não é possível alterar a data inicial.")
                event.widget.destroy()
                return
            else:
                self.entry_data_inicial_prevista = (self.parse_date(new_value) - timedelta(days=float(self.entry_tempo_previsto))).strftime("%d/%m/%Y")
    
        elif self.column_index == 11:
            if new_value != '':
                self.entry_per_execucao = f"{float(1.00):.2%}"
            else:
                self.entry_per_execucao = f"{float(0.00):.2%}"

        if self.column_index == -1:
            self.item(selected_iid, text=new_value)
        else:
            current_values = self.item(selected_iid).get('values')
            current_values[1] = self.entry_id
            current_values[2] = self.entry_descricao
            current_values[3] = self.entry_responsavel
            current_values[4] = self.entry_dependencia
            current_values[5] = self.entry_tempo_espera
            current_values[6] = self.entry_tempo_previsto
            current_values[7] = self.entry_per_execucao
            current_values[8] = self.entry_data_inicial_prevista
            current_values[9] = self.entry_data_inicial_realizada
            current_values[10] = self.entry_data_conclusao_prevista
            current_values[11] = self.entry_data_conclusao_realizada
            current_values[12] = self.entry_observacao
            current_values[self.column_index] = new_value
            
            self.item(selected_iid, values=current_values)

            self.atualiza_cronograma_interacao(10)
            self.ajustar_list()

        event.widget.destroy()

    def update_date_format(self, event):
        # Obtém o valor editado
        current_value = event.widget.get()

        sel_start = len(current_value)
        if len(current_value) == 2:
            current_value += "/"
            sel_start = 4
        elif len(current_value) == 5:
            current_value += "/"
            sel_start = 7

        # Update entry value and position cursor
        event.widget.delete(0, tk.END)
        event.widget.insert(0, current_value)
        event.widget.icursor(sel_start)

    def calendario(self, event):
        # self.window_calendar = Tk()
        self.window_calendar = customtkinter.CTkToplevel(self.master)
        self.window_calendar.title('Calendário')
        calendario = tkcalendar.Calendar(self.window_calendar, locale='pt_br')
        calendario.pack(pady=10)

        def get_data(event):
            dta = calendario.get_date()
            for widget in self.window_calendar.winfo_children():
                widget.destroy()

            self.window_calendar.destroy()  # Destroi
            self.window_calendar = None  # Reseta a referência do frame atual
            self.entry_edit.delete(0, "end")
            self.entry_edit.insert(0, dta.strip())

        calendario.bind('<<CalendarSelected>>', get_data)
        self.window_calendar.focus_force()
        self.window_calendar.grab_set()

    def atualiza_cronograma_interacao(self, nr_interacao):
        for _ in range(nr_interacao):
            for i in range(len(self.get_children())):
                item_id = self.get_children()[i]
                values = self.item(item_id, 'values')
                tarefa_dependencia = values[4]
                # if tarefa_dependencia:
                self.predessessora(item_id)

        self.dta_tarefa_mae()

    def is_valid_date(self, date_str):
        try:
            self.parse_date(date_str)
            return True
        except ValueError:
            return False

    def parse_date(self, date_str, fallback_date=None):
        if isinstance(date_str, datetime):
            return date_str  # Retorna se já for um objeto datetime

        if date_str:  # Verifica se date_str não é vazio
            try:
                # Tenta analisar o formato com hora
                # Formato para data com hora
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                pass

            try:
                # Se necessário, tenta o formato sem hora
                # Formato sem hora
                return datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError as e:
                pass

        if fallback_date:
            if isinstance(fallback_date, datetime):
                return fallback_date  # Retorne se já é um objeto datetime
            try:
                # Formato do fallback
                return datetime.strptime(fallback_date, '%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                pass

        return None  # Retorna None se não conseguiu analisar

    def status_on(self, selected_iid, dta_inicio_prev, dta_inicio_real, dta_conclusao_prev, dta_conclusao_real, per_conclusao):
        try:
            # Carrega os farois
            icon_image_azul = self.base64_to_farois('semafaro_azul')
            icon_image_verde = self.base64_to_farois('semafaro_verde')
            icon_image_amarelo = self.base64_to_farois('semafaro_amarelo')
            icon_image_vermelho = self.base64_to_farois('semafaro_vermelho')

            # Remova a hora e o minuto
            if isinstance(dta_inicio_prev, datetime):
                dta_inicio_prev = dta_inicio_prev.date()  # Converte para date

            if isinstance(dta_inicio_real, datetime):
                dta_inicio_real = dta_inicio_real.date()  # Converte para date

            if isinstance(dta_conclusao_prev, datetime):
                dta_conclusao_prev = dta_conclusao_prev.date()  # Converte para date

            if isinstance(dta_conclusao_real, datetime):
                dta_conclusao_real = dta_conclusao_real.date()  # Converte para date

            if isinstance(dta_inicio_real, str):
                dta_inicio_real = datetime.strptime(
                    dta_inicio_real, "%d/%m/%Y").date()

            if isinstance(dta_inicio_prev, str):
                dta_inicio_prev = datetime.strptime(
                    dta_inicio_prev, "%d/%m/%Y").date()

            if isinstance(dta_conclusao_prev, str):
                dta_conclusao_prev = datetime.strptime(
                    dta_conclusao_prev, "%d/%m/%Y").date()
            
            if isinstance(dta_conclusao_real, str):
                dta_conclusao_real = datetime.strptime(
                    dta_conclusao_real, "%d/%m/%Y").date()

            today = datetime.now().date()
            if dta_inicio_real == '' or dta_inicio_real is None:
                if dta_inicio_prev < today:
                    icon_image = icon_image_vermelho
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                else:
                    icon_image = icon_image_amarelo
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
            else:
                if dta_conclusao_real == '' or dta_conclusao_real is None:
                    if dta_inicio_real != '' or dta_inicio_real is not None and dta_conclusao_prev < today:
                        icon_image = icon_image_vermelho
                        # Armazenar referência
                        self.images[selected_iid] = icon_image
                    else:
                        icon_image = icon_image_azul
                        # Armazenar referência
                        self.images[selected_iid] = icon_image
                elif float(per_conclusao) == 100.00:
                    icon_image = icon_image_verde
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                elif dta_conclusao_prev >= today:
                    icon_image = icon_image_azul
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                elif dta_conclusao_prev < today:
                    icon_image = icon_image_vermelho
                    # Armazenar referência
                    self.images[selected_iid] = icon_image
                else:
                    icon_image = icon_image_amarelo
                    # Armazenar referência
                    self.images[selected_iid] = icon_image

            return icon_image

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def predessessora(self, item_id):
        try:
            current_values = self.item(item_id).get('values')
            tasks_ids = self.get_children()
            task = self.item(item_id)
            lin = task['values'][0]
            strEndereco = task['values'][4] if task['values'][4] else ""

            tarefa_check = None
            tarefa_check = '01.02.01'
            semaforo = []

            tarefa_id = str(task['values'][1]).zfill(2)
            tarefa_dependencia = str(task['values'][4])
            tempo_espera = float(task['values'][5])
            tempo_previsto = float(task['values'][6])

            per_conclusao = float(task['values'][7].replace("%", ""))
            data_inicial_prevista = self.parse_date(task['values'][8])
            data_inicial_realizada = self.parse_date(task['values'][9])
            data_conclusao_prevista = self.parse_date(task['values'][10])
            data_conclusao_realizada = self.parse_date(task['values'][11])

            nr_caracteres = len(str(strEndereco))
            dta_precedente = None
            lin_dependente = ''
            if nr_caracteres != 0:
                for viContador in range(nr_caracteres):
                    char = str(strEndereco)[viContador]
                    if char != ';':
                        lin_dependente += char
                    else:
                        if int(lin_dependente) >= len(self.get_children()):
                            return

                        index = int(lin_dependente)
                        dep_task_id = tasks_ids[index]
                        dep_sub_items = self.item(dep_task_id, 'values')
                        
                        data_inicial_realizada = self.parse_date(dep_sub_items[9])
                        data_conclusao_prevista = self.parse_date(dep_sub_items[10])
                        data_conclusao_realizada = self.parse_date(dep_sub_items[11])
                        
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            if data_conclusao_realizada and self.is_valid_date(data_conclusao_realizada):
                                if dta_precedente is not None and dta_precedente < data_conclusao_realizada:
                                    dta_precedente = data_conclusao_realizada
                                else:
                                    dta_precedente = data_conclusao_prevista
                            else:
                                dta_precedente = data_conclusao_prevista
                        else:
                            if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                                dta_precedente = data_conclusao_prevista

                        lin_dependente = ''

                if lin_dependente and int(lin_dependente) <= len(self.get_children()):
                    index = int(lin_dependente) - 1
                    dep_task_id = tasks_ids[index]
                    dep_task = self.item(dep_task_id, 'values')
                    dep_sub_items = self.item(dep_task_id, 'values')

                    data_inicial_realizada = self.parse_date(dep_sub_items[9])
                    data_conclusao_prevista = self.parse_date(dep_sub_items[10])
                    data_conclusao_realizada = self.parse_date(dep_sub_items[11])

                    if data_conclusao_realizada and self.is_valid_date(data_conclusao_realizada):
                        if dta_precedente is None or dta_precedente < data_conclusao_realizada:
                            dta_precedente = data_conclusao_realizada
                    else:
                        if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                            dta_precedente = data_conclusao_prevista
                else:
                    if dta_precedente is None or dta_precedente < data_conclusao_prevista:
                        dta_precedente = data_conclusao_prevista

                if dta_precedente or dta_precedente is not None:
                    current_values[8] = (dta_precedente + timedelta(days=tempo_espera)).strftime("%d/%m/%Y")
                    
                nr_caracteres = int(len(tarefa_id))
                if lin + 1 < len(self.get_children()):
                    index = int(lin + 1)
                    next_task_id = tasks_ids[index]
                    next_task = self.item(next_task_id, 'values')
                    nr_caracteres_seguintes = int(len(next_task[1]))

                    if nr_caracteres_seguintes <= nr_caracteres:
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            current_values[10] = (self.parse_date(data_inicial_realizada) + timedelta(days=tempo_espera) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
                        else:
                            current_values[10] = (self.parse_date(data_inicial_prevista) + timedelta(days=tempo_espera) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
            else:
                nr_caracteres = int(len(tarefa_id))
                if lin + 1 < len(self.get_children()):
                    index = int(lin + 1)
                    next_task_id = tasks_ids[index]
                    next_task = self.item(next_task_id, 'values')
                    nr_caracteres_seguintes = int(len(next_task[1]))

                    if nr_caracteres_seguintes <= nr_caracteres:
                        if data_inicial_realizada and self.is_valid_date(data_inicial_realizada):
                            current_values[10] = (self.parse_date(data_inicial_realizada) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")
                        else:
                            current_values[10] = (self.parse_date(data_inicial_prevista) + timedelta(days=tempo_previsto)).strftime("%d/%m/%Y")

            self.item(item_id, values=current_values)

        except Exception as e:
            messagebox.showerror("Error", f"Error in calculate_predecessor: {str(e)}")
          
    def ajustar_list(self):
        try:
            for i in range(len(self.get_children())):  # Itera sobre os itens no Treeview
                item_id = self.get_children()[i]
                task_data = self.item(item_id)  # Obtém os dados do item
                # Assume tarefa_ID está na posição 1
                tarefa_id = str(task_data['values'][1])
                nrcarat = len(tarefa_id.upper())
                linha = i + 1

                if linha < len(self.get_children()):
                    next_item_id = self.get_children()[linha]
                    next_task_data = self.item(next_item_id)
                    # Assume tarefa_ID está na posição 1
                    next_tarefa_id = str(next_task_data['values'][1])
                    nrcarat_seguinte = len(next_tarefa_id.upper())
                else:
                    nrcarat_seguinte = nrcarat

                # Aplica formatação baseada nos critérios
                if nrcarat_seguinte > nrcarat:
                    self.item(item_id, tags=('bold_blue',))
                elif nrcarat_seguinte == nrcarat and nrcarat > 2:
                    self.item(item_id, tags=('normal_black',))
                elif nrcarat_seguinte == nrcarat and nrcarat <= 2:
                    self.item(item_id, tags=('bold_blue',))
                else:
                    self.item(item_id, tags=('normal_black',))

                # Para última linha, verifica comparação com a linha anterior
                if i == len(self.get_children()) - 1:
                    # Assume tarefa_ID está na posição 1
                    
                    tarefa_id = str(self.item(item_id)['values'][1]).zfill(2)
                    tarefa_id_anterior = str(self.item(self.get_children()[i - 1])['values'][1]).zfill(2)
                    if len(tarefa_id.upper()) < len(tarefa_id_anterior.upper()):
                        self.item(item_id, tags=('bold_blue',))

                per_conclusao = float(task_data['values'][7].replace("%", ""))
                data_inicial_prevista = self.parse_date(task_data['values'][8])
                data_inicial_realizada = self.parse_date(task_data['values'][9])
                data_conclusao_prevista = self.parse_date(task_data['values'][10])
                data_conclusao_realizada = self.parse_date(task_data['values'][11])
                
                semaforo = self.status_on(item_id, data_inicial_prevista, data_inicial_realizada,
                                        data_conclusao_prevista, data_conclusao_realizada, per_conclusao)
                self.item(item_id, image=semaforo)

            # Configura as tags para o Treeview
            self.tag_configure('bold_blue', font=('Helvetica', 10, 'bold'), foreground='blue')
            self.tag_configure('normal_black', font=('Helvetica', 10), foreground='black')

        except Exception as e:
            messagebox.showerror("Erro!", f"Erro: {str(e)}")  # Exibe mensagem de erro
    
    def dta_tarefa_mae(self):
        for idx in range(len(self.get_children())):
            item_id = self.get_children()[idx]
            values = self.item(item_id, 'values')
            tasks_ids = self.get_children()
            
            nrcarat = 0
            NrCampos = values[0]
            tarefa_id = values[1].zfill(2)
            nrcarat = len(tarefa_id)
            entry_descricao = values[2]
            entry_responsavel = values[3]
            entry_dependencia = values[4]
            entry_tempo_espera = values[5]
            entry_tempo_previsto = values[6]
            per_conclusao = float(values[7].replace("%", ""))
            data_inicial_prevista = self.parse_date(values[8])
            data_inicial_realizada = self.parse_date(values[9])
            data_conclusao_prevista = self.parse_date(values[10])
            data_conclusao_realizada = self.parse_date(values[11])
            dta_provisoria_inicial_prevista = ''
            dta_provisoria_inicial_realizada = ''
            dta_provisoria_conclusao_prevista = ''
            dta_provisoria_conclusao_realizada = ''

            Lin = idx + 1
            if Lin >= len(self.get_children()):
                return
            else:
                dep_task_id = tasks_ids[Lin]
                dep_sub_items = self.item(dep_task_id, 'values')
                tarefa_id_reg_seg = dep_sub_items[1].zfill(2)
                NrCaraceteres_Reg_Seg = len(tarefa_id_reg_seg)

            nrcarat_seguinte = 0
            nr_tarefas_concluidas = 0
            
            nrregistros = int(len(tarefa_id_reg_seg))
            linha = Lin + 1
            
            Lin_proxima = Lin
            dep_task_id = tasks_ids[Lin]
            dep_sub_items = self.item(dep_task_id, 'values')
            
            while tarefa_id_reg_seg[:nrcarat] == tarefa_id and len(self.get_children()) > linha:
                
                base_tarefa_sequencia_id = tasks_ids[linha]
                base_tarefa_sequencia_items = self.item(base_tarefa_sequencia_id, 'values')
                tarefa_id_reg_sequencia = base_tarefa_sequencia_items[1].zfill(2)
                
                if int(len(tarefa_id_reg_sequencia)) <= int(nrregistros):
                    per_conclusao_items = float(dep_sub_items[7].replace("%", ""))
                    data_inicial_prevista_items = self.parse_date(dep_sub_items[8])
                    data_inicial_realizada_items = self.parse_date(dep_sub_items[9])
                    data_conclusao_prevista_items = self.parse_date(dep_sub_items[10])
                    data_conclusao_realizada_items = self.parse_date(dep_sub_items[11])
                    
                    if data_inicial_prevista_items is not None:
                        if dta_provisoria_inicial_prevista == '':
                            dta_provisoria_inicial_prevista = data_inicial_prevista_items
                            data_inicial_prevista = data_inicial_prevista_items
                        else:
                            data_inicial_prevista = min(self.parse_date(data_inicial_prevista_items), self.parse_date(dta_provisoria_inicial_prevista))
                            dta_provisoria_inicial_prevista = data_inicial_prevista
                        
                    if data_inicial_realizada_items is not None:
                        if dta_provisoria_inicial_realizada == '':
                            dta_provisoria_inicial_realizada = data_inicial_realizada_items
                            data_inicial_realizada = data_inicial_realizada_items
                        else:
                            data_inicial_realizada = min(self.parse_date(data_inicial_realizada_items), self.parse_date(dta_provisoria_inicial_realizada))
                            dta_provisoria_inicial_realizada = data_inicial_realizada 
                    
                    if data_conclusao_prevista_items is not None:
                        if dta_provisoria_conclusao_prevista == '':
                            dta_provisoria_conclusao_prevista = data_conclusao_prevista_items
                            data_conclusao_prevista = data_conclusao_prevista_items 
                        else:
                            data_conclusao_prevista = max(self.parse_date(data_conclusao_prevista_items), self.parse_date(dta_provisoria_conclusao_prevista))
                            dta_provisoria_conclusao_prevista = data_conclusao_prevista_items
                    
                    if data_conclusao_realizada_items is not None:
                        if dta_provisoria_conclusao_realizada == '':
                            dta_provisoria_conclusao_realizada = data_conclusao_realizada_items
                            data_conclusao_realizada = data_conclusao_realizada_items
                        else:
                            data_conclusao_realizada = max(self.parse_date(data_conclusao_realizada_items), self.parse_date(dta_provisoria_conclusao_realizada))
                            dta_provisoria_conclusao_realizada = data_conclusao_realizada
                    
                    # Count completed tasks
                    
                    if per_conclusao_items == 100.0:
                        nr_tarefas_concluidas += 1

                    nrcarat_seguinte += 1
                        
                Lin_proxima += 1
                if Lin_proxima <= len(self.get_children()):
                    dep_task_id = tasks_ids[Lin_proxima]
                    dep_sub_items = self.item(dep_task_id, 'values')
                    tarefa_id_reg_seg = dep_sub_items[1].zfill(2)
                    nrregistros = int(len(tarefa_id_reg_seg))

                linha += 1
            
                # Calcular o Percentual de Execução
                per_conclusao = (nr_tarefas_concluidas / nrcarat_seguinte) * 100 if nr_tarefas_concluidas > 0 else 0
            
            # per_conclusao = percentual_execucao
            
            
            if NrCaraceteres_Reg_Seg > nrcarat:
                if data_inicial_realizada and data_conclusao_realizada and per_conclusao >= 1:
                    entry_tempo_previsto = data_conclusao_realizada - data_inicial_realizada
                    entry_tempo_previsto = entry_tempo_previsto.days
                elif data_inicial_prevista and data_conclusao_prevista:
                    entry_tempo_previsto = data_conclusao_prevista - data_inicial_prevista
                    entry_tempo_previsto = entry_tempo_previsto.days
            
            # Lin += 1
            if data_inicial_prevista != '' and data_inicial_prevista is not None:
                data_inicial_prevista = data_inicial_prevista.strftime("%d/%m/%Y")
            else:
                data_inicial_prevista = ''

            if data_inicial_realizada != '' and data_inicial_realizada is not None:
                data_inicial_realizada = data_inicial_realizada.strftime("%d/%m/%Y")
            else:
                data_inicial_realizada = ''

            if data_conclusao_prevista != '' and data_conclusao_prevista is not None:    
                data_conclusao_prevista = data_conclusao_prevista.strftime("%d/%m/%Y")
            else:
                data_conclusao_prevista = ''

            if data_conclusao_realizada != '' and data_conclusao_realizada is not None:    
                data_conclusao_realizada = data_conclusao_realizada.strftime("%d/%m/%Y")
            else:
                data_conclusao_realizada = ''
            
            current_values = self.item(item_id).get('values')
            current_values[0] = NrCampos
            current_values[1] = tarefa_id.zfill(2)
            current_values[2] = entry_descricao
            current_values[3] = entry_responsavel
            current_values[4] = entry_dependencia
            current_values[5] = int(entry_tempo_espera)
            current_values[6] = int(entry_tempo_previsto)
            current_values[7] = f'{float(per_conclusao)/100:.2%}'
            current_values[8] = data_inicial_prevista
            current_values[9] = data_inicial_realizada
            current_values[10] = data_conclusao_prevista
            current_values[11] = data_conclusao_realizada
            self.item(item_id, values=current_values)
    
    def gravar_cronograma_tarefa(self, selected_iid):
        try:
            selected_item = self.item(selected_iid)
            projeto_ID = self.projeto_id
            projeto_DS = self.projeto_ds
            projeto_cr = 0
            tarefa_id = ""
            tarefa_DS = ""
            responsavel_nome = ""
            tarefa_dependencia = ""
            Tempo_Espera = 0
            Tempo_Previsto = 0
            data_inicial_Prevista = ""
            data_inicial_Realizada = ""
            dias_diferenca_inicio = 0
            data_Conclusao_Prevista = ""
            data_Conclusao_Realizada = ""
            prazo_fatal_dias = 0
            dias_diferenca_Conclusao = 0
            status_projeto = ""
            observacao = ""
            Anexos = ""
            percentual_execucao = ""

            # Assign values from the selected item (simulating UsrCronograma)
            tarefa_id = selected_item['values'][1]
            tarefa_DS = selected_item['values'][2].strip()
            responsavel_nome = selected_item['values'][3]
            tarefa_dependencia = selected_item['values'][4]
            Tempo_Espera = selected_item['values'][5]
            Tempo_Previsto = selected_item['values'][6]
            percentual_execucao = selected_item['values'][7]
            data_inicial_Prevista = datetime.strptime(
                selected_item['values'][8], "%d/%m/%Y")
            data_inicial_Realizada = datetime.strptime(
                selected_item['values'][9], "%d/%m/%Y") if selected_item['values'][9] else None
            data_Conclusao_Prevista = datetime.strptime(
                selected_item['values'][10], "%d/%m/%Y")
            data_Conclusao_Realizada = datetime.strptime(
                selected_item['values'][11], "%d/%m/%Y") if selected_item['values'][11] else None
            observacao = selected_item['values'][12]
            Anexos = ''

            # Calculate date differences
            dias_diferenca_inicio = (
                data_inicial_Realizada - data_inicial_Prevista).days if data_inicial_Realizada else 0
            prazo_fatal_dias = (datetime.now() - data_Conclusao_Prevista).days
            dias_diferenca_Conclusao = (
                data_Conclusao_Prevista - data_Conclusao_Realizada).days if data_Conclusao_Realizada else 0

            sql = """
                            UPDATE programas_atividades SET
                                projeto_DS = %s,
                                projeto_cr = %s,
                                tarefa_DS = %s,
                                responsavel_nome = %s,
                                tarefa_dependencia = %s,
                                tempo_espera = %s,
                                tempo_previsto = %s,
                                percentual_execucao = %s,
                                Data_inicial_prevista = %s,
                                Data_inicial_Realizada = %s,
                                dias_diferenca_inicio = %s,
                                data_conclusao_prevista = %s,
                                data_conclusao_realizada = %s,
                                prazo_fatal_dias = %s,
                                dias_diferenca = %s,
                                status = %s,
                                observacao = %s,
                                anexos = %s
                            WHERE projeto_ID = %s AND tarefa_ID = %s
                    """

            parameters = (
                projeto_DS,
                projeto_cr,
                tarefa_DS.replace("'", " "),
                responsavel_nome,
                tarefa_dependencia,
                Tempo_Espera,
                Tempo_Previsto,
                float(percentual_execucao.strip('%')) / 100,
                data_inicial_Prevista.strftime('%Y-%m-%d'),
                data_inicial_Realizada.strftime(
                    '%Y-%m-%d') if data_inicial_Realizada else '1899-12-30',
                dias_diferenca_inicio,
                data_Conclusao_Prevista.strftime('%Y-%m-%d'),
                data_Conclusao_Realizada.strftime(
                    '%Y-%m-%d') if data_Conclusao_Realizada else '1899-12-30',
                prazo_fatal_dias,
                dias_diferenca_Conclusao,
                status_projeto,
                observacao.replace("'", " "),
                Anexos,
                projeto_ID,
                tarefa_id
            )

            # Execute the SQL command
            db.executar_consulta(sql, parameters)
            # messagebox.showinfo("Sucesso", "Tarefa Alterada com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")
        finally:
            pass

    def base64_to_farois(self, icon_tpo):

        if icon_tpo == 'semafaro_azul':
            icon_base = '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'
        elif icon_tpo == 'semafaro_vermelho':
            icon_base = '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'
        elif icon_tpo == 'semafaro_verde':
            icon_base = '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'
        elif icon_tpo == 'semafaro_verde_conclusao':
            icon_base = 'iVBORw0KGgoAAAANSUhEUgAAAuQAAALkCAIAAADIxrcyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAP+lSURBVHhe7P1ZkyPJlif4/c9RVTPA19i3zIjc95v3Zt5bdesuXTVV0y3TUyIUsoUzD3zhl+AnqC/CB1I4DyNCPpAyPWx2l7RUTW13qbvmvkYusWRGZGy+ADAz1XP4oGYGONwjMiMzFrjH+QkSGQ4H4IDBYHpM9ehRUlUYY4wxxiwqnr/BGGOMMWaRWLBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYox94r0/9Idt5tHjXSX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'
        elif icon_tpo == 'semafaro_amarelo':
            icon_base = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAZmSURBVEhLRZZJk11HEUZPZg333Te0uluyBpAlYwIbYzlCAQ5YsfBf4NeyYMm0wLKNbQxClmQhWZJ7fN1vuENVJosngqj9ia8yo+o7UvzSicIEUHArIr0I0EB0x4RSyBHBzEyI5qAABiLgiKCMQk/NEBAAcd840SwVIwSCIBhUXDCDgDpeYEQqVggZEjVgwV08qClmhDAqRTyBguIubiMoohUcxFFDDNTwLfQMS2xLKPiAdXglz4kH2Ayfo5kYCl6pAYkEXHEwxIuDE8TBwIzoCCP9Ef0pmyPWx/3quO/Oa117tLSYtJNFjPvka7R3ad+iaV3iQBZiAjHBBd+hBaQaBRFlhA4/5/LJ6smXq9dPJ1JmOQYZJQwktuNQrbfNOoSD+eF9btzj4A7TG4VZJQWqmqhFHLHRJYAUs07VYM321eb44cl/vtgP/SIr3bqsLmNy4rjenAQtWvtxe1rHnNt3w+H76fZ93v4YuVmZK4aLeMCRzj1CwPAeNqxfrI+/uTx6dKUpcdzEYdxcLJN4fuc6ubt89KCcPd/LFmqxKqO2K93n2geLu7/Nb31CfpuQHfAq4lqh94EyYpXubDh62l18P0kmooSZXHt3dvcjmV/jsvhF7WsKjDqsGDaqQzO5bOX5ePbp5fM/sX5Md4QXAaMWTB1TAYV+xemzi6N/788kRLF4kK5/wP5PmdySK3e6dGMjt/dv3Gtne26DS8SNcTnNq4N0HFZfXj75PeO/sDUOkotFBU8I3jOe+fpFm9fu69Dk6bU7LG6TD0pcjJP9fHhn9uP78e7HIcw1Bo/uocKAbBtWM459/fnww1/gCB8BUVXdDbqu2b7sVo+atCps4nRKc4U4J01K09bckPeItwg3JR2QszdjTZ1HB8VDYpTx24vjPzN+i53q7n0kAhTsku0PVs5g47XkyRzJkIghTUJslABV2VQPsUb1XDwXDxAUVbS2cWPDC1bfoksxV9AA1AHtbDjJCawGEmmOqXUd3YX3Zz6ei60JPXGsWjwWspHNM0SIRvDY5CbJ5elTdImdRVDDkAHp+vE0teZ2Ib6inNK/LJuntn5i2+d1+9LqCXKJrAiDR/NYNVZSICoRkrkQY9iuTmALI6AjFQXZ9nWJLN1+qOMTLj7z7oFvH+jwj2xPor0SO0KO4YzUSyohFkmIKkGJleRV1UXVdx9ooKIOoFgt3pV6Xvx47J9tzr+qq89s/cA2X9XNw7F/Wssr6hmsidWjSTRRVBxxAq5OxgIhNRiQcLQtCW8wnV5ZrMpS0ibLcmIvY33clEfeP67l2VCf1fIa6bFStdBIBVHIihhBJankGqZSQ0AbJOMoDh7IC8mTGgtpm3OnYUn/Uvx1kKMUz5p8nvIJeoyc19h5QFMiJNQIoAGNHumrzfbegsmuKZQAAjpPkwOSWBqZ9ISBRiUJuq52XMvLzeaRnX+2Pf9cdKnJRSdIQiEJuSVNquaR3F59l7EFfXNwoI3TW7m9SVpYapgEkpONWEMqTeOziWlb2rnE5CEFj3iAbEydmdK0g+5P5j9hegf2ICFoheLAjPbuZHZP4s9KuOp5SnJSJSE5Tdqp5gXhCs1+DJnk2lRpBxaFRaHtt0kt3l4c/hJuoQdUAHUwjzCF66n5MDU/N70+xpZpZKZMAhHHrD/n4rt69pgwWDDPgWmilZq1i6HTeZrd08V9/ABJVUCR3t0LTQBfYd9Rvhi2f7D69xS+D3HDsCvt0Yqo7JVx1DyACROJ4jIOnqrexO9PJ7+j+TX1kJCcDZh07grREXd0CU/Z/HEon4p8k/KJ1ZVKjxhmaKJWglIF5khbPBQ/jM17Mf0GPoF33BIKbJ1BRq+g6juz6GGJf488Hrd/df3a4j81HEcRpcGyFddkXmutbbVDlbspfkT8FbwPN2GvouxQghTvQAVVAm4wYivkCHto8vWofzNeCDUQ8AbzMq5Vc9B91duq7yEfwi/gBqRKhP8tEMT8EsTJSsJBCrtSp4NjeDjWF2M997pxDKvT1IrOJPwIuQlvw1WYQ+uo7cCUnYi8QQsZwhvfoodd+fRwCuewgg6GN2bEHK7CPr4HESkOvIm8SwaYuI/gYI6KJwDpwfo+BtEYB7SHLVQQiNDgCc94wnEFXYPDXBxkBNulFPedNo0Q3CLg2gku3r65nxTowfAGTyA4OA44RJALKMIh/0c3OP8FSlq9fv89QRMAAAAASUVORK5CYII='

        # Corrigindo padding se necessário
        missing_padding = len(icon_base) % 4
        if missing_padding:
            icon_base += '=' * (4 - missing_padding)

        try:
            # Decodifica a imagem
            image_data = base64.b64decode(icon_base)
            image = Image.open(io.BytesIO(image_data))
            # original_image = Image.open(icon_path)
            # Redimensionando para 32x32 pixels
            resized_image = image.resize((18, 18), Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print(f"Erro ao decodificar a imagem: {e}")
            return None  # Retorna None ou tratamento de erro apropriado
