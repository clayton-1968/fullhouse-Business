from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Pesquisa_Anexos(Widgets):

    def pesquisa_anexos(self, projeto_id, tarefa_id):
        self.janela_documentos_anexos = customtkinter.CTkToplevel(self.window_one)
        self.janela_documentos_anexos.title('Relatório de Documentos Anexados')
        width = self.janela_documentos_anexos.winfo_screenwidth()
        height = self.janela_documentos_anexos.winfo_screenheight()
        self.janela_documentos_anexos.geometry(f"{width}x{height}+0+0")
        self.janela_documentos_anexos.resizable(True, True)
        self.janela_documentos_anexos.lift()  # Traz a janela para frente
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_documentos_anexos.protocol("WM_DELETE_WINDOW", self.on_closing_tela_documentos_anexos)

        self.frame_list_pesquisa_anexos(self.janela_documentos_anexos)
        self.frame_carregar_dados_anexos(projeto_id, tarefa_id)

        self.janela_documentos_anexos.focus_force()
        self.janela_documentos_anexos.grab_set()

################# dividindo a janela ###############
    def frame_list_pesquisa_anexos(self, janela):
        # Listbox _ Informações Pesquisa
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.001,relwidth=0.985, relheight=0.985)
        
        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')
        
        
        # Widgets - Listar Parcelas
        self.LPesquisa_Anexos = ttk.Treeview(self.fr_list, height=7, column=(
                                                                                'projeto',
                                                                                'tarefa',
                                                                                'anexo',
                                                                                'doc'
                                                                            ), show='headings')  # , show='headings'

        self.LPesquisa_Anexos.heading('#0', text='#', anchor='center')
        self.LPesquisa_Anexos.heading('#1', text='Projeto', anchor='center')
        self.LPesquisa_Anexos.heading('#2', text='Tarefa', anchor='center')
        self.LPesquisa_Anexos.heading('#3', text='Anexo', anchor='center')
        self.LPesquisa_Anexos.heading('#4', text='Documento', anchor='center')

        self.LPesquisa_Anexos.column('#0', width=2, anchor='w')
        self.LPesquisa_Anexos.column('projeto', width=2, anchor='w')
        self.LPesquisa_Anexos.column('tarefa', width=2, anchor='w')
        self.LPesquisa_Anexos.column('anexo', width=10, anchor='w')
        self.LPesquisa_Anexos.column('doc', width=1000, anchor='w')

        self.LPesquisa_Anexos.pack(expand=True, fill='both')
        self.LPesquisa_Anexos.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)
        

        def selectec_abrir():
            selected_item = self.LPesquisa_Anexos.selection()
            if selected_item:
                values = self.LPesquisa_Anexos.item(self.LPesquisa_Anexos.selection(), 'values')
                projeto_id = values[0]
                tarefa_id = values[1]
                anexo_id = values[2]
                doc_num_documento = values[3]
                self.upload_arquivo_cronograma(projeto_id, tarefa_id, anexo_id, doc_num_documento)
            else:
                messagebox.showwarning("Anexo", "Selecionar uma linha de documento!!!", parent=self.janela_documentos_anexos)
                return

        def selected_excluir():
            selected_item = self.LPesquisa_Anexos.selection()
            if selected_item:
                values = self.LPesquisa_Anexos.item(self.LPesquisa_Anexos.selection(), 'values')
                self.row_id = selected_item[0]
                projeto_id = values[0]
                
            conditions = []  # Lista para armazenar as condições
            conditions.append('Projeto_ID = %s')
            params = [projeto_id]
            

            if messagebox.askyesno("Confirmar", "Tem Certeza que deseja Excluir?"):
                strSql = f"""DELETE 
                         FROM TB_Gedoc_Tarefas
                         WHERE {' AND '.join(conditions)}"""

                results = db.executar_consulta(strSql, params)
                self.LPesquisa_Anexos.delete(self.row_id)

            else:
                pass

        def postPopUpMenu(event):
            self.row_id = self.LPesquisa_Anexos.identify_row(event.y)
            if self.row_id:  # Realiza a verificação se a linha existe.
                self.LPesquisa_Anexos.selection_set(self.row_id)
                row_values = self.LPesquisa_Anexos.item(self.row_id)['values']
                # print(row_values)
                postPopUpMenu = tk.Menu(
                    self.LPesquisa_Anexos, tearoff=0, font=('Verdana', 11))
                postPopUpMenu.add_command(
                    label='Abrir Anexo', accelerator='Ctrl+M', command=selectec_abrir)
                postPopUpMenu.add_separator()
                postPopUpMenu.add_command(
                    label='Excluir Anexo', accelerator='Delete', command=selected_excluir)
                postPopUpMenu.post(event.x_root, event.y_root)

        # 'Double-1' é o duplo clique do mouse
        self.LPesquisa_Anexos.bind("<Double-1>", postPopUpMenu)
        # 'Button-3' é o clique direito do mouse
        self.LPesquisa_Anexos.bind("<Button-3>", postPopUpMenu)
        self.LPesquisa_Anexos.bind(
            '<Control-m>', lambda event: selectec_abrir() if self.list_g.selection() else None)
        self.LPesquisa_Anexos.bind(
            '<Delete>', lambda event: selected_excluir() if self.list_g.selection() else None)

    def frame_carregar_dados_anexos(self, projeto_id, tarefa_id):
        self.consultar_pesquisa_anexos(projeto_id, tarefa_id)

    def consultar_pesquisa_anexos(self, projeto_id, tarefa_id):
        try:
            conditions = []  
            conditions.append('Projeto_ID = %s')
            params = [projeto_id]
            conditions.append('Tarefa_ID = %s')
            params.append(tarefa_id)

            sql_query = f"""
                            SELECT 
                                Empresa_ID          AS Empresa, 
                                Projeto_ID          AS Projeto, 
                                Tarefa_ID           AS Tarefa, 
                                ID_Anexo            AS Anexo, 
                                Doc_Num_Documento   AS Doc 
                            FROM 
                                TB_Gedoc_Tarefas 
                            WHERE {' AND '.join(conditions)}
                        """

            # Execute the SQL query
            results = db.executar_consulta(sql_query, params)
            
            if not results:
                messagebox.showinfo("Info", "Documentos Não Cadastrado!", parent=self.principal_frame)
                return

            # Initialize the user annexes dialog
            for row in results:
                self.LPesquisa_Anexos.insert('', 'end',
                                                values=(
                                                    row['Projeto'],
                                                    row['Tarefa'],
                                                    row['Anexo'],
                                                    row['Doc']
                                                )
                                                )

            self.LPesquisa_Anexos.tag_configure('odd', background='#eee')
            self.LPesquisa_Anexos.tag_configure('even', background='#ddd')
            self.LPesquisa_Anexos.configure(yscrollcommand=self.scrollbar.set)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro! {str(e)}", self.principal_frame)

    def upload_arquivo_cronograma(self, projeto_id, tarefa_id, anexo_id, doc_num_documento):

        try:
            conditions = []  
            conditions.append('Projeto_ID = %s')
            params = [projeto_id]
            conditions.append('Tarefa_ID = %s')
            params.append(tarefa_id)
            conditions.append('ID_Anexo = %s')
            params.append(anexo_id)
            # Prepare SQL query
            sql_query = f"""
                            SELECT 
                                Empresa_ID          AS Empresa_ID, 
                                Projeto_ID          AS Projeto_ID, 
                                Tarefa_ID           AS Tarefa_ID, 
                                Doc_Num_Documento   AS Doc_Num_Documento, 
                                BinarioPDF          AS pdf
                            FROM TB_Gedoc_Tarefas 
                            WHERE {' AND '.join(conditions)} 
                        """
            
            record = db.executar_consulta(sql_query, params)
            if record is None:
                messagebox.showinfo("Info", "Documentos Não Cadastrado!", parent=self.principal_frame)
                return
            b64_data = record[0]['pdf']
            if b64_data is not None:
                file_path = os.path.join(os.getcwd(), doc_num_documento)
                with open(file_path, 'wb') as file:
                    file.write(b64_data)  # Write the binary data to a file

                messagebox.showinfo("Sucesso", "Documento Baixado com sucesso!!!.", parent=self.principal_frame)
            else:
                messagebox.showinfo(
                    "Informações", "Nenhum documento encontrado!!!.", parent=self.principal_frame)

        except Exception as e:
            messagebox.showerror("Error", f"Erro ocorrido: {str(e)}", parent=self.principal_frame)

Pesquisa_Anexos()

class Pesquisa_Anexos_Simulador(Widgets):

    def pesquisa_anexos_simulador(self, ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        self.janela_simulador_anexos = customtkinter.CTkToplevel(self.window_one)
        self.janela_simulador_anexos.title('Relatório de Documentos Anexados')
        width = self.janela_simulador_anexos.winfo_screenwidth()
        height = self.janela_simulador_anexos.winfo_screenheight()
        self.janela_simulador_anexos.geometry(f"{width}x{height}+0+0")
        self.janela_simulador_anexos.resizable(True, True)
        self.janela_simulador_anexos.lift()  # Traz a janela para frente
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.janela_simulador_anexos.protocol("WM_DELETE_WINDOW", self.on_closing_tela_simulador_anexos)

        self.frame_list_pesquisa_anexos_simulador(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area, self.janela_simulador_anexos)
        self.consultar_pesquisa_anexos_simulador(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)
        # self.frame_carregar_dados_anexos(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)

        self.janela_simulador_anexos.focus_force()
        self.janela_simulador_anexos.grab_set()

################# dividindo a janela ###############
    def frame_list_pesquisa_anexos_simulador(self, ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area, janela):
        # Listbox _ Informações Pesquisa
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
        
        self.fr_list = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        self.fr_list.place(relx=0.005, rely=0.001,relwidth=0.985, relheight=0.985)
        
        self.scrollbar = ttk.Scrollbar(self.fr_list, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')
        
        
        # Widgets - Listar Parcelas
        self.LPesquisa_Anexos_Simulador = ttk.Treeview(self.fr_list, height=7, column=(
                                                                                'ID',
                                                                                'doc'
                                                                            ), show='headings')  # , show='headings'

        self.LPesquisa_Anexos_Simulador.heading('#0', text='#', anchor='center')
        self.LPesquisa_Anexos_Simulador.heading('#1', text='ID', anchor='center')
        self.LPesquisa_Anexos_Simulador.heading('#2', text='Documento', anchor='center')
        
        self.LPesquisa_Anexos_Simulador.column('#0', width=2, anchor='w')
        self.LPesquisa_Anexos_Simulador.column('ID', width=2, anchor='w')
        self.LPesquisa_Anexos_Simulador.column('doc', width=1000, anchor='w')

        self.LPesquisa_Anexos_Simulador.pack(expand=True, fill='both')
        self.LPesquisa_Anexos_Simulador.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)
        

        def selectec_abrir():
            selected_item = self.LPesquisa_Anexos_Simulador.selection()
            if selected_item:
                values = self.LPesquisa_Anexos_Simulador.item(self.LPesquisa_Anexos_Simulador.selection(), 'values')
                anexo_id = values[0]
                doc_num_documento = values[1]
                
                self.upload_arquivo_simulador(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area, anexo_id, doc_num_documento)
            else:
                messagebox.showwarning("Anexo", "Selecionar uma linha de documento!!!", parent=self.janela_simulador_anexos)
                return

        def selected_excluir():
            selected_item = self.LPesquisa_Anexos.selection()
            if selected_item:
                values = self.LPesquisa_Anexos.item(self.LPesquisa_Anexos.selection(), 'values')
                self.row_id = selected_item[0]
                anexo_id = values[0]
                doc_num_documento = values[1]
                
            conditions = []  
            conditions.append('Empresa_ID = %s')
            params = [ID_Empresa]

            conditions.append('UF = %s')
            params.append(UF)

            conditions.append('Cidade = %s')
            params.append(Cidade)

            conditions.append('Tipo_Estudo = %s')
            params.append(Tipo)

            conditions.append('Nome_Area = %s')
            params.append(Nome_da_Area)

            conditions.append('ID_Anexo = %s')
            params.append(anexo_id)

            conditions.append('Doc_Num_Documento = %s')
            params.append(doc_num_documento)
            
            if messagebox.askyesno("Confirmar", "Tem Certeza que deseja Excluir?"):
                strSql = f"""DELETE 
                         FROM TB_Gedoc
                         WHERE {' AND '.join(conditions)}"""

                results = db.executar_consulta(strSql, params)
                self.LPesquisa_Anexos_Simulador.delete(self.row_id)

            else:
                pass

        def postPopUpMenu(event):
            self.row_id = self.LPesquisa_Anexos_Simulador.identify_row(event.y)
            if self.row_id:  # Realiza a verificação se a linha existe.
                self.LPesquisa_Anexos_Simulador.selection_set(self.row_id)
                row_values = self.LPesquisa_Anexos_Simulador.item(self.row_id)['values']
                # print(row_values)
                postPopUpMenu = tk.Menu(
                    self.LPesquisa_Anexos_Simulador, tearoff=0, font=('Verdana', 11))
                postPopUpMenu.add_command(
                    label='Abrir Anexo', accelerator='Ctrl+M', command=selectec_abrir)
                postPopUpMenu.add_separator()
                postPopUpMenu.add_command(
                    label='Excluir Anexo', accelerator='Delete', command=selected_excluir)
                postPopUpMenu.post(event.x_root, event.y_root)

        # 'Double-1' é o duplo clique do mouse
        self.LPesquisa_Anexos_Simulador.bind("<Double-1>", postPopUpMenu)
        # 'Button-3' é o clique direito do mouse
        self.LPesquisa_Anexos_Simulador.bind("<Button-3>", postPopUpMenu)
        self.LPesquisa_Anexos_Simulador.bind(
            '<Control-m>', lambda event: selectec_abrir() if self.list_g.selection() else None)
        self.LPesquisa_Anexos_Simulador.bind(
            '<Delete>', lambda event: selected_excluir() if self.list_g.selection() else None)

    def consultar_pesquisa_anexos_simulador(self, ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        try:
            conditions = []  
            conditions.append('Empresa_ID = %s')
            params = [ID_Empresa]

            conditions.append('UF = %s')
            params.append(UF)

            conditions.append('Cidade = %s')
            params.append(Cidade)

            conditions.append('Tipo_Estudo = %s')
            params.append(Tipo)

            conditions.append('Nome_Area = %s')
            params.append(Nome_da_Area)

            
            sql_query = f"""
                            SELECT
                                ID_Anexo,
                                Empresa_ID,
                                UF,
                                Cidade,
                                Tipo_Estudo,
                                Nome_Area,
                                Doc_Num_Documento,
                                BinarioPDF
                            FROM
                                TB_Gedoc
                            WHERE {' AND '.join(conditions)}
                        """

            # Execute the SQL query
            results = db.executar_consulta(sql_query, params)
            
            if not results:
                messagebox.showinfo("Info", "Documentos Não Cadastrado!", parent=self.janela_simulador_anexos)
                return

            # Initialize the user annexes dialog
            for row in results:
                self.LPesquisa_Anexos_Simulador.insert('', 'end',
                                                values=(
                                                    row['ID_Anexo'],
                                                    row['Doc_Num_Documento']
                                                    )
                                                )

            self.LPesquisa_Anexos_Simulador.tag_configure('odd', background='#eee')
            self.LPesquisa_Anexos_Simulador.tag_configure('even', background='#ddd')
            self.LPesquisa_Anexos_Simulador.configure(yscrollcommand=self.scrollbar.set)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro! {str(e)}", parent=self.janela_simulador_anexos)

    def upload_arquivo_simulador(self, empresa_id, uf, cidade, tipo_estudo, nome_estudo, anexo_id, doc_num_documento):
        try:
            conditions = []  
            conditions.append('Empresa_ID = %s')
            params = [empresa_id]

            conditions.append('UF = %s')
            params.append(uf)

            conditions.append('Cidade = %s')
            params.append(cidade)

            conditions.append('Tipo_Estudo = %s')
            params.append(tipo_estudo)

            conditions.append('Nome_Area = %s')
            params.append(nome_estudo)

            conditions.append('ID_Anexo = %s')
            params.append(anexo_id)

            conditions.append('Doc_Num_Documento = %s')
            params.append(doc_num_documento)

            
            
            # Prepare SQL query
            sql_query = f"""
                            SELECT
                                ID_Anexo            AS id_anexo,
                                Empresa_ID          AS empresa_id,
                                UF                  AS uf,
                                Cidade              AS cidade,
                                Tipo_Estudo         AS tipo_estudo,
                                Nome_Area           AS nome_area,
                                Doc_Num_Documento   AS doc_num_documento,
                                BinarioPDF          AS pdf
                            FROM
                                TB_Gedoc
                            WHERE {' AND '.join(conditions)} 
                        """
            
            record = db.executar_consulta(sql_query, params)
            if record is None:
                messagebox.showinfo("Info", "Documentos Não Cadastrado!", parent=self.janela_simulador_anexos)
                return
            b64_data = record[0]['pdf']
            if b64_data is not None:
                file_path = os.path.join(os.getcwd(), doc_num_documento)
                with open(file_path, 'wb') as file:
                    file.write(b64_data)  # Write the binary data to a file

                messagebox.showinfo("Sucesso", "Documento Baixado com sucesso!!!.", parent=self.janela_simulador_anexos)
            else:
                messagebox.showinfo(
                    "Informações", "Nenhum documento encontrado!!!.", parent=self.janela_simulador_anexos)

        except Exception as e:
            messagebox.showerror("Error", f"Erro ocorrido: {str(e)}", parent=self.janela_simulador_anexos)

Pesquisa_Anexos()