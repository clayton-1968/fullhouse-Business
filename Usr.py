import os

from imports import *

db = MySqlDatabase()

"""Função de Autenticação do Usuário"""

versao = '1.00.00.026'

CREDENTIALS_FILE = 'credentials.txt'

class Login(Limpeza):
    
    def loginauth(self, username, password, remember=False):
        self.check_email_user()
        Usr_Email = self.insert_user.get()
        Usr_Senha = self.insert_senha.get()

        if self.valida_email_usuario == 'valido':
            vsSQL = """SELECT 
                            u.Usr_Login, 
                            u.Usr_senhaexcel, 
                            sv.versao_nr 
                        FROM usuarios u  
                        JOIN sys_versao sv ON sv.versao_id=(SELECT MAX(versao_id) FROM sys_versao)  
                        WHERE u.Usr_Email = %s"""   
            
            myresult = db.executar_consulta(vsSQL, Usr_Email)
                    
            if myresult:

                self.save_credentials(username, password, remember)

                versao_sys = myresult[0]['versao_nr']
                self.versao_ds = versao_sys
                if versao_sys != versao:
                    messagebox.showinfo('Gestor Negócios', 'Versão do Sistema desatualizada, favor atualizar.')
                    caminho_exec = r"C:\FullBusiness\atualizador.exe"  # Caminho para o executável
                    try:
                        messagebox.showinfo('Gestor Negócios', f'Executável {caminho_exec} foi iniciado.')
                        subprocess.Popen(caminho_exec)  # Inicia o executável
                    except Exception as e:
                        messagebox.showinfo('Gestor Negócios', f'Erro ao iniciar o executável: {e}')
                        self.window_one.quit

                Usr_senhaexcel = myresult[0]['Usr_senhaexcel']
                Usr_login = myresult[0]['Usr_Login']
                os.environ['Usr_email'] = Usr_Email
                os.environ['Usr_login'] = Usr_login
                if self.check_senha_user() != 'None' and Login.criptografar_md5(Usr_Senha) == Usr_senhaexcel:
                    self.tela()
                    # self.window_one.mainloop()
                else:
                    messagebox.showinfo(
                        'Gestor Negócios', 'Usuário ou senha incorretos, tente novamente.')
            else:
                messagebox.showinfo('Gestor Negócios',
                                    'Usuário não cadastrado.')
        else:
            messagebox.showinfo(
                'Gestor Negócios', 'Por favor, preencher os campos de usuário e senha.')

    def save_credentials(self, username, password, remember=False):
        if remember:
            with open(CREDENTIALS_FILE, "w") as file:
                file.write(f"{username}\n{password}")
        else:
            if os.path.exists(CREDENTIALS_FILE):
                os.remove(CREDENTIALS_FILE)

    def load_credentials(self):
        if os.path.exists(CREDENTIALS_FILE):
            with open(CREDENTIALS_FILE, "r") as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    return lines[0].strip(), lines[1].strip()

        return "", ""

    def check_email_cad(self):
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.search(self.regex, self.cadastrese_user.get())):
            self.valida_email_cadastro = 'valido'
            # print("Valid Email")
        else:
            self.valida_email_cadastro = 'invalido'
            # print("Invalid Email")

    def check_senha_cad(self):
        if self.cadastrese_senha.get() == '':
            self.valida_senha_cadastro = 'vazio'
            print("Senha vazia")
        if self.cadastrese_senha.get() == 'Insira uma senha que ira lembrar':
            self.valida_senha_cadastro = 'vazio'
            print("Senha vazia")
        else:
            self.valida_senha_cadastro = 'ocupado'
            pass

    def check_senha_user(self):
        if self.insert_senha.get() == '':
            self.valida_senha_user = 'vazio'
            messagebox.showinfo('Senha em Branco!.')
        if self.insert_senha.get() == 'Insira sua senha':
            self.valida_senha_user = 'vazio'
            messagebox.showinfo('Senha em Branco!.')
        else:
            self.valida_senha_user = 'ocupado'
            pass

    def check_email_user(self):
        self.regex2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # Validação de email
        if (re.search(self.regex2, self.insert_user.get())):
            self.valida_email_usuario = 'valido'
        else:
            self.valida_email_usuario = 'invalido'    

    def autenticar_usuarios(Per_Modulo):
        """atenticar o acesso do usuário no modulo"""
        UsR_Login = os.environ.get('Usr_login')
        Permitido = False
        # if UsR_Login == 'Admin' or UsR_Login == 'ADMIN' or UsR_Login == 'admin':
        #     Permitido = True
        if UsR_Login != None:
            vsSQL = f"SELECT usr.Usr_Login, pp.Permissao_Modulo, pp.Permissao_Tipo FROM usuarios usr \
                    INNER JOIN TB_Permissoes pp ON usr.Usr_Login=pp.UsR_Login \
                    WHERE usr.Usr_Login='{UsR_Login}' \
                    GROUP BY pp.Permissao_Tipo, pp.Permissao_Modulo \
                    ORDER BY pp.Permissao_Tipo, pp.Permissao_Modulo"
            myresult = db._querying(vsSQL)
            Lin = 0
            for i in myresult:
                Usr_login_Permissao = myresult[Lin]['Usr_Login']
                Permissao_Tipo = myresult[Lin]['Permissao_Tipo']
                if Usr_login_Permissao == 'Admin':
                    Permitido = True
                else:
                    if Permissao_Tipo == 'Todos':
                        Permitido = True
                    elif Permissao_Tipo == Per_Modulo:
                        Permitido = True
                Lin = Lin + 1
        else:
            msg = f'Usuário não logado.'
            pg = 'login_msg.html'
            Permitido = False

        return (Permitido)

    def criar_senha():
        import random as rd

        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '%', '&', '*', '+',
                      '-', '.', '*', '=', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 't', 'm', 'n', 'z', 'x']
        num_list = int(len(characters)+1)
        num_char = 8
        i = 0
        n_list = []
        while i < num_char:
            n_list.append(characters[rd.randint(0, num_list)])
            print(num_list)
            i += 1

        password = ",".join(n_list)
        print("\nsua senha é:", password.replace(",", ""))
        return password.replace(",", "")

    # Criptografar Senha
    def criptografar_md5(texto):
        hash_md5 = hashlib.md5()
        hash_md5.update(texto.encode('utf-8'))
        return hash_md5.hexdigest()

    # Checar atualizações do Sistema
    def notificador(self):
        pass
        # self.dados_login()
        # try:
        #     ws = self.gc.open_by_key(self.planilha_login_code).worksheet('Página2')
        #     self.notifica = ws.col_values(1)
        # except google.auth.exceptions.RefreshError:
        #     messagebox("Gestor de Negócios", "Erro")

    # Acessar uma planilha de Dados
    def dados_login(self):
        pass
        # self.planilha_login_code = ' '
        # self.keyjson = {
        #     "type": "service_account",
        #     "project_id": "glacx-oficinas",
        #     "private_key_id": "",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\,
        #                    "client_email": "gserviceaccount.com",
        # "client_id": "11",
        # "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        # "token_uri": "https://oauth2.googleapis.com/token",
        # "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        # "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata.iam.gserviceaccount.com",
        # "universe_domain": "googleapis.com"}
        # self.gc = gspread.service_account_from_dict(self.keyjson)

    def submeter_cadastro(self):
        # Aqui você implementa a lógica para submissão do cadastro
        email = self.cadastrese_user.get()
        senha = self.cadastrese_senha.get()
        messagebox.showinfo("Cadastro", f"Usuário {email} cadastrado")

    # Cadastrar Novo Usuário
    def submeter_login(self):
        self.check_email_cad()
        self.check_senha_cad()
        if self.valida_senha_cadastro == 'vazio':
            messagebox.showinfo('Gestor de Negócios',
                                'Campo senha não pode ficar vazio.')
        if self.valida_email_cadastro == 'valido':
            if self.valida_senha_cadastro == 'vazio':
                messagebox.showinfo('Gestor de Negócios',
                                    'Campo senha não pode ficar vazio.')
            else:
                # mac_address = str(hex(uuid.getnode()))
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("noreply@fullhouse.tec.br", "@taideMelo24")
                server.sendmail(from_addr="noreply@fullhouse.tec.br",
                                to_addrs="noreply@fullhouse.tec.br; clayton@fullhouse.tec.br",
                                msg=self.cadastrese_user.get())
                server.quit()
                messagebox.showinfo(
                    'Gestor de Negócios', 'E-mail cadastrado, seu acesso foi liberado.')
                self.cadastrese_user.delete('0', 'end')
                self.cadastrese_senha.delete('0', 'end')
                self.cadastrese_user.destroy()
                self.cadastrese_senha.destroy()
                self.cadastrese.destroy()
                self.window_one.quit()
                self.login_screen().delete('0', 'end')
                self.cadastrese_user.destroy()
                self.cadastrese_senha.destroy()
                self.cadastrese.destroy()
                self.window_one.quit()
                self.login_screen()