from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Resumo_Estudos(Widgets):
    def resumo_estudos(self):
        self.window_one.title('Resumo Estudos de Negócios')
        self.clearFrame_principal()
        self.frame_parametros(self.principal_frame)
        
################# dividindo a janela ###############
    def frame_parametros(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.34
        coordenadas_relheight = 0.07
        self.frame_empresa(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_uf))

        # Estado
        coordenadas_relx = 0.35
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        self.frame_uf(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_municipio))

        # Municipio
        coordenadas_relx = 0.415
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        self.frame_municipio(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_status))

        # Status
        coordenadas_relx = 0.62
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.28
        coordenadas_relheight = 0.07
        self.fram_status(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)

        def consultar():
            if self.combo_empresa.get() != '':
                ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            UF = self.combo_uf.get()
            Cidade = self.combo_municipio.get()
            Status = self.combo_status.get()
            lista = self.Consulta_Negocios(ID_Empresa, UF, Cidade, Status)
            
            self.fr_list_estudosnegocios = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
            self.fr_list_estudosnegocios.place(relx=0.005, rely=0.09, relwidth=0.986, relheight=0.87)
            
            self.scrollbar_estudos = ttk.Scrollbar(self.fr_list_estudosnegocios, orient='vertical')
            self.scrollbar_estudos.pack(side='right', fill='y')
            
            # Widgets - Listar
            self.list_g = ttk.Treeview(self.fr_list_estudosnegocios, height=12,
                                       columns=("Cadastro", "Usuário", "Status", "Tipo", "Cenário",
                                                "Cidade", "UF", "VGV-Bruto", "Com.Venda", "Com.Neg.", "Impostos", "VGV- Líq.", "Permutante",
                                                "VGV - Urban.", "Terreno", "Custos", "$ M.O.", "% M.O.", "Mult.", "Exp.Max.", "T.I.R. (a.a.)"), 
                                                show='headings', selectmode='browse')
            self.list_g.pack(side='left', fill='both', expand=1)            
            
            # Definindo cores
            bg_color = '#FFFFFF'  # Fundo branco
            text_color = '#000000'  # Texto preto
            selected_color = '#0078d7'  # Azul para selecionados

            treestyle = ttk.Style()
            treestyle.theme_use('default')
            treestyle.configure("Treeview", background=bg_color,foreground=text_color, fieldbackground=bg_color, borderwidth=0)
            treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
            
            
            # Configurando as headings e a largura das colunas
            column_widths = {
                "Cadastro": 60,
                "Usuário": 30,
                "Status": 80,
                "Tipo": 120,
                "Cenário": 120,
                "Cidade": 80,
                "UF": 30,
                "VGV-Bruto": 80,
                "Com.Venda": 80,
                "Com.Neg.": 80,
                "Impostos": 80,
                "VGV- Líq.": 80,
                "Permutante": 80,
                "VGV - Urban.": 80,
                "Terreno": 80,
                "Custos": 80,
                "$ M.O.": 80,
                "% M.O.": 50,
                "Mult.": 50,
                "Exp.Max.": 80,
                "T.I.R. (a.a.)": 50,
            }

            for col in self.list_g['columns']:
                self.list_g.heading(col, text=col)
                if col == 'Usuário' or col == 'Status' or col == 'Tipo' or col == 'Cenário' or col == 'Cidade':
                    # Alinhamento centralizado
                    self.list_g.column(col, width=column_widths[col], anchor='w')
                elif col == 'VGV-Bruto' or col == 'Com.Venda' or col == 'Com.Neg' or col == 'Impostos' or col == 'VGV-Líq.':
                    # Alinhamento centralizado
                    self.list_g.column( col, width=column_widths[col], anchor='e')
                elif col == 'Permutante' or col == 'VGV-Urban.' or col == 'Terreno' or col == 'Custos' or col == '$ M.O.':
                    # Alinhamento centralizado
                    self.list_g.column(col, width=column_widths[col], anchor='e')
                elif col == '% M.O.' or col == 'Mult.' or col == 'Exp.Max.' or col == 'T.I.R. (a.a.)':
                    # Alinhamento centralizado
                    self.list_g.column(col, width=column_widths[col], anchor='e')
                else:
                    # Alinhamento centralizado
                    self.list_g.column(col, width=column_widths[col], anchor='center')

            self.list_g.pack(pady=10)
            
            self.list_g.place(relx=0.005, rely=0.01, relwidth=0.985, relheight=0.985)

            # Limpa a lista atual antes de inserir novos resultados
            self.list_g.delete(*self.list_g.get_children())

            for item in lista:
                Dta_Registro = item.get('Dta_Registro')
                
                if Dta_Registro is not None:
                    data_formatada = Dta_Registro.strftime('%d/%m/%Y')
                else:
                    data_formatada = ''  # Valor padrão ou outro tratamento de erro
                
                formatted_item = (
                    data_formatada,
                    item.get('Usr_Registro'),
                    item.get('Status_Prospeccao'),
                    item.get('Tipo'),
                    item.get('Nome_da_Area'),
                    item.get('Cidade'),
                    item.get('UF'),
                    item.get('VGV_Total'),
                    item.get('Comissao_Vendas'),
                    item.get('Comissao_Negocio'),
                    item.get('Impostos'),
                    item.get('VGV_Liquido'),
                    item.get('Repasse_Parceiro'),
                    item.get('Receita_Liquida'),
                    item.get('Terreno'),
                    item.get('TotalGastos'),
                    item.get('Margem_Valor'),
                    item.get('Margem_Percent'),
                    item.get('Multiplicador'),
                    item.get('Vlr_Exposicao_Maxima'),
                    item.get('Tir_Urbanizadora')
                )
                self.list_g.insert('', 'end', values=formatted_item)

            self.list_g.tag_configure('odd', background='#eee')
            self.list_g.tag_configure('even', background='#ddd')
            self.list_g.configure(yscrollcommand=self.scrollbar_estudos.set)
            self.scrollbar_estudos.configure(command=self.list_g.yview)

            def selected_simulador():
                selected_item = self.list_g.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.list_g.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.list_g.item(selected_item, 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
                    DS_Empresa = self.combo_empresa.get()
                    UF = values[6]
                    Cidade = values[5]
                    Tipo = values[3]
                    Nome_da_Area = values[4]
                    self.simulador_estudos_rel(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)

            def selected_fluxo():
                selected_item = self.list_g.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.list_g.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.list_g.item(selected_item, 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
                    DS_Empresa = self.combo_empresa.get()
                    UF = values[6]
                    Cidade = values[5]
                    Tipo = values[3]
                    Nome_da_Area = values[4]
                    self.fluxo_projetado(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)

            def selected_maps():
                selected_item = self.list_g.selection()
                if selected_item:
                    # Texto do item selecionado
                    item_text = self.list_g.item(self.list_g.selection(), 'text')
                    # Obtém os valores associados (como uma tupla)
                    values = self.list_g.item(self.list_g.selection(), 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
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
                # self.list_g.delete(row_id)
                messagebox.showinfo("Informação", "Em Manutenção!!")

            def selected_pesquisa():
                selected_item = self.list_g.selection()
                if selected_item:
                    # Get the text of the selected item
                    item_text = self.list_g.item(selected_item, 'text')
                    # Get associated values as a tuple
                    values = self.list_g.item(selected_item, 'values')
                    
                    ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
                    DS_Empresa = self.combo_empresa.get()
                    UF = values[6]
                    Cidade = values[5]
                    Tipo = values[3]
                    Nome_da_Area = values[4]
                    self.pesquisa_mercado(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)
                
            def selected_enviar_email():
                messagebox.showinfo("Informação", "Em Manutenção!!")
            
            def selected_enviar_whatsapp():
                messagebox.showinfo("Informação", "Em Manutenção!!")

            def postPopUpMenu(event):
                row_id = self.list_g.identify_row(event.y)
                if row_id:  # Realiza a verificação se a linha existe.
                    self.list_g.selection_set(row_id)
                    row_values = self.list_g.item(row_id)['values']
                    # print(row_values)
                    
                    postPopUpMenu = tk.Menu(self.list_g, tearoff=0, font=('Verdana', 11))
                    
                    postPopUpMenu.add_command(label='Simulador', accelerator='Ctrl+S', command= selected_simulador)
                    postPopUpMenu.add_command(label='Fluxo Projetado', accelerator='Ctrl+F', command=selected_fluxo)
                    postPopUpMenu.add_command(label='Maps', accelerator='Ctrl+M', command=selected_maps)
                    postPopUpMenu.add_command(label='Pesquisas', accelerator='Ctrl+P', command=selected_pesquisa)
                    postPopUpMenu.add_separator()
                    postPopUpMenu.add_command(label='Enviar Maps Email', accelerator='Alt+E', command=selected_enviar_email)
                    postPopUpMenu.add_command(label='Enviar Maps WhatsApp', accelerator='Alt+W', command=selected_enviar_whatsapp)
                    postPopUpMenu.add_separator()
                    postPopUpMenu.add_command(label='Excluir Estudo', accelerator='Delete', command=selected_excluir)
                    postPopUpMenu.post(event.x_root, event.y_root)
            
            self.list_g.bind("<Double-1>", postPopUpMenu)  # 'Double-1' é o duplo clique do mouse
            self.list_g.bind("<Button-3>", postPopUpMenu)  # 'Button-3' é o clique direito do mouse
            self.list_g.bind('<Control-s>', lambda event: selected_simulador() if self.list_g.selection() else None)
            self.list_g.bind('<Control-f>', lambda event: selected_fluxo() if self.list_g.selection() else None)
            self.list_g.bind('<Control-m>', lambda event: selected_maps() if self.list_g.selection() else None)
            self.list_g.bind('<Control-p>', lambda event: selected_pesquisa() if self.list_g.selection() else None)
            self.list_g.bind('<Alt-e>', lambda event: selected_enviar_email() if self.list_g.selection() else None)
            self.list_g.bind('<Alt-w>', lambda event: selected_enviar_whatsapp() if self.list_g.selection() else None)
            self.list_g.bind('<Delete>', lambda event: selected_excluir() if self.list_g.selection() else None)

        # Botão de Consultar
        icon_image = self.base64_to_photoimage('lupa')
        self.btn_consultar = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=consultar)
        self.btn_consultar.pack(pady=10)
        self.btn_consultar.place(relx=0.905, rely=0.02, relwidth=0.04, relheight=0.05)

        # Botão Incluir Novo Estudo
        def novo_estudo():
            if self.combo_empresa.get() != '':
                ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), janela)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            DS_Empresa = self.combo_empresa.get()
            UF = self.combo_uf.get()
            Cidade = self.combo_municipio.get()
            Status = self.combo_status.get()
            Tipo = ''
            Nome_da_Area = ''

            
            self.simulador_estudos_rel(ID_Empresa, DS_Empresa, UF, Cidade, Tipo, Nome_da_Area)
            
        icon_image = self.base64_to_photoimage('open_book')
        self.btn_novo_estudo = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=novo_estudo)
        self.btn_novo_estudo.pack(pady=10)
        self.btn_novo_estudo.place(relx=0.95, rely=0.02, relwidth=0.04, relheight=0.05)

Resumo_Estudos()
