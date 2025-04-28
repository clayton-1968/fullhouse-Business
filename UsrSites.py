from imports import *
from widgets import Widgets
from PIL import ImageTk, Image

class Sites_rel(Widgets):

    def sites(self):
        self.images_base64()
        
        self.window_one.title('Sites Cadastrados')
        self.clearFrame_principal()
        
        # Iniciar variáveis do Formulário
        
        self.linha1_cabecalho(self.principal_frame)
        self.linha2_lista(self.principal_frame)
        
    def linha1_cabecalho(self, janela):
        # Empresa
        coordenadas_relx = 0.01
        coordenadas_rely = 0.02
        coordenadas_relwidth = 0.38
        coordenadas_relheight = 0.09
        self.frame_empresa(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tipo_site_descr))

        # Tipo site
        fr_tipo_site = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_tipo_site.place(relx=0.395, rely=0.02, relwidth=0.10, relheight=0.09)

        lb_tipo_site = customtkinter.CTkLabel(fr_tipo_site, text="Tipo Site")
        lb_tipo_site.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)
        
        self.opcoes = ['Todos', 'Leis Federais', 'Leis Municipais', 'T.I.', 'Curiosidades', 'Outros']
        self.entry_tipo_site_descr = customtkinter.CTkComboBox(fr_tipo_site, fg_color="white", text_color="black", justify=tk.CENTER, values=self.opcoes)
        self.entry_tipo_site_descr.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
        self.entry_tipo_site_descr.bind("<Return>", lambda event: self.muda_barrinha(event,  self.text_descricao))

        # Descrição
        fr_descricao = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_descricao.place(relx=0.50, rely=0.02, relwidth=0.15, relheight=0.09)

        lb_descricao = customtkinter.CTkLabel(fr_descricao, text="Descricão")
        lb_descricao.place(relx=0.02, rely=0, relwidth=0.4, relheight=0.125)

        self.text_descricao = customtkinter.CTkEntry(fr_descricao, fg_color="black", text_color="white", width=300, height=100)
        self.text_descricao.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.40)
        self.text_descricao.bind("<Return>", lambda event: self.muda_barrinha(event,self.entry_informacoes_https))

        # Site
        fr_informacoes = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_informacoes.place(relx=0.655, rely=0.02, relwidth=0.30, relheight=0.09)
        lb_informacoes = customtkinter.CTkLabel(fr_informacoes, text="Site", text_color="white", font=('Arial', 12, 'bold'), anchor=tk.W)
        lb_informacoes.place(relx=0.05, rely=0, relheight=0.10, relwidth=0.70)

        # Https://
        lb_informacoes_https = customtkinter.CTkLabel(janela, text="Https://", text_color="black", font=('Arial', 10), anchor=tk.W)
        lb_informacoes_https.place(relx=0.45, rely=0.11, relheight=0.07, relwidth=0.97)
        self.entry_informacoes_https = customtkinter.CTkEntry(fr_informacoes, fg_color="black", text_color="white", justify=tk.LEFT)
        self.entry_informacoes_https.place(relx=0.01, rely=0.5, relwidth=0.89, relheight=0.40)
        
        # Botão Incluir Sites
        bt_incluir_sites = customtkinter.CTkButton(fr_informacoes, image=self.btsavedown_img, text='', fg_color='transparent', command=self.incluir_sites_click)
        bt_incluir_sites.place(relx=0.905, rely=0.40, relwidth=0.08, relheight=0.5)

        # Botão Consultar
        bt_consultar = customtkinter.CTkButton(janela, image=self.btconsulta_img, text='', fg_color='transparent', command=self.consulta_sites)
        bt_consultar.place(relx=0.96, rely=0.02, relwidth=0.035, relheight=0.09)
      
    def linha2_lista(self, janela):
        
        ## Listbox _ Informações Site
         # Listbox _ Cronograma de Atividades
        # Definindo cores
        bg_color = '#FFFFFF'  # Fundo branco
        text_color = '#000000'  # Texto preto
        selected_color = '#0078d7'  # Azul para selecionados
        
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
        treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])

        # Widgets - Listar Parcelas
        self.LSites = ttk.Treeview(janela, height=7, column=('tpo', 'ds', 'http'), show='headings') # , show='headings'
        # self.LSites.heading('#0', text='#', anchor='center')
        self.LSites.heading('#1', text='Tipo Site', anchor='center')
        self.LSites.heading('#2', text='Descrição', anchor='center')
        self.LSites.heading('#3', text='Endereço Site', anchor='center')

        # self.LSites.column('#0', width=2, anchor='w')
        self.LSites.column('tpo', width=80, anchor='w')
        self.LSites.column('ds', width=400, anchor='w')
        self.LSites.column('http', width=1000, anchor='w')
        
        self.LSites.pack(expand=True, fill='both')
        
        self.LSites.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.85)
        self.LSites.bind("<Double-1>", self.OnDoubleClick_site)

Sites_rel()