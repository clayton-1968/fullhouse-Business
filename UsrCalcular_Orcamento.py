from imports import *
from widgets import Widgets
from datetime import datetime


################# criando janela ###############
class Processar_Premissas_Orcamento(Widgets):
    def processar_premissas_orcamento(self):
        self.window_one.title('Processar Premissas Orçamentárias')
        self.clearFrame_principal()
        # self.frame_parametros(self.principal_frame)
        
        self.frame_processar_premissas_linha_1(self.principal_frame)
        # self.frame_linha_2(self.principal_frame)
       
################# dividindo a janela ###############
    def frame_processar_premissas_linha_1(self, janela):
        # Empresa
        coordenadas_relx = 0.005
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.455
        coordenadas_relheight = 0.07
        fr_empresa = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_empresa.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_empresa = customtkinter.CTkLabel(fr_empresa, text="Empresa", anchor='w')
        lb_empresa.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        empresas = []

        self.entry_empresa = AutocompleteCombobox(fr_empresa, width=30, font=('Times', 11), completevalues=empresas)
        self.entry_empresa.pack()
        self.entry_empresa.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_empresa.bind("<Button-1>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<KeyRelease>", lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind('<Down>', lambda event: self.atualizar_empresas(event, self.entry_empresa))
        self.entry_empresa.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_orcamento))

        # Orçamento
        coordenadas_relx = 0.465
        coordenadas_rely = 0.01
        coordenadas_relwidth = 0.33
        coordenadas_relheight = 0.07
        fr_orcamento = customtkinter.CTkFrame(janela, border_color="gray75", border_width=1)
        fr_orcamento.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
        lb_orcamento = customtkinter.CTkLabel(fr_orcamento, text="Orçamento", anchor='w')
        lb_orcamento.place(relx=0.009, rely=0.01, relheight=0.25, relwidth=0.55)

        orcamentos = []

        self.entry_orcamento = AutocompleteCombobox(fr_orcamento, width=30, font=('Times', 11), completevalues=orcamentos)
        self.entry_orcamento.pack()
        self.entry_orcamento.place(relx=0.01, rely=0.5, relwidth=0.985, relheight=0.4)
        self.entry_orcamento.bind("<Button-1>", lambda event: self.atualizar_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_orcamento))
        self.entry_orcamento.bind("<KeyRelease>", lambda event: self.atualizar_orcamentos(event, self.obter_Empresa_ID(self.entry_empresa.get(), janela), self.entry_orcamento))
        self.entry_orcamento.bind('<Down>', lambda event: self.atualizar_orcamentos(event, self.entry_empresa.get(), self.entry_orcamento))
        self.entry_orcamento.bind("<Return>", lambda event: self.muda_barrinha(event, self.entry_tipo_lcto_descr))

        def CalPremissas():
            Empresa_DS = self.entry_empresa.get()
            Orc_DS = self.entry_orcamento.get()

            if Empresa_DS != '':
                ID_Empresa = self.obter_Empresa_ID(Empresa_DS, janela)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher a Empresa!!")
                return
            
            if Orc_DS != '':
                ID_Orc = self.obter_Orc_ID(Orc_DS, janela)
            else:
                messagebox.showinfo("Gestor de Negócios", "Preencher Orçamento!!")
                return
            
            conditions = []  # Lista para armazenar as condições
            conditions.append("Empresa_ID = %s")
            params = [ID_Empresa]
            conditions.append("Orc_ID = %s")
            params.append(ID_Orc)
            
            vsSQL = f"""
                        SELECT 
                            Empresa_ID,
                            Orc_ID,
                            Orc_Descricao,
                            Orc_Status,
                            Orc_Observacao 
                        FROM orc_orcamentos
                        WHERE {' AND '.join(conditions)} 
                    """
            orcamentos = db.executar_consulta(vsSQL, params)
            
            if orcamentos:
                # first_record = orcamentos[0]  # Gets the first dictionary
                if orcamentos[0]['Orc_Status'] == "F":
                    messagebox.showinfo("Gestor de Negócios", "ESTE ORÇAMENTO JÁ ESTÁ FINALIZADO!!")
                    return
            else:
                messagebox.showinfo("Gestor de Negócios", "Orçamento não Cadastrado!!")
                return

            conditions = []  # Lista para armazenar as condições
            conditions.append("pp.Status_ID<>'E'")
            conditions.append("pp.Pri_ID = %s")
            params = [ID_Empresa]
            conditions.append("pp.Orc_ID = %s")
            params.append(ID_Orc)

            vsSQL = f"""
                    SELECT 
                        pp.Pri_ID           AS Empresa, 
                        pp.Orc_ID           AS Orc_ID, 
                        pp.Prem_ID          AS Prem_ID, 
                        pp.Prem_Tipo        AS Prem_Tipo,
                        pp.Cen_ID_Debito    AS CenDebito, 
                        pp.Cen_ID_Credito   AS CenCredito,
                        pp.Con_ID_Debito    AS ConDebito, 
                        pp.Con_ID_Credito   AS ConCredito,
                        pp.Prem_Quantidade  AS Quantidade , 
                        pp.Prem_Dedutivel   AS Dedutivel,
                        pp.Idx_ID           AS Idx_ID, 
                        pp.Prem_Financeiro  AS Financeiro, 
                        pp.Prem_PrazoPgto   AS PrazoPgto,
                        pp.Prem_aVista      AS aVista, 
                        pp.Prem_aPrazo      AS aPrazo, 
                        pp.Prem_nrParc      AS NrParcelas,
                        pp.Prem_txJuros     AS txJuros, 
                        pp.Idx_Data         AS Idx_Data, 
                        pp.Periodi_ID       AS Periodi_ID,
                        pp.Prem_DtaInicio   AS DtaInicio, 
                        pp.Prem_DtaFim      AS DtaFim,
                        pr.Preco_Valor      AS Preco_Valor, 
                        pp.Nat_ID           AS Nat_ID, 
                        pp.Nat_Tipo         AS Nat_Tipo,
                        pp.Prem_ICMS        AS ICMS, 
                        pp.Prem_PISCofins   AS PISCofins, 
                        pp.Status_ID        AS Status, 
                        pp.Tipo_Lcto        AS Tipo_Lcto
                    FROM orc_premissas pp
                    INNER JOIN orc_precos pr on pr.Preco_ID=pp.Preco_ID and pr.Orc_ID=pp.Orc_ID and pr.Empresa_ID=pp.Pri_ID
                    WHERE {' AND '.join(conditions)}
                """
            premissas = db.executar_consulta(vsSQL, params)
            
            if not premissas:
                messagebox.showinfo("Gestor de Negócios", "Não Existe Valores Lançados para Calculo referente ao orçamento selecionado!!!")
                return
            
            conditions = []  # Lista para armazenar as condições
            conditions.append("LEFT(Prem_Tipo, 3) = 'PRM'")
            conditions.append("Pri_ID = %s")
            params = [ID_Empresa]
            conditions.append("Orc_ID = %s")
            params.append(ID_Orc)

            vsSQL = f"""DELETE FROM orc_orcado 
                    WHERE {' AND '.join(conditions)}
                    """
            db.executar_consulta(vsSQL, params)

            # Cria uma nova janela (tela de carregamento)
            coordenadas_relx = 0.20
            coordenadas_rely = 0.30
            coordenadas_relwidth = 0.50
            coordenadas_relheight = 0.20
            self.frm_barra_progresso = customtkinter.CTkFrame(janela, border_color="gray75", border_width=0, fg_color='transparent')
            self.frm_barra_progresso.place(relx=coordenadas_relx, rely=coordenadas_rely,relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)
            lb_barra_progresso = customtkinter.CTkLabel(self.frm_barra_progesso, text="Aguarde Processando...", anchor='w')
            lb_barra_progresso.place(relx=0.001, rely=0.10, relheight=0.25, relwidth=0.55)
            
            # Cria a Barra de Progresso
            self.progress_bar = ctk.CTkProgressBar(
                                                    self.frm_barra_progresso,
                                                    width=400,
                                                    height=30,
                                                    corner_radius=30,
                                                    fg_color='#003',
                                                    progress_color='#060',
                                                )
            self.progress_bar.pack(pady=10, padx=50)
            self.progress_bar.place(relx=0.009, rely=0.50, relheight=0.25, relwidth=0.98)
            self.progress_bar.set(0)  # Reseta a barra de progresso para 0
            self.total_records = len(premissas)  # Total records to process
            self.current_index = 0
            
            for index, premissa in enumerate(premissas, start=1):
                self.process_records()  # Começa a processar os registros        
                
                dta_inicio = premissa['DtaInicio']
                if isinstance(dta_inicio, datetime):
                    dta_ref_calculo = self.ult_dia_mes(dta_inicio) 
                    str_ano_base = datetime.strptime(dta_ref_calculo, '%Y-%m-%d').year
                elif isinstance(dta_inicio, date):
                    dta_ref_calculo = self.ult_dia_mes(datetime.combine(dta_inicio, datetime.min.time()))  # Combines 
                    str_ano_base = datetime.strptime(dta_ref_calculo, '%Y-%m-%d').year
                elif isinstance(dta_inicio, str):
                    dta_inicio = datetime.strptime(dta_inicio, '%Y-%m-%d')
                    dta_ref_calculo = self.ult_dia_mes(dta_inicio) 
                    str_ano_base = datetime.strptime(dta_ref_calculo, '%Y-%m-%d').year
                else:
                    print('Erro: DtaInicio não é um objeto datetime válido.')
                    continue  
                
                dta_fim = premissa['DtaFim']  # This should also be a datetime.date object
                if isinstance(dta_fim, date):
                    dta_fim = datetime.combine(dta_fim, datetime.min.time())

                dta_ref_calculo = datetime.strptime(dta_ref_calculo, '%Y-%m-%d')         
                while dta_ref_calculo <= dta_fim:
                    str_registros = ''
                    Idx_ID = premissa['Idx_ID']
                    Idx_Data = premissa['Idx_Data']
                    
                    if isinstance(Idx_Data, datetime):
                        Idx_Data = self.ult_dia_mes(Idx_Data) 
                    elif isinstance(Idx_Data, date):
                        Idx_Data = self.ult_dia_mes(datetime.combine(Idx_Data, datetime.min.time()))  # Combines 
                    elif isinstance(Idx_Data, str):
                        Idx_Data = datetime.strptime(Idx_Data, '%Y-%m-%d')
                        Idx_Data = self.ult_dia_mes(datetime.combine(Idx_Data, datetime.min.time()))  # Combines 
                        # Idx_Data = self.ult_dia_mes(Idx_Data) 
                    else:
                        print('Erro: Dta Reajuste não é um objeto datetime válido.')
                        continue  
                    

                    conditions = []  # Lista para armazenar as condições
                    conditions.append("Empresa_ID = %s")
                    params = [ID_Empresa]
                    conditions.append("Orc_ID = %s")
                    params.append(ID_Orc)
                    conditions.append("Idx_ID = %s")
                    params.append(Idx_ID)
                    conditions.append("Idx_Data = %s")
                    params.append(Idx_Data)

                    vsSQL = f"""
                                SELECT Idx_ID, Idx_Valor 
                                FROM Orc_Indices
                                WHERE {' AND '.join(conditions)}
                                
                            """
                    indice = db.executar_consulta(vsSQL, params)
                    
                    id_reajuste = 1 if not indice else indice['Idx_Valor']
                    
                    # Logic for Data_Lancamento and other calculations
                    periodicidade = premissa['Periodi_ID']
                    data_lancamento = dta_ref_calculo
                    preco_p0 = premissa['Preco_Valor']
                    quantidade = premissa['Quantidade']
                    dedutivel = premissa['Dedutivel']
                    financeiro = premissa['Financeiro']
                    prazo_pgto = premissa['PrazoPgto']
                    a_vista = premissa['aVista']
                    a_prazo = premissa['aPrazo']
                    nr_parcelas = premissa['NrParcelas']
                    tx_juros = premissa['txJuros']
                    icms = premissa['ICMS']
                    pis_cofins = premissa['PISCofins']
                    nat_id = premissa['Nat_ID']
                    nat_tipo = premissa['Nat_Tipo']
                    dt_inicio = datetime.combine(premissa['DtaInicio'], datetime.min.time())
                    dt_fim = datetime.combine(premissa['DtaFim'], datetime.min.time())
                    pri_id = premissa['Empresa']

                    if prazo_pgto != 0:
                        if data_lancamento.month == 12:
                            mes_pgto = 1
                            ano_pgto = data_lancamento.year + 1
                        else:
                            mes_pgto = data_lancamento.month + 1
                            ano_pgto = data_lancamento.year
                    else:
                        mes_pgto = data_lancamento.month
                        ano_pgto = data_lancamento.year
                    
                    data_pgto = self.ult_dia_mes(datetime(ano_pgto, mes_pgto, 1))
                    data_pgto = datetime.strptime(data_pgto, '%Y-%m-%d') 

                    va_lcto_apr = self.custos(preco_p0, quantidade, id_reajuste, periodicidade, dt_inicio, dt_fim, data_lancamento, Idx_Data)
                    
                    if va_lcto_apr == None:
                        va_lcto_apr = 0
                    
                    parcelas = 1
                    va_lcto_ipt = va_lcto_apr * icms  
                    va_lcto_apr *= (1 - icms) 
                    
                    while parcelas <= nr_parcelas and va_lcto_apr != 0:
                        if parcelas == 1:
                            va_lcto_pto = va_lcto_apr * (a_vista / 100)
                        
                            if premissa['Tipo_Lcto'] == "CPA":
                                if data_pgto.year >= str_ano_base and va_lcto_pto != 0 and premissa['Financeiro'] == "S":
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMPG', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '{premissa['ConCredito']}', " \
                                                    f"'111110101', '{data_pgto.strftime('%Y-%m-%d')}', '{nat_id}', " \
                                                    f"'F', '{dedutivel}', '{(va_lcto_pto)}')"

                                if data_pgto.year >= str_ano_base and va_lcto_ipt != 0:
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMIP', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '{premissa['ConCredito']}', " \
                                                    f"'111110101', '{data_pgto.strftime('%Y-%m-%d')}', '26', " \
                                                    f"'F', '{dedutivel}', '{(va_lcto_ipt)}')"

                            # Process for Tipo_Lcto = "CRE"
                            elif premissa['Tipo_Lcto'] == "CRE":
                                if data_pgto.year >= str_ano_base and va_lcto_pto != 0 and premissa['Financeiro'] == "S":
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMRE', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '111110101', " \
                                                    f"'{premissa['ConDebito']}', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'{nat_id}', 'F', '{dedutivel}', '{(va_lcto_pto)}')"

                                if data_pgto.year >= str_ano_base and va_lcto_ipt != 0:
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMIP', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '111110101', " \
                                                    f"'{premissa['ConDebito']}', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'26', 'F', '{dedutivel}', '{(va_lcto_ipt)}')"
                        else:
                            va_prestacao = npf.pmt(tx_juros,  nr_parcelas, -va_lcto_apr * (a_prazo / 100), fv=0, when='end'  )
                            va_lcto_pto = (va_lcto_apr * a_prazo) / nr_parcelas  # Portion of the total for each installment
                            va_lcto_pto_juros = va_prestacao - va_lcto_pto  # Amount attributed to interest

                            # Update payment month and year for the next payment
                            if data_pgto.month == 12:
                                mes_pgto = 1
                                ano_pgto = data_pgto.year + 1
                            else:
                                mes_pgto = data_pgto.month + 1
                                ano_pgto = data_pgto.year

                            # Set updated payment date as the last day of the following month
                            data_pgto = self.ult_dia_mes(datetime(ano_pgto, mes_pgto, 1))  # Calculate the last day of the next payment month
                            data_pgto = datetime.strptime(data_pgto, '%Y-%m-%d') 
                            
                            # Tipo_Lcto = "CPA"
                            if premissa['Tipo_Lcto'] == "CPA":
                                if data_pgto.year >= str_ano_base and va_lcto_pto != 0 and premissa['Financeiro'] == "S":
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMPG', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '{premissa['ConCredito']}', " \
                                                    f"'111110101', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'{nat_id}', 'F', '{dedutivel}', '{(va_lcto_pto)}')"

                                if data_pgto.year >= str_ano_base and va_lcto_ipt != 0 and premissa['Financeiro'] == "S":
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMIP', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '{premissa['ConCredito']}', " \
                                                    f"'111110101', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'26', 'F', '{dedutivel}', '{(va_lcto_ipt)}')"

                            # Tipo_Lcto = "CRE"
                            elif premissa['Tipo_Lcto'] == "CRE":
                                if data_pgto.year >= str_ano_base and va_lcto_pto != 0 and premissa['Financeiro'] == "S":
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMRE', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '111110101', " \
                                                    f"'{premissa['ConDebito']}', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'{nat_id}', 'F', '{dedutivel}', '{(va_lcto_pto)}')"

                                if data_pgto.year >= str_ano_base and va_lcto_ipt != 0:
                                    if str_registros:
                                        str_registros += ", "
                                    str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMIP', " \
                                                    f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '111110101', " \
                                                    f"'{premissa['ConDebito']}', '{data_pgto.strftime('%Y-%m-%d')}', " \
                                                    f"'26', 'F', '{dedutivel}', '{(va_lcto_ipt)}')"

                        parcelas += 1
                    
                    # Gravar lançamento de apropriação
                    if data_lancamento.year >= str_ano_base and va_lcto_apr != 0:
                        if str_registros:
                            str_registros += ", "
                        str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', '{premissa['Prem_Tipo']}', " \
                                        f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '{premissa['ConDebito']}', '{premissa['ConCredito']}', " \
                                        f"'{data_lancamento.strftime('%Y-%m-%d')}', '{nat_id}', '{nat_tipo}', '{dedutivel}', " \
                                        f"'{(va_lcto_apr)}')"

                    # Gravar lançamento de imposto
                    if data_lancamento.year >= str_ano_base and va_lcto_ipt != 0:
                        if str_registros:
                            str_registros += ", "
                        str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMIP', " \
                                        f"'{premissa['CenDebito']}', '{premissa['CenCredito']}', '113020202', '{premissa['ConCredito']}', " \
                                        f"'{data_lancamento.strftime('%Y-%m-%d')}', '25', 'O', '{dedutivel}', " \
                                        f"'{(va_lcto_ipt)}')"
                    
                    # Gravar lançamento do credito do pis e cofins
                    if premissa['PISCofins'] != 0:  
                        va_lcto_ipt = abs(va_lcto_apr) * 0.076 

                        if data_lancamento.year >= str_ano_base and va_lcto_ipt != 0:
                            if str_registros:
                                str_registros += ", "
                            str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMCOFINSA', " \
                                            f"'510102001', '510102001', '213010101', '312010101', " \
                                            f"'{data_lancamento.strftime('%Y-%m-%d')}', '23', 'R', '{dedutivel}', " \
                                            f"{(va_lcto_ipt)})"

                        data_pgto = self.ult_dia_mes(data_lancamento + timedelta(days=30))  # Move to next month

                        if data_pgto.year >= str_ano_base and va_lcto_ipt != 0:
                            if str_registros:
                                str_registros += ", "
                            str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMCOFINSP', " \
                                            f"'510102001', '510102001', '111010101', '213010101', " \
                                            f"'{data_pgto.strftime('%Y-%m-%d')}', '23', 'F', 'N', " \
                                            f"{(va_lcto_ipt)})"

                        # Additional PIS logic, if needed
                        # Update values for PIS
                        va_lcto_ipt = abs(va_lcto_apr) * 0.0165  # Calculate the second PIS value
                        
                        if data_lancamento.year >= str_ano_base and va_lcto_ipt != 0:
                            if str_registros:
                                str_registros += ", "
                            str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMPISA', " \
                                            f"'510102001', '510102001', '213010102', '312010102', " \
                                            f"'{data_lancamento.strftime('%Y-%m-%d')}', '23', 'R', '{dedutivel}', " \
                                            f"{(va_lcto_ipt)})"

                        data_pgto = self.ult_dia_mes(data_lancamento + timedelta(days=30))  # Move to next month

                        if data_pgto.year >= str_ano_base and va_lcto_ipt != 0:
                            if str_registros:
                                str_registros += ", "
                            str_registros += f"('{premissa['Empresa']}', '{premissa['Orc_ID']}', '{premissa['Prem_ID']}', 'PRMPISP', " \
                                            f"'510102001', '510102001', '111110101', '213010102', " \
                                            f"'{data_pgto.strftime('%Y-%m-%d')}', '23', 'F', 'N', " \
                                            f"{(va_lcto_ipt)})"
                    
                    if str_registros:
                        self.gravar_orcamento(str_registros)

                    # Calculate Data_Pgto as the last day of the payment month
                    dta_ref_calculo = self.ult_dia_mes(self.add_months(dta_ref_calculo, 1))  # Move to the next month
                    dta_ref_calculo = datetime.strptime(dta_ref_calculo, '%Y-%m-%d')  
                
                
        # Botão de Calcular
        icon_image = self.base64_to_photoimage('save')
        self.btn_processar_premissas = customtkinter.CTkButton(janela, text='', image=icon_image, fg_color='transparent', command=CalPremissas)
        self.btn_processar_premissas.place(relx=0.955, rely=0.012, relwidth=0.04, relheight=0.05)
 
    def custos(self, preco_p0, quantidade, id_reajuste, periodicidade, dt_inicio: datetime, dt_fim: datetime, dt_lancamento: datetime, data_reajuste: datetime):
        """
            Esta Função calcula os custos durante o período em questão :

            '   Preço_P0 - Preço sem reajuste
            '   Indice_Reajuste - Código do Indice a ser utilizado
            '   Data_Reajuste - Data de aniversário do reajuste
            '   Periodiciadade - períodos
            '   Início e Fim - Inicio do custo e fim do custo
        
        """
        grupo_bimestral = None
        grupo_trimestral = None
        grupo_quadrimestral = None
        grupo_quinquemestral = None
        grupo_semestral = None
        
        #   Bimestral
        #   Grupo_1 = 1,3,5,7,9,11
        #   Grupo_2 = 2,4,6,8,10,12
        if dt_inicio.month in [1, 3, 5, 7, 9, 11]:
            grupo_bimestral = 1
        else:
            grupo_bimestral = 2

        #   Trimestral
        #   Grupo_1 = 1,4,7,10
        #   Grupo_2 = 2,5,8,11
        #   Grupo_3 = 3,6,9,12
        if dt_inicio.month in [1, 4, 7, 10]:
            grupo_trimestral = 1
        elif dt_inicio.month in [2, 5, 8, 11]:
            grupo_trimestral = 2
        else:
            grupo_trimestral = 3

        #   Quadrimestral
        #   Grupo_1 = 1,5,9
        #   Grupo_2 = 2,6,10
        #   Grupo_3 = 3,7,11
        #   Grupo_4 = 4,8,12
        if dt_inicio.month in [1, 5, 9]:
            grupo_quadrimestral = 1
        elif dt_inicio.month in [2, 6, 10]:
            grupo_quadrimestral = 2
        elif dt_inicio.month in [3, 7, 11]:
            grupo_quadrimestral = 3
        else:
            grupo_quadrimestral = 4

        #   Quinquemestral
        #   Grupo_1 = 1,6,11
        #   Grupo_2 = 2,7,12
        #   Grupo_3 = 3,8
        #   Grupo_4 = 4,9
        #   Grupo_5 = 5,10
        if dt_inicio.month in [1, 6, 11]:
            grupo_quinquemestral = 1
        elif dt_inicio.month in [2, 7, 12]:
            grupo_quinquemestral = 2
        elif dt_inicio.month in [3, 8]:
            grupo_quinquemestral = 3
        elif dt_inicio.month in [4, 9]:
            grupo_quinquemestral = 4
        elif dt_inicio.month in [5, 10]:
            grupo_quinquemestral = 5

        # Semestral
        #   Grupo_1 = 1,7
        #   Grupo_2 = 2,8
        #   Grupo_3 = 3,9
        #   Grupo_4 = 4,10
        #   Grupo_5 = 5,11
        #   Grupo_6 = 6,12
        if dt_inicio.month in [1, 7]:
            grupo_semestral = 1
        elif dt_inicio.month in [2, 8]:
            grupo_semestral = 2
        elif dt_inicio.month in [3, 9]:
            grupo_semestral = 3
        elif dt_inicio.month in [4, 10]:
            grupo_semestral = 4
        elif dt_inicio.month in [5, 11]:
            grupo_semestral = 5
        else:
            grupo_semestral = 6
        
        data_reajuste = datetime.strptime(data_reajuste, '%Y-%m-%d')
        data_reajuste = datetime.combine(data_reajuste, datetime.min.time())
        custos = 0
        # Periodicidade
        if periodicidade == 1:  # Periodicidade 1 (Monthly)
            if dt_lancamento >= dt_inicio and dt_lancamento <= dt_fim:
                
                if dt_lancamento >= data_reajuste:
                    custos = preco_p0 * quantidade * id_reajuste
                else:
                    custos = preco_p0 * quantidade
            
            return custos
        
        elif periodicidade == 2:  # Periodicidade 2 (Bimonthly)
            
            if dt_lancamento >= dt_inicio and dt_lancamento <= dt_fim:
                if grupo_bimestral == 1:
                    # Odd months
                    if dt_lancamento.month in [1, 3, 5, 7, 9, 11]:
                        if dt_lancamento >= data_reajuste:
                            custos =  preco_p0 * quantidade * id_reajuste
                        else:
                            custos =  preco_p0 * quantidade
            
                elif grupo_bimestral == 2:
                    # Even months
                    if dt_lancamento.month in [2, 4, 6, 8, 10, 12]:
                        if dt_lancamento >= data_reajuste:
                            custos = preco_p0 * quantidade * id_reajuste
                        else:
                            custos = preco_p0 * quantidade
            return custos
        
        elif dt_lancamento >= dt_inicio and periodicidade == 3 and dt_lancamento <= dt_fim:
            if grupo_trimestral == 1:
                if dt_lancamento.month in {1, 4, 7, 10}:  # January, April, July, October
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0  # Not in the valid months

            elif grupo_trimestral == 2:
                if dt_lancamento.month in {2, 5, 8, 11}:  # February, May, August, November
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            elif grupo_trimestral == 3:
                if dt_lancamento.month in {3, 6, 9, 12}:  # March, June, September, December
                    custos = preco_p0 * quantidade * id_reajuste
                else:
                    custos = 0
            
            return custos
        elif dt_lancamento >= dt_inicio and periodicidade == 4 and dt_lancamento <= dt_fim:
            if grupo_quadrimestral == 1:  # First group (1, 5, 9)
                if dt_lancamento.month in {1, 5, 9}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0  # Not in the valid months

            elif grupo_quadrimestral == 2:  # Second group (2, 6, 10)
                if dt_lancamento.month in {2, 6, 10}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            elif grupo_quadrimestral == 3:  # Third group (3, 7, 11)
                if dt_lancamento.month in {3, 7, 11}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0
            elif grupo_quadrimestral == 4:  # Group 4
                if dt_lancamento.month in {4, 8, 12}:  # April, August, December
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0  # Not in valid months of group 4

            return custos
        if dt_lancamento >= dt_inicio and periodicidade == 5 and dt_lancamento <= dt_fim:
            if grupo_quinquemestral == 1:  # Group 1 (1, 6, 11)
                if dt_lancamento.month in {1, 6, 11}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0  # Not in valid months

            elif grupo_quinquemestral == 2:  # Group 2 (2, 7, 12)
                if dt_lancamento.month in {2, 7, 12}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            elif grupo_quinquemestral == 3:  # Group 3 (3, 8)
                if dt_lancamento.month in {3, 8}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            elif grupo_quinquemestral == 4:  # Group 4 (4, 9)
                if dt_lancamento.month in {4, 9}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            elif grupo_quinquemestral == 5:  # Group 5 (5, 10)
                if dt_lancamento.month in {5, 10}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            return custos
        elif dt_lancamento >= dt_inicio and periodicidade == 6 and dt_lancamento <= dt_fim:
            if grupo_semestral == 1:  # Group 1 (January, July)
                if dt_lancamento.month in {1, 7}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0  # Not in valid months

            elif grupo_semestral == 2:  # Group 2 (February, August)
                if dt_lancamento.month in {2, 8}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0
            
            elif grupo_semestral == 3:  # Group 3 (March, September)
                if dt_lancamento.month in {3, 9}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0
            
            elif grupo_semestral == 4:  # Group 4 (April, October)
                if dt_lancamento.month in {4, 10}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0
                
            elif grupo_semestral == 5:  # Group 5 (May, November)
                if dt_lancamento.month in {5, 11}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0
            
            elif grupo_semestral == 6:  # Group 6 (June, December)
                if dt_lancamento.month in {6, 12}:
                    if dt_lancamento >= data_reajuste:
                        custos = preco_p0 * quantidade * id_reajuste
                    else:
                        custos = preco_p0 * quantidade
                else:
                    custos = 0

            return custos
        elif dt_lancamento >= dt_inicio and periodicidade == 7 and dt_lancamento <= dt_fim:
            if dt_lancamento.month == dt_inicio.month:
                if dt_lancamento >= data_reajuste:
                    custos = preco_p0 * quantidade * id_reajuste
                else:
                    custos = preco_p0 * quantidade
            else:
                custos = 0  
            
            return custos
        
        elif dt_lancamento == dt_inicio and periodicidade == 8:
            if dt_lancamento >= data_reajuste:
                custos = preco_p0 * quantidade * id_reajuste
            else:
                custos = preco_p0 * quantidade

            return custos

    def gravar_orcamento(self, str_registro):
        vs_sql = """
            INSERT INTO orc_orcado (
                                    Pri_ID, 
                                    Orc_ID, 
                                    Prem_ID, 
                                    Prem_Tipo, 
                                    Cen_IDDebito, 
                                    Cen_IDCredito, 
                                    Con_IDDebito, 
                                    Con_IDCredito, 
                                    Orc_Data, 
                                    Nat_ID, 
                                    Nat_Tipo, 
                                    Prem_Dedutivel, 
                                    Orc_Valor) 
            VALUES {}
        """.format(str_registro)  # Use .format to insert the record string
        db._querying(vs_sql)
        
    def process_records(self):
        if self.current_index < self.total_records:
            self.current_index += 1 
            progress_value = self.current_index / self.total_records
            self.progress_bar.set(progress_value)
            self.window_one.after(1000, self.process_records)
            self.window_one.update_idletasks()  # Atualiza a interface gráfica
        else:
            self.progress_bar.stop()  # Para a barra de progresso
            self.frm_barra_progresso.destroy()
            

Processar_Premissas_Orcamento()
