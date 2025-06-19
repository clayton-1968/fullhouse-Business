from imports                          import *

from Usr                              import Login
from LancFinanceiro                   import Lanc_fin
from UsrRelatorio_EstudosNegocio      import Resumo_Estudos
from Lx.UsrSimulador                  import Simulador_Estudos
from UsrSimulador_rel                 import Simulador_Estudos_Rel
from UsrSimulador_Maps                import Simulador_Maps
from UsrSites                         import Sites_rel
from UsrPesquisaMercado               import Pesquisa_Mercado
from UsrRelatorio_Fluxo_Projetado     import Fluxo_Projetado
from UsrExtratosClientes_Fornecedores import Extrato_Clientes_Fornecedores
from UsrPremissas                     import Premissas_Orcamento
from UsrRelatorio_Premissas           import Resumo_Premissas
from UsrCalcular_Orcamento            import Processar_Premissas_Orcamento
from UsrRelatorio_Orcamento           import Relatorio_Orcamento
from UsrCadastros                     import Versoes
from UsrAprovacaoLctos                import AprovacaoLctos
from UsrExtratoBancario               import ExtratoBancario
from UsrBaixasFinanceiras             import BaixasFinanceiras
from UsrCronograma                    import Cronograma_Atividades
from UsrCronograma_Hierarquico        import Cronograma_Atividades_Hierarquico
from UsrAnexos                        import Pesquisa_Anexos
from UsrAnexos                        import Pesquisa_Anexos_Simulador
from UsrTelaPrincipal                 import Tela_Principal
from UsrCadastro_Curvas_Negocio       import Cadastrar_Curvas_Negocio
from UsrBorderoBancario               import BorderoBancario
from UsrAlterar_Senha                 import AlterarSenha
from UsrUsuarios_Sistema              import UsuariosSistema
from UsrPermissoes_Sistema            import PermissoesSistema
from UsrContas_Pagar                  import ContasPagar
from UsrModulos_Sistema               import ModuloSistema
from UsrSistema_Amortizacao           import SistemaAmortizacao


class PrimaryWindow(
                    Login,
                    Lanc_fin,
                    Resumo_Estudos,
                    Simulador_Estudos,
                    Simulador_Estudos_Rel,
                    Simulador_Maps,
                    Sites_rel,
                    Pesquisa_Mercado,
                    Fluxo_Projetado,
                    Extrato_Clientes_Fornecedores,
                    Premissas_Orcamento,
                    Resumo_Premissas,
                    Processar_Premissas_Orcamento,
                    Relatorio_Orcamento,
                    Versoes,
                    AprovacaoLctos,
                    ExtratoBancario,
                    BaixasFinanceiras,
                    Cronograma_Atividades,
                    Cronograma_Atividades_Hierarquico,
                    Pesquisa_Anexos,
                    Pesquisa_Anexos_Simulador,
                    Tela_Principal,
                    Cadastrar_Curvas_Negocio,
                    BorderoBancario,
                    AlterarSenha,
                    UsuariosSistema,
                    PermissoesSistema,
                    ContasPagar,
                    ModuloSistema,
                    SistemaAmortizacao,
                    ):

    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.login_screen()
        
    def menu_conectar(self, modulo):
        Permitido = self.usuario_autentic(os.environ.get('Usr_login'), modulo)
        if Permitido == True:
            if modulo == 'Simulador':
                self.simulador_estudos()
            elif modulo == 'Indicadores':
                self.resumo_estudos()
            elif modulo == 'Lcto_Documentos':
                self.lancamentos()
            elif modulo == 'Sites':
                self.sites()
            elif modulo == 'Cadastro_Pesquisas':
                self.pesquisa_mercado()
            elif modulo == 'Extrato_Financeiro':
                self.extrato_clientes_fornecedores()
            elif modulo == 'Planejamento_Cadastro_Premissas':
                self.premissas_orcamentos()
            elif modulo == 'Planejamento_Relatorio_Premissas':
                self.resumo_premissas()
            elif modulo == 'Planejamento_Processar_Premissas':
                self.processar_premissas_orcamento()
            elif modulo == 'Planejamento_Relatorio_Orcamento':
                self.relatorio_orcamento()
            elif modulo == 'Manutencao':
                messagebox.showinfo("Gestor de Negócios", "Em Manutenção!!")
                # self.processar_premissas_orcamento()
            elif modulo == 'Versoes':
                self.cad_versoes()
            elif modulo == 'Aprovacao_Lctos':
                self.aprovacao_lctos(self.principal_frame)
            elif modulo == 'Extrato_Bancario':
                self.extrato_bancario(self.principal_frame)
            elif modulo == 'Baixas_Financeiras':
                self.baixas_financeiras(self.principal_frame)
            elif modulo == 'Cronograma_Barra_Projetos':
                self.cronograma_atividades()
            elif modulo == 'Cronograma_Barra_Projetos_Hierarquico':
                self.cronograma_atividades_hierarquico()
            elif modulo == 'Cadastro_Curvas':
                self.cadastrar_curvas_negocio()
            elif modulo == 'Bordero_Bancario':
                self.consultar_bordero(self.principal_frame)
            elif modulo == 'Alterar_Senha':
                self.alterar_senha(self.principal_frame, self.username)
            elif modulo == "Usuarios_Sistema":
                self.usuarios_sistema(self.principal_frame)
            elif modulo == 'Permissoes_Sistema':
                self.permissoes_sistema(self.principal_frame)
            elif modulo == 'Contas_Pagar':
                self.contas_pagar(self.principal_frame)
            elif modulo == 'Modulos_Sistema': 
                self.consultar_modulo(self.principal_frame)
            elif modulo == 'Sistema_Amortizacao':
                self.consultar_amortizacao(self.principal_frame)
                

    def login_screen(self):
        # Configura a janela principal
        self.window_one = customtkinter.CTk()  # Usando customtkinter
        self.window_one.title("Login - Gestor de Negócios")
        self.window_one.geometry("700x500+250+150")
        self.window_one.configure(background='#456E96')
        self.window_one.resizable(False, False)

        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.window_one.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.frame_login()
        self.window_one.mainloop()

    def frame_login(self):
        self.login_frame = customtkinter.CTkFrame(self.window_one)  # Frame de login
        self.login_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Adicionando elementos de login
        customtkinter.CTkLabel(self.login_frame, text="Gestor de Negócios", font=("Roboto", 30, "bold")).pack(pady=10)
        customtkinter.CTkLabel(self.login_frame, text="Login", font=("Roboto", 24)).pack(pady=10)

        # Entradas para usuário e senha
        self.insert_user = customtkinter.CTkEntry(self.login_frame, placeholder_text="Informe o e-mail", width=210, border_color="#2cb67d")
        self.insert_user.pack(pady=10)
        self.insert_user.bind("<Return>", lambda event: self.muda_barrinha(event, self.insert_senha))

        self.insert_senha = customtkinter.CTkEntry(self.login_frame, placeholder_text="Insira sua senha", show="*", width=210, border_color="#2cb67d")
        self.insert_senha.pack(pady=10)
        # self.insert_senha.bind("<Return>", lambda event: self.muda_barrinha(event, self.btn_login))

        # Cbk lembrar senha
        self.lembrar_senha = ctk.BooleanVar(value=False)
        self.cbk_lembrar_senha = customtkinter.CTkCheckBox(self.login_frame, text=" Lembrar Senha", variable=self.lembrar_senha)
        self.cbk_lembrar_senha.pack(pady=10)

        username, password = self.load_credentials()

        if len(username) > 0 and len(password) > 0:
            self.insert_user.insert(0, username)
            self.insert_senha.insert(0, password)
            self.cbk_lembrar_senha.select()
        
        self.username = self.insert_user.get()

        # Botão de login
        self.btn_login = customtkinter.CTkButton(self.login_frame, text='Login',
                                                 command=lambda: self.loginauth(
                                                     username=self.username,
                                                     password=self.insert_senha.get(),
                                                     remember=self.lembrar_senha.get()))
        self.btn_login.pack(pady=10)

        # Link para cadastro
        customtkinter.CTkLabel(self.login_frame, text="Ainda não é cadastrado? ").pack(pady=10)
        customtkinter.CTkButton(self.login_frame, text='Cadastre-se', command=self.tela_cadastro).pack(pady=10)

    def tela_cadastro(self):
        self.clear_frame()
        self.cadastro_frame = customtkinter.CTkFrame(
            self.window_one)  # Frame de cadastro
        self.cadastro_frame.pack(pady=30, padx=30, fill="both", expand=True)

        # Adicionando elementos à tela de cadastro
        customtkinter.CTkLabel(self.cadastro_frame, text="Cadastro", font=(
            "Roboto", 30, "bold")).pack(pady=10)
        customtkinter.CTkLabel(
            self.cadastro_frame, text="Insira seu e-mail para cadastro").pack(pady=10)

        self.cadastro_user = customtkinter.CTkEntry(
            self.cadastro_frame, placeholder_text="Insira um e-mail válido para cadastro")
        self.cadastro_user.pack(pady=10)

        self.cadastro_senha = customtkinter.CTkEntry(
            self.cadastro_frame, placeholder_text="Insira uma senha que irá lembrar", show="*")
        self.cadastro_senha.pack(pady=10)

        customtkinter.CTkButton(
            self.cadastro_frame, text='Submeter', command=self.submeter_cadastro).pack(pady=10)

    def tela(self):
        self.clear_frame()
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.window_one.title("Gestor de Negócios")
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 
        self.window_one.resizable(TRUE, TRUE)
        self.window_one.minsize(width=970, height=700)
        
        # Flag para controle do estado da aplicação
        self.app_closing = False
        
        # Vincular o evento de fechamento da janela
        self.window_one.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.principal_frame = customtkinter.CTkFrame(self.window_one, fg_color='black')  # Frame Principal
        self.principal_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.tela_principal()
        self.menus()
        
        def site_rfz():
            webbrowser.open("https://www.fullhouse.com.br")

    def menus(self):
        menubar = Menu(self.window_one)
        self.window_one.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar, tearoff=0)
        filemenu3 = Menu(menubar, tearoff=0)
        filemenu4 = Menu(menubar, tearoff=0)
        filemenu5 = Menu(menubar, tearoff=0)
        filemenu6 = Menu(menubar, tearoff=0)
        filemenu7 = Menu(menubar, tearoff=0)
        filemenu8 = Menu(menubar, tearoff=0)
        filemenu9 = Menu(menubar, tearoff=0)

        def quit():
            self.on_closing()

        def helpme():
            msg = "Ajuda"
            msg += ""
            messagebox.showinfo("Gestor de Negócios ", msg)

        def sobre():
            msg = "Gestor de Negócios -        XXXX@fullhouse.tec.com           \n "
            msg += "FullHouse - https://www.facebook.com/fullhouse/ - Brazil"
            messagebox.showinfo("Gestor de Negócios ", msg)

        def manual():
            webbrowser.open(
                "https://docs.google.com/document/d/1AyvAEJngBzOGpq5lXcxnNRDQrJxjVW30qvurceokePU/edit?usp=sharing")

        def modo_claro():
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")

        def modo_escuro():
            customtkinter.set_appearance_mode("Dark")
            customtkinter.set_default_color_theme("dark-blue")

        menubar.add_cascade(label="Cadastros", menu=filemenu)
        menubar.add_cascade(label="Dashboard", menu=filemenu2)
        menubar.add_cascade(label="Simulador", menu=filemenu3)
        menubar.add_cascade(label="Financeiro", menu=filemenu4)
        menubar.add_cascade(label="Planejamento", menu=filemenu5)
        menubar.add_cascade(label="Imobiliário", menu=filemenu6)
        menubar.add_cascade(label="Administrador", menu=filemenu7)
        menubar.add_cascade(label="Ajuda", menu=filemenu8)
        menubar.add_cascade(label="Sair", command=quit)

        filemenu.add_command(label="Pessoas")  # , command=self.cadaut)
        filemenu.add_command(label="Unidades de Negócio")
        filemenu.add_command(label="Centro Resultados")
        filemenu.add_command(label="Naturezas Financeira")
        filemenu.add_command(label="Plano de Contas")
        filemenu.add_command(label="Bancos")  # , command=self.cadprod)
        filemenu.add_command(label="Contas Bancárias")
        filemenu.add_command(label="Produtos e Serviços")
        filemenu.add_command(label="Unidades Medidas")
        filemenu.add_command(label="Trocar Senha", command=lambda: self.menu_conectar('Alterar_Senha'))

        filemenu2.add_command(label="Informe Gestão")
        filemenu2.add_command(label="Previsão Financeira")

        filemenu3.add_command(label="Estudos", command=lambda: self.menu_conectar('Indicadores'))
        filemenu3.add_command(label="Tpo Empreendimento")
        filemenu3.add_command(label="Cadastro Estudos")
        filemenu3.add_command(label="Curvas de Negócio", command=lambda: self.menu_conectar('Cadastro_Curvas'))
        filemenu3.add_command(label="Etapas Curvas")
        filemenu3.add_command(label="Status Negócio")  # , command=modo_claro)

        filemenu4.add_command(label="Lcto (CPA/CRE)", command=lambda: self.menu_conectar('Lcto_Documentos'))
        filemenu4.add_command(label="Aprovação Lçtos", command=lambda: self.menu_conectar('Aprovacao_Lctos'))
        filemenu4.add_command(label="Borderô Bancário", command=lambda: self.menu_conectar('Bordero_Bancario'))
        filemenu4.add_command(label="Baixas Financeiras", command=lambda: self.menu_conectar('Baixas_Financeiras'))
        filemenu4.add_command(label="Relatório Cli/Fornec.", command=lambda: self.menu_conectar('Extrato_Financeiro'))
        filemenu4.add_command(label="Extrato Bancário", command=lambda: self.menu_conectar('Extrato_Bancario'))
        filemenu4.add_command(label="Contas a Pagar", command=lambda: self.menu_conectar('Contas_Pagar'))

        filemenu5.add_command(label="Cronograma", command=lambda: self.menu_conectar('Cronograma_Barra_Projetos'))
        filemenu5.add_command(label="Cronograma Hierarquico", command=lambda: self.menu_conectar('Cronograma_Barra_Projetos_Hierarquico'))
        filemenu5.add_command(label="Reuniões")
        filemenu5.add_command(label="Cad. Projetos") 
        filemenu5.add_command(label="Envios de SMS")
        filemenu5.add_command(label="Envios de Whatsapp")
        # Criação de submenu Planejamento
        sub_menu_planejamento = Menu(filemenu5, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_parametros = Menu(sub_menu_planejamento, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_parametros.add_command(label="Orçamentos")
        sub_menu_parametros.add_command(label="Preços")
        sub_menu_parametros.add_command(label="Naturezas Financeiras")
        sub_menu_parametros.add_command(label="Centros de Resultado")
        sub_menu_parametros.add_command(label="Parâmetros")
        sub_menu_parametros.add_command(label="Indicadores")
        sub_menu_parametros.add_command(label="Índices")
        sub_menu_planejamento.add_cascade(label="Parâmetros", menu=sub_menu_parametros)  # Adiciona o submenu

        sub_menu_folha = Menu(sub_menu_planejamento, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_folha.add_command(label="Pessoal")
        sub_menu_folha.add_command(label="Funcionários")
        sub_menu_folha.add_command(label="Função")
        sub_menu_folha.add_command(label="Aumentos Previstos")
        sub_menu_folha.add_command(label="Folha Orçamento")
        sub_menu_folha.add_command(label="Folha Real")
        sub_menu_planejamento.add_cascade(label="Folha de Pagto", menu=sub_menu_folha)

        sub_menu_premissas = Menu(sub_menu_planejamento, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_premissas.add_command(label="Premissas", command=lambda: self.menu_conectar('Planejamento_Relatorio_Premissas'))
        sub_menu_premissas.add_command(label="Carry Over")
        sub_menu_planejamento.add_cascade(label="Premissas", menu=sub_menu_premissas)

        sub_menu_relatorios = Menu(sub_menu_planejamento, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_relatorios.add_command(label="xxxxxxxxx", command=lambda: self.menu_conectar('Manutencao'))
        sub_menu_relatorios.add_command(label="Orçamento", command=lambda: self.menu_conectar('Planejamento_Relatorio_Orcamento'))
        sub_menu_planejamento.add_cascade(label="Relatórios", menu=sub_menu_relatorios)
        
        sub_menu_calcular = Menu(sub_menu_planejamento, tearoff=0)  # tearoff=0 para eliminar a linha separadora
        sub_menu_calcular.add_command(label="Outorga")
        sub_menu_calcular.add_command(label="Impostos")
        sub_menu_calcular.add_command(label="Aportes")
        sub_menu_calcular.add_command(label="Premissas", command=lambda: self.menu_conectar('Planejamento_Processar_Premissas'))
        sub_menu_calcular.add_command(label="Folha")
        sub_menu_calcular.add_command(label="Investimentos")
        sub_menu_planejamento.add_cascade(label="Calcular", menu=sub_menu_calcular)
        filemenu5.add_cascade(label="Planejamento", menu=sub_menu_planejamento)  # Adiciona o submenu

        filemenu6.add_command(label="Cadastro Quadras")
        filemenu6.add_command(label="Cadastro Unidades")
        filemenu6.add_command(label="Tabela Preços")  # , command=modo_escuro)
        filemenu6.add_command(label="Contrato Venda")  # , command=modo_escuro)
        filemenu6.add_command(label="Contrato Cessão")
        filemenu6.add_command(label="Contrato Novação")
        filemenu6.add_command(label="Atualização Monetária")
        filemenu6.add_command(label="Extrato Clientes")
        filemenu6.add_command(label="Atendimento Cliente")
        filemenu6.add_command(label="Resumo clientes")

        filemenu7.add_command(label="Usuários Sistema", command=lambda: self.menu_conectar('Usuarios_Sistema'))
        filemenu7.add_command(label="Permissões", command=lambda: self.menu_conectar('Permissoes_Sistema'))
        filemenu7.add_command(label="Modulos", command=lambda: self.menu_conectar('Modulos_Sistema'))  # , command=modo_escuro)
        filemenu7.add_command(label="Clientes do Sistema")
        filemenu7.add_command(label="Sistema Amortização", command=lambda: self.menu_conectar('Sistema_Amortizacao'))
        filemenu7.add_command(label="Atualizações - Versão Sistema", command=lambda: self.menu_conectar('Versoes'))

        filemenu8.add_command(label="Manual de uso do sistema", command=manual)
        filemenu8.add_command(label="Sites Cadastrados", command=lambda: self.menu_conectar('Sites'))
        filemenu8.add_command(label="Sobre", command=sobre)

if __name__ == "__main__":
    app = PrimaryWindow()