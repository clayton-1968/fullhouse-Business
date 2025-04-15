import datetime

from UsrCadastros import *
from widgets import Widgets


class ExtratoBancario(Widgets, Consultas_Financeiro, Pessoas, Produtos, Icons):
    def extrato_bancario(self, principal_frame):
        self.images_base64()

        self.window_one.title('Extrato Bancário')
        self.clearFrame_principal()

        self.frame_principal = principal_frame

        self.create_widgets()

    def create_widgets(self):
        # CNPJ (Empresa)
        self.frame_empresa(self.frame_principal, 0, 0.02, 0.30, 0.09)
        self.combo_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.combo_pessoa))

        # Banco
        self.fr_banco = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_banco.place(relx=0.31, rely=0.02, relwidth=0.20, relheight=0.09)

        self.lb_banco = customtkinter.CTkLabel(self.fr_banco, text="Banco")
        self.lb_banco.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.bancos = []
        self.entry_banco = AutocompleteCombobox(self.fr_banco, width=30, justify=tk.LEFT, font=('Times', 8),
                                                completevalues=self.bancos)
        self.entry_banco.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.4)
        self.entry_banco.bind("<Button-1>", lambda event: self.atualizar_bancos(event, self.entry_banco))
        self.entry_banco.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia))

        # Agência
        self.fr_agencia = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_agencia.place(relx=0.52, rely=0.02, relwidth=0.14, relheight=0.09)

        self.lb_agencia = customtkinter.CTkLabel(self.fr_agencia, text="Agência")
        self.lb_agencia.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_agencia = customtkinter.CTkEntry(self.fr_agencia, fg_color="white", text_color="black", justify=tk.RIGHT)
        self.entry_agencia.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.4)
        self.entry_agencia.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_agencia_dv))

        self.entry_agencia_dv = customtkinter.CTkEntry(self.fr_agencia, fg_color="white", text_color="black",
                                                       justify=tk.RIGHT)
        self.entry_agencia_dv.place(relx=0.62, rely=0.5, relwidth=0.35, relheight=0.4)
        self.entry_agencia_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Conta
        self.fr_contacorrente = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_contacorrente.place(relx=0.67, rely=0.02, relwidth=0.14, relheight=0.09)

        self.lb_contacorrente = customtkinter.CTkLabel(self.fr_contacorrente, text="Conta")
        self.lb_contacorrente.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        self.entry_contacorrente = customtkinter.CTkEntry(self.fr_contacorrente, fg_color="white", text_color="black",
                                                          justify=tk.RIGHT)
        self.entry_contacorrente.place(relx=0.01, rely=0.5, relwidth=0.65, relheight=0.4)
        self.entry_contacorrente.bind("<Return>", lambda event: self.muda_barrinha(event, None))

        self.entry_contacorrente_dv = customtkinter.CTkEntry(self.fr_contacorrente, fg_color="white", text_color="black",
                                                       justify=tk.RIGHT)
        self.entry_contacorrente_dv.place(relx=0.62, rely=0.5, relwidth=0.35, relheight=0.4)
        self.entry_contacorrente_dv.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_contacorrente))

        # Período
        self.fr_periodo = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_periodo.place(relx=0.82, rely=0.02, relwidth=0.14, relheight=0.09)
        self.lb_periodo = customtkinter.CTkLabel(self.fr_periodo, text="Período")
        self.lb_periodo.place(relx=0.1, rely=0, relheight=0.25, relwidth=0.8)

        # Data inicio
        self.lb_dt_inicio = customtkinter.CTkLabel(self.fr_periodo, text="Data Início")
        self.lb_dt_inicio.place(relx=0.1, rely=0.25, relheight=0.125, relwidth=0.35)

        self.entry_dt_inicio = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_inicio.delete(0, 'end')
        self.entry_dt_inicio.insert(0, datetime.strptime("01/01/2000", "%d/%m/%Y").strftime("%d/%m/%Y"))
        self.entry_dt_inicio.place(relx=0.01, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_inicio.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_inicio))
        self.entry_dt_inicio.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_inicio, self.entry_dt_inicio))

        # Data fim
        self.lb_dt_fim = customtkinter.CTkLabel(self.fr_periodo, text="Data Fim")
        self.lb_dt_fim.place(relx=0.6, rely=0.25, relheight=0.125, relwidth=0.35)

        self.entry_dt_fim = customtkinter.CTkEntry(self.fr_periodo, fg_color="white", text_color="black", justify=tk.CENTER)
        self.entry_dt_fim.delete(0, 'end')
        self.entry_dt_fim.insert(0, datetime.now().strftime("%d/%m/%Y"))
        self.entry_dt_fim.place(relx=0.50, rely=0.46, relwidth=0.485, relheight=0.50)
        self.entry_dt_fim.bind("<Button-1>", lambda event: self.calendario(event, self.entry_dt_fim))
        self.entry_dt_fim.bind("<Return>", lambda event: self.muda_barrinha_dta(event, self.entry_dt_fim, self.entry_dt_fim))

        # Botão de consulta
        icon_image = self.base64_to_photoimage('lupa')
        self.botao_consultar_extrato = customtkinter.CTkButton(self.frame_principal, text='', image=icon_image,
                                                     fg_color='transparent', command=self.consultar_extrato)
        self.botao_consultar_extrato.pack(pady=10)
        self.botao_consultar_extrato.place(relx=0.96, rely=0.02, relwidth=0.05, relheight=0.07)

        # Resultado
        self.fr_extrato_result = customtkinter.CTkFrame(self.frame_principal, border_color="gray75", border_width=1)
        self.fr_extrato_result.place(relx=0, rely=0.125, relwidth=1, relheight=1)

        self.extrato_result = ttk.Treeview(self.fr_extrato_result, columns=("DATA", "DOCUMENTO", "HISTÓRICO", "MOVTO", "SALDO"),
                                     show="headings")
        self.extrato_result.heading("DATA", text="DATA")
        self.extrato_result.heading("DOCUMENTO", text="DOCUMENTO")
        self.extrato_result.heading("HISTÓRICO", text="HISTÓRICO")
        self.extrato_result.heading("MOVTO", text="MOVTO")
        self.extrato_result.heading("SALDO", text="SALDO")
        self.extrato_result.column("DATA", width=80, anchor="center")
        self.extrato_result.column("DOCUMENTO", width=200, anchor="center")
        self.extrato_result.column("HISTÓRICO", width=495, anchor="center")
        self.extrato_result.column("MOVTO", width=110, anchor="e")
        self.extrato_result.column("SALDO", width=110, anchor="e")
        self.extrato_result.grid(row=0, column=0, sticky="nsew")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.fr_extrato_result, orient="vertical", command=self.extrato_result.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.extrato_result.configure(yscrollcommand=scrollbar.set)

        self.fr_extrato_result.grid_rowconfigure(0, weight=1)
        self.fr_extrato_result.grid_columnconfigure(0, weight=1)

    def consultar_extrato(self):
        self.extrato_result.delete(*self.extrato_result.get_children())

        # if not self.combo_empresa.get():
        #     messagebox.showerror("Erro", "Empresa não pode ser branco!")
        #     return
        #
        # if not self.entry_banco.get():
        #     messagebox.showerror("Erro", "Banco não pode ser branco!")
        #     return

        if not self.entry_dt_inicio.get() or not self.entry_dt_fim.get():
            messagebox.showerror("Erro", "Datas não podem ser branco!")
            return

        try:
            self.dt_inicio = datetime.strptime(self.entry_dt_inicio.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
            self.dt_fim = datetime.strptime(self.entry_dt_fim.get(), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use DD/MM/YYYY")
            return

        try:
            query = f"""
                SELECT SUM(ff.Fin_VlR_Liquidacao) As Saldo_Anterior 
                FROM TB_Financeiro ff 
                WHERE ff.Fin_Dta_Liquidacao < '{self.dt_inicio}'
            """

            if self.combo_empresa.get():
                self.id_empresa = self.obter_Empresa_ID(self.combo_empresa.get())
                query += f' AND ff.ID_Empresa = "{self.id_empresa}"'

            if self.entry_banco.get():
                self.id_banco = self.obter_banco(self.entry_banco.get())
                query += f" AND ff.ID_Bco_Liquidacao = {self.id_banco}"

            if self.entry_agencia.get():
                query += f" AND ff.Fin_Agencia_Liquidacao = {self.entry_agencia.get()}"

            if self.entry_contacorrente.get():
                query += f" AND ff.Fin_Conta_Liquidacao = {self.entry_contacorrente.get()}"

            query += " GROUP BY ff.ID_Empresa"

            myresult = db._querying(query)
            saldo_inicial = myresult[0]['Saldo_Anterior'] if myresult else 0.0

            prev_day = (datetime.strptime(self.dt_inicio, "%Y-%m-%d") - timedelta(days=1)).strftime(
                "%d/%m/%Y")
            self.extrato_result.insert("", "end", values=(
                prev_day,
                "",
                "SALDO ANTERIOR",
                "",
                f"{saldo_inicial:,.2f}"
            ))

            saldo_dia = saldo_inicial

            query2 = f"""
                SELECT
                    ff.Fin_Dta_Liquidacao,
                    ff.Fin_Num_documento,
                    pp.Pessoas_Descricao,
                    ff.Fin_VlR_Liquidacao
                FROM TB_Financeiro ff
                LEFT JOIN TB_CB_Doc dc ON dc.ID_Empresa = ff.ID_Empresa AND dc.ID_Pessoa = ff.ID_Pessoa 
                    AND dc.ID_Unidade = ff.ID_Unidade AND dc.Doc_Num_Documento = ff.Fin_Num_Documento
                LEFT JOIN TB_Pessoas pp ON pp.Pessoas_CPF_CNPJ = ff.ID_Pessoa AND pp.Empresa_ID = ff.ID_Empresa
                WHERE ff.Fin_Dta_Liquidacao BETWEEN '{self.dt_inicio}' AND '{self.dt_fim}'
            """

            if self.combo_empresa.get():
                query2 += f' AND ff.ID_Empresa = "{self.id_empresa}"'

            if self.entry_banco.get():
                query2 += f" AND ff.ID_Bco_Liquidacao = {self.id_banco}"

            if self.entry_agencia.get():
                query2 += f" AND ff.Fin_Agencia_Liquidacao = {self.entry_agencia.get()}"

            if self.entry_contacorrente.get():
                query2 += f" AND ff.Fin_Conta_Liquidacao = {self.entry_contacorrente.get()}"

            query2 += " ORDER BY ff.Fin_Dta_Liquidacao"

            myresult2 = db._querying(query2)
            consulta = [consulta for consulta in myresult2]

            if not consulta:
                messagebox.showinfo("Informação", "Não Foram encontrados lançamentos!")
                return

            for item in consulta:
                transaction_date = datetime.strptime(str(item['Fin_Dta_Liquidacao']), "%Y-%m-%d").strftime("%d/%m/%Y")
                doc_number = item['Fin_Num_documento']
                description = item['Pessoas_Descricao'] if item['Pessoas_Descricao'] else "Não Cadastrado...!!!"
                amount = float(item['Fin_VlR_Liquidacao'])
                saldo_dia += amount

                self.extrato_result.insert("", "end", values=(
                    transaction_date,
                    doc_number,
                    description,
                    f"{amount:,.2f}",
                    f"{saldo_dia:,.2f}"
                ))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {str(e)}")


ExtratoBancario()