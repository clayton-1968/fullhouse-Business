from UsrCadastros import *
from widgets import Widgets
import hashlib
from db.db_conector import MySqlDatabase

class AlterarSenha(Widgets, Pessoas, Produtos, Icons):

    def alterar_senha(self, principal_frame, user):
        self.images_base64()

        self.window_one.title('Trocar Senha')
        self.clearFrame_principal()

        self.frame_principal = principal_frame
        self.user = user

        self.criar_widgets_alterar_senha()

    def criar_widgets_alterar_senha(self):
        self.fr_alterar_senha = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_alterar_senha.pack(pady=30, padx=30, fill="both", expand=True)

        customtkinter.CTkLabel(self.fr_alterar_senha, text="Trocar Senha", font=(
            "Roboto", 30, "bold")).pack(pady=10)

        self.senha_atual = customtkinter.CTkEntry(
            self.fr_alterar_senha, placeholder_text="Senha atual", show="*")
        self.senha_atual.pack(pady=10)

        self.senha_nova = customtkinter.CTkEntry(
            self.fr_alterar_senha, placeholder_text="Senha nova", show="*")
        self.senha_nova.pack(pady=10)

        self.senha_nova_repetida = customtkinter.CTkEntry(
            self.fr_alterar_senha, placeholder_text="Repetir senha nova", show="*")
        self.senha_nova_repetida.pack(pady=10)

        customtkinter.CTkButton(
            self.fr_alterar_senha, text='Submeter', command=self.efetivar_troca_senha).pack(pady=10)

    def efetivar_troca_senha(self):

        if self.senha_nova.get() != self.senha_nova_repetida.get():
            messagebox.showinfo("Aviso", "As senhas não coincidem.", parent=self.frame_principal)
            return

        elif self.senha_nova.get() == self.senha_atual.get():
            messagebox.showinfo("Aviso", "A nova senha não pode ser igual a atual.", parent=self.frame_principal)
            return

        # Recuperar hash
        query = f"SELECT usr_senhaexcel FROM usuarios WHERE Usr_email = '{self.user}'"
        result = db._querying(query)
        row = next(iter(result), None)

        if not row:
            messagebox.showinfo("Aviso", "Usuário não encontrado.", parent=self.frame_principal)
            return

        hash_armazenado = row['usr_senhaexcel']
        senha_atual = self.senha_atual.get()
        senha_hash_md5 = hashlib.md5(senha_atual.encode()).hexdigest()

        if senha_hash_md5 != hash_armazenado:
            messagebox.showinfo("Aviso", "Senha atual incorreta.", parent=self.window_one)
            return

        # Gera novo hash
        nova_senha = self.senha_nova.get()
        hash_novo = hashlib.md5(nova_senha.encode()).hexdigest()

        try:
            db.begin_transaction()

            query = f"""
                UPDATE usuarios 
                SET usr_senhaexcel = %s
                WHERE Usr_email = %s
            """

            db.executar_consulta(query, (str(hash_novo), str(self.user)))
            db.commit_transaction()

            messagebox.showinfo("Aviso", "Senha alterada com sucesso!", parent=self.window_one)
        except:
            messagebox.showerror("Erro", "Erro ao alterar senha!", parent=self.window_one)
            return

AlterarSenha()
