from imports import *
from widgets import Widgets
from Lx.tela_opcoes import Opcoes_Modulos
from datetime import datetime


################# criando janela ###############
class Resumo_Estudos(Widgets, Opcoes_Modulos):
    def resumo_estudos(self):
        self.window_one.title('Resumo Estudos de Negócios')
        self.clearFrame_principal()
        self.frame_parametros(self.principal_frame)
        
        
################# dividindo a janela ###############
    def frame_parametros(self, janela):
        # Empresa
        coordenadas_relx = 0
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.34
        coordenadas_relheight = 0.07
        self.frame_empresa(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_uf))

        # Estado
        coordenadas_relx = 0.34
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.06
        coordenadas_relheight = 0.07
        self.frame_uf(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_uf.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_municipio))

        # Municipio
        coordenadas_relx = 0.40
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        self.frame_municipio(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_municipio.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_status))

        # Status
        coordenadas_relx = 0.60
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        self.fram_status(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)

        def consultar():
            if self.combo_empresa.get() != '':
                ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            UF = self.combo_uf.get()
            Cidade = self.combo_municipio.get()
            Status = self.combo_status.get()
            lista = self.Consulta_Negocios(ID_Empresa, UF, Cidade, Status)

            # Widgets - Listar
            self.list_g = ttk.Treeview(janela, height=12,
                                       columns=("Cadastro", "Usuário", "Status", "Tipo", "Cenário",
                                                "Cidade", "UF", "VGV-Bruto", "Com.Venda", "Com.Neg.", "Impostos", "VGV- Líq.", "Permutante",
                                                "VGV - Urban.", "Terreno", "Custos", "$ M.O.", "% M.O.", "Mult.", "Exp.Max.", "T.I.R. (a.a.)"), show='headings')

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

            # scrollbar vertical
            vsb = ttk.Scrollbar(self.list_g, orient="vertical", command=self.list_g.yview)
            # scrollbar horizontal
            hsb = ttk.Scrollbar(
                self.list_g, orient="horizontal", command=self.list_g.xview)
            self.list_g.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            self.list_g.grid(column=0, row=0, sticky="nsew")
            vsb.place(relx=1, rely=0.12)
            hsb.place(relx=0, rely=1)

            self.list_g.place(relx=0, rely=0.12, relwidth=1, relheight=0.87)

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

            self.list_g.bind("<Double-1>", self.opcoes_modulos)

        # Botão de Consultar
        self.btn_consultar = customtkinter.CTkButton(janela, text='Consultar', command=consultar)
        self.btn_consultar.pack(pady=10)
        self.btn_consultar.place(relx=0.87, rely=0.02, relwidth=0.05, relheight=0.05)

        # Botão Incluir Novo Estudo
        def novo_estudo():
            if self.combo_empresa.get() != '':
                ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            UF = self.combo_uf.get()
            Cidade = self.combo_municipio.get()
            Status = self.combo_status.get()
            Tipo = ''
            Nome_da_Area = ''

            
            self.simulador_estudos_rel(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)

        self.btn_consultar = customtkinter.CTkButton(janela, text='Novo', command=novo_estudo)
        self.btn_consultar.pack(pady=10)
        self.btn_consultar.place(relx=0.93, rely=0.02, relwidth=0.05, relheight=0.05)

        

Resumo_Estudos()
