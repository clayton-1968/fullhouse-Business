import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

import customtkinter # type: ignore

from Usr import db
from funcoes import Icons


class ConsultaAprovacoes(Icons):
    def baixas_financeiras(self):
        # self.root = root
        # self.root.title("Baixas Financeiras")

        self.janela_baixas_financeiras = customtkinter.CTkToplevel(self.window_one)
        self.janela_baixas_financeiras.title('Baixas Financeiras')
        self.janela_baixas_financeiras.geometry("1280x720")  # Ajusta o tamanho da janela

        # Criando o frame principal
        self.frame_top = tk.Frame(self.janela_baixas_financeiras, bg="black", height=120)
        self.frame_top.pack(fill=tk.X)

        # Labels e entradas para Empresa e CNPJ
        tk.Label(self.frame_top, text="Empresa", fg="white", bg="black").grid(row=0, column=0, padx=5, pady=2,
                                                                              sticky="w")
        tk.Entry(self.frame_top, width=30).grid(row=0, column=1, padx=5, pady=2)
        tk.Label(self.frame_top, text="CNPJ", fg="white", bg="black").grid(row=0, column=2, padx=5, pady=2, sticky="w")
        tk.Entry(self.frame_top, width=20).grid(row=0, column=3, padx=5, pady=2)

        # Unidade de Negócio
        tk.Label(self.frame_top, text="Unid. Negócios", fg="white", bg="black").grid(row=1, column=0, padx=5, pady=2,
                                                                                     sticky="w")
        tk.Entry(self.frame_top, width=15).grid(row=1, column=1, padx=5, pady=2)
        tk.Entry(self.frame_top, width=40).grid(row=1, column=2, columnspan=2, padx=5, pady=2)

        # Centro de Resultado
        tk.Label(self.frame_top, text="Centro de Resultado", fg="white", bg="black").grid(row=0, column=4, padx=5,
                                                                                          pady=2, sticky="w")
        tk.Entry(self.frame_top, width=10).grid(row=0, column=5, padx=5, pady=2)
        tk.Entry(self.frame_top, width=25).grid(row=0, column=6, padx=5, pady=2)

        # Natureza Financeira
        tk.Label(self.frame_top, text="Natureza Financeira", fg="white", bg="black").grid(row=1, column=4, padx=5,
                                                                                          pady=2, sticky="w")
        tk.Entry(self.frame_top, width=10).grid(row=1, column=5, padx=5, pady=2)
        tk.Entry(self.frame_top, width=25).grid(row=1, column=6, padx=5, pady=2)

        # Data e botão de busca
        tk.Label(self.frame_top, text="Data", fg="white", bg="black").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        tk.Entry(self.frame_top, width=15).grid(row=2, column=1, padx=5, pady=2)

        icone_pesquisa = self.base64_to_photoimage('lupa')
        self.btn_consulta = customtkinter.CTkButton(self.frame_top, image=icone_pesquisa, text='', fg_color='transparent', command=self.consulta_aprovacoes)
        self.btn_consulta.grid(row=2, column=2, padx=5, pady=2)

        tk.Label(self.frame_top, text="Aprovados", fg="white", bg="black").grid(row=2, column=3, padx=5, pady=2,
                                                                                sticky="w")
        tk.Entry(self.frame_top, width=20).grid(row=2, column=4, padx=5, pady=2)

        # Criando a Treeview
        self.tree = ttk.Treeview(self.janela_baixas_financeiras, columns=(
        "Unid_ID", "Centro_ID", "Natureza_ID", "Pessoa_ID", "Pessoas_Descricao", "Nr_Documento", "Valor", "Status"),
                                 show='headings')
        # "CpfCnpj", "Descricao", "Unid_ID", "Unidade_Negocio", "Centro_ID", "Centro_Resultado", "Natureza_ID",
        # "Natureza_Financeira", "Valor", "Nr_Documento", "Status", "Anexo"), show='headings')

        col_widths = [80, 200, 30, 80, 40, 100, 50, 100]
        headers = ["Unid_ID", "Centro_ID", "Natureza_ID", "Pessoa_ID", "Pessoas_Descricao", "Nr_Documento", "Valor", "Status"]

        for col, width in zip(self.tree['columns'], col_widths):
            self.tree.heading(col, text=headers[col_widths.index(width)])
            self.tree.column(col, width=width)

        self.tree.pack(expand=True, fill=tk.BOTH)

        #self.consulta_aprovacoes()

        # Conexão com o banco de dados
        # self.conexao = sqlite3.connect("financeiro.db")
        # self.cursor = self.conexao.cursor()

    def consulta_aprovacoes(self):
        self.tree.delete(*self.tree.get_children())

        # SELECT ID_Unidade, Unidade_Descricao, ID_CR, Cen_Descricao, ID_Natureza, Nat_Descricao, ID_Pessoa, Pessoas_Descricao,
        #        Doc_Num_Documento, Vlr_Total, Doc_DS_Observacao, Doc_AprovacaoJose, Anexo
        query = """
        SELECT ID_Unidade, ID_CR, ID_Natureza, ID_Pessoa, Pessoas_Descricao,
          Doc_Num_Documento, Vlr_Total, Doc_AprovacaoJose
        FROM TB_Itens
        LEFT JOIN TB_Pessoas ON TB_Itens.ID_Pessoa = TB_Pessoas.Pessoas_CPF_CNPJ
        """

        myresult = db._querying(query)
        consulta = [(consulta) for consulta in myresult]

        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!")
            return

        # Inserir dados na tabela

        for item in consulta:
            formatted_item = (
                item['ID_Unidade'],
                item['ID_CR'],
                item['ID_Natureza'],
                item['ID_Pessoa'],
                item['Pessoas_Descricao'],
                item['Doc_Num_Documento'],
                item['Vlr_Total'],
                item['Doc_AprovacaoJose'],
            )
            self.tree.insert('', 'end', values=formatted_item)

    # def __del__(self):
    #     self.conexao.close()