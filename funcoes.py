from db.db_conector import MySqlDatabase

from customtkinter import *
import customtkinter
import customtkinter as ctk

from tkinter import StringVar, OptionMenu, font, messagebox, ttk
from tkinter import *

import tkcalendar
import numpy as np
import numpy_financial as npf 
import math
from datetime import datetime, timedelta
from calendar import monthrange
from dateutil.relativedelta import relativedelta
import base64
from PIL import ImageTk, Image
import os
import webbrowser
import io
import requests
import xml.etree.ElementTree as ET
import re
import uuid

db = MySqlDatabase()
class Gravar():
    
    def gravar_sites(self):
        if not  self.combo_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.')
            self.combo_empresa.focus()
            return
                
        # Definição de variáveis
        ID_Empresa = self.obter_Empresa_ID( self.combo_empresa.get())
        site_tpo = self.entry_tipo_site_descr.get().strip()  # Remove espaços em branco das extremidades
        site_ds = self.text_descricao.get().strip()
        site_http = self.entry_informacoes_https.get().strip()
        vs_sql = """INSERT INTO sites_cadastros 
                    (
                            Empresa_ID, 
                            Site_tpo, 
                            Site_Descricao, 
                            Site_http 
                    ) 
                    VALUES (%s, %s, %s, %s)
                    """
        values = (
                ID_Empresa, 
                site_tpo, 
                site_ds, 
                site_http
                )
        myresult = db.executar_consulta(vs_sql,  values)

    def gravar_produtos(self):
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.')
            self.entry_cpf_cpj_pessoa.focus()
            return
                
        # Definição de variáveis
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
        produto_descricao = self.entry_descricao_produto.get().strip()  # Remove espaços em branco das extremidades
        produto_ncm = self.entry_ncm_produto.get()
        produto_spead_ds = self.entry_spead_produto.get()
        produto_spead_id = self.obter_Spead_ID(produto_spead_ds) if produto_spead_ds else ''
        produto_unidade_ds = self.entry_tpomedida_produto.get()
        produto_unidade_id = self.obter_UnidadeMedida_ID(produto_unidade_ds)
        ativo = "A"
        
        produto_cfop = ""
        produto_icms = 0
        produto_ipi = 0
        produto_o_cst = ""
        produto_observacao = ""

        
            
        # Consulta para verificar se o produto já existe
        vs_sql = """SELECT * FROM TB_Produtos 
                    WHERE 
                        Empresa_ID=%s
                        AND Produto_Descricao=%s 
                        
                    """
        myresult = db.executar_consulta(vs_sql, (str(ID_Empresa), str(produto_descricao)))
        
        if not myresult:  # Se não encontrou registros
            # Inserção do novo produto
            vs_sql = """INSERT INTO TB_Produtos 
                        (
                                Empresa_ID, 
                                Produto_Descricao, 
                                Produto_NCM, 
                                Produto_CFOP, 
                                Produto_Tipo, 
                                Produto_Unidade, 
                                Ativo
                                
                        ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                     """
            values = (
                    ID_Empresa, 
                    produto_descricao, 
                    produto_ncm, 
                    produto_cfop, 
                    produto_spead_id, 
                    produto_unidade_id, 
                    ativo
                    )
            myresult = db.executar_consulta(vs_sql,  values)
            
        else:
            # Atualização do produto existente
            vs_sql = """UPDATE TB_Produtos SET 
                                Produto_NCM=%s, 
                                Produto_CFOP=%s, 
                                Produto_Tipo=%s, 
                                Produto_Unidade=%s
                                
                        WHERE 
                            Empresa_ID=%s
                            AND produto_descricao=%s 
                            
                        """
            myresult = db.executar_consulta(vs_sql,  (produto_ncm, 
                                                      produto_cfop, 
                                                      produto_spead_id, 
                                                      produto_unidade_id, 
                                                      ID_Empresa, 
                                                      produto_descricao,))

    def gravar_pessoas(self):
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.')
            self.entry_cpf_cpj_pessoa.focus()
            return
        
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
        Tpo_Pessoa = self.entry_tipo_pessoa.get()
        ID_Pessoa_Check = self.entry_cpf_cpj_pessoa.get()
        ID_Pessoa = self.entry_cpf_cpj_pessoa.get().replace(".", "").replace("/", "").replace("-", "")
        DS_Pessoa = self.entry_nome_pessoa.get()
        Proprietario = self.entry_proprietario.get()
        DS_Banco = self.entry_banco.get()
        ID_Banco = self.obter_banco(DS_Banco) if DS_Banco else ''
        Agencia_Nr = self.entry_agencia.get()
        Agencia_DV = self.entry_agencia_dv.get()
        Conta_Corrente_Nr = self.entry_contacorrente.get()
        Conta_Corrente_DV = self.entry_contacorrente_dv.get()
        Chave_Pix = self.entry_chave_pix.get()
        CEP = self.entry_cep.get()
        UF = self.entry_uf.get()
        municipios_atualizados = self.atualizar_municipio_fx(self.entry_uf.get())
        Municipio_DS = municipios_atualizados
        Municipio_DS = self.entry_municipio.get()
        Municipio_ID = self.obter_municipio_IBGE(Municipio_DS) if Municipio_DS else ''
        Endereco = self.entry_endereco.get()
        Endereco_Nr = self.entry_endereco_nr.get()
        Endereco_Compl = self.entry_endereco_complemento.get()
        Endereco_Bairro = self.entry_endereco_bairro.get()
        Inscricao_Municipal = self.entry_incricao_municipal.get()
        Inscricao_Estadual = self.entry_incricao_estadual.get()
        Suframa = self.entry_suframa.get()
        Telefone = self.entry_telefone.get()
        WhatsApp = self.entry_celular_whatsapp.get()
        Email = self.entry_email.get()
        
        if not ID_Pessoa.isdigit():
            messagebox.showinfo('Gestor Negócios', 'Caracter Inválido!!!.')
            return

        if Tpo_Pessoa not in ["J", "F"]:
            messagebox.showinfo('Gestor Negócios', 'Definir Tipo J=Pessoa Jurídica ou F=Pessoa Física!!!.')
            return

        if Tpo_Pessoa == "J":
            if not self.verificar_cnpj(ID_Pessoa):
                messagebox.showinfo('Gestor Negócios', 'Número do CNPJ Inválido!!!.')
                return
        elif Tpo_Pessoa == "F":
            if not self.validar_cpf(ID_Pessoa):
                messagebox.showinfo('Gestor Negócios', 'Número do CPF Inválido!!!.')
                return

        if not DS_Pessoa:
            messagebox.showinfo('Gestor Negócios', 'Descrição não cadastrada!!!.')
            return
        
        elif len(DS_Pessoa) > 100:
            # self.entry_nome_pessoa = DS_Pessoa[:100]
            DS_Pessoa = DS_Pessoa[:100]

        if Proprietario not in ["S", "N"]:
            messagebox.showinfo('Gestor Negócios', 'Definir S=Sim ou N=Não!!!.')
            return

        # Confirmar gravação
        # resposta = input("Dados validados, deseja gravar%s (s/n): ")
        # if resposta.lower() != 's':
        #     return

        # Verificar se a pessoa já existe
        vsSQL = """
                    SELECT * 
                        FROM TB_Pessoas 
                        WHERE 
                        Empresa_ID=%s
                        AND Pessoas_CPF_CNPJ=%s
                        
                """
        myresult = db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Pessoa_Check)))
        
        if not myresult:
            strSql = """
                        INSERT INTO TB_Pessoas (
                            Empresa_ID, 
                            Pessoas_Tipo, 
                            Pessoas_CPF_CNPJ, 
                            Pessoas_Descricao, 
                            Pessoas_Bco, 
                            Pessoas_Agencia, 
                            Pessoas_DVAgencia, 
                            Pessoas_Conta, 
                            Pessoas_DVConta, 
                            Pessoas_Chave_PiX, 
                            Pessoas_Proprietaria, 
                            Pessoas_EndLogradouro, 
                            Pessoas_EndNumero, 
                            Pessoas_EndBairro, 
                            Pessoas_EndComplemento, 
                            Pessoas_UF, 
                            Pessoas_CodMunicipioFiscal, 
                            Pessoas_EndCidade, 
                            Pessoas_CEP, 
                            Pessoas_InscricaoEstadual, 
                            Pessoas_InscricaoMunicipal, 
                            Pessoas_Suframa, 
                            Pessoas_Telefone, 
                            Pessoas_Fax, 
                            Pessoas_Email
                            )

                        
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            values = (
                        ID_Empresa, 
                        Tpo_Pessoa,
                        ID_Pessoa_Check,
                        DS_Pessoa.upper(),
                        ID_Banco,
                        Agencia_Nr,
                        Agencia_DV,
                        Conta_Corrente_Nr,
                        Conta_Corrente_DV,
                        Chave_Pix,
                        Proprietario,
                        Endereco,
                        Endereco_Nr,
                        Endereco_Bairro,
                        Endereco_Compl,
                        UF,
                        Municipio_ID,
                        Municipio_DS,
                        CEP,
                        Inscricao_Estadual,
                        Inscricao_Municipal,
                        Suframa,
                        Telefone,
                        WhatsApp,
                        Email
                    )
            myresult = db.executar_consulta(strSql, values)
            self.consulta_pessoas()
            messagebox.showinfo("Sucesso", "Cadastro Incluído com sucesso!")
        else:
            strSql = """UPDATE TB_Pessoas SET 
                            Pessoas_Descricao=%s, 
                            Pessoas_Bco=%s, 
                            Pessoas_Agencia=%s, 
                            Pessoas_DVAgencia=%s, 
                            Pessoas_Conta=%s, 
                            Pessoas_DVConta=%s, 
                            Pessoas_Chave_PiX=%s, 
                            Pessoas_Proprietaria=%s, 
                            Pessoas_EndLogradouro=%s, 
                            Pessoas_EndNumero=%s, 
                            Pessoas_EndBairro=%s, 
                            Pessoas_EndComplemento=%s, 
                            Pessoas_UF=%s, 
                            Pessoas_CodMunicipioFiscal=%s, 
                            Pessoas_EndCidade=%s, 
                            Pessoas_CEP=%s, 
                            Pessoas_InscricaoEstadual=%s, 
                            Pessoas_InscricaoMunicipal=%s, 
                            Pessoas_Suframa=%s, 
                            Pessoas_Telefone=%s, 
                            Pessoas_Fax=%s, 
                            Pessoas_Email=%s 
                        WHERE 
                            Empresa_ID=%s
                            AND Pessoas_CPF_CNPJ=%s
                            
                    """
            
            values = (
                        DS_Pessoa.upper(),
                        ID_Banco,
                        Agencia_Nr,
                        Agencia_DV,
                        Conta_Corrente_Nr,
                        Conta_Corrente_DV,
                        Chave_Pix,
                        Proprietario,
                        Endereco,
                        Endereco_Nr,
                        Endereco_Bairro,
                        Endereco_Compl,
                        UF,
                        Municipio_ID,
                        Municipio_DS,
                        CEP,
                        Inscricao_Estadual,
                        Inscricao_Municipal,
                        Suframa,
                        Telefone,
                        WhatsApp,
                        Email,
                        ID_Empresa,
                        ID_Pessoa_Check
                    )
            
            myresult = db.executar_consulta(strSql, values)
            self.consulta_pessoas()
            messagebox.showinfo("Sucesso", "Cadastro Alterado com sucesso!")
            
    def Gravar_Estudos(self,
                        ID_Empresa, 
                        UF, 
                        Cidade, 
                        Tipo, 
                        Nome_da_Area,
                        Tela
                        ):
        ID_Empresa = ID_Empresa
        if not ID_Empresa:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        UF = UF.upper()
        if not UF:
            messagebox.showinfo('Gestor Negócios', 'UF em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        Cidade = Cidade
        if not Cidade:
            messagebox.showinfo('Gestor Negócios', 'Município em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        Tipo_Estudo = Tipo
        if not Tipo_Estudo:
            messagebox.showinfo('Gestor Negócios', 'Tipo do Estudo em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        impostos_per = self.get_aliquota_imposto(Tipo)
        TPer_Impostos = float(impostos_per[0])
        
        Nome_Area = Nome_da_Area
        if not Nome_Area:
            messagebox.showinfo('Gestor Negócios', 'Nome da Área em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        ID_Unidade = self.entry_informacoes_unidade_negocio.get() # ARRUMAR PARA UNIDADE NEGÓCIO SEJA ID
        Dta_Registro = datetime.now() #aJUSTAR PARA DATA DO DIA DO REGISTRO
        Usr = os.environ.get('Usr_login')
        
        CEP = ''
        Endereco = ''
        EndNr = ''
        EndCompl = ''
        EndBairro = ''
        
        TPer_Desconto_VPL = float(self.entry_taxa_desconto.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        Dta_Documento = self.entry_informacoes_data.get()  
        Dta_Documento = datetime.strptime(Dta_Documento, "%d/%m/%Y").date()  # Formato ajustado
        
        Tamanho_Area = float(self.entry_area_total.get().replace(" m²", "").replace(".", "").replace(",", ".")) 
        Per_Aproveitamento = float(self.entry_area_aproveitamento.get().replace("%", "").replace(",", ".")[:7]) / 100
        Area_aproveitada = float(self.entry_area_aproveitado.get().replace(" m²", "").replace(".", "").replace(",", ".")) 
        
        Medidas_Unidade = self.entry_area_lote_padrao.get()
        Unidade_Area_Media = float(self.entry_area_lote_medio.get().replace(" m²", "").replace('.', '').replace(',', '.')[:15])
        Quantidade_Unidades = float(self.entry_area_nr_lotes.get().replace('.', '').replace(',', '.')[:15])
        
        Per_Urban = float(self.entry_participacao_urbanizador.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_Parceiro = float(self.entry_participacao_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        TPer_PermutaLotes = float(self.entry_participacao_permuta.get().replace("%", "").replace(",", ".")[:7]) / 100
        TPer_Comissao_Negocio = float(self.entry_comissao_intermediacao.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_CustoAdm = float(self.entry_admmkt_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_Total_Urban = float(self.entry_total_urbanizadora.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_Total_Parceiro = float(self.entry_total_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        TInvestimento_Valor = float(self.entry_investimento_valor.get().replace('.', '').replace(',', '.')[:15])
        TInvestimento_Inicio = float(self.entry_investimento_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TInvestimento_Curva = self.entry_investimento_curva_investimento.get()
        TInvestimento_Aporte = self.entry_investimento_aporte.get()

        TAdtoParceiro_Valor = float(self.entry_adto_parceiro_valor.get().replace('.', '').replace(',', '.')[:15])
        TTAdtoParceiro_TaxaImob = float(self.entry_adto_parceiro_per_urbanizadora.get().replace("%", "").replace(",", ".")[:7]) / 100
        TTAdtoParceiro_TaxaParc = float(self.entry_adto_parceiro_per_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        TAdtoParceiro_Inicio = float(self.entry_adto_parceiro_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TAdtoParceiro_Curva = self.entry_adto_parceiro_curva_adto.get()

        Valor_m2_Venda = float(self.entry_vendas_preco_m2.get().replace('.', '').replace(',', '.')[:15])
        Per_Comissao_Venda = float(self.entry_vendas_comissao_per.get().replace("%", "").replace(",", ".")[:7]) / 100
        Valor_m2_com_comissao_Venda = float(self.entry_vendas_vendas_preco_m2_com_comissao.get().replace('.', '').replace(',', '.')[:15])
        Tickt_Medio = float(self.entry_vendas_lote_medio.get().replace('.', '').replace(',', '.')[:15])
        
        TVendas_FinanciamentoVendas_Prazo = float(self.entry_vendas_financiamento_prazo.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        Tvendas_Sistema_Amortizacao = self.entry_vendas_sistema_amortizacao.get()
        Per_Taxa = float(self.entry_vendas_juros_aa.get().replace("%", "").replace(",", ".")[:7]) / 100
        Per_Taxa_am = float(self.entry_vendas_juros_am.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        TVendas_Per_Entrada = float(self.entry_vendas_entrada.get().replace("%", "").replace(",", ".")[:7]) / 100
        Nr_ParEntrada = float(self.entry_vendas_nr_parcelas_entrada.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        TVendas_Per_Reforcos = float(self.entry_vendas_reforcos.get().replace("%", "").replace(",", ".")[:7]) / 100
        Nr_ParReforcos = float(self.entry_vendas_nr_parcelas_reforcos.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        Periodicidade_Reforcos = float(self.entry_vendas_period_reforcos.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TVendas_Per_aVista = float(self.entry_vendas_per_avista.get().replace("%", "").replace(",", ".")[:7]) / 100
        TVendas_Vendas_Inicio = float(self.entry_vendas_inicio.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TVendas_Vendas_Curva = self.entry_vendas_curva.get()
        PmT_PRICE = float(self.entry_vendas_parcela_price.get().replace('.', '').replace(',', '.')[:15])
        PmT_Sacoc = float(self.entry_vendas_parcela_sacoc.get().replace('.', '').replace(',', '.')[:15])

        TProjetos_Per = float(self.entry_projetos_per_obra.get().replace("%", "").replace(",", ".")[:7]) / 100
        TProjetos_Valor_Total = float(self.entry_projetos_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TProjetos_Inicio = float(self.entry_projetos_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TProjetos_Curva = self.entry_projetos_curva_projeto.get()

        TMkT_Per = float(self.entry_mkt_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
        TMkT_Valor_Total =  float(self.entry_mkt_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TMkT_Inicio = float(self.entry_mkt_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TMkT_Curva = self.entry_mkt_curva_mkt.get()

        TOverHead_Per = float(self.entry_overhead_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
        TOverHead_Valor_Total =  float(self.entry_overhead_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TOverHead_Inicio = float(self.entry_overhead_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TOverHead_Curva = self.entry_overhead_curva_overhead.get()

        TObras_Valor_m2 = float(self.entry_obras_valor_m2.get().replace('.', '').replace(',', '.')[:15]) 
        TObras_Valor_Total = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TObras_Inicio = float(self.entry_obras_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TObras_Curva = self.entry_obras_curva_obras.get()

        TPosObras_Per = float(self.entry_pos_obras_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
        TPosObras_Valor_Total = float(self.entry_pos_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TPosObras_Inicio = float(self.entry_pos_obras_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TPosObras_Curva = self.entry_pos_obras_curva_obras.get()

        TAdmObras_Per = float(self.entry_adm_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
        TAdmObras_Valor_Total = float(self.entry_adm_valor_total.get().replace('.', '').replace(',', '.')[:15])
        TAdmObras_Inicio = float(self.entry_adm_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TAdmObras_Curva = self.entry_adm_curva_obras.get()
        
        TFinancimento_Vlr_Captacao = float(self.entry_financiamento_valor_captacao.get().replace('.', '').replace(',', '.')[:15])
        TFinancimento_SistemaAmortizacao = self.entry_financiamento_sistema_amortizacao.get()
        TFinancimento_PrazoAmortizacao = float(self.entry_financiamento_prazo_amortizacao.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        TFinancimento_Inicio_Liberacao = float(self.entry_financiamento_inicio_liberacao.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TFinancimento_Inicio_Amortizacao = float(self.entry_financiamento_inicio_amortizacao.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TFinancimento_Inicio_PagtoJuros = float(self.entry_financiamento_inicio_pagto_juros.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        TFinancimento_Valor_Juros = float(self.entry_financiamento_juros.get().replace('.', '').replace(',', '.')[:15])
        TFinancimento_Taxa_Per = float(self.entry_financiamento_juros_aa.get().replace("%", "").replace(",", ".")[:7]) / 100
        TFinancimento_Curva = self.entry_financiamento_curva_liberacao.get()
        TFinancimento_Origem_Parceiro = self.entry_financiamento_financiador.get()
        
        TObservacaoNegocio = self.text_observacoes.get("1.0", "end")
        TStatus = self.entry_informacoes_status.get()
        if not TStatus:
            messagebox.showinfo('Gestor Negócios', 'Status do Estudo em Branco!!!', parent=self.janela_simulador_rel)
            return
        
        TAnexos = self.entry_informacoes_anexos.get()
        
        TDta_Contrato = self.entry_informacoes_data.get()
        TDta_Contrato = datetime.strptime(TDta_Contrato, "%d/%m/%Y")  # Ajuste o formato conforme necessário
        TDta_Contrato = TDta_Contrato.strftime("%Y-%m-%d")  # Formata a data
        
        TObservacao = self.entry_informacoes_https.get()
        EndCoordenadas = self.entry_informacoes_maps.get()

        TResultado_VGV_Bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
        TResultado_comissao_vendas = float(self.entry_dre_comissao.get().replace('.', '').replace(',', '.')[:15])
        TResultado_VGV_Liquido = float(self.entry_dre_vgv_liquido.get().replace('.', '').replace(',', '.')[:15])
        TResultado_impostos = float(self.entry_dre_impostos.get().replace('.', '').replace(',', '.')[:15])
        TResultado_comissao_negocio = float(self.entry_dre_comissao_negocio.get().replace('.', '').replace(',', '.')[:15])
        TResultado_Receita_Liquida = float(self.entry_dre_receita_liquida.get().replace('.', '').replace(',', '.')[:15])
        TResultado_VGV_Parceiro = float(self.entry_dre_vgv_parceiro.get().replace('.', '').replace(',', '.')[:15])
        TResultado_Receita_Urbanizador = float(self.entry_dre_receita_liquida_urbanizadora.get().replace('.', '').replace(',', '.')[:15])
        TResultado_Ebtda_Valor = float(self.entry_dre_ebtda_valor.get().replace('.', '').replace(',', '.')[:15])
        TResultado_Ebtda_Percente = float(self.entry_dre_ebtda_per.get().replace("%", "").replace(",", ".")[:7]) / 100
        TTIR_aa = float(self.entry_indicadores_tir_aa.get().replace("%", "").replace(",", ".")[:7]) / 100
        TTIR_am = float(self.entry_indicadores_tir_am.get().replace("%", "").replace(",", ".")[:7]) / 100
        TPayback = float(self.entry_indicadores_payback.get().replace(" Anos", "").replace(",", ".")[:7])
        TMultiplicador = float(self.entry_indicadores_multiplicador_investimento.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
        TExposicaoMaximaCaixa = float(self.entry_indicadores_exposicaomax_caixa.get().replace('.', '').replace(',', '.')[:15])
        TVPL_Urbanizadora = float(self.entry_indicadores_vpl_urbanizadora.get().replace('.', '').replace(',', '.')[:15])
        TVPL_Terreneiro = float(self.entry_indicadores_vpl_parceiro.get().replace('.', '').replace(',', '.')[:15])
        rs = self.Consulta_Negocio(ID_Empresa, UF, Cidade, Tipo, Nome_da_Area)
        
        if not rs:
            
            # Montagem da consulta SQL
            str_sql = """
                        INSERT INTO Dados_Prospeccao (
                        Empresa_ID, 
                        UF, 
                        Cidade, 
                        Nome_da_Area, 
                        Tipo, 
                        Unidade_ID, 
                        dta_registro, 
                        usr_registro,
                        
                        Area_EndCEP,
                        Area_EndLogradouro,
                        Area_EndNumero,
                        Area_EndComplemento,
                        Area_EndBairro,
                        
                        Area_Total_m2,
                        Per_Aproveitamento,
                        Area_Aproveitada,
                        Medidas_Lote,
                        Area_Lote_Medio,
                        Nr_Unidades,

                        Participação_Urbanizadora,
                        Participação_Parceiro,
                        Per_Permuta_em_Lotes,
                        Per_Comissão_Negócio,
                        Per_Adm_Mkt,
                        Participação_Total_Urbanizadora,
                        Participação_Total_Parceiro,

                        Investimento_Vlr_Parceiro,
                        Investimento_Inicio_Parceiro,
                        Investimento_Curva_Parceiro,
                        Aporte,

                        Vlr_Adiantamento_Parceiro,
                        Urbanizadora_Per_Taxa,
                        Parceiro_Per_Taxa,
                        Adiantamento_Inicio_Parceiro,
                        Adiantamento_Curva_Parceiro,

                        Valor_m2,
                        Per_Comissão,
                        Valor_m2_com_comissao,
                        tickt_medio,
                        Prazo_Financiamento,
                        Sistema_Amortização_Cliente,
                        Per_Juros,
                        Per_Juros_am,
                        
                        Per_Entrada,
                        Nr_Parc_Entrada,
                        Per_Reforços,
                        Nr_Parc_Reforços,
                        Periodicidade_Reforços,
                        Vendas_Per_Avista,
                        Vendas_Inicio,
                        Vendas_Curva,
                        PmT_PRICE,
                        PmT_Sacoc,
                        
                        Per_Impostos,

                        Projetos_Per_da_Obra,
                        Projetos_Valor,
                        Projetos_Inicio,
                        Projetos_Curva,
                        
                        Mkt_Per_VGV,
                        Mkt_Valor,
                        Mkt_Inicio,
                        Mkt_Curva,

                        Adm_Per_Receita,
                        OverHead_Valor,
                        OverHead_Inicio,
                        OverHead_Curva,

                        Custo_Obra_m2_Lote,
                        Obra_Valor,
                        Obra_Inicio,
                        Obra_Curva,
                        
                        Pos_Obra_Per_Obra,
                        Pos_Obra_Valor,
                        Pos_Obra_Inicio,
                        Pos_Obra_Curva,

                        AdmObras_Per_Obras,
                        AdmObras_Valor,
                        AdmObras_Inicio,
                        AdmObras_Curva,

                        Valor_Financiamento,
                        Sistema_Amortizacao,
                        Prazo_Amortizacao,
                        Inicio_Amortizacao,
                        Inicio_Pagto_Juros,
                        Taxa_Financiamento,
                        Liberacao_Financiamento,
                        Curva_Liberacao,
                        Financiador_Parceiro,
                        
                        ObservacaoNegocio,

                        DrE_VgV_Bruto,
                        DrE_comissao_venda,
                        DrE_VgV_Liquido,
                        DrE_impostos,
                        DrE_comissao_negocio,
                        DrE_Receita_Liquida,
                        DrE_Receita_Parceiro,
                        DrE_Receita_Urbanizador,
                        DrE_Ebtda_Valor,
                        DrE_Ebtda_Percente,
                        Tir_Urbanizadora,
                        Tir_Urbanizadora_am,
                        PayBack_Urbanizadora,
                        Multiplicador,
                        Vlr_Exposicao_Maxima,
                        VpL_Urbanizadora,
                        VpL_Parceiro,
                        
                        Status_Prospeccao,
                        Anexos,
                        Data_Contrato,
                        Observacao,
                        Area_EndCoordenadas,
                        VpL_Taxa_Desconto

                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
            # Definindo os valores a serem inseridos
            values = (
                ID_Empresa,
                UF,
                Cidade,
                Nome_Area,
                Tipo_Estudo,
                ID_Unidade,
                Dta_Registro.strftime("%Y-%m-%d"),  # Formata a data
                Usr,

                CEP,
                Endereco,
                EndNr,
                EndCompl,
                EndBairro,
               
                Tamanho_Area,
                Per_Aproveitamento,
                Area_aproveitada,
                Medidas_Unidade,
                Unidade_Area_Media,
                Quantidade_Unidades,
                
                Per_Urban,
                Per_Parceiro,
                TPer_PermutaLotes,
                TPer_Comissao_Negocio,
                Per_CustoAdm,
                Per_Total_Urban,
                Per_Total_Parceiro,
                
                TInvestimento_Valor,
                TInvestimento_Inicio,
                TInvestimento_Curva,
                TInvestimento_Aporte,
                
                TAdtoParceiro_Valor,
                TTAdtoParceiro_TaxaImob,
                TTAdtoParceiro_TaxaParc,
                TAdtoParceiro_Inicio,
                TAdtoParceiro_Curva,

                Valor_m2_Venda,
                Per_Comissao_Venda,
                Valor_m2_com_comissao_Venda,
                Tickt_Medio,
                TVendas_FinanciamentoVendas_Prazo, 
                Tvendas_Sistema_Amortizacao,
                Per_Taxa,
                Per_Taxa_am, 
                TVendas_Per_Entrada,
                Nr_ParEntrada,
                TVendas_Per_Reforcos,
                Nr_ParReforcos,
                Periodicidade_Reforcos,
                TVendas_Per_aVista,
                TVendas_Vendas_Inicio,
                TVendas_Vendas_Curva, 
                PmT_PRICE,
                PmT_Sacoc,

                TPer_Impostos,

                TProjetos_Per,
                TProjetos_Valor_Total,
                TProjetos_Inicio,
                TProjetos_Curva,

                TMkT_Per,
                TMkT_Valor_Total,
                TMkT_Inicio,
                TMkT_Curva,

                TOverHead_Per,
                TOverHead_Valor_Total,
                TOverHead_Inicio,
                TOverHead_Curva,

                TObras_Valor_m2,
                TObras_Valor_Total,
                TObras_Inicio, 
                TObras_Curva,
                
                TPosObras_Per,
                TPosObras_Valor_Total,
                TPosObras_Inicio,
                TPosObras_Curva,
                
                TAdmObras_Per,
                TAdmObras_Valor_Total,
                TAdmObras_Inicio,
                TAdmObras_Curva,
                
                TFinancimento_Vlr_Captacao,
                TFinancimento_SistemaAmortizacao, 
                TFinancimento_PrazoAmortizacao,
                TFinancimento_Inicio_Amortizacao,
                TFinancimento_Inicio_PagtoJuros,
                TFinancimento_Taxa_Per, 
                TFinancimento_Inicio_Liberacao,
                TFinancimento_Curva,
                TFinancimento_Origem_Parceiro,
                
                TObservacaoNegocio,

                TResultado_VGV_Bruto,
                TResultado_comissao_vendas,
                TResultado_VGV_Liquido,
                TResultado_impostos,
                TResultado_comissao_negocio,
                TResultado_Receita_Liquida,
                TResultado_VGV_Parceiro,
                TResultado_Receita_Urbanizador,
                TResultado_Ebtda_Valor,
                TResultado_Ebtda_Percente,
                TTIR_aa,
                TTIR_am,
                TPayback,
                TMultiplicador,
                TExposicaoMaximaCaixa,
                TVPL_Urbanizadora,
                TVPL_Terreneiro,

                TStatus,
                TAnexos,
                Dta_Documento, 
                TObservacao,
                EndCoordenadas,
                TPer_Desconto_VPL
                )
            # print(str_sql, values)

            myresult = db.executar_consulta(str_sql, (values))
        else:
            
            # Gravar a Alteração nos Demais Campos
            str_sql = """
                    UPDATE Dados_Prospeccao SET 
                        Unidade_ID                      = %s,

                        Area_Total_m2                   = %s,
                        Per_Aproveitamento              = %s,
                        Area_Aproveitada                = %s,
                        Medidas_Lote                    = %s,
                        Area_Lote_Medio                 = %s,
                        Nr_Unidades                     = %s,

                        Participação_Urbanizadora       = %s,
                        Participação_Parceiro           = %s,
                        Per_Permuta_em_Lotes            = %s,
                        Per_Comissão_Negócio            = %s,
                        Per_Adm_Mkt                     = %s,
                        Participação_Total_Urbanizadora = %s,
                        Participação_Total_Parceiro     = %s,

                        Investimento_Vlr_Parceiro       = %s,
                        Investimento_Inicio_Parceiro    = %s,
                        Investimento_Curva_Parceiro     = %s,
                        Aporte                          = %s,

                        Vlr_Adiantamento_Parceiro       = %s,
                        Urbanizadora_Per_Taxa           = %s,
                        Parceiro_Per_Taxa               = %s,
                        Adiantamento_Inicio_Parceiro    = %s,
                        Adiantamento_Curva_Parceiro     = %s,

                        Valor_m2                        = %s,
                        Per_Comissão                    = %s,
                        Valor_m2_com_comissao           = %s,
                        tickt_medio                     = %s,
                        Prazo_Financiamento             = %s,
                        Sistema_Amortização_Cliente     = %s,
                        Per_Juros                       = %s,
                        Per_Juros_am                    = %s,
                        
                        Per_Entrada                     = %s,
                        Nr_Parc_Entrada                 = %s,
                        Per_Reforços                    = %s,
                        Nr_Parc_Reforços                = %s,
                        Periodicidade_Reforços          = %s,
                        Vendas_Per_Avista               = %s,
                        Vendas_Inicio                   = %s,
                        Vendas_Curva                    = %s,
                        PmT_PRICE                       = %s,
                        PmT_Sacoc                       = %s,
                        
                        Per_Impostos                    = %s,

                        Projetos_Per_da_Obra            = %s,
                        Projetos_Valor                  = %s,
                        Projetos_Inicio                 = %s,
                        Projetos_Curva                  = %s,
                        
                        Mkt_Per_VGV                     = %s,
                        Mkt_Valor                       = %s,
                        Mkt_Inicio                      = %s,
                        Mkt_Curva                       = %s,

                        Adm_Per_Receita                 = %s,
                        OverHead_Valor                  = %s,
                        OverHead_Inicio                 = %s,
                        OverHead_Curva                  = %s,

                        Custo_Obra_m2_Lote              = %s,
                        Obra_Valor                      = %s,
                        Obra_Inicio                     = %s,
                        Obra_Curva                      = %s,
                        
                        Pos_Obra_Per_Obra               = %s,
                        Pos_Obra_Valor                  = %s,
                        Pos_Obra_Inicio                 = %s,
                        Pos_Obra_Curva                  = %s,

                        AdmObras_Per_Obras              = %s,
                        AdmObras_Valor                  = %s,
                        AdmObras_Inicio                 = %s,
                        AdmObras_Curva                  = %s,

                        Valor_Financiamento             = %s,
                        Sistema_Amortizacao             = %s,
                        Prazo_Amortizacao               = %s,
                        Inicio_Amortizacao              = %s,
                        Inicio_Pagto_Juros              = %s,
                        Taxa_Financiamento              = %s,
                        Liberacao_Financiamento         = %s,
                        Curva_Liberacao                 = %s,
                        Financiador_Parceiro            = %s,
                        
                        ObservacaoNegocio               = %s,

                        DrE_VgV_Bruto                   = %s,
                        DrE_comissao_venda              = %s,
                        DrE_VgV_Liquido                 = %s,
                        DrE_impostos                    = %s,
                        DrE_comissao_negocio            = %s,
                        DrE_Receita_Liquida             = %s,
                        DrE_Receita_Parceiro            = %s,
                        DrE_Receita_Urbanizador         = %s,
                        DrE_Ebtda_Valor                 = %s,
                        DrE_Ebtda_Percente              = %s,
                        Tir_Urbanizadora                = %s,
                        Tir_Urbanizadora_am             = %s,
                        PayBack_Urbanizadora            = %s,
                        Multiplicador                   = %s,
                        Vlr_Exposicao_Maxima            = %s,
                        VpL_Urbanizadora                = %s,
                        VpL_Parceiro                    = %s,
                        
                        Status_Prospeccao               = %s,
                        Anexos                          = %s,
                        Data_Contrato                   = %s,
                        Observacao                      = %s,
                        Area_EndCoordenadas             = %s,
                        VpL_Taxa_Desconto               = %s
                        
                    
                    WHERE Empresa_ID = %s
                        AND UF = %s
                        AND Cidade = %s
                        AND Tipo = %s
                        AND Nome_da_Area = %s
                    """

            # Definindo os valores a serem inseridos
            values = (
                    ID_Unidade,

                    Tamanho_Area,
                    Per_Aproveitamento,
                    Area_aproveitada,
                    Medidas_Unidade,
                    Unidade_Area_Media,
                    Quantidade_Unidades,
                    
                    Per_Urban,
                    Per_Parceiro,
                    TPer_PermutaLotes,
                    TPer_Comissao_Negocio,
                    Per_CustoAdm,
                    Per_Total_Urban,
                    Per_Total_Parceiro,
                    
                    TInvestimento_Valor,
                    TInvestimento_Inicio,
                    TInvestimento_Curva,
                    TInvestimento_Aporte,
                    
                    TAdtoParceiro_Valor,
                    TTAdtoParceiro_TaxaImob,
                    TTAdtoParceiro_TaxaParc,
                    TAdtoParceiro_Inicio,
                    TAdtoParceiro_Curva,

                    Valor_m2_Venda,
                    Per_Comissao_Venda,
                    Valor_m2_com_comissao_Venda,
                    Tickt_Medio,
                    TVendas_FinanciamentoVendas_Prazo, 
                    Tvendas_Sistema_Amortizacao,
                    Per_Taxa,
                    Per_Taxa_am, 
                    TVendas_Per_Entrada,
                    Nr_ParEntrada,
                    TVendas_Per_Reforcos,
                    Nr_ParReforcos,
                    Periodicidade_Reforcos,
                    TVendas_Per_aVista,
                    TVendas_Vendas_Inicio,
                    TVendas_Vendas_Curva, 
                    PmT_PRICE,
                    PmT_Sacoc,

                    TPer_Impostos,

                    TProjetos_Per,
                    TProjetos_Valor_Total,
                    TProjetos_Inicio,
                    TProjetos_Curva,

                    TMkT_Per,
                    TMkT_Valor_Total,
                    TMkT_Inicio,
                    TMkT_Curva,

                    TOverHead_Per,
                    TOverHead_Valor_Total,
                    TOverHead_Inicio,
                    TOverHead_Curva,

                    TObras_Valor_m2,
                    TObras_Valor_Total,
                    TObras_Inicio, 
                    TObras_Curva,
                    
                    TPosObras_Per,
                    TPosObras_Valor_Total,
                    TPosObras_Inicio,
                    TPosObras_Curva,
                    
                    TAdmObras_Per,
                    TAdmObras_Valor_Total,
                    TAdmObras_Inicio,
                    TAdmObras_Curva,
                    
                    TFinancimento_Vlr_Captacao,
                    TFinancimento_SistemaAmortizacao, 
                    TFinancimento_PrazoAmortizacao,
                    TFinancimento_Inicio_Amortizacao,
                    TFinancimento_Inicio_PagtoJuros,
                    TFinancimento_Taxa_Per, 
                    TFinancimento_Inicio_Liberacao,
                    TFinancimento_Curva,
                    TFinancimento_Origem_Parceiro,
                    
                    TObservacaoNegocio,

                    TResultado_VGV_Bruto,
                    TResultado_comissao_vendas,
                    TResultado_VGV_Liquido,
                    TResultado_impostos,
                    TResultado_comissao_negocio,
                    TResultado_Receita_Liquida,
                    TResultado_VGV_Parceiro,
                    TResultado_Receita_Urbanizador,
                    TResultado_Ebtda_Valor,
                    TResultado_Ebtda_Percente,
                    TTIR_aa,
                    TTIR_am,
                    TPayback,
                    TMultiplicador,
                    TExposicaoMaximaCaixa,
                    TVPL_Urbanizadora,
                    TVPL_Terreneiro,

                    TStatus,
                    TAnexos,
                    Dta_Documento,
                    TObservacao,
                    EndCoordenadas,
                    TPer_Desconto_VPL,
                    
                    ID_Empresa,
                    UF,
                    Cidade,
                    Tipo_Estudo,
                    Nome_Area
                    )
            
            myresult = db.executar_consulta(str_sql, values)

        # GRAVAR FLUXO DE CAIXA MENSAL
        Dta_Inicio = TDta_Contrato
        if TStatus == "Contratado":
            Dta_Inicio = datetime.strptime(Dta_Inicio, '%Y-%m-%d')  # Ajuste conforme necessário
            Dta_Inicio = Dta_Inicio.replace(day=self.ult_dia_mes(Dta_Inicio))

            str_sql = """
                SELECT * FROM Dados_Fluxo
                WHERE Empresa_ID = %s 
                AND UF = %s 
                AND Cidade = %s 
                AND Tipo = %s 
                AND Nome_da_Area = %s 
                AND Periodo_Nr = %s
                """
            # Executando a consulta com os parâmetros
            params = (ID_Empresa, UF, Cidade, Tipo_Estudo, Nome_Area, vi_contador)
            myresult = db.executar_consulta(str_sql, params)
            
            if myresult:
                str_sql = """
                        DELETE FROM Dados_Fluxo
                        WHERE Empresa_ID = %s 
                        AND UF = %s 
                        AND Cidade = %s 
                        AND Tipo = %s 
                        AND Nome_da_Area = %s 
                      """
                # Executando a consulta com os parâmetros
                params = (ID_Empresa, UF, Cidade, Tipo_Estudo, Nome_Area)
                myresult = db.executar_consulta(str_sql, params)

            for vi_contador in range(0, self.nr_anos_projeto):
                # Montagem da consulta SQL
                str_sql = """
                INSERT INTO Dados_Fluxo (
                    Empresa_ID, 
                    UF, 
                    Cidade, 
                    Nome_da_Area, 
                    Tipo, 
                    Periodo_Nr, 
                    Periodo_Dta, 
                    Valor_Vendas, 
                    Valor_Parcelas, 
                    Valor_Terreno, 
                    Valor_Projetos, 
                    Valor_Obras, 
                    Valor_AdmObras, 
                    Valor_Mkt, 
                    Valor_PosObras, 
                    Valor_Adm, 
                    Valor_Parcelas_Parceiro, 
                    Valor_Comissao_Venda, 
                    Valor_Comissao_Negocio, 
                    Valor_Impostos, 
                    Valor_Adto, 
                    Valor_CustoAdto, 
                    Valor_CustoAdtoPar,
                    Valor_AmortAdto, 
                    Valor_Liberacao, 
                    Vlr_ParcelaFinanciamento,
                    Valor_Fx,
                    Valor_Fx_Acumulado
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                """
                # Formatação da data
                dta_inicio_formatada = Dta_Inicio.strftime("%Y-%m-%d")

                # Definindo os valores a serem inseridos
                values = (
                    ID_Empresa,
                    UF,
                    Cidade,
                    Nome_Area,
                    Tipo_Estudo,
                    float(vi_contador+1),
                    dta_inicio_formatada,
                    float(self.Valor_Mensal[vi_contador]),
                    float(self.Valor_Parcelas[vi_contador]),
                    float(self.Valor_Terreno[vi_contador]),
                    float(self.Valor_Projetos[vi_contador]),
                    float(self.Valor_Obras[vi_contador]),
                    float(self.Valor_Adm_Obras[vi_contador]),
                    float(self.Valor_Mkt[vi_contador]),
                    float(self.Valor_PosObras[vi_contador]),
                    float(self.Valor_Adm[vi_contador]),
                    float(self.Valor_Parcelas_Parceiro[vi_contador]),
                    float(self.Valor_Comissao_Venda[vi_contador]),
                    float(self.Valor_Comissao_Negocio[vi_contador]),
                    float(self.Valor_Impostos[vi_contador]),
                    float(self.Valor_Adto[vi_contador]),
                    float(self.Valor_CustoAdto[vi_contador]),
                    float(self.Valor_CustoAdtoPar[vi_contador]),
                    float(self.Valor_DevolucaoAdto[int(vi_contador)]),
                    float(self.Valor_Liberacao[vi_contador]),
                    float(self.Valor_ParcelaFinanciamento[vi_contador]),
                    float(self.Fluxo[vi_contador]),
                    float(self.FluxoAcumulado[vi_contador])
                )
                myresult = db.executar_consulta(str_sql, (values))
                Dta_Inicio = Dta_Inicio + relativedelta(months=1)
                
        else:
            str_sql = """
                        SELECT * FROM Dados_Fluxo
                        WHERE Empresa_ID = %s 
                        AND UF = %s 
                        AND Cidade = %s 
                        AND Tipo = %s 
                        AND Nome_da_Area = %s 
                      """
                # Executando a consulta com os parâmetros
            params = (ID_Empresa, UF, Cidade, Tipo_Estudo, Nome_Area)
            myresult = db.executar_consulta(str_sql, params)
            
            if myresult:
                str_sql = """
                        DELETE FROM Dados_Fluxo
                        WHERE Empresa_ID = %s 
                        AND UF = %s 
                        AND Cidade = %s 
                        AND Tipo = %s 
                        AND Nome_da_Area = %s 
                      """
                # Executando a consulta com os parâmetros
                params = (ID_Empresa, UF, Cidade, Tipo_Estudo, Nome_Area)
                myresult = db.executar_consulta(str_sql, params)
            
            for vi_contador in range(0, self.nr_anos_projeto):
                # Montagem da consulta SQL
                str_sql = """
                INSERT INTO Dados_Fluxo (
                    Empresa_ID, 
                    UF, 
                    Cidade, 
                    Nome_da_Area, 
                    Tipo, 
                    Periodo_Nr,
                    Valor_Vendas, 
                    Valor_Parcelas, 
                    Valor_Terreno, 
                    Valor_Projetos, 
                    Valor_Obras, 
                    Valor_AdmObras, 
                    Valor_Mkt, 
                    Valor_PosObras, 
                    Valor_Adm, 
                    Valor_Parcelas_Parceiro, 
                    Valor_Comissao_Venda, 
                    Valor_Comissao_Negocio, 
                    Valor_Impostos, 
                    Valor_Adto, 
                    Valor_CustoAdto, 
                    Valor_CustoAdtoPar,
                    Valor_AmortAdto, 
                    Valor_Liberacao, 
                    Vlr_ParcelaFinanciamento,
                    Valor_Fx,
                    Valor_Fx_Acumulado
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                """
                # Definindo os valores a serem inseridos
                
                values = (
                    ID_Empresa,
                    UF,
                    Cidade,
                    Nome_Area,
                    Tipo_Estudo,
                    float(vi_contador+1),
                    float(self.Valor_Mensal[vi_contador]),
                    float(self.Valor_Parcelas[vi_contador]),
                    float(self.Valor_Terreno[vi_contador]),
                    float(self.Valor_Projetos[vi_contador]),
                    float(self.Valor_Obras[vi_contador]),
                    float(self.Valor_Adm_Obras[vi_contador]),
                    float(self.Valor_Mkt[vi_contador]),
                    float(self.Valor_PosObras[vi_contador]),
                    float(self.Valor_Adm[vi_contador]),
                    float(self.Valor_Parcelas_Parceiro[vi_contador]),
                    float(self.Valor_Comissao_Venda[vi_contador]),
                    float(self.Valor_Comissao_Negocio[vi_contador]),
                    float(self.Valor_Impostos[vi_contador]),
                    float(self.Valor_Adto[vi_contador]),
                    float(self.Valor_CustoAdto[vi_contador]),
                    float(self.Valor_CustoAdtoPar[vi_contador]),
                    float(self.Valor_DevolucaoAdto[int(vi_contador)]),
                    float(self.Valor_Liberacao[vi_contador]),
                    float(self.Valor_ParcelaFinanciamento[vi_contador]),
                    float(self.Fluxo[vi_contador]),
                    float(self.FluxoAcumulado[vi_contador])
                )
                myresult = db.executar_consulta(str_sql, (values))   

        Tela.focus()
        messagebox.showinfo('Gestor Negócios', 'Concluído!!!', parent=self.janela_simulador_rel)
class Consultas_Financeiro():
    
    def calcular_total_itens(self, event, target):
        if self.entry_itens_nota_quant2.get() != '':
            item_quantidade = float(self.entry_itens_nota_quant2.get().replace('.', '').replace(',', '.')[:15])
        else:
            item_quantidade = 0

        if self.entry_itens_nota_valor_unit.get() != '':
            item_valor = float(self.entry_itens_nota_valor_unit.get().replace('.', '').replace(',', '.')[:15])
        else:
            item_valor = 0
        item_valor_total = item_quantidade * item_valor

        target.delete(0, 'end')  # Limpa o campo
        target.insert(0, self.format_valor_fx(item_valor_total))

    def incluir_parcelas_click(self):
        if self.entry_info_pag_forma_liq.get() != "":
            nr_de_parcelas = int(self.entry_doc_parcelas.get())
            nr_da_parcela = int(self.entry_info_pag_nr_parc.get())
            
            if self.entry_info_pag_valor_parc.get() == '':
                valor_parcela = 0
            else:
                valor_parcela = float(self.entry_info_pag_valor_parc.get().replace('.', '').replace(',', '.')[:15])
            
            if self.entry_doc_valor_total.get() == '':
                valor_total = 0
            else:
                valor_total = float(self.entry_doc_valor_total.get().replace('.', '').replace(',', '.')[:15])

            self.Vlr +=  valor_parcela
            
            if valor_total > 0 and self.Vlr <= valor_total:
                if nr_da_parcela <= nr_de_parcelas:
                    if (nr_da_parcela == nr_de_parcelas and self.Vlr != valor_total):
                        messagebox.showerror("Erro", "Valor Total das Parcelas tem que ser igual ao Valor Total do Documento!")
                        self.entry_info_pag_nr_parc.delete(0, 'end')  # Limpa o campo
                        self.entry_info_pag_nr_parc.insert(0, 1)
                        self.Vlr = 0  # Reset value
                        self.LSites.delete(0, ctk.END)  # Clear the Listbox
                        self.entry_info_pag_nr_parc.focus  # Set focus back to installment number
                        return
                    
                    else:
                        self.incluir_parcelas()  # INCLUIR NO LIST

                        current_value = int(self.entry_info_pag_nr_parc.get()) + 1
                        Dta_Vencto = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
                        self.entry_info_pag_nr_parc.delete(0, 'end')  # Limpa o campo
                        self.entry_info_pag_nr_parc.insert(0, str(current_value))  # Insere o novo valor
                        self.entry_info_pag_dt_venc.delete(0, 'end')  # Limpa o campo
                        self.entry_info_pag_dt_venc.insert(0, Dta_Vencto)
                else:
                    self.entry_info_pag_forma_liq.focus()
                    messagebox.showinfo('Gestor Negócios', 'Nr de Parcelas Concluídas!!!')
                    # Set focus to another input field (not implemented here)
            else:
                messagebox.showerror("Erro", "Valor da soma das parcelas não pode ser diferente do Valor da Documento!")
                self.Vlr -=  valor_parcela
                self.entry_info_pag_valor_parc.focus()
                self.entry_info_pag_valor_parc.delete(0, 'end')  # Limpa o campo

        else:
            messagebox.showerror("Erro", "Preencher a Forma de Liquidação!")
            # Set focus back to the payment method (not implemented here)

    def incluir_parcelas(self):
        # Create a new entry in the Treeview
        try:
            lista = self.LParcelasFinanceiras.insert("", "end", text=self.entry_info_pag_nr_parc.get())
            # Insert the subitems
            self.LParcelasFinanceiras.item(lista, values=(
                self.entry_info_pag_nr_parc.get(),
                self.entry_info_pag_dt_venc.get(),
                self.entry_info_pag_valor_parc.get(),
                self.entry_info_pag_forma_liq.get()
            ))

            # Update total parcel value
            self.Vlr_TotalParcelas += float(self.entry_info_pag_valor_parc.get().replace('.', '').replace(',', '.')[:15])

            # Sort the Treeview if needed
            self.LParcelasFinanceiras.heading('Nr', text='Nr.')
            self.LParcelasFinanceiras.heading('Dta_Vcto', text='Dta Vcto')
            self.LParcelasFinanceiras.heading('Valor', text='Valor')
            self.LParcelasFinanceiras.heading('Forma_Pagto', text='Forma de Liquidação')
            

            # print(f"Total de Parcelas: {self.Vlr_TotalParcelas:.2f}")  # Print or update the total as necessary
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao incluir a parcela: {str(e)}", parent=self.window_one)

    def incluir_itens_click(self):
        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.', parent=self.window_one)
            return

        documento_valor_total = float(self.entry_doc_valor_total.get().replace('.', '').replace(',', '.')[:15])

        if self.entry_itens_nota_prod_descr.get() != '':
            item_produto = self.entry_itens_nota_prod_descr.get()
        else:
            messagebox.showerror("Erro", "Preencher o Produto!", parent=self.window_one)
            return
        
        if  self.entry_itens_nota_centro.get() != '':
            item_centro = self.entry_itens_nota_centro.get()
        else:
            messagebox.showerror("Erro", "Preencher o Centro Resultado!", parent=self.window_one)
            return
        
        if self.entry_itens_nota_natureza.get() != '':
            item_natureza = self.entry_itens_nota_natureza.get()
        else:
            messagebox.showerror("Erro", "Preencher a Natureza Financeira!", parent=self.window_one)
            return
        
        ID_Produto = self.obter_Produto_ID(item_produto)
        ID_CR = self.obter_Centro_ID(item_centro)
        ID_Nat = self.obter_Natureza_ID(item_natureza)
        
        if self.entry_itens_nota_peso.get() != '': 
            item_peso = float(self.entry_itens_nota_peso.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Peso em branco, Preecher pelo menos com zero!", parent=self.window_one)
            return
        
        if self.entry_itens_nota_quant2.get() != '':
            item_quantidade = float(self.entry_itens_nota_quant2.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Quantidade em branco, Preecher com valor!", parent=self.window_one)
            return
        
        if self.entry_itens_nota_valor_unit != '':
            item_valor_unitario = float(self.entry_itens_nota_valor_unit.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Valor Unitário em branco, Preecher com valor!", parent=self.window_one)
            return
        
        item_valor_total = float(self.entry_itens_nota_valor_total.get().replace('.', '').replace(',', '.')[:15])
            
        # Create a new item in the Listbox
        # item_text = self.Nr_Item
        # self.LItens.insert(ctk.END, item_text)  # Add new item to Listbox
        
        # Prepare the SQL SELECT statement to check if the item exists
        select_sql = """
                        SELECT * 
                            FROM TB_Itens ii
                        WHERE 
                            ii.ID_Empresa = %s 
                            AND ii.ID_Pessoa = %s 
                            AND ii.ID_Unidade = %s 
                            AND ii.Doc_Num_Documento = %s 
                            AND ii.Item_Nr = %s
                    """
        
        myresult = db.executar_consulta(select_sql, (str(ID_Empresa), str(ID_Fornecedor), int(ID_Unidade), str(Nr_Documento), str(self.Nr_Item)))
        
        # If the record exists
        if myresult:
            # Update the item's values based on the input fields
            # update_sql = """
            #                 UPDATE TB_Itens SET 
            #                     ID_Produto = %s, 
            #                     ID_CR = %s, 
            #                     ID_Natureza = %s
            #                 WHERE 
            #                     ID_Empresa = %s 
            #                     AND ID_Pessoa = %s 
            #                     AND ID_Unidade = %s 
            #                     AND Doc_Num_Documento = %s 
            #                     AND Item_Nr = %s
            #              """
            
            # # Execute the update with the new values
            # values = (
            #             ID_Produto,
            #             ID_CR,
            #             ID_Nat,
            #             ID_Empresa, 
            #             ID_Fornecedor, 
            #             ID_Unidade, 
            #             Nr_Documento, 
            #             self.Nr_Item                        
            #         )
            # myresult = db.executar_consulta(update_sql, values)
            # messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")
            self.limpar_campos_lcto
            self.Vlr = 0
            self.Vlr_TotalItens = 0
            self.vlr_soma_itens = 0

            self.consulta_lcto()
            messagebox.showinfo("Erro", "Documento já existe, com Itens Cadastrado!", parent=self.window_one)
            
        else:
            self.vlr_soma_itens += item_valor_total  # Existing total value of items
            vlr_total = documento_valor_total  # Get the total value from the item field

            # Check if the total value of items does not exceed document total
            if round(self.vlr_soma_itens, 2) <= round(vlr_total, 2):
                # Increment item count
                valor_decimal = '0,00'
                self.NrCampos += 1  # Assuming NrCampos is tracked in your class

                # Call the function to include items (the equivalent of Incluir_Itens)
                self.incluir_itens()  # Ensure this method handles adding items to whatever structure you use

                # Reset input fields after inclusion
                self.entry_itens_nota_prod_descr.set("")
                self.entry_itens_nota_centro.set("")
                self.entry_itens_nota_natureza.set("")

                self.entry_itens_nota_peso.delete(0, 'end')  # Limpa o campo
                self.entry_itens_nota_peso.insert(0, valor_decimal)
                
                self.entry_itens_nota_quant2.delete(0, 'end')  # Limpa o campo
                self.entry_itens_nota_quant2.insert(0, valor_decimal)
                
                self.entry_itens_nota_valor_unit.delete(0, 'end')  # Limpa o campo
                self.entry_itens_nota_valor_unit.insert(0, valor_decimal)
                
                self.entry_itens_nota_valor_total.delete(0, 'end')  # Limpa o campo
                self.entry_itens_nota_valor_total.insert(0, valor_decimal)
            
                # Set focus back to the product ID input
                self.entry_itens_nota_prod_descr.focus()  # Note: use focus() for Tkinter SetFocus equivalent

            else:
                # If the total of items exceeds the document value, show an error message
                self.vlr_soma_itens -= item_valor_total  # Adjust the current total value
                messagebox.showerror("Erro", "Soma dos Itens não pode ser Maior que o Valor Total do Documento!", parent=self.window_one)
                self.entry_itens_nota_prod_descr.focus()  # Set focus to the product ID input       

    def incluir_itens(self):
        item_peso = float(self.entry_itens_nota_peso.get().replace('.', '').replace(',', '.')[:15])
        item_quantidade = float(self.entry_itens_nota_quant2.get().replace('.', '').replace(',', '.')[:15])
        item_valor_unitario = float(self.entry_itens_nota_valor_unit.get().replace('.', '').replace(',', '.')[:15])
        item_valor_total = float(self.entry_itens_nota_valor_total.get().replace('.', '').replace(',', '.')[:15])
        
        if item_valor_total == 0:
            messagebox.showinfo('Gestor Negócios', 'Erro Valor Total do Item não pode ser Zero!!!.', parent=self.window_one)
            return
        
        # Create a new item in the list
        item_id = len(self.LItens.get_children()) + 1 # Simple ID based on current item count
        item_values = (
                        item_id,
                        self.entry_itens_nota_prod_descr.get(),
                        self.entry_itens_nota_centro.get(),
                        self.entry_itens_nota_natureza.get(),
                        self.format_valor_fx(item_peso),
                        self.format_valor_fx(item_quantidade),
                        self.format_valor_fx(item_valor_unitario),
                        self.format_valor_fx(item_valor_total)
                    )

        # Add the item to the Treeview
        self.LItens.insert('', 'end', values=item_values)
        
        # Update total items value
        item_valor_total = float(self.entry_itens_nota_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_TotalItens += item_valor_total
        
    def gravar_lcto(self):
        Modulo_Financeiro = self.entry_tipo_lcto_descr.get()
        
        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.')
            return
        
        NotaEstado = self.combo_uf.get()
        Frete_DS = self.combo_frete.get()
        Frete = self.obter_Frete_ID(self.combo_frete.get(), self.window_one) 
        Dta_Lcto = datetime.now() #aJUSTAR PARA DATA DO DIA DO REGISTRO
        Dta_Documento = datetime.strptime(self.entry_doc_dt_emissao.get(), "%d/%m/%Y")
        Dta_Documento = Dta_Documento.strftime("%Y-%m-%d")
        SerieNota = self.entry_doc_serie.get()
        Nr_Contrato = self.entry_doc_numcontrato.get()
        Vlr_Documento = float(self.entry_doc_valor_total.get().replace('.', '').replace(',', '.')[:15])
                
        DS_Observacao = self.text_historico.get("1.0", "end")
        Aprovacao = "N"
        
        if not Nr_Documento:
            messagebox.showerror("Erro", "Erro - NR do Documento em Branco!")
            return
        
        if Modulo_Financeiro == "CPA":
            TipoLan = "D"
        elif Modulo_Financeiro == "CRE":
            TipoLan = "C"
        else:
            messagebox.showerror("Erro", "Erro: Informe CPA:Contas a Pagar ou CRE:Contas a Receber!")
            return

        check_empresa_sql = """
                                SELECT Pessoas_Proprietaria FROM TB_Pessoas
                                WHERE Pessoas_CPF_CNPJ = %s
                            """
        myresult = db.executar_consulta(check_empresa_sql, ID_Empresa)
        
        if myresult is None:
            messagebox.showerror("Erro", "Erro Empresa não Cadastrada!")
            return

        # Validate other fields
        if not ID_Empresa:
            messagebox.showerror("Erro", "Código da Empresa em Branco!")
            return

        # Assuming further field validation as per your original VBA code...
        if not ID_Fornecedor:
            messagebox.showerror("Erro", "Código Favorecido em Branco!")
            return

        if not ID_Unidade:
            messagebox.showerror("Erro", "Código da Unidade/Fazenda em Branco!")
            return

        if not Nr_Documento:
            messagebox.showerror("Erro", "Nr. Documento em Branco!")
            return

        if not NotaEstado:
            messagebox.showerror("Erro", "Estado em Branco!")
            return

        # Validate if state is registered
        if NotaEstado:
            myresult = db.executar_consulta("SELECT * FROM Estados WHERE UF = %s", NotaEstado)
            if myresult is None:
                messagebox.showerror("Erro", "UF Não Cadastrada!")
                return

        # Validate document date
        try:
            datetime.strptime(Dta_Documento, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Data do documento com preenchimento errado!")
            return

        # Validate document amount
        if Vlr_Documento <= 0:
            messagebox.showerror("Erro", "Valor do documento em branco ou zero!")
            return
        
        # Check if TipoLan is "D" (likely meaning "Debito" or similar)
        if TipoLan == "D":
            Vlr_Documento *= -1  # Negate the document value
            
            # Check if the rounded total value of parcels matches the document value
            if round(self.Vlr_TotalParcelas * -1, 2) != round(Vlr_Documento, 2):
                print(round(self.Vlr_TotalParcelas * -1, 2), round(Vlr_Documento, 2))
                messagebox.showerror("Erro", "Valor das Parcelas Não Fecha com Valor do Documento!")
                return False
                
            # Check if the rounded total value of items matches the document value
            if round(self.Vlr_TotalItens * -1, 2) != round(Vlr_Documento, 2):
                print(round(self.Vlr_TotalItens * -1, 2), round(Vlr_Documento, 2))
                messagebox.showerror("Erro", "Valor dos Itens Não Fecha com Valor do Documento!")
                return False
        
        else:
            # For the case when TipoLan is not "D"
            if round(self.Vlr_TotalParcelas, 2) != round(Vlr_Documento, 2):
                messagebox.showerror("Erro", "Valor das Parcelas Não Fecha com Valor do Documento!")
                return False
            
            if round(self.Vlr_TotalItens, 2) != round(Vlr_Documento, 2):
                messagebox.showerror("Erro", "Valor dos Itens Não Fecha com Valor do Documento!")
                return False

        # Check if the freight value is empty
        if not Frete or Frete == "":
            messagebox.showerror("Erro", "Valor do documento em branco ou zero!")
            return False
        
        strSql = """
                    SELECT 
                    cb.Doc_Tipo, 
                    cb.Doc_Dta_Lcto, 
                    cb.Doc_Dta_Documento,
                    cb.Doc_Num_Documento, 
                    cb.ID_Empresa, 
                    cb.ID_Pessoa,
                    cb.ID_Unidade, 
                    cb.Doc_VlR, 
                    cb.Doc_Num_Contrato,
                    cb.Doc_DS_Observacao, 
                    cb.Doc_Aprovacao
                    FROM TB_CB_Doc cb
                    WHERE Doc_Tipo = %s 
                    AND cb.ID_Empresa = %s 
                    AND cb.ID_Pessoa = %s 
                    AND cb.ID_Unidade = %s 
                    AND cb.Doc_Num_Documento = %s
                """
        values = (
                    TipoLan, 
                    ID_Empresa, 
                    ID_Fornecedor, 
                    ID_Unidade, 
                    Nr_Documento
                    )
        try:
            myresult = db.executar_consulta(strSql, values)
            
            # Fetch results
            if myresult:
                messagebox.showerror("Erro", "Erro - Documento Já Existe!")
                return
            
            # Continue with further operations since the document does not exist
            # messagebox.showinfo("Sucesso", "Documento verificado com sucesso!")
            strSql = """
                        INSERT INTO TB_CB_Doc (
                                                Doc_Tipo, 
                                                Doc_Aprovacao, 
                                                Doc_Dta_Lcto, 
                                                Doc_Dta_Documento, 
                                                Doc_Num_Documento, 
                                                ID_Empresa, 
                                                ID_Pessoa, 
                                                ID_Unidade, 
                                                Doc_VlR, 
                                                Doc_Num_Contrato, 
                                                Doc_Serie, 
                                                Doc_Estado, 
                                                Doc_Frete, 
                                                Doc_DS_Observacao
                                                )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            values = (
                    TipoLan,  
                    Aprovacao,
                    Dta_Lcto.strftime("%Y-%m-%d"),  
                    Dta_Documento,  
                    Nr_Documento,  
                    ID_Empresa,  
                    ID_Fornecedor,  
                    ID_Unidade,  
                    Vlr_Documento,  
                    Nr_Contrato,
                    SerieNota,  
                    NotaEstado,  
                    Frete,  
                    DS_Observacao.replace("'", " ")  
                )
            
            myresult = db.executar_consulta(strSql, values)
            messagebox.showinfo("Sucesso", "Compras gravadas com sucesso!")
            
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

        
        # Assuming you have a Listbox or similar widget storing your financial parcels
        nr_total_parcelas = len(self.LParcelasFinanceiras.get_children())
        parcelas_ids = self.LParcelasFinanceiras.get_children()
        
        for i in range(0, nr_total_parcelas):
            item_parcela = self.LParcelasFinanceiras.item(parcelas_ids[i])
            values = item_parcela['values'] 
            Nr_Parcela =  values[0]
            data_vcto = datetime.strptime(values[1], "%d/%m/%Y") 
            Dta_Parc = data_vcto.strftime("%Y-%m-%d") 
            Vlr_Parc = float(values[2].replace('.', '').replace(',', '.')[:15])
            FormaLiquidacao_ID = self.obter_FormaLiquidacao_ID(values[3]) 
            if TipoLan == "D":
                Vlr_Parc *= -1  # Negate the value if TipoLan is "D"

            if Vlr_Parc != 0:
                # Prepare the SQL INSERT statement
                strSql = """
                        INSERT INTO TB_Financeiro (
                                                    Fin_Num_Documento, 
                                                    ID_Empresa, 
                                                    ID_Pessoa, 
                                                    ID_Unidade,
                                                    Fin_Parcela, 
                                                    Fin_Dta_Vcto, 
                                                    Fin_Vlr_Parcela, 
                                                    TipoPagamento_ID
                                                    ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """
                values = (
                            Nr_Documento,
                            ID_Empresa,
                            ID_Fornecedor,
                            ID_Unidade,
                            Nr_Parcela,
                            Dta_Parc,  
                            Vlr_Parc,
                            FormaLiquidacao_ID  
                        )
                # Execute the insert statement with parameters
                try:
                    myresult = db.executar_consulta(strSql, values)
                    
                except Exception as e:
                    messagebox.showerror("Erro", f"Ocorreu um erro ao salvar parcelas: {str(e)}")
        nr_total_itens = len(self.LItens.size()) - 1
        item_ids = self.LItens.get_children()
        for i in range(0, nr_total_itens):
            item = self.LItens.item(item_ids[i])
            values = item['values']
            Nr_Item = values[0]  
            ID_Produto = self. obter_Produto_ID(values[1])  
            ID_CR = self.obter_Centro_ID(values[2])      
            ID_Nat = self.obter_Natureza_ID(values[3])  
            Kg_Peso = float(values[4].replace('.', '').replace(',', '.')[:15])
            QtD = float(values[5].replace('.', '').replace(',', '.')[:15])  
            
            # Adjust values based on TipoLan
            if TipoLan == "D":
                VlR_UnI = float(values[6].replace('.', '').replace(',', '.')[:15]) * -1  
                vlr_total = float(values[7].replace('.', '').replace(',', '.')[:15]) * -1  
            else:
                VlR_UnI = float(values[6].replace('.', '').replace(',', '.')[:15])  
                vlr_total = float(values[7].replace('.', '').replace(',', '.')[:15])  

            # Prepare the SQL INSERT statement
            strSql = """
                        INSERT INTO TB_Itens (
                                                Doc_Num_Documento, 
                                                ID_Empresa, 
                                                ID_Pessoa, 
                                                ID_Unidade, 
                                                Item_Nr, 
                                                ID_Produto, 
                                                ID_CR, 
                                                ID_Natureza, 
                                                Kg_Tara, 
                                                QtD, 
                                                Vlr_Unit, 
                                                Vlr_Total, 
                                                Doc_AprovacaoZe, 
                                                Doc_AprovacaoJose
                                            ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
            values = (
                        Nr_Documento,
                        ID_Empresa,
                        ID_Fornecedor,
                        ID_Unidade,
                        Nr_Item,
                        ID_Produto,
                        ID_CR,
                        ID_Nat,
                        Kg_Peso,
                        QtD,
                        VlR_UnI,
                        vlr_total,
                        Aprovacao,
                        Aprovacao  
                    )
            
            myresult = db.executar_consulta(strSql, values)
            self.Vlr = 0
            self.Vlr_TotalParcelas = 0
            self.Vlr_TotalItens = 0
            self.vlr_soma_itens = 0
            self.limpar_campos_lcto()

    def delete_document(self):
        response = messagebox.askyesno("Exclusão Documento", "Tem Certeza que deseja excluir %s")
        if response:  # If the user clicked 'Yes'
            self.excluir_lcto()  # Call the deletion function

    def excluir_lcto(self):
        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.', parent=self.window_one)
            return
                
        # Check if there are associated financial records
        vsSQL = """
                    SELECT * FROM TB_Financeiro
                    WHERE 
                    ID_Empresa = %s 
                    AND ID_Pessoa = %s 
                    AND ID_Unidade = %s 
                    AND Fin_Num_documento = %s 
                    AND Fin_Dta_Liquidacao IS NOT NULL
                """
        myresult = db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Fornecedor), str(ID_Unidade), str(Nr_Documento)))
        
        if myresult:  
            messagebox.showinfo("Info", "Documento Não Pode ser Excluídos, existem Baixas Financeiras!", parent=self.window_one)
            return
        
        try:
            db.begin_transaction()
            
            # DELETE from TB_Financeiro
            vsSQL = """
                        DELETE FROM TB_Financeiro
                        WHERE 
                        ID_Empresa = %s 
                        AND ID_Pessoa = %s 
                        AND ID_Unidade = %s 
                        AND Fin_Num_documento = %s
                    """
            db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Fornecedor), str(ID_Unidade), str(Nr_Documento)))

            # DELETE from TB_Itens
            vsSQL = """
                        DELETE FROM TB_Itens
                        WHERE 
                        ID_Empresa = %s 
                        AND ID_Pessoa = %s 
                        AND ID_Unidade = %s 
                        AND Doc_Num_Documento = %s
                    """
            db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Fornecedor), str(ID_Unidade), str(Nr_Documento)))

            # DELETE from TB_CB_Doc
            vsSQL = """
                        DELETE FROM TB_CB_Doc
                        WHERE 
                        ID_Empresa = %s 
                        AND ID_Pessoa = %s 
                        AND ID_Unidade = %s 
                        AND Doc_Num_Documento = %s
                    """
            db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Fornecedor), str(ID_Unidade), str(Nr_Documento)))

            # Commit the transaction
            db.commit_transaction()
            messagebox.showinfo("Info", "Lançamento excluído com sucesso!")

            # Optionally clear fields or update UI
            self.limpar_campos_lcto()
            self.LParcelasFinanceiras.delete(*self.LParcelasFinanceiras.get_children())
            self.LItens.delete(*self.LItens.get_children())
        
        except Exception as e:
            db.rollback_transaction()  # Rollback in case of error
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
        
    def excluir_itens(self):
        ID_Empresa = self.combo_empresa.get()
        ID_Fornecedor = self.combo_pessoa.get()
        ID_Unidade = self.combo_unidade_negocio.get()
        Nr_Documento = self.entry_doc_num.get()
        Nr_Item = self.LItens.curselection()
        
        if not Nr_Item:
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um item para excluir.", parent=self.window_one)
            return
        
        Nr_Item = self.LItens.get(Nr_Item[0])  # Get the selected item

        # Prepare the SQL query
        vsSQL = """
                SELECT * FROM TB_Itens ii
                WHERE ii.ID_Empresa = %s 
                AND ii.ID_Pessoa = %s 
                AND ii.ID_Unidade = %s 
                AND ii.Doc_Num_Documento = %s 
                AND ii.Item_Nr = %s
        """
        
        cursor = self.connection.cursor()
        cursor.execute(vsSQL, (ID_Empresa, ID_Fornecedor, ID_Unidade, Nr_Documento, Nr_Item))

        if cursor.fetchone() is not None:  
            messagebox.showinfo("Info", "Item da Nota já gravado, só pode ser excluído toda a nota!", parent=self.window_one)
            cursor.close()
            return
        
        self.LItens.delete(Nr_Item[0])
        
        cursor.close()  # Close the cursor

    def consulta_lcto(self):
        Modulo_Financeiro = self.entry_tipo_lcto_descr.get()

        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.', parent=self.window_one)
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.', parent=self.window_one)
            return
        
        # Limpa a lista atual antes de inserir novos resultados
        self.limpar_campos_lcto
        self.LParcelasFinanceiras.delete(*self.LParcelasFinanceiras.get_children())
        self.LItens.delete(*self.LItens.get_children())
        vsSQL = """
                    SELECT 
                        cb.Doc_Tipo             AS Doc_Tipo, 
                        cb.Doc_Dta_Documento    AS Doc_Dta_Documento, 
                        cb.Doc_Num_Contrato     AS Doc_Num_Contrato, 
                        cb.Doc_VlR              AS Doc_VlR,
                        cb.Doc_DS_Observacao    AS Doc_DS_Observacao, 
                        cb.Doc_Serie            AS Doc_Serie, 
                        cb.Doc_Estado           AS Doc_Estado, 
                        cb.Doc_Frete            AS Doc_Frete,
                        ff.TipoPagamento_ID     AS TipoPagamento_ID, 
                        tp.TipoPagamento_Cod    AS TipoPagamento_Cod
                    FROM TB_CB_Doc cb
                    LEFT JOIN TB_Financeiro ff ON ff.ID_Empresa = cb.ID_Empresa AND ff.ID_Pessoa = cb.ID_Pessoa AND ff.ID_Unidade = cb.ID_Unidade AND ff.Fin_Num_documento = cb.Doc_Num_Documento
                    LEFT JOIN TB_TiposPagamento tp ON tp.TipoPagamento_ID = ff.TipoPagamento_ID
                    WHERE 
                    cb.ID_Empresa = %s 
                    AND cb.ID_Pessoa = %s 
                    AND cb.ID_Unidade = %s 
                    AND cb.Doc_Num_Documento = %s
                """
        
        results = db.executar_consulta(vsSQL, (str(ID_Empresa), str(ID_Fornecedor), int(ID_Unidade), str(Nr_Documento)))
        
        if not results:
            messagebox.showinfo('Gestor Negócios', 'Documento Não Existe!!!.', parent=self.window_one)
            self.limpar_campos_lcto()
            return

        for record in results:
            if isinstance(record, dict):  # Verifique se o record é um dicionário
                Doc_Tipo = record['Doc_Tipo']
                Modulo_Financeiro = 'CPA' if Doc_Tipo == 'D' else 'CRE' if Doc_Tipo == 'C' else None
                Dta_Documento = record['Doc_Dta_Documento']
                Nr_Contrato = record['Doc_Num_Contrato']
                Vlr_Documento = record['Doc_VlR']
                Vlr_Documento = self.format_valor_fx(float(Vlr_Documento) * -1) if Modulo_Financeiro == "CPA" else self.format_valor_fx(float(Vlr_Documento))
                DS_Observacao = record['Doc_DS_Observacao']
                SerieNota = record['Doc_Serie']
                NotaEstado = record['Doc_Estado']
                Frete = self.obter_Frete_DS(str(record['Doc_Frete']))
                FormaLiquidacao_ID = record['TipoPagamento_ID']
                FormaLiquidacao_DS = record['TipoPagamento_Cod']
                
            else:
                print(f"Tipo inesperado: {type(record)} - {record}")
        
        # Frete Tipo
        frete_map = {
                    "0": "Contratação do frete por conta do remetente (CIF)",
                    "1": "Contratação do frete por conta do destinatário (FOB)",
                    "2": "Contratação do frete por conta de terceiros",
                    "3": "Transporte próprio por conta do remetente",
                    "4": "Transporte próprio por conta do destinatário",
                    "9": "Sem ocorrência de transporte"
                    }
        
        Frete_DS = frete_map.get(Frete, "Desconhecido")

        # Update UI Fields
        self.combo_uf.set(NotaEstado)
        self.combo_frete.set(Frete)
        self.entry_doc_dt_emissao.delete(0, 'end')
        self.entry_doc_dt_emissao.insert(0, Dta_Documento.strftime("%d/%m/%Y"))
        self.entry_doc_serie.delete(0, 'end')
        self.entry_doc_serie.insert(0, SerieNota)
        self.entry_doc_numcontrato.delete(0, 'end')
        self.entry_doc_numcontrato.insert(0, Nr_Contrato)
        self.entry_doc_valor_total.delete(0, 'end')
        self.entry_doc_valor_total.insert(0, Vlr_Documento)
        self.text_historico.delete('1.0', 'end')
        if DS_Observacao is not None:
                self.text_historico.insert('1.0', str(DS_Observacao))
        
        # FINANCEIRO
        vsSQL = """
                    SELECT 
                        ff.Fin_Parcela, 
                        ff.Fin_Dta_Vcto, 
                        ff.Fin_VlR_Parcela,
                        ff.TipoPagamento_ID, 
                        tp.TipoPagamento_Desc
                    FROM TB_Financeiro ff
                    LEFT JOIN TB_TiposPagamento tp ON tp.TipoPagamento_ID = ff.TipoPagamento_ID
                    WHERE 
                    ID_Empresa = %s 
                    AND ID_Pessoa = %s 
                    AND ID_Unidade = %s 
                    AND Fin_Num_documento = %s
                    ORDER BY ff.Fin_Parcela
                """
        rs_parcelas = db.executar_consulta(vsSQL, (ID_Empresa, ID_Fornecedor, ID_Unidade, Nr_Documento))
        rs_parcelas = [(consulta) for consulta in rs_parcelas]
        
        # Carregar as Parcelas Financediras
        for row in rs_parcelas:
            lista_item = self.LParcelasFinanceiras.insert("", "end", text=row['Fin_Parcela'])
            self.LParcelasFinanceiras.item(lista_item, 
                                           values=(
                                               row['Fin_Parcela'],
                                               row['Fin_Dta_Vcto'].strftime("%d/%m/%Y"),
                                               f"{self.format_valor_fx(float(row['Fin_VlR_Parcela'] * -1))}" if Modulo_Financeiro == "CPA" else f"{self.format_valor_fx(float(row['Fin_VlR_Parcela']))}",
                                               row['TipoPagamento_Desc']
                                               )
                                            )
            
            
        # ITENS
        vsSQL = """
                    SELECT 
                        ii.Item_Nr, 
                        ii.ID_Produto, 
                        tb.Produto_Descricao, 
                        ii.ID_CR,
                        cr.Cen_Descricao, 
                        ii.ID_Natureza, 
                        nt.Nat_Descricao,
                        ii.Kg_Tara, 
                        ii.Kg_PesoBruto, 
                        ii.Kg_PesoLiquido,
                        ii.Kg_PesoRomaneio, 
                        ii.Qtd, 
                        ii.Vlr_Unit, 
                        ii.Vlr_Total
                    FROM TB_Itens ii
                    LEFT JOIN TB_Produtos tb ON ii.ID_Produto = tb.Produto_ID AND ii.ID_Empresa = tb.Empresa_ID
                    LEFT JOIN centrocusto cr ON ii.ID_CR = cr.Cen_ID AND ii.ID_Empresa = cr.Empresa_ID
                    LEFT JOIN TB_Natureza nt ON ii.ID_Natureza = nt.Nat_ID AND ii.ID_Empresa = nt.Empresa_ID
                    WHERE 
                    ii.ID_Empresa = %s 
                    AND ii.ID_Pessoa = %s 
                    AND ii.ID_Unidade = %s 
                    AND ii.Doc_Num_Documento = %s 
                    ORDER BY ii.Item_Nr
                """
        rs_itens = db.executar_consulta(vsSQL, (ID_Empresa, ID_Fornecedor, ID_Unidade, Nr_Documento))
        rs_itens = [(consulta) for consulta in rs_itens]

        # Populate the item information in the UI
        for row in rs_itens:
            lista_item = self.LItens.insert("", "end", text=row['Item_Nr'])
            self.LItens.item(lista_item, 
                                           values=(
                                                row['Item_Nr'],
                                                row['Produto_Descricao'],
                                                row['Cen_Descricao'],
                                                row['Nat_Descricao'],
                                                self.format_valor_fx(float(row['Kg_Tara'])),
                                                self.format_valor_fx(float(row['Qtd'])),
                                                f"{self.format_valor_fx(float(row['Vlr_Unit'] * -1))}" if Modulo_Financeiro == "CPA" else f"{self.format_valor_fx(float(row['Vlr_Unit']))}",
                                                f"{self.format_valor_fx(float(row['Vlr_Total'] * -1))}" if Modulo_Financeiro == "CPA" else f"{self.format_valor_fx(float(row['Vlr_Total']))}"
                                               )
                                            )
class Consultas():

    def consulta_sites(self):
        tpo_site = self.entry_tipo_site_descr.get()

        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.', parent=self.window_one)
            return
        
        # Limpa a lista atual antes de inserir novos resultados
        self.limpar_campos_site
        self.LSites.delete(*self.LSites.get_children())
        if tpo_site == 'Todos':
            vsSQL = """
                        SELECT 
                            Empresa_ID      AS Empresa_ID, 
                            Site_tpo        AS Site_tpo, 
                            Site_Descricao  AS Site_Descricao, 
                            Site_http       AS Site_http
                        FROM sites_cadastros
                        WHERE 
                        Empresa_ID = %s 
                    """
            
            results = db.executar_consulta(vsSQL, (str(ID_Empresa)))
        else:
            vsSQL = """
                        SELECT 
                            Empresa_ID      AS Empresa_ID, 
                            Site_tpo        AS Site_tpo, 
                            Site_Descricao  AS Site_Descricao, 
                            Site_http       AS Site_http
                        FROM sites_cadastros
                        WHERE 
                        Empresa_ID = %s 
                        AND Site_tpo = %s 
                    """
            
            results = db.executar_consulta(vsSQL, (str(ID_Empresa), str(tpo_site)))

        if not results:
            messagebox.showinfo('Gestor Negócios', 'Não Existe Cadastros para os dados Informados!!!.')
            self.limpar_campos_site()
            return

        # Carregar as Parcelas Financediras
        icon_image = self.base64_to_photoimage('lupa')
        for row in results:
            self.LSites.insert('', 'end', 
                               values=(
                                    row['Site_tpo'],
                                    row['Site_Descricao'],
                                    row['Site_http']
                                    )
                                )
    
    def incluir_sites_click(self):
        if self.entry_informacoes_https.get() != "":
            site = str(self.entry_informacoes_https.get())
            self.gravar_sites() # Gravar os dados
            self.incluir_sites()  # INCLUIR NO LIST
            self.entry_informacoes_https.delete(0, 'end')  # Limpa o campo
        else:
            messagebox.showerror("Erro", "Preencher Endereço do Site!")
            # Set focus back to the payment method (not implemented here)

    def incluir_sites(self):
        # Create a new entry in the Treeview
        try:
            lista = self.LSites.insert("", "end", text=self.entry_tipo_site_descr.get())
            # Insert the subitems
            self.LSites.item(lista, values=(
                self.entry_tipo_site_descr.get(),
                self.text_descricao.get(),
                self.entry_informacoes_https.get()
            ))

            # Sort the Treeview if needed
            self.LSites.heading('tpo', text='Tipo Site')
            self.LSites.heading('ds', text='Descrição')
            self.LSites.heading('http', text='Endereço Site')
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao incluir o site: {str(e)}")

    def consulta_produtos(self):
            
        # Verifica se o campo TCnpj está preenchido
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.')
            return
        
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
        
        # Preparar a tabela
        self.LItens_produtos.delete(*self.LItens_produtos.get_children())  # Limpa a tabela
        self.LItens_produtos.heading('Nr', text="Nr.")
        self.LItens_produtos.column('Nr', width=5, anchor='e')
        self.LItens_produtos.heading('Descricao', text="Descrição")
        self.LItens_produtos.column('Descricao', width=350, anchor='w')
        self.LItens_produtos.heading('NCM', text="NCM")
        self.LItens_produtos.column('NCM', width=50, anchor='w')
        self.LItens_produtos.heading('Tipo_ID', text="ID")
        self.LItens_produtos.column('Tipo_ID', width=4, anchor='c')
        self.LItens_produtos.heading('Tipo', text="Tipo Spead")
        self.LItens_produtos.column('Tipo', width=50, anchor='w')
        self.LItens_produtos.heading('Unidade_Medida_ID', text="U.M.")
        self.LItens_produtos.column('Unidade_Medida_ID', width=10, anchor='c')
        self.LItens_produtos.heading('Unidade_Medida', text="U.M. Descrição")
        self.LItens_produtos.column('Unidade_Medida', width=50, anchor='w')


        # SQL para buscar os dados
        vs_sql = """SELECT 
                        pd.*, 
                        tdm.TipodeMedida_Desc, 
                        tim.TipoItem_Desc
                    FROM TB_Produtos pd 
                        LEFT JOIN TB_TiposdeMedida AS tdm ON Produto_Unidade= tdm.TipodeMedida_Diminutivo 
                        LEFT JOIN TB_TipoItem AS tim ON Produto_Tipo = tim.TipoItem_Cod 
                    WHERE 
                        pd.Empresa_ID=%s
                    ORDER BY Produto_Descricao ASC """
        
        myresult = db.executar_consulta(vs_sql, (str(ID_Empresa)))
        consulta = [(consulta) for consulta in myresult]
        
        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!")
            return
                
        # Inserir dados na tabela
        
        for item in consulta:
            formatted_item = (
                    item.get('Produto_ID'),
                    item.get('Produto_Descricao'),
                    item.get('Produto_NCM'),
                    item.get('Produto_Tipo'),
                    item.get('TipoItem_Desc'),
                    item.get('Produto_Unidade'),
                    item.get('TipodeMedida_Desc')
                )
            self.LItens_produtos.insert('', 'end', values=formatted_item)
        
    def consulta_pessoas(self):
            
        # Verifica se o campo TCnpj está preenchido
        if not self.entry_empresa.get().strip():
            messagebox.showinfo('Gestor Negócios', 'Erro: Preencher o Campo da Empresa!!!.')
            return
        
        ID_Empresa = self.obter_Empresa_ID(self.entry_empresa.get())
        
        # Preparar a tabela
        self.LItens_cadastro_pessoas.delete(*self.LItens_cadastro_pessoas.get_children())  # Limpa a tabela
        self.LItens_cadastro_pessoas.heading('Tpo', text="T")
        self.LItens_cadastro_pessoas.column('Tpo', width=3, anchor='c')
        self.LItens_cadastro_pessoas.heading('CpF_CnPj', text="CPf/CnPj")
        self.LItens_cadastro_pessoas.column('CpF_CnPj', width=100, anchor='e')
        self.LItens_cadastro_pessoas.heading('Descricao', text="Descrição")
        self.LItens_cadastro_pessoas.column('Descricao', width=100, anchor='w')
        self.LItens_cadastro_pessoas.heading('Banco', text="Banco")
        self.LItens_cadastro_pessoas.column('Banco', width=60, anchor='w')
        self.LItens_cadastro_pessoas.heading('Agencia', text="Agência")
        self.LItens_cadastro_pessoas.column('Agencia', width=60, anchor='e')
        self.LItens_cadastro_pessoas.heading('Agencia_D', text="D")
        self.LItens_cadastro_pessoas.column('Agencia_D', width=5, anchor='e')
        self.LItens_cadastro_pessoas.heading('Conta', text="Conta")
        self.LItens_cadastro_pessoas.column('Conta', width=60, anchor='e')
        self.LItens_cadastro_pessoas.heading('Conta_D', text="D")
        self.LItens_cadastro_pessoas.column('Conta_D', width=5, anchor='e')
        self.LItens_cadastro_pessoas.heading('Pix', text="Pix")
        self.LItens_cadastro_pessoas.column('Pix', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Proprietario_sn', text="Propr.")
        self.LItens_cadastro_pessoas.column('Proprietario_sn', width=3, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco', text="Endereço")
        self.LItens_cadastro_pessoas.column('Endereco', width=100, anchor='w')
        self.LItens_cadastro_pessoas.heading('Endereco_Nr', text="Nr")
        self.LItens_cadastro_pessoas.column('Endereco_Nr', width=50, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Bairro', text="Bairro")
        self.LItens_cadastro_pessoas.column('Endereco_Bairro', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_Compl', text="Complemento")
        self.LItens_cadastro_pessoas.column('Endereco_Compl', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Endereco_UF', text="UF")
        self.LItens_cadastro_pessoas.column('Endereco_UF', width=20, anchor='c')
        self.LItens_cadastro_pessoas.heading('IbGe', text="IBGE")
        self.LItens_cadastro_pessoas.column('IbGe', width=60, anchor='c')
        self.LItens_cadastro_pessoas.heading('Endereco_Cidade', text="Município")
        self.LItens_cadastro_pessoas.column('Endereco_Cidade', width=80, anchor='w')
        self.LItens_cadastro_pessoas.heading('CeP', text="CEP")
        self.LItens_cadastro_pessoas.column('CeP', width=80, anchor='e')
        self.LItens_cadastro_pessoas.heading('Insc_Estadual', text="Insc. Estadual")
        self.LItens_cadastro_pessoas.column('Insc_Estadual', width=60, anchor='w')
        self.LItens_cadastro_pessoas.heading('Insc_Municipal', text="Insc. Municipal")
        self.LItens_cadastro_pessoas.column('Insc_Municipal', width=60, anchor='w')
        self.LItens_cadastro_pessoas.heading('Insc_Suframa', text="Suframa")
        self.LItens_cadastro_pessoas.column('Insc_Suframa', width=60, anchor='w')
        self.LItens_cadastro_pessoas.heading('Telefone_fixo', text="Telefone")
        self.LItens_cadastro_pessoas.column('Telefone_fixo', width=60, anchor='e')
        self.LItens_cadastro_pessoas.heading('WhatsApp', text="WhatsApp")
        self.LItens_cadastro_pessoas.column('WhatsApp', width=60, anchor='w')
        self.LItens_cadastro_pessoas.heading('Email', text="Email")
        self.LItens_cadastro_pessoas.column('Email', width=80, anchor='w')

        # SQL para buscar os dados
        vs_sql = """SELECT * 
                        FROM TB_Pessoas 
                        WHERE Empresa_ID=%s 
                        ORDER BY Pessoas_Descricao
                """
        
        myresult = db.executar_consulta(vs_sql, (str(ID_Empresa)))
        consulta = [(consulta) for consulta in myresult]
        
        if not consulta:
            messagebox.showinfo("Aviso", "Não Existem Dados Para Esta Consulta!")
            return
                
        # Inserir dados na tabela
        
        for item in consulta:
            formatted_item = (
                    item.get('Pessoas_Tipo'),
                    item.get('Pessoas_CPF_CNPJ'),
                    item.get('Pessoas_Descricao'),
                    item.get('Pessoas_Bco'),
                    item.get('Pessoas_Agencia'),
                    item.get('Pessoas_DVAgencia'),
                    item.get('Pessoas_Conta'),
                    item.get('Pessoas_DVConta'),
                    item.get('Pessoas_Chave_PiX'),
                    item.get('Pessoas_Proprietaria'),
                    item.get('Pessoas_EndLogradouro'),
                    item.get('Pessoas_EndNumero'),
                    item.get('Pessoas_EndBairro'),
                    item.get('Pessoas_EndComplemento'),
                    item.get('Pessoas_UF'),
                    item.get('Pessoas_CodMunicipioFiscal'),
                    item.get('Pessoas_EndCidade'),
                    item.get('Pessoas_CEP'),
                    item.get('Pessoas_InscricaoEstadual'),
                    item.get('Pessoas_InscricaoMunicipal'),
                    item.get('Pessoas_Suframa'),
                    item.get('Pessoas_Telefone'),
                    item.get('Pessoas_Fax'),
                    item.get('Pessoas_Email')
                )
            self.LItens_cadastro_pessoas.insert('', 'end', values=formatted_item)
                  
    def Consulta_Negocios(self, ID_Empresa, UF, Cidade, Status):
        ID_Empresa = str(ID_Empresa.strip()) if ID_Empresa != '' else None
        UF = UF.strip() if UF != '' else None
        Cidade = Cidade.strip() if Cidade != '' else None
        Status = Status.strip() if Status != '' else None

        conditions = []  # Lista para armazenar as condições
        # Condições iniciais
        conditions.append("dd.Nome_da_Area <> ''")

        params = []
        if ID_Empresa is not None:
            conditions.append("dd.Empresa_ID = %s")
            params.append(ID_Empresa)

        if UF is not None:
            conditions.append("dd.UF = %s")
            params.append(UF)

        if Cidade is not None:
            conditions.append("dd.Cidade = %s")
            params.append(Cidade)

        if Status is not None:
            conditions.append("dd.Status_Prospeccao = %s")
            params.append(Status)

        strSql = f"""SELECT
                Dta_Registro                                        									                        AS Dta_Registro,
                Usr_Registro                  															                        AS Usr_Registro,
                Status_Prospeccao             															                        AS Status_Prospeccao,
                Tipo                          															                        AS Tipo,
                Nome_da_Area                  															                        AS Nome_da_Area,
                Cidade                        															                        AS Cidade,
                UPPER(UF)                            															                AS UF,
                FORMAT(DrE_VgV_Bruto, 2, 'de_DE')								                                                AS VGV_Total,
                FORMAT(DrE_comissao_venda, 2, 'de_DE')			                                                                AS Comissao_Vendas,
                FORMAT(DrE_comissao_negocio, 2, 'de_DE')					                                                    AS Comissao_Negocio,
                FORMAT(DrE_impostos, 2, 'de_DE') 									                                            AS Impostos,
                FORMAT(DrE_Receita_Liquida, 2, 'de_DE') 					                                                    AS VGV_Liquido,
                FORMAT(DrE_Receita_Parceiro, 2, 'de_DE')                                                                        AS Repasse_Parceiro,
                FORMAT(DrE_Receita_Urbanizador, 2, 'de_DE')                                                                     AS Receita_Liquida,
                FORMAT(Investimento_Vlr_Parceiro, 2, 'de_DE') 											                        AS Terreno,
                
                # FORMAT(Projetos_Valor, 2, 'de_DE') 								                                            AS Projetos,
                # FORMAT(Obra_Valor, 2, 'de_DE') 											                                    AS Obras,
                # FORMAT(AdmObras_Valor, 2, 'de_DE') 								                                            AS AdmObras,
                # FORMAT(Pos_Obra_Valor, 2, 'de_DE') 								                                            AS PosObras,
                # FORMAT(OverHead_Valor, 2, 'de_DE') 											                                AS Administracao,
                # FORMAT(Mkt_Valor, 2, 'de_DE') 											                                    AS MkT,

                FORMAT(Projetos_Valor + Obra_Valor + Mkt_Valor + OverHead_Valor + Pos_Obra_Valor + AdmObras_Valor, 2, 'de_DE')  AS TotalGastos,
                FORMAT(DrE_Ebtda_Valor, 2, 'de_DE')                                                                             AS Margem_Valor,
                FORMAT(DrE_Ebtda_Percente, 2, 'de_DE')                                                                          AS Margem_Percent,
                
                FORMAT(Multiplicador, 2, 'de_DE')			                                                                    AS Multiplicador,
                FORMAT(Vlr_Exposicao_Maxima, 2, 'de_DE')                                                                        AS Vlr_Exposicao_Maxima,
                FORMAT(Tir_Urbanizadora*100, 4, 'de_DE')		                                                                AS Tir_Urbanizadora

                FROM (
                SELECT
                mm.IBGE                             					AS IBGE,
                dd.Cidade                           					AS Cidade,
                dd.UF                               					AS UF,
                dd.Nome_da_Area                     					AS Nome_da_Area,
                dd.Dta_Registro                     					AS Dta_Registro,
                dd.usr_registro                     					AS Usr_Registro,
                dd.Status_Prospeccao                					AS Status_Prospeccao,
                ss.Status_Order                     					AS Status_Order,
                dd.Tipo                             					AS Tipo,
                dd.Valor_m2                         					AS Valor_m2,
                dd.Valor_m2 * (1 + dd.Per_Comissão) 					AS Preco_MetroQuadrado,
                dd.Per_Comissão                     					AS Per_Comissao,
                dd.Area_Aproveitada  	                                AS Area_Aproveitada,
                dd.Area_Total_m2                                        AS Area_Total_m2,
                dd.per_Aproveitamento                                   AS Per_Aproveitamento,
                dd.Per_Permuta_em_Lotes                                 AS Per_Permuta_em_Lotes,
                dd.Per_Impostos                     					AS Per_Impostos,
                dd.Per_Comissão_Negócio             					AS Per_Comissão_Negócio,
                dd.Participação_Urbanizadora        					AS Participação_Urbanizadora,
                dd.Per_Adm_Mkt                      					AS Per_Adm_Mkt,
                dd.Investimento_Vlr_Parceiro        					AS Investimento_Vlr_Parceiro,

                dd.Projetos_Valor 								        AS Projetos_Valor,
                dd.Obra_Valor 											AS Obra_Valor,
                dd.AdmObras_Valor 								        AS AdmObras_Valor,
                dd.Pos_Obra_Valor 								        AS Pos_Obra_Valor,
                dd.OverHead_Valor 										AS OverHead_Valor,
                dd.Mkt_Valor 											AS Mkt_Valor,

                dd.Custo_Obra_m2_Lote               					AS Custo_Obra_m2_Lote,
                dd.AdmObras_Per_Obras               					AS AdmObras_Per_obras,
                dd.Projetos_Per_da_Obra             					AS Projetos_Per_da_Obra,
                dd.MkT_Per_VGV                      					AS Mkt_Per_VGV,
                dd.Pos_Obra_Per_Obra                					AS Pos_Obra_Per_Obra,
                dd.Adm_Per_Receita                  					AS Adm_Per_Receita,
                
                dd.DrE_VgV_Bruto								        AS DrE_VgV_Bruto,
                dd.DrE_comissao_venda			                        AS DrE_comissao_venda,
                dd.DrE_comissao_negocio					                AS DrE_comissao_negocio,
                dd.DrE_impostos 									    AS DrE_impostos,
                dd.DrE_Receita_Liquida					                AS DrE_Receita_Liquida,
                dd.DrE_Receita_Parceiro                                 AS DrE_Receita_Parceiro,
                dd.DrE_Receita_Urbanizador                              AS DrE_Receita_Urbanizador,
                dd.DrE_Ebtda_Valor                                      AS DrE_Ebtda_Valor,
                dd.DrE_Ebtda_Percente                                   AS DrE_Ebtda_Percente,

                dd.Multiplicador							            AS Multiplicador,
                dd.Vlr_Exposicao_Maxima							        AS Vlr_Exposicao_Maxima,
                dd.Tir_Urbanizadora							            AS Tir_Urbanizadora
                FROM Dados_Prospeccao dd
                INNER JOIN Municipios_IBGE mm ON mm.UF = dd.UF AND mm.Município = dd.Cidade
                INNER JOIN Status_Prospeccao ss ON ss.Empresa_ID = dd.Empresa_ID AND ss.Status = dd.Status_Prospeccao
                WHERE {' AND '.join(conditions)})
                AS COMPLETO
                ORDER BY Status_Order, UF, Cidade, Nome_da_Area"""

        myresult = db.executar_consulta(strSql, params)
        consulta = [(consulta) for consulta in myresult]

        return consulta

    def Consulta_Negocio(self, ID_Empresa, UF, Cidade, Tipo, Nome_da_Area):
        conditions = []  # Lista para armazenar as condições
        # Condições iniciais
        conditions.append("dp.Empresa_ID = %s")
        params = [ID_Empresa]
        conditions.append("dp.UF = %s")
        params.append(UF)
        conditions.append("dp.Cidade = %s")
        params.append(Cidade)
        conditions.append("dp.Tipo = %s")
        params.append(Tipo)
        conditions.append("dp.Nome_da_Area = %s")
        params.append(Nome_da_Area)
        # print(params)
        strSql = f"""SELECT
                        Pri_Descricao,
                        UF,
                        Cidade,
                        Tipo,
                        Nome_da_Area,

                        Area_Total,
                        Per_Aproveitamento,
                        Area_Aproveitada,
                        Medidas_Lote,
                        Area_Lote_Medio,
                        Nr_Unidades,

                        Participacao_Urbanizadora,
                        Participação_Parceiro,
                        Permuta_em_Lotes,
                        Per_Comissao_Negocio,
                        Per_MkT_Cobrado,
                        Participação_Total_Urbanizadora,
                        Participação_Total_Parceiro,

                        Investimento_Area,
                        Investimento_Area_Inicio,
                        Investimento_Area_Curva,
                        Investimento_Aporte,

                        Adto_Parceiro_Valor,
                        Adto_Parceiro_Urb_Juros,
                        Adto_Parceiro_Per_Juros,
                        Adto_Parceiro_Inicio,
                        Adto_Parceiro_Curva,

                        Vendas_Valor_m2,
                        Vendas_comissao_per,
                        Valor_m2_com_comissao,
                        tickt_medio,
                        Vendas_prazo_financiamento,
                        Vendas_sistema_amortizacao,
                        Vendas_juros_taxa,
                        Per_Juros_am,
                        Vendas_per_entrada,
                        Vendas_parcela_entrada,
                        Vendas_per_reforcos,
                        Vendas_parcela_reforcos,
                        Vendas_periodicidade_reforcos,
                        Vendas_per_avista,
                        Vendas_inicio,
                        Vendas_curva,
                        PmT_PRICE,
                        PmT_Sacoc,
                        Per_Impostos,

                        Projetos_per_obra,
                        Projetos_Valor,
                        Projetos_inicio,
                        Projetos_curva,

                        MkT_per_vgv,
                        Mkt_Valor,
                        MkT_inicio,
                        MkT_curva,

                        Adm_per_receita,
                        OverHead_Valor,
                        OverHead_Inicio,
                        OverHead_Curva,

                        Obras_custo_m2,
                        Obra_Valor,
                        Obras_inicio,
                        Obras_curva,

                        Pos_Obra_per_obra,
                        Pos_Obra_Valor,
                        Pos_Obra_Inicio,
                        Pos_Obra_Curva,

                        AdmObra_per_obra,
                        AdmObras_Valor,
                        AdmObras_Inicio,
                        AdmObras_Curva,

                        Financiamento_valor,
                        Financiamento_sistema_amortizacao,
                        Financiamento_prazo_amortizacao,
                        Financiamento_inicio_amortizacao,
                        Financiamento_inicio_pagto_juros,
                        Financiamento_taxa,
                        Financiamento_liberacao,
                        Financiamento_curva,
                        Financiamento_financiador,

                        Observacao,

                        DrE_VgV_Bruto,
                        DrE_comissao_venda,
                        DrE_VgV_Liquido,
                        DrE_impostos,
                        DrE_comissao_negocio,
                        DrE_Receita_Liquida,
                        DrE_Receita_Parceiro,
                        DrE_Receita_Urbanizador,
                        DrE_Ebtda_Valor,
                        DrE_Ebtda_Percente,
                        Tir,
                        Tir_Urbanizadora_am,
                        Tir_Parceiro,
                        Payback,
                        PayBack_Parceiro,
                        Multiplicador,
                        ExposicaoMax,
                        Vpl_Urb,
                        Vpl_Parceiro,
                        VpL_Taxa_Desconto,

                        Status_Prospeccao,
                        Anexos,
                        Dta_Contrato,
                        Unidade,
                        Http,
                        Coordenadas,

                        Usr,
                        Dta_Registro
                        
                     FROM (
                     select
                     dp.Empresa_ID 			            AS CnPj,
                     ee.Pri_Descricao			        AS Pri_Descricao,
                     dp.UF				                AS UF,
                     dp.Cidade                          AS Cidade,
                     dp.Tipo				            AS Tipo,
                     dp.Nome_da_Area			        AS Nome_da_Area,
                     dp.Area_Total_m2                   AS Area_Total,
                     dp.Per_Aproveitamento              AS Per_Aproveitamento,
                     dp.Area_Aproveitada                AS Area_Aproveitada,
                     dp.Medidas_Lote                    AS Medidas_Lote,
                     dp.Area_Lote_Medio                 AS Area_Lote_Medio,
                     dp.Nr_Unidades                     AS Nr_Unidades,

                     dp.Participação_Urbanizadora       AS Participacao_Urbanizadora,
                     dp.Participação_Parceiro           AS Participação_Parceiro,
                     dp.Per_Permuta_em_Lotes            AS Permuta_em_Lotes,
                     dp.Per_Comissão_Negócio            AS Per_Comissao_Negocio,
                     dp.Per_Adm_Mkt                     AS Per_MkT_Cobrado,
                     dp.Participação_Total_Urbanizadora AS Participação_Total_Urbanizadora,
                     dp.Participação_Total_Parceiro     AS Participação_Total_Parceiro,

                     dp.Investimento_Vlr_Parceiro       AS Investimento_Area,
                     dp.Investimento_Inicio_Parceiro    AS Investimento_Area_Inicio,
                     dp.Investimento_Curva_Parceiro     AS Investimento_Area_Curva,
                     dp.Aporte                          AS Investimento_Aporte,

                     dp.Vlr_Adiantamento_Parceiro       AS Adto_Parceiro_Valor,
                     dp.Urbanizadora_Per_Taxa           AS Adto_Parceiro_Urb_Juros,
                     dp.Parceiro_Per_Taxa               AS Adto_Parceiro_Per_Juros,
                     dp.Adiantamento_Inicio_Parceiro    AS Adto_Parceiro_Inicio,
                     dp.Adiantamento_Curva_Parceiro     AS Adto_Parceiro_Curva,

                     dp.Valor_m2                        AS Vendas_Valor_m2,
                     dp.Per_Comissão                    AS Vendas_comissao_per,
                     dp.Valor_m2_com_comissao           AS Valor_m2_com_comissao,
                     dp.tickt_medio                     AS tickt_medio,
                     dp.Prazo_Financiamento             AS Vendas_prazo_financiamento,
                     dp.Sistema_Amortização_Cliente     AS Vendas_sistema_amortizacao,
                     dp.Per_Juros                       AS Vendas_juros_taxa,
                     dp.Per_Juros_am                    AS Per_Juros_am,
                     dp.Per_Entrada                     AS Vendas_per_entrada,
                     dp.Nr_Parc_Entrada                 AS Vendas_parcela_entrada,
                     dp.Per_Reforços                    AS Vendas_per_reforcos,
                     dp.Nr_Parc_Reforços                AS Vendas_parcela_reforcos,
                     dp.Periodicidade_Reforços          AS Vendas_periodicidade_reforcos,
                     dp.Vendas_Per_Avista               AS Vendas_per_avista,
                     dp.Vendas_Inicio                   AS Vendas_inicio,
                     dp.Vendas_Curva                    AS Vendas_curva,
                     dp.PmT_PRICE                       AS PmT_PRICE,
                     dp.PmT_Sacoc                       AS PmT_Sacoc,
                     dp.Per_Impostos                    AS Per_Impostos,

                     dp.Projetos_Per_da_Obra            AS Projetos_per_obra,
                     dp.Projetos_Valor                  AS Projetos_Valor,
                     dp.Projetos_Inicio                 AS Projetos_inicio,
                     dp.Projetos_Curva                  AS Projetos_curva,

                     dp.Mkt_Per_VGV                     AS MkT_per_vgv,
                     dp.Mkt_Valor                       AS Mkt_Valor,
                     dp.Mkt_Inicio                      AS MkT_inicio,
                     dp.Mkt_Curva                       AS MkT_curva,

                     dp.Adm_Per_Receita                 AS Adm_per_receita,
                     dp.OverHead_Valor                  AS OverHead_Valor,
                     dp.OverHead_Inicio                 AS OverHead_Inicio,
                     dp.OverHead_Curva                  AS OverHead_Curva,

                     dp.Custo_Obra_m2_Lote              AS Obras_custo_m2,
                     dp.Obra_Valor                      AS Obra_Valor,
                     dp.Obra_Inicio                     AS Obras_inicio,
                     dp.Obra_Curva                      AS Obras_curva,

                     dp.Pos_Obra_Per_Obra               AS Pos_Obra_per_obra,
                     dp.Pos_Obra_Valor                  AS Pos_Obra_Valor,
                     dp.Pos_Obra_Inicio                 AS Pos_Obra_Inicio,
                     dp.Pos_Obra_Curva                  AS Pos_Obra_Curva,

                     dp.AdmObras_Per_Obras              AS AdmObra_per_obra,
                     dp.AdmObras_Valor                  AS AdmObras_Valor,
                     dp.AdmObras_Inicio                 AS AdmObras_Inicio,
                     dp.AdmObras_Curva                  AS AdmObras_Curva,

                     dp.Valor_Financiamento             AS Financiamento_valor,
                     dp.Sistema_Amortizacao             AS Financiamento_sistema_amortizacao,
                     dp.Prazo_Amortizacao               AS Financiamento_prazo_amortizacao,
                     dp.Inicio_Amortizacao              AS Financiamento_inicio_amortizacao,
                     dp.Inicio_Pagto_Juros              AS Financiamento_inicio_pagto_juros,
                     dp.Taxa_Financiamento              AS Financiamento_taxa,
                     dp.Liberacao_Financiamento         AS Financiamento_liberacao,
                     dp.Curva_Liberacao                 AS Financiamento_curva,
                     dp.Financiador_Parceiro            AS Financiamento_financiador,

                     dp.ObservacaoNegocio               AS Observacao,

                     dp.DrE_VgV_Bruto                   AS DrE_VgV_Bruto,
                     dp.DrE_comissao_venda              AS DrE_comissao_venda,
                     dp.DrE_VgV_Liquido                 AS DrE_VgV_Liquido,
                     dp.DrE_impostos                    AS DrE_impostos,
                     dp.DrE_comissao_negocio            AS DrE_comissao_negocio,
                     dp.DrE_Receita_Liquida             AS DrE_Receita_Liquida,
                     dp.DrE_Receita_Parceiro            AS DrE_Receita_Parceiro,
                     dp.DrE_Receita_Urbanizador         AS DrE_Receita_Urbanizador,
                     dp.DrE_Ebtda_Valor                 AS DrE_Ebtda_Valor,
                     dp.DrE_Ebtda_Percente              AS DrE_Ebtda_Percente,
                     dp.Tir_Urbanizadora                AS Tir,
                     dp.Tir_Urbanizadora_am             AS Tir_Urbanizadora_am,
                     dp.Tir_Parceiro                    AS Tir_Parceiro,
                     dp.PayBack_Urbanizadora            AS Payback,
                     dp.PayBack_Parceiro                AS PayBack_Parceiro,
                     dp.Multiplicador                   As Multiplicador,
                     dp.Vlr_Exposicao_Maxima            AS ExposicaoMax,
                     dp.VpL_Urbanizadora                AS Vpl_Urb,
                     dp.VpL_Parceiro                    AS Vpl_Parceiro,
                     
                     dp.Status_Prospeccao               AS Status_Prospeccao,
                     dp.Anexos                          AS Anexos,
                     dp.Data_Contrato                   As Dta_Contrato,
                     dp.Unidade_ID                      AS Unidade,
                     dp.Observacao                      AS Http,
                     dp.Area_EndCoordenadas		        AS Coordenadas,
                     dp.VpL_Taxa_Desconto               AS VpL_Taxa_Desconto,

                     dp.usr_registro                    AS Usr,
                     dp.dta_registro                    AS Dta_Registro

                    from Dados_Prospeccao dp
                    LEFT JOIN TB_Empresas ee ON ee.Pri_Cnpj=dp.Empresa_ID
                    WHERE {' AND '.join(conditions)})
                    AS COMPLETO"""

        myresult = db.executar_consulta(strSql, params)
        consulta = [(consulta) for consulta in myresult]
        return consulta 

    def Consulta_Prazo_Curvas(self, curva, janela):
        Empresa_ID = self.obter_Empresa_ID(self.combo_empresa.get(), janela)

        conditions = []  # Lista para armazenar as condições
        conditions.append("ct.Empresa_ID = %s ")
        params = [Empresa_ID]
        conditions.append("ct.DS_Curva = %s ")
        params.append(curva)   
        
        strSql = f"""SELECT
                     ct.Prazo_Curva AS Prazo_Curva,
                     ct.Mes_Inicio  AS Mes_Inicio,
                     ct.Mes_Fim     AS Mes_Fim,
                     ct.Per_Mensal  AS Per_Mensal
                     FROM Curva_Tempo ct
                     WHERE {' AND '.join(conditions)} ORDER BY DS_Curva, Mes_Inicio"""
        
        myresult = db.executar_consulta(strSql, params)
        return myresult
    
    def Fluxo_Caixa(self, 
                    ID_Empresa, 
                    UF, 
                    Cidade, 
                    Tipo, 
                    Nome_da_Area,
                    Tela
                    ):
           
        self.Vlr_Investimentos = float(self.entry_investimento_valor.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Adto = float(self.entry_adto_parceiro_valor.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Venda = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Projetos = float(self.entry_projetos_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Mkt = float(self.entry_mkt_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Adm = float(self.entry_overhead_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Obra = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_PosObra = float(self.entry_pos_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_AdmObras = float(self.entry_adm_valor_total.get().replace('.', '').replace(',', '.')[:15])
        self.Vlr_Financiamento = float(self.entry_financiamento_valor_captacao.get().replace('.', '').replace(',', '.')[:15])
        self.vlr_VGV_Bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
        self.vlr_VGV_líquido = float(self.entry_dre_receita_liquida.get().replace('.', '').replace(',', '.')[:15])
        self.per_parc = float(self.entry_total_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.per_comissao_venda = float(self.entry_vendas_comissao_per.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Per_Venda_Avista = float(self.entry_vendas_per_avista.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Periodicidade_Reforcos = float(self.entry_vendas_period_reforcos.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) 
        self.Per_Entrada = float(self.entry_vendas_entrada.get().replace("%", "").replace(",", ".")[:7]) / 100
        Nr_ParEntrada = float(self.entry_vendas_nr_parcelas_entrada.get().replace("x", "").replace(",", ".")[:7])
        self.Per_Reforcos = float(self.entry_vendas_reforcos.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Nr_ParReforcos = float(self.entry_vendas_nr_parcelas_reforcos.get().replace("x", "").replace(",", ".")[:7])
        self.Per_Mensal = float(self.entry_vendas_juros_am.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Sistema_Amortização_Cliente = self.entry_vendas_sistema_amortizacao.get()
        self.Nrper = float(self.entry_vendas_financiamento_prazo.get().replace("x", "").replace(",", ".")[:7])
        self.TVendas_Preço_m2_semComissao = float(self.entry_vendas_preco_m2.get().replace('.', '').replace(',', '.')[:15])
        if self.entry_area_lote_medio.get() != '':
            self.TArea_LoteMedio = float(self.entry_area_lote_medio.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
        else:
            self.TArea_LoteMedio = float(0)
        self.Per_Comissao_Negocio = float(self.entry_comissao_intermediacao.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Per_Impostos = self.get_aliquota_imposto(Tipo)
        self.Per_Impostos = float(self.Per_Impostos[0])
        self.Per_OverHead = float(self.entry_overhead_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Per_custoadtoPar = float(self.entry_adto_parceiro_per_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Per_custoadto = float(self.entry_adto_parceiro_per_urbanizadora.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.Valor_Adto = float(self.entry_adto_parceiro_valor.get().replace('.', '').replace(',', '.')[:15])
        self.Per_Urban = float(self.entry_total_urbanizadora.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.TPer_Desconto_VPL = 0.12

        # INVESTIMENTOS - Aquisição de Área
        self.curva_de_investimentos = self.Consulta_Prazo_Curvas(self.entry_investimento_curva_investimento.get(), Tela) 
        self.prazo_investimentos = [prazo['Prazo_Curva'] for prazo in self.curva_de_investimentos]
        if isinstance(self.prazo_investimentos, list) and len(self.prazo_investimentos) > 0:
            self.prazo_investimentos = float(self.prazo_investimentos[0])
        else:
            self.prazo_investimentos = 0

        self.inicio_investimentos = float(self.entry_investimento_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_investimentos = []  # Lista para armazenar os dados mensais
        for investimento in self.curva_de_investimentos:
            mes_inicio = int(investimento['Mes_Inicio'])
            mes_fim = int(investimento['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_investimentos.append(investimento['Per_Mensal'])
                mes_inicio += 1
        self.ComAporte = self.entry_investimento_aporte.get()

        # ADIANTAMENTO A PARCEIRO
        self.curva_de_adto = self.Consulta_Prazo_Curvas(self.entry_adto_parceiro_curva_adto.get(), Tela) 
        self.prazo_adto = [prazo['Prazo_Curva'] for prazo in self.curva_de_adto]
        if isinstance(self.prazo_adto, list) and len(self.prazo_adto) > 0:
            self.prazo_adto = float(self.prazo_adto[0])
        else:
            self.prazo_adto = 0

        self.inicio_adto = float(self.entry_adto_parceiro_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_adto = []  # Lista para armazenar os dados mensais
        for adto in self.curva_de_adto:
            mes_inicio = int(adto['Mes_Inicio'])
            mes_fim = int(adto['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_adto.append(adto['Per_Mensal'])
                mes_inicio += 1
        
        # VENDAS
        self.curva_de_vendas = self.Consulta_Prazo_Curvas(self.entry_vendas_curva.get(), Tela) 
        self.prazo_vendas = [prazo['Prazo_Curva'] for prazo in self.curva_de_vendas]
        if isinstance(self.prazo_vendas, list) and len(self.prazo_vendas) > 0:
            self.prazo_vendas = float(self.prazo_vendas[0])
        else:
           self. prazo_vendas = 0

        self.inicio_vendas = float(self.entry_vendas_inicio.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_vendas = []  # Lista para armazenar os dados mensais
        for vendas in self.curva_de_vendas:
            mes_inicio = int(vendas['Mes_Inicio'])
            mes_fim = int(vendas['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_vendas.append(vendas['Per_Mensal'])
                mes_inicio += 1
        
        # PROJETOS
        self.curva_de_projetos = self.Consulta_Prazo_Curvas(self.entry_projetos_curva_projeto.get(), Tela) 
        self.prazo_projetos = [prazo['Prazo_Curva'] for prazo in self.curva_de_projetos]
        if isinstance(self.prazo_projetos, list) and len(self.prazo_projetos) > 0:
            self.prazo_projetos = float(self.prazo_projetos[0])
        else:
            self.prazo_projetos = 0

        self.inicio_projetos = float(self.entry_projetos_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_projetos = []  # Lista para armazenar os dados mensais
        for projeto in self.curva_de_projetos:
            mes_inicio = int(projeto['Mes_Inicio'])
            mes_fim = int(projeto['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_projetos.append(projeto['Per_Mensal'])
                mes_inicio += 1

        # MkT
        self.curva_de_mkt = self.Consulta_Prazo_Curvas(self.entry_mkt_curva_mkt.get(), Tela) 
        self.prazo_mkt = [prazo['Prazo_Curva'] for prazo in self.curva_de_mkt]
        if isinstance(self.prazo_mkt, list) and len(self.prazo_mkt) > 0:
            self.prazo_mkt = float(self.prazo_mkt[0])
        else:
            self.prazo_mkt = 0

        self.inicio_mkt = float(self.entry_mkt_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_mkt = []  # Lista para armazenar os dados mensais
        for mkt in self.curva_de_mkt:
            mes_inicio = int(mkt['Mes_Inicio'])
            mes_fim = int(mkt['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_mkt.append(mkt['Per_Mensal'])
                mes_inicio += 1

        # OBRAS
        self.curva_de_obras = self.Consulta_Prazo_Curvas(self.entry_obras_curva_obras.get(), Tela) 
        self.prazo_obras = [prazo['Prazo_Curva'] for prazo in self.curva_de_obras]
        if isinstance(self.prazo_obras, list) and len(self.prazo_obras) > 0:
            self.prazo_obras = float(self.prazo_obras[0])
        else:
            self.prazo_obras = 0

        self.inicio_obras = float(self.entry_obras_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_obras = []  # Lista para armazenar os dados mensais
        for obras in self.curva_de_obras:
            mes_inicio = int(obras['Mes_Inicio'])
            mes_fim = int(obras['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_obras.append(obras['Per_Mensal'])
                mes_inicio += 1
        
        # PÓS OBRAS
        self.prazo_posobras = 60
        self.inicio_posobras = self.prazo_obras + self.inicio_obras + 1
        
        # ADM OBRAS
        self.inicio_admobras = float(self.entry_adm_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.curva_per_admobras = float(self.entry_adm_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
        
        #OVERHEAD
        self.prazo_total_obras = self.prazo_obras + self.prazo_projetos
        if self.prazo_vendas > 0:
            self.prazo_total_vendas = self.inicio_vendas + self.prazo_vendas + self.Nrper
        else:
            self.prazo_total_vendas = self.inicio_vendas + 0 + self.Nrper

        if self.prazo_total_vendas > self.prazo_total_obras:
            self.nr_anos_projeto = int(self.prazo_total_vendas)
        else:
            self.nr_anos_projeto = int(self.prazo_total_obras)
        
        self.prazo_overhead = self.nr_anos_projeto
        
        if isinstance(self.prazo_overhead, list) and len(self.prazo_overhead) > 0:
            self.prazo_overhead = float(self.prazo_overhead[0])
        else:
            self.prazo_overhead = 0
        self.inicio_overhead = float(self.entry_vendas_inicio.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres

        # FINANCIAMENTO
        self.valor_liberado = float(self.entry_financiamento_valor_captacao.get().replace('.', '').replace(',', '.')[:15])
        self.inicio_financiamento = float(self.entry_financiamento_inicio_liberacao.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        self.sistema_amortizacao = self.entry_financiamento_sistema_amortizacao.get()
        self.prazo_financiamento = float(self.entry_financiamento_prazo_amortizacao.get().replace("x", "").replace(",", ".")[:7])
        self.inicio_amortizacao = float(self.entry_financiamento_inicio_amortizacao.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        self.inicio_pagto_juros = float(self.entry_financiamento_inicio_pagto_juros.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
        self.valor_juros = float(self.entry_financiamento_juros.get().replace('.', '').replace(',', '.')[:15])
        self.per_taxajuros = float(self.entry_financiamento_juros_aa.get().replace("%", "").replace(",", ".")[:7]) / 100
        self.i_am = ((1 + self.per_taxajuros) ** (1/12))
        self.Financiador = self.entry_financiamento_financiador.get()

        self.curva_de_financiamento = self.Consulta_Prazo_Curvas(self.entry_financiamento_curva_liberacao.get(), Tela) 
        self.prazo_financiamento = [prazo['Prazo_Curva'] for prazo in self.curva_de_financiamento]
        if isinstance(self.prazo_financiamento, list) and len(self.prazo_financiamento) > 0:
            self.prazo_financiamento = float(self.prazo_financiamento[0])
        else:
            self.prazo_financiamento = 0

        self.curva_per_financiamento = []  # Lista para armazenar os dados mensais
        for financiamento in self.curva_de_financiamento:
            mes_inicio = int(financiamento['Mes_Inicio'])
            mes_fim = int(financiamento['Mes_Fim'])
            # Loop para cada mês no intervalo
            while mes_inicio <= mes_fim:
                self.curva_per_financiamento.append(financiamento['Per_Mensal'])
                mes_inicio += 1   
        
        self.nrper = float(self.entry_vendas_financiamento_prazo.get().replace(' x', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
        
        
        self.Valor_Liberacao = [0] * (self.nr_anos_projeto)  # Ajuste o tamanho conforme necessário
        self.Valor_ParcelaFinanciamento = [0] * (self.nr_anos_projeto )  # Ajuste o tamanho conforme necessário 
        self.Valor_Mensal = [0] * (self.nr_anos_projeto)
        self.Valor_Mensal_Parceiro = [0] * (self.nr_anos_projeto)
        self.Valor_Parcelas = [0] * (self.nr_anos_projeto)
        self.Valor_Parcelas_Parceiro = [0] * (self.nr_anos_projeto)
        self.Valor_Parceiro = [0] * (self.nr_anos_projeto)
        self.Valor_Comissao_Negocio = [0] * (self.nr_anos_projeto)
        self.Valor_Impostos = [0] * (self.nr_anos_projeto)
        self.Valor_Adm = [0] * (self.nr_anos_projeto)
        self.Valor_InvPar  = [0] * (self.nr_anos_projeto)
        self.Valor_Terreno = [0] * (self.nr_anos_projeto)
        self.Valor_Adto = [0] * (self.nr_anos_projeto)
        self.Valor_Comissao_Venda  = [0] * (self.nr_anos_projeto)
        self.Valor_Projetos = [0] * (self.nr_anos_projeto)
        self.Valor_Obras = [0] * (self.nr_anos_projeto)
        self.Valor_Adm_Obras = [0] * (self.nr_anos_projeto)
        self.Valor_PosObras = [0] * (self.nr_anos_projeto)
        self.Valor_Mkt = [0] * (self.nr_anos_projeto)
        self.Receita_Parceiro = [0] * (self.nr_anos_projeto )
        
        self.Fluxo = [0] * (self.nr_anos_projeto)
        self.Fluxo_Parceiro = [0] * (self.nr_anos_projeto)
        self.FluxoAcumulado = [0] * (self.nr_anos_projeto)
        self.FluxoAcumuladoPar = [0] * (self.nr_anos_projeto)
        
        self.Valor_SaldoAdto = [0] * (self.nr_anos_projeto)
        self.Valor_CustoAdto = [0] * (self.nr_anos_projeto)
        self.Valor_CustoAdtoPar = [0] * (self.nr_anos_projeto)
        self.Valor_DevolucaoAdto = [0] * (self.nr_anos_projeto)
        
        self.total_parceiro = 0
        self.npos = 1
        self.Entrada_NrPar = 1
        self.Reforcos_NrPar = 1
        self.Mensais_NrPar = 1
        self.val_entrada = 0
        self.val_reforcos = 0
        self.val_prestacao = 0
        self.vlr_amortizacao = 0
        self.vlr_a_vista = 0
        
        for vi_contador in range(0, self.nr_anos_projeto):
            # Bloco de Investimento Aquisição de Área
            if self.Vlr_Investimentos != 0:
                if (vi_contador + 1) >= self.inicio_investimentos and (vi_contador + 2 - self.inicio_investimentos) <= self.prazo_investimentos:
                    if self.ComAporte == "Não":
                        self.Valor_InvPar[vi_contador] = self.Vlr_Investimentos * self.curva_per_investimentos[int(vi_contador + 1 - self.inicio_investimentos)]
                        self.Valor_Terreno[vi_contador] = 0
                    else:
                        index = int(vi_contador + 1 - self.inicio_investimentos)
                        if 0 <= index < len(self.curva_per_investimentos):
                            self.Valor_InvPar[vi_contador] = 0
                            self.Valor_Terreno[vi_contador] = -self.Vlr_Investimentos * self.curva_per_investimentos[index]
                        else:
                            # # Handle the case where the index is not valid
                            # print(f"Index {index} is out of range for curva_per_investimentos with length {len(self.curva_per_investimentos)}.")
                            self.Valor_InvPar[vi_contador] = 0
                            self.Valor_Terreno[vi_contador] = 0

                else:
                    self.Valor_InvPar[vi_contador] = 0
                    self.Valor_Terreno[vi_contador] = 0
            else:
                self.Valor_InvPar[vi_contador] = 0
                self.Valor_Terreno[vi_contador] = 0
            
            # Bloco de Adto
            if self.Vlr_Adto != 0:
                if (vi_contador + 1) >= self.inicio_adto and (vi_contador + 2 - self.inicio_adto) <= self.prazo_adto:
                    self.Valor_Adto[vi_contador] = self.Vlr_Adto * -self.curva_per_adto[int(vi_contador + 1 - self.inicio_adto)]
                else:
                    self.Valor_Adto[vi_contador] = 0
            else:
                self.Valor_Adto[vi_contador] = 0

            # Bloco de Vendas
            
            if (vi_contador + 1) >= self.inicio_vendas and (vi_contador + 2 - self.inicio_vendas) <= self.prazo_vendas:
                self.Valor_Mensal[vi_contador] = self.Vlr_Venda * self.curva_per_vendas[int(vi_contador + 1 - self.inicio_vendas)]
                self.Valor_Mensal_Parceiro[vi_contador] = (self.vlr_VGV_líquido * self.per_parc) * self.curva_per_vendas[int(vi_contador + 1 - self.inicio_vendas)]
                self.Valor_Comissao_Venda[vi_contador] = self.Valor_Mensal[int(vi_contador)] * - self.per_comissao_venda
            else:
                self.Valor_Mensal[vi_contador] = 0
                self.Valor_Mensal_Parceiro[vi_contador] = 0
                self.Valor_Comissao_Venda[vi_contador] = 0
            
            # Bloco de Projetos
            if int(vi_contador + 1) >= int(self.inicio_projetos) and (int(vi_contador + 2) - self.inicio_projetos) <= int(self.prazo_projetos):
                self.Valor_Projetos[int(vi_contador)] = self.Vlr_Projetos * self.curva_per_projetos[int(vi_contador + 1 - self.inicio_projetos)]
            else:
                self.Valor_Projetos[vi_contador] = 0
            
            # Bloco de mkt
            if int(vi_contador + 1) >= int(self.inicio_mkt) and (int(vi_contador + 2) - self.inicio_mkt) <= int(self.prazo_mkt):
                self.Valor_Mkt[int(vi_contador)] = self.Vlr_Mkt * self.curva_per_mkt[int(vi_contador + 1 - self.inicio_mkt)]
            else:
                self.Valor_Mkt[vi_contador] = 0

            # Bloco de Obras
            if int(vi_contador + 1) >= int(self.inicio_obras):
                if (int(vi_contador + 2 - self.inicio_obras)) <= int(self.prazo_obras):
                    self.Valor_Obras[int(vi_contador)] = self.Vlr_Obra * self.curva_per_obras[int(vi_contador + 1 - self.inicio_obras)]
                    self.Valor_Adm_Obras[int(vi_contador)] = (self.Vlr_Obra * self.curva_per_obras[int(vi_contador + 1 - self.inicio_obras)]) * (float(self.curva_per_admobras))
                else:
                    self.Valor_Obras[int(vi_contador)] = 0
                    self.Valor_Adm_Obras[int(vi_contador)] = 0

                if int(vi_contador + 1) >= int(self.inicio_posobras) and int(self.npos) <= 60:
                    self.Valor_PosObras[int(vi_contador)] = self.Vlr_PosObra * (round((100 / 60) / 100, 4))
                    self.npos += 1
                else:
                    self.Valor_PosObras[int(vi_contador)] = 0
            else:
                self.Valor_Obras[int(vi_contador)] = 0
                self.Valor_Obras[int(vi_contador)] = 0
                self.Valor_Adm_Obras[int(vi_contador)] = 0
            
            # Bloco de Financiamento
            if self.Vlr_Financiamento != 0:
                if (vi_contador + 1) >= self.inicio_financiamento and (vi_contador + 2 - self.inicio_financiamento) <= self.prazo_financiamento:
                    self.Valor_Liberacao[int(vi_contador)] = -self.Vlr_Financiamento * self.curva_per_financiamento[int(vi_contador + 1 - self.inicio_financiamento)]
                else:
                    self.Valor_Liberacao[int(vi_contador)] = 0

                if self.Vlr_Financiamento != 0:
                    self.vlr_amortizacao = npf.pmt(self.i_am, self.prazo_financiamento, (self.Valor_Liberacao[int(vi_contador)] * -1) * ((1 + self.per_taxajuros) ** ((self.inicio_amortizacao - vi_contador) / 12)), fv=0, when='end'  )
                else:
                    self.vlr_amortizacao = 0

                for vicontadorPar in range(vi_contador, self.nr_anos_projeto + 1):
                    if vicontadorPar >= self.inicio_amortizacao and self.Mensais_NrPar <= self.prazo_financiamento:
                        self.Valor_ParcelaFinanciamento[int(vicontadorPar)] += self.vlr_amortizacao
                        self.Mensais_NrPar += 1
                
                self.Mensais_NrPar = 1
                self.val_prestacao = 0
                self.vlr_amortizacao = 0
            
            # Bloco Mensal
            if self.Valor_Mensal[int(vi_contador)] > 0:
                Vlr_AVista = self.Valor_Mensal[int(vi_contador)] * self.Per_Venda_Avista
                Vlr_AVista_Parceiro = self.Valor_Mensal_Parceiro[int(vi_contador)] * self.Per_Venda_Avista
                Reforcos_Period = vi_contador + (self.Periodicidade_Reforcos - 1)
                if self.Per_Entrada != 0:
                    if self.Per_Entrada != 0:
                        Val_Entrada = ((self.Valor_Mensal[int(vi_contador)] - Vlr_AVista) * self.Per_Entrada) / Nr_ParEntrada
                        Val_Entrada_Parceiro = ((self.Valor_Mensal_Parceiro[int(vi_contador)] - Vlr_AVista_Parceiro) * self.Per_Entrada) / Nr_ParEntrada
                    else:
                        Val_Entrada = 0
                        Val_Entrada_Parceiro = 0

                    if self.Per_Reforcos != 0:
                        Val_Reforços = (self.Valor_Mensal[int(vi_contador)] - Vlr_AVista) * self.Per_Reforcos / self.Nr_ParReforcos
                        Val_Reforços_Parceiro = (self.Valor_Mensal_Parceiro[int(vi_contador)] - Vlr_AVista_Parceiro) * self.Per_Reforcos / self.Nr_ParReforcos
                    else:
                        Val_Reforços = 0
                        Val_Reforços_Parceiro = 0
                    e = npf.pv(self.Per_Mensal,  Nr_ParEntrada, -Val_Entrada, fv=0, when='end'  )
                    e_Parceiro = npf.pv(self.Per_Mensal,  Nr_ParEntrada, -Val_Entrada_Parceiro, fv=0, when='end'  )
                    r = npf.pv(((1 + self.Per_Mensal) ** 12) - 1,  self.Nr_ParReforcos, -Val_Reforços, fv=0, when='end'  )
                    r_Parceiro = npf.pv(((1 + self.Per_Mensal) ** 12) - 1,  self.Nr_ParReforcos, -Val_Reforços_Parceiro, fv=0, when='end'  )
                    
                    if self.Per_Mensal != 0:
                        Val_Financiado = self.Valor_Mensal[int(vi_contador)] - e - r * (((1 + self.Per_Mensal) ** (Nr_ParEntrada - 1)) - 1)
                        Val_Financiado_Parceiro = self.Valor_Mensal_Parceiro[int(vi_contador)] - e_Parceiro - r_Parceiro * (((1 + self.Per_Mensal) ** (Nr_ParEntrada - 1)) - 1)
                    else:
                        Val_Financiado = self.Valor_Mensal[int(vi_contador)] - e - r
                        Val_Financiado_Parceiro = self.Valor_Mensal_Parceiro[int(vi_contador)] - e_Parceiro - r_Parceiro

                    # Amortização
                    if self.Sistema_Amortização_Cliente == "Price" or self.Sistema_Amortização_Cliente == "PRICE":
                        Val_Prestacao = npf.pmt(self.Per_Mensal,  self.Nrper + Nr_ParEntrada, -Val_Financiado, fv=0, when='end'  )
                        Val_Prestacao_Parceiro = npf.pmt(self.Per_Mensal,  self.Nrper + Nr_ParEntrada, -Val_Financiado_Parceiro, fv=0, when='end'  )
                    
                    elif self.Sistema_Amortização_Cliente == "SACOC":
                        Valor_Prestacao_SACOC = [0] * (self.Nrper + 1)  # Inicializa a lista
                        Valor_Prestacao_SACOC_Parceiro = [0] * (self.Nrper + 1)  # Inicializa a lista
                        for intAndamento in range(1, self.Nrper + 1):
                            Valor_Prestacao_SACOC[int(intAndamento)] = (Val_Financiado / self.Nrper) * ((1 + self.Per_Mensal) ** intAndamento)
                            Valor_Prestacao_SACOC_Parceiro[int(intAndamento)] = (Val_Financiado_Parceiro / self.Nrper) * ((1 + self.Per_Mensal) ** intAndamento)

                    # Cálculo do valor do terreno
                    Vlr_Terreno = float(self.TVendas_Preço_m2_semComissao) * float(self.TArea_LoteMedio)
                    # Cálculo da entrada
                    Vlr_Entrada = npf.pv(self.Per_Mensal,  Nr_ParEntrada, -(Vlr_Terreno * self.Per_Entrada / Nr_ParEntrada), fv=0, when='begin')
                    # Verificação e cálculo do valor de reforço
                    if self.Per_Reforcos != 0:
                        Vlr_Entrada = npf.pv(((1 + self.Per_Mensal) ** 12) - 1,  self.Nr_ParReforcos, -(Vlr_Terreno * self.Per_Reforcos / self.Nr_ParReforcos), fv=0, when='end'  )
                    else:
                        Vlr_Reforco = 0
                else:
                    Nr_ParEntrada = 1
                    Val_Reforços = (self.Valor_Mensal[int(vi_contador)] - Vlr_AVista) * self.Per_Reforcos / self.Nr_ParReforcos
                    Val_Reforços_Parceiro = (self.Valor_Mensal_Parceiro[int(vi_contador)] - Vlr_AVista_Parceiro) * self.Per_Reforcos / self.Nr_ParReforcos
                    e = 0
                    e_Parceiro = 0
                    r = npf.pv(((1 + self.Per_Mensal) ** 12) - 1,  self.Nr_ParReforcos, -Val_Reforços, fv=0, when='end')
                    r_Parceiro = npf.pv(((1 + self.Per_Mensal) ** 12) - 1,  self.Nr_ParReforcos, -Val_Reforços_Parceiro, fv=0, when='end')
                                    
                    if self.Per_Mensal != 0:
                        Val_Financiado = (self.Valor_Mensal[int(vi_contador)] - e - r - Vlr_AVista * (((1 + self.Per_Mensal) ** (Nr_ParEntrada - 1)) - 1))
                        Val_Financiado_Parceiro = (self.Valor_Mensal_Parceiro[int(vi_contador)] - e_Parceiro - r_Parceiro - Vlr_AVista_Parceiro * (((1 + self.Per_Mensal) ** (Nr_ParEntrada - 1)) - 1))
                    else:
                        Val_Financiado = (self.Valor_Mensal[int(vi_contador)] - e - r - Vlr_AVista)
                        Val_Financiado_Parceiro = (self.Valor_Mensal_Parceiro[int(vi_contador)] - e - r - Vlr_AVista_Parceiro)

                    # Calculo da prestação
                    if self.Sistema_Amortização_Cliente == "Price" or self.Sistema_Amortização_Cliente == "PRICE":
                        Val_Prestacao = npf.pmt(self.Per_Mensal, self.Nrper + Nr_ParEntrada, -Val_Financiado, fv=0, when='end'  )
                        Val_Prestacao_Parceiro = npf.pmt(self.Per_Mensal, self.Nrper + Nr_ParEntrada, -Val_Financiado_Parceiro, fv=0, when='end'  )
                    elif self.Sistema_Amortização_Cliente == "SACOC":
                        Valor_Prestacao_SACOC = [0] * (self.Nrper + 1)  # Inicializa a lista
                        Valor_Prestacao_SACOC_Parceiro = [0] * (self.Nrper + 1)  # Inicializa a lista
                        for intAndamento in range(1, self.Nrper + 1):
                            Valor_Prestacao_SACOC[int(intAndamento)] = (Val_Financiado / self.Nrper) * ((1 + self.Per_Mensal) ** intAndamento)
                            Valor_Prestacao_SACOC_Parceiro[int(intAndamento)] = (Val_Financiado_Parceiro / self.Nrper) * ((1 + self.Per_Mensal) ** intAndamento)

                    # Cálculo do valor do terreno e da prestação final
                    Vlr_Terreno = float(self.TVendas_Preço_m2_semComissao) * float(self.TArea_LoteMedio)
                    Val_Entrada = Val_Prestacao
                    Vlr_Reforco = npf.pmt(((1 + self.Per_Mensal) ** 12) - 1, self.Nr_ParReforcos, -(Vlr_Terreno * self.Per_Reforcos / self.Nr_ParReforcos), fv=0, when='end'  )
                    TParcela_PRICE_Vlr = npf.pmt(self.Per_Mensal, self.Nrper + Nr_ParEntrada, -Vlr_Terreno + (Vlr_Entrada + Vlr_Reforco), fv=0, when='end'  )
            
                for vicontadorPar in range(0, self.nr_anos_projeto):
                    if (vicontadorPar >= vi_contador) and (self.Entrada_NrPar <= Nr_ParEntrada):
                        self.Valor_Parcelas[int(vicontadorPar)] += Val_Entrada + Vlr_AVista
                        self.Valor_Parcelas_Parceiro[int(vicontadorPar)] += Val_Entrada_Parceiro + Vlr_AVista_Parceiro
                        
                        self.Valor_Parceiro[int(vicontadorPar)] = self.Valor_Parcelas_Parceiro[int(vicontadorPar)]
                        self.Valor_Comissao_Negocio[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Comissao_Negocio
                        self.Valor_Impostos[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Impostos
                        self.Valor_Adm[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -(float(self.Per_OverHead))
                        self.Entrada_NrPar += 1
                    
                    if Reforcos_Period == vicontadorPar and self.Reforcos_NrPar <= self.Nr_ParReforcos:
                        self.Valor_Parcelas[int(vicontadorPar)] += Val_Reforços
                        self.Valor_Parcelas_Parceiro[int(vicontadorPar)] += Val_Reforços_Parceiro
                        
                        self.Valor_Parceiro[int(vicontadorPar)] = self.Valor_Parcelas_Parceiro[int(vicontadorPar)]
                        self.Valor_Comissao_Negocio[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Comissao_Negocio
                        self.Valor_Impostos[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Impostos
                        self.Valor_Adm[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -(float(self.Per_OverHead))
                        
                        Reforcos_Period += self.Periodicidade_Reforcos
                        self.Reforcos_NrPar += 1
                    
                    if vicontadorPar >= (vi_contador + Nr_ParEntrada) and self.Mensais_NrPar <= self.Nrper:
                        if self.Sistema_Amortização_Cliente == "Price" or self.Sistema_Amortização_Cliente == "PRICE":
                            self.Valor_Parcelas[int(vicontadorPar)] += Val_Prestacao
                            self.Valor_Parcelas_Parceiro[int(vicontadorPar)] += Val_Prestacao_Parceiro
                            
                            self.Valor_Parceiro[int(vicontadorPar)] = self.Valor_Parcelas_Parceiro[int(vicontadorPar)]
                            self.Valor_Comissao_Negocio[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Comissao_Negocio
                            self.Valor_Impostos[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Impostos
                            self.Valor_Adm[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -(float(self.Per_OverHead))
                            
                        elif self.Sistema_Amortização_Cliente == "SACOC":
                            self.Valor_Parcelas[int(vicontadorPar)] += Valor_Prestacao_SACOC[int(intAndamento)]
                            self.Valor_Parcelas_Parceiro[int(vicontadorPar)] += Valor_Prestacao_SACOC_Parceiro[int(intAndamento)]
                            
                            self.Valor_Parceiro[int(vicontadorPar)] = self.Valor_Parcelas_Parceiro[int(vicontadorPar)]
                            self.Valor_Comissao_Negocio[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Comissao_Negocio
                            self. Valor_Impostos[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -self.Per_Impostos
                            self.Valor_Adm[int(vicontadorPar)] = self.Valor_Parcelas[int(vicontadorPar)] * -(float(self.Per_OverHead))
                            
                            intAndamento += 1
                            
                        self.Mensais_NrPar += 1
            
            self.Fluxo[int(vi_contador)] = (self.Valor_Parcelas[int(vi_contador)] + 
                                  self.Valor_Terreno[int(vi_contador)] + 
                                  self.Valor_Projetos[int(vi_contador)] + 
                                  self.Valor_Obras[int(vi_contador)] + 
                                  self.Valor_Adm_Obras[int(vi_contador)] + 
                                  self.Valor_Mkt[int(vi_contador)] + 
                                  self.Valor_PosObras[int(vi_contador)] - 
                                  self.Valor_Parcelas_Parceiro[int(vi_contador)] + 
                                  self.Valor_Comissao_Venda[int(vi_contador)] + 
                                  self.Valor_Comissao_Negocio[int(vi_contador)] + 
                                  self.Valor_Impostos[int(vi_contador)])
            
            self.Receita_Parceiro[int(vi_contador)] = self.Valor_Parceiro[int(vi_contador)] 
            self.total_parceiro += self.Receita_Parceiro[int(vi_contador)]
            # Reinicia as variáveis
            self.PayBack = 0
            self.PayBackPar = 0
            self.Val_Entrada = 0
            self.Val_Reforços = 0
            self.Val_Prestacao = 0
            self.Entrada_NrPar = 1
            self.Reforcos_NrPar = 1
            self.Mensais_NrPar = 1
        
        if self.Per_custoadto != 0: # Calcula o % de Amortização
            self.Per_AmortAdto = self.Per_custoadto
        else:
            self.Per_AmortAdto = 0

        # Inicialização das variáveis
        self.nrFluxosNegativos_Urb = 0
        self.nrFluxosNegativos_Par = 0
        self.Vlr_Exposicao_Maxima = 0
        for vi_contador in range(0, self.nr_anos_projeto):
            if vi_contador > 0:
                self.Valor_SaldoAdto[int(vi_contador)] = self.Valor_SaldoAdto[int(vi_contador-1)]
                if self.Valor_SaldoAdto[int(vi_contador-1)] != 0:
                    self.Valor_CustoAdtoPar[int(vi_contador)] = self.Valor_SaldoAdto[int(vi_contador-1)] * (self.Per_custoadtoPar / 12)
                    self.Valor_CustoAdto[int(vi_contador)] = 0
                    self.Valor_DevolucaoAdto[int(vi_contador)] = (self.Receita_Parceiro[int(vi_contador)] * self.Per_AmortAdto)
                    
                    if (self.Valor_DevolucaoAdto[int(vi_contador)] * -1) < self.Valor_SaldoAdto[int(vi_contador)]:
                        self.Valor_DevolucaoAdto[int(vi_contador)] = (self.Valor_SaldoAdto[int(vi_contador)]) * -1
                   
                self.Valor_SaldoAdto[int(vi_contador)] += self.Valor_Adto[int(vi_contador)] + self.Valor_CustoAdtoPar[int(vi_contador)] + self.Valor_DevolucaoAdto[int(vi_contador)]
                  
            else:
                self.Valor_SaldoAdto[int(vi_contador)] = self.Valor_Adto[int(vi_contador)]

            if self.Financiador == 'Sim':
                self.Fluxo_Parceiro[int(vi_contador)] = (self.Receita_Parceiro[int(vi_contador)] - 
                                               self.Valor_InvPar[int(vi_contador)] - self.Valor_Adto[int(vi_contador)] - 
                                               (self.Receita_Parceiro[int(vi_contador)] * self.Per_AmortAdto) +
                                                self.Valor_CustoAdtoPar[int(vi_contador)] + 
                                                (self.Valor_Liberacao[int(vi_contador)] * -1) + 
                                                (self.Valor_ParcelaFinanciamento[int(vi_contador)] * -1))
            else:
                self.Fluxo_Parceiro[vi_contador] = (self.Receita_Parceiro[int(vi_contador)] - 
                                               self.Valor_InvPar[int(vi_contador)] + 
                                               self.Valor_Adto[int(vi_contador)] - 
                                               (self.Receita_Parceiro[int(vi_contador)] * self.Per_AmortAdto) + 
                                               self.Valor_CustoAdtoPar[int(vi_contador)])
            
            if self.Fluxo_Parceiro[int(vi_contador)] < 0:
                self.nrFluxosNegativos_Par += 1
            
            self.Fluxo[int(vi_contador)] = (self.Fluxo[int(vi_contador)] + 
                                  self.Valor_Adm[int(vi_contador)] + 
                                  self.Valor_Adto[int(vi_contador)] + 
                                  self.Valor_DevolucaoAdto[int(vi_contador)] - 
                                  self.Valor_Liberacao[int(vi_contador)] + 
                                  self.Valor_ParcelaFinanciamento[int(vi_contador)])
            
            if self.Fluxo[int(vi_contador)] < 0:
                self.nrFluxosNegativos_Urb += 1
            
            if vi_contador == 0:
                self.FluxoAcumulado[int(vi_contador)] = self.Fluxo[int(vi_contador)]
                self.FluxoAcumuladoPar[int(vi_contador)] = self.Fluxo_Parceiro[int(vi_contador)]
                if self.Fluxo[int(vi_contador)] < 0:
                    self.Vlr_Exposicao_Maxima = self.Fluxo[int(vi_contador)]
                else:
                    self.Vlr_Exposicao_Maxima = 0
            else:
                self.FluxoAcumulado[int(vi_contador)] = self.FluxoAcumulado[int(vi_contador - 1)] + self.Fluxo[int(vi_contador)]
                self.FluxoAcumuladoPar[int(vi_contador)] = self.FluxoAcumuladoPar[int(vi_contador - 1)] + self.Fluxo_Parceiro[int(vi_contador)]
                if self.FluxoAcumulado[int(vi_contador)] < self.Vlr_Exposicao_Maxima:
                    self.Vlr_Exposicao_Maxima = self.FluxoAcumulado[int(vi_contador)] 

            if self.FluxoAcumulado[int(vi_contador)] <= 0:
                self.PayBack += 1

            if self.FluxoAcumuladoPar[int(vi_contador)] <= 0:
                self.PayBackPar += 1
        # print(self.Valor_DevolucaoAdto)
        if self.Vlr_Financiamento != 0:
            self.getirr = self.getIRR_EXEC(self.Fluxo, self.nr_anos_projeto)
            if not self.getirr:
                self.RetRate = 0
            else:
                self.RetRate = npf.irr(self.Fluxo)
            
            self.getirr = self.getIRR_EXEC(self.Fluxo_Parceiro, self.nr_anos_projeto)
            if not getirr:
                RetRatePar = 0
            else:
                RetRatePar = self.getIRR_EXEC(self.Fluxo_Parceiro(), self.nr_anos_projeto)
        else:
            self.getirr = self.getIRR_EXEC(self.Fluxo, self.nr_anos_projeto)
            if not self.getirr:
                self.RetRate = 0
            else:
                self.RetRate = npf.irr(self.Fluxo) 

            if self.Valor_InvPar != 0 and self.Per_Urban < 1:
                getirr = self.getIRR_EXEC(self.Fluxo_Parceiro, self.nr_anos_projeto)
                if not getirr:
                    RetRatePar = 0
                else:
                    RetRatePar = self.getIRR_EXEC(self.Fluxo_Parceiro, self.nr_anos_projeto)
            else:
                self.RetRatePar = 0
        
        if math.isnan(self.RetRate):
            self.entry_indicadores_tir_aa.delete(0, "end")
            self.entry_indicadores_tir_aa.insert(0, self.format_per_fx(0))
            self.entry_indicadores_tir_am.delete(0, "end")
            self.entry_indicadores_tir_am.insert(0, self.format_per_fx(0))
        else:
            self.entry_indicadores_tir_aa.delete(0, "end")
            self.entry_indicadores_tir_aa.insert(0,  self.format_per_fx(((float(1 + self.RetRate)) ** 12) - 1))
            self.entry_indicadores_tir_am.delete(0, "end")
            self.entry_indicadores_tir_am.insert(0, self.format_per_fx(float(self.RetRate)))

        self.entry_indicadores_payback.delete(0, "end")
        self.entry_indicadores_payback.insert(0, self.format_ano_fx((float(self.PayBack) / 12)))
        self.entry_indicadores_exposicaomax_caixa.delete(0, "end")
        self.entry_indicadores_exposicaomax_caixa.insert(0, self.format_valor_fx((float(self.Vlr_Exposicao_Maxima))))
        
        # Cálculo do valor presente líquido (NPV) para urbanizadora e parceiro
        discount_rate = ((float(1 + self.TPer_Desconto_VPL)) ** (1 / 12)) - 1

        NetPVal_Urbanizadora = npf.npv(discount_rate, self.Fluxo)
        NetPVal_Parceiro = npf.npv(discount_rate, self.Fluxo_Parceiro)

        # VPL dos resultados
        self.entry_indicadores_vpl_urbanizadora.delete(0, "end")
        self.entry_indicadores_vpl_urbanizadora.insert(0, self.format_valor_fx(float(NetPVal_Urbanizadora)))
        self.entry_indicadores_vpl_parceiro.delete(0, "end")
        self.entry_indicadores_vpl_parceiro.insert(0, self.format_valor_fx(float(NetPVal_Parceiro)))

        # Atribuição da taxa de juros
        Per_TaxaJuros = float(self.TPer_Desconto_VPL)
        # self.entry_financiamento_juros = vlr_total_liberado + vlr_total_amortizado # Ajustar quando existir

        self.Gravar_Estudos(
                            ID_Empresa, 
                            UF, 
                            Cidade, 
                            Tipo, 
                            Nome_da_Area,
                            Tela
                            )
    
    def Acessar_Maps(self):
        self.entry_informacoes_https.delete(0, 'end')
        # Construa a URL
        url = f"https://srv-web-full-gestor.eastus2.cloudapp.azure.com/maps/getCoordenadas.php?cidade={self.entry_municipio.get()}&uf={self.entry_uf.get()}" 
        # Abre a URL no navegador padrão
        webbrowser.open(url)
     
    def consulta_cep(self, cep, campo):
        # Faz a requisição para a API do ViaCEP
        url = f"https://viacep.com.br/ws/{cep}/xml/"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            # Carrega o conteúdo XML retornado na resposta
            xml_doc = ET.ElementTree(ET.fromstring(response.content))
            
            # Procura pelo campo desejado no XML
            for elem in xml_doc.iter(campo):
                return elem.text  # Retorna o texto do campo encontrado
                
        return None  # Caso o CEP não seja encontrado ou a requisição falhe
class Limpeza():

    def on_closing_tela_fluxo_projetado(self):
        self.janela_fluxo_projetado.destroy()  # Fechar a janela principal    
        self.janela_fluxo_projetado = None  # Initialize the attribute
        self.window_one.update_idletasks()  # Update the window to get correct dimensions
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 
    
    def on_closing_tela_documentos_anexos(self):
        self.janela_documentos_anexos.destroy()  # Fechar a janela principal    
        self.janela_documentos_anexos = None  # Initialize the attribute
        self.window_one.update_idletasks()  # Update the window to get correct dimensions
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 

    def on_closing_tela_pesquisa_mercado(self):
        self.janela_pesquisa_mercado.destroy()  # Fechar a janela principal    
        self.janela_pesquisa_mercado = None  # Initialize the attribute
        self.window_one.update_idletasks()  # Update the window to get correct dimensions
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 
    
    def limpar_campos_site(self):
        dta_atual = datetime.now()
        
        # Limpa a entrada
        self.text_descricao.delete(0, 'end')
        self.entry_informacoes_https.delete(0, 'end')
        
        # Limpa a lista atual antes de inserir novos resultados
        self.LSites.delete(*self.LSites.get_children())   

    def limpar_campos_pesquisa_mercado(self):
        valor_decimal = '0,00'
        valor_m2 = '0,00  m²'
        
        # Limpa a entrada
        self.entry_nome_empreendimento.delete(0, 'end')
        self.entry_area_unidade.delete(0, 'end')
        self.entry_preco_unidade.delete(0, 'end')
        self.entry_preco_m2_unidade.delete(0, 'end')
        self.entry_url.delete(0, 'end')

        self.entry_area_unidade.insert(0, valor_m2.strip())
        self.entry_preco_unidade.insert(0, valor_decimal.strip())
        self.entry_preco_m2_unidade.insert(0, valor_decimal.strip())

        
        # Limpa a lista atual antes de inserir novos resultados
        self.LPesquisa_Mercado.delete(*self.LPesquisa_Mercado.get_children())     

    def clear_screen_login(self):
        try:
            self.descrData2.destroy()
            self.descrData3.destroy()
            self.loginBot.destroy()
            self.insert_user.destroy()
            self.insert_senha.destroy()
        except:
            self.descrData3.destroy()
            self.cadastrese_user.destroy()
            self.cadastrese_senha.destroy()
            self.cadastrese.destroy()

    def clearFrame_principal(self):
        for widget in self.principal_frame.winfo_children():
            widget.destroy()

    def clearFrame_button(self):
        for widget in self.fr_comboModulos.winfo_children():
            widget.destroy()

        self.fr_comboModulos.destroy()  # Destroi
        self.fr_comboModulos = None  # Reseta a referência do frame atual

    def clear_frame(self):
        """Limpa todos os widgets do frame atual, mantendo menus e a janela principal."""

        if hasattr(self, 'login_frame'):
            self.login_frame.destroy()  # Destroi o Login
            self.login_frame = None  # Reseta a referência do frame atual
            del self.login_frame

        elif hasattr(self, 'login_frame'):
            self.cadastro_frame.destroy()  # Limpa Cadastro Usuários
            self.cadastro_frame = None

    def limpar_simulador_negocios(self):
        valor_decimal = '0,00'
        valor_percente = '0,00 %'
        valor_percente_taxa_vpl = '12,00 %'
        valor_m2 = '0,00  m²'
        valor_inicio = '1º mês'
        curva_basica = 'Padrão 1 Mês'
        sistema_amortizacao = 'PRICE'
        dta_atual = datetime.now()
        prazo = '1 x'
        # Limpa a entrada
        self.entry_area_total.delete(0, 'end')
        self.entry_area_total.insert(0, valor_decimal.strip())

        self.entry_area_aproveitamento.delete(0, 'end')
        self.entry_area_aproveitamento.insert(0, valor_percente.strip())

        self.entry_area_aproveitado.delete(0, 'end')
        self.entry_area_aproveitado.insert(0, valor_m2.strip())

        self.entry_area_lote_padrao.delete(0, 'end')
        
        self.entry_area_lote_medio.delete(0, 'end')
        self.entry_area_lote_medio.insert(0, valor_m2.strip())
        
        self.entry_area_nr_lotes.delete(0, 'end')
        self.entry_area_nr_lotes.insert(0, valor_decimal.strip())

        self.entry_participacao_urbanizador.delete(0, 'end')
        self.entry_participacao_urbanizador.insert(0, valor_percente.strip())

        self.entry_participacao_parceiro.delete(0, 'end')
        self.entry_participacao_parceiro.insert(0, valor_percente.strip())

        self.entry_participacao_permuta.delete(0, 'end')
        self.entry_participacao_permuta.insert(0, valor_percente.strip())

        self.entry_comissao_intermediacao.delete(0, 'end')
        self.entry_comissao_intermediacao.insert(0, valor_percente.strip())

        self.entry_admmkt_parceiro.delete(0, 'end')
        self.entry_admmkt_parceiro.insert(0, valor_percente.strip())

        self.entry_total_urbanizadora.delete(0, 'end')
        self.entry_total_urbanizadora.insert(0, valor_percente.strip())

        self.entry_total_parceiro.delete(0, 'end')
        self.entry_total_parceiro.insert(0, valor_percente.strip())

        self.entry_investimento_valor.delete(0, 'end')
        self.entry_investimento_valor.insert(0, valor_decimal.strip())
        
        self.entry_investimento_inicio_desembolso.delete(0, 'end')
        self.entry_investimento_inicio_desembolso.insert(0, valor_inicio.strip())

        self.entry_investimento_curva_investimento.delete(0, 'end')
        self.entry_investimento_curva_investimento.insert(0, curva_basica.strip())
        
        self.entry_adto_parceiro_valor.delete(0, 'end')
        self.entry_adto_parceiro_valor.insert(0, valor_decimal.strip())

        self.entry_adto_parceiro_per_urbanizadora.delete(0, 'end')
        self.entry_adto_parceiro_per_urbanizadora.insert(0, valor_percente.strip())

        self.entry_adto_parceiro_per_parceiro.delete(0, 'end')
        self.entry_adto_parceiro_per_parceiro.insert(0, valor_percente.strip())

        self.entry_adto_parceiro_inicio_desembolso.delete(0, 'end')
        self.entry_adto_parceiro_inicio_desembolso.insert(0, valor_inicio.strip())

        self.entry_adto_parceiro_curva_adto.delete(0, 'end')
        self.entry_adto_parceiro_curva_adto.insert(0, curva_basica.strip())

        self.entry_vendas_preco_m2.delete(0, 'end')
        self.entry_vendas_preco_m2.insert(0, valor_decimal.strip())

        self.entry_vendas_comissao_per.delete(0, 'end')
        self.entry_vendas_comissao_per.insert(0, valor_percente.strip())

        self.entry_vendas_vendas_preco_m2_com_comissao.delete(0, 'end')
        self.entry_vendas_vendas_preco_m2_com_comissao.insert(0, valor_decimal.strip())

        self.entry_vendas_lote_medio.delete(0, 'end')
        self.entry_vendas_lote_medio.insert(0, valor_decimal.strip())

        self.entry_vendas_financiamento_prazo.delete(0, 'end')
        self.entry_vendas_financiamento_prazo.insert(0, prazo.strip())

        self.entry_vendas_sistema_amortizacao.delete(0, 'end')
        self.entry_vendas_sistema_amortizacao.insert(0, sistema_amortizacao.strip())

        self.entry_vendas_juros_aa.delete(0, 'end')
        self.entry_vendas_juros_aa.insert(0, valor_percente.strip())

        self.entry_vendas_juros_am.delete(0, 'end')
        self.entry_vendas_juros_am.insert(0, valor_percente.strip())

        self.entry_vendas_entrada.delete(0, 'end')
        self.entry_vendas_entrada.insert(0, valor_percente.strip())

        self.entry_vendas_nr_parcelas_entrada.delete(0, 'end')
        self.entry_vendas_nr_parcelas_entrada.insert(0, '1 x')

        self.entry_vendas_reforcos.delete(0, 'end')
        self.entry_vendas_reforcos.insert(0, valor_percente.strip())

        self.entry_vendas_nr_parcelas_reforcos.delete(0, 'end')
        self.entry_vendas_nr_parcelas_reforcos.insert(0, '1 x')

        self.entry_vendas_period_reforcos.delete(0, 'end')
        self.entry_vendas_period_reforcos.insert(0, '12º mês')
        
        self.entry_vendas_per_avista.delete(0, 'end')
        self.entry_vendas_per_avista.insert(0, valor_percente.strip())

        self.entry_vendas_inicio.delete(0, 'end')
        self.entry_vendas_inicio.insert(0, valor_inicio.strip())

        self.entry_vendas_curva.delete(0, 'end')
        self.entry_vendas_curva.insert(0, curva_basica.strip())

        self.entry_vendas_parcela_price.delete(0, 'end')
        self.entry_vendas_parcela_price.insert(0, valor_decimal.strip())

        self.entry_vendas_parcela_sacoc.delete(0, 'end')
        self.entry_vendas_parcela_sacoc.insert(0, valor_decimal.strip())

        self.entry_projetos_per_obra.delete(0, 'end')
        self.entry_projetos_per_obra.insert(0, valor_percente.strip())

        self.entry_projetos_valor_total.delete(0, 'end')
        self.entry_projetos_valor_total.insert(0, valor_decimal.strip())

        self.entry_projetos_inicio_desembolso.delete(0, 'end')
        self.entry_projetos_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_projetos_curva_projeto.delete(0, 'end')
        self.entry_projetos_curva_projeto.insert(0, curva_basica.strip())

        self.entry_mkt_per_vgv.delete(0, 'end')
        self.entry_mkt_per_vgv.insert(0, valor_percente.strip())

        self.entry_mkt_valor_total.delete(0, 'end')
        self.entry_mkt_valor_total.insert(0, valor_decimal.strip())

        self.entry_mkt_inicio_desembolso.delete(0, 'end')
        self.entry_mkt_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_mkt_curva_mkt.delete(0, 'end')
        self.entry_mkt_curva_mkt.insert(0, curva_basica.strip())

        self.entry_overhead_per_vgv.delete(0, 'end')
        self.entry_overhead_per_vgv.insert(0, valor_percente.strip())

        self.entry_overhead_valor_total.delete(0, 'end')
        self.entry_overhead_valor_total.insert(0, valor_decimal.strip())

        self.entry_overhead_inicio_desembolso.delete(0, 'end')
        self.entry_overhead_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_overhead_curva_overhead.delete(0, 'end')
        self.entry_overhead_curva_overhead.insert(0, curva_basica.strip())

        self.entry_obras_valor_m2.delete(0, 'end')
        self.entry_obras_valor_m2.insert(0, valor_decimal.strip())

        self.entry_obras_valor_total.delete(0, 'end')
        self.entry_obras_valor_total.insert(0, valor_decimal.strip())

        self.entry_obras_inicio_desembolso.delete(0, 'end')
        self.entry_obras_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_obras_curva_obras.delete(0, 'end')
        self.entry_obras_curva_obras.insert(0, curva_basica.strip())

        self.entry_pos_obras_per_obras.delete(0, 'end')
        self.entry_pos_obras_per_obras.insert(0, valor_percente.strip())

        self.entry_pos_obras_valor_total.delete(0, 'end')
        self.entry_pos_obras_valor_total.insert(0, valor_decimal.strip())

        self.entry_pos_obras_inicio_desembolso.delete(0, 'end')
        self.entry_pos_obras_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_pos_obras_curva_obras.delete(0, 'end')
        self.entry_pos_obras_curva_obras.insert(0, 'Pós Obras 60 Meses')

        self.entry_adm_per_obras.delete(0, 'end')
        self.entry_adm_per_obras.insert(0, valor_percente.strip())

        self.entry_adm_valor_total.delete(0, 'end')
        self.entry_adm_valor_total.insert(0, valor_decimal.strip())

        self.entry_adm_inicio_desembolso.delete(0, 'end')
        self.entry_adm_inicio_desembolso.insert(0, valor_inicio.strip())
        
        self.entry_adm_curva_obras.delete(0, 'end')
        self.entry_adm_curva_obras.insert(0, curva_basica.strip())

        self.entry_financiamento_valor_captacao.delete(0, 'end')
        self.entry_financiamento_valor_captacao.insert(0, valor_decimal.strip())

        self.entry_financiamento_sistema_amortizacao.delete(0, 'end')
        self.entry_financiamento_sistema_amortizacao.insert(0, sistema_amortizacao.strip())

        self.entry_financiamento_prazo_amortizacao.delete(0, 'end')
        self.entry_financiamento_prazo_amortizacao.insert(0, prazo.strip())

        self.entry_financiamento_inicio_amortizacao.delete(0, 'end')
        self.entry_financiamento_inicio_amortizacao.insert(0, valor_inicio.strip())

        self.entry_financiamento_inicio_pagto_juros.delete(0, 'end')
        self.entry_financiamento_inicio_pagto_juros.insert(0, valor_inicio.strip())

        self.entry_financiamento_juros.delete(0, 'end')
        self.entry_financiamento_juros.insert(0, valor_decimal.strip())

        self.entry_financiamento_juros_aa.delete(0, 'end')
        self.entry_financiamento_juros_aa.insert(0, valor_percente.strip())

        self.entry_financiamento_inicio_liberacao.delete(0, 'end')
        self.entry_financiamento_inicio_liberacao.insert(0, valor_inicio.strip())
        
        self.entry_financiamento_curva_liberacao.delete(0, 'end')
        self.entry_financiamento_curva_liberacao.insert(0, curva_basica.strip())

        
        self.entry_dre_vgv_bruto.delete(0, 'end')
        self.entry_dre_vgv_bruto.insert(0, valor_decimal.strip())

        self.entry_dre_comissao.delete(0, 'end')
        self.entry_dre_comissao.insert(0, valor_decimal.strip())

        self.entry_dre_vgv_liquido.delete(0, 'end')
        self.entry_dre_vgv_liquido.insert(0, valor_decimal.strip())

        self.entry_dre_impostos.delete(0, 'end')
        self.entry_dre_impostos.insert(0, valor_decimal.strip())

        self.entry_dre_comissao_negocio.delete(0, 'end')
        self.entry_dre_comissao_negocio.insert(0, valor_decimal.strip())

        self.entry_dre_receita_liquida.delete(0, 'end')
        self.entry_dre_receita_liquida.insert(0, valor_decimal.strip())

        self.entry_dre_vgv_parceiro.delete(0, 'end')
        self.entry_dre_vgv_parceiro.insert(0, valor_decimal.strip())

        self.entry_dre_receita_liquida_urbanizadora.delete(0, 'end')
        self.entry_dre_receita_liquida_urbanizadora.insert(0, valor_decimal.strip())

        self.entry_dre_ebtda_valor.delete(0, 'end')
        self.entry_dre_ebtda_valor.insert(0, valor_decimal.strip())

        self.entry_dre_ebtda_per.delete(0, 'end')
        self.entry_dre_ebtda_per.insert(0, valor_percente.strip())

        self.entry_indicadores_tir_aa.delete(0, 'end')
        self.entry_indicadores_tir_aa.insert(0, valor_percente.strip())

        self.entry_indicadores_tir_am.delete(0, 'end')
        self.entry_indicadores_tir_am.insert(0, valor_percente.strip())

        self.entry_indicadores_payback.delete(0, 'end')
        self.entry_indicadores_payback.insert(0, '0 Anos')

        self.entry_indicadores_multiplicador_investimento.delete(0, 'end')
        self.entry_indicadores_multiplicador_investimento.insert(0, prazo.strip())

        self.entry_indicadores_exposicaomax_caixa.delete(0, 'end')
        self.entry_indicadores_exposicaomax_caixa.insert(0, valor_decimal.strip())

        self.entry_indicadores_vpl_urbanizadora.delete(0, 'end')
        self.entry_indicadores_vpl_urbanizadora.insert(0, valor_decimal.strip())

        self.entry_indicadores_vpl_parceiro.delete(0, 'end')
        self.entry_indicadores_vpl_parceiro.insert(0, valor_decimal.strip())
        
        self.entry_taxa_desconto.delete(0, 'end')
        self.entry_taxa_desconto.insert(0, valor_percente_taxa_vpl.strip())

        self.text_observacoes.delete('1.0', 'end')

        self.entry_informacoes_status.delete(0, 'end')
        self.entry_informacoes_status.insert(0, '')

        self.entry_informacoes_anexos.delete(0, 'end')
        
        self.entry_informacoes_data.delete(0, 'end')
        self.entry_informacoes_data.insert(0, dta_atual.strftime("%d/%m/%Y"))
        
        self.entry_informacoes_unidade_negocio.delete(0, 'end')
        self.entry_informacoes_https.delete(0, 'end')
        self.entry_informacoes_maps.delete(0, 'end')

    def limpar_opcoes(self, event):
        if hasattr(self, 'janela_opcoes'):
            if self.janela_opcoes.winfo_exists():
                self.janela_opcoes.destroy()
                del self.janela_opcoes  # Opcional: Remover referência
    
    def limpar_campos_lcto(self):
        valor_decimal = '0,00'
        valor_percente = '0,00 %'
        valor_percente_taxa_vpl = '12,00 %'
        valor_m2 = '0,00  m²'
        valor_inicio = '1º mês'
        curva_basica = 'Padrão 1 Mês'
        sistema_amortizacao = 'PRICE'
        dta_atual = datetime.now()
        prazo = 1
        
        # Limpa a entrada
        self.entry_doc_num.delete(0, 'end')
        self.entry_doc_dt_emissao.delete(0, 'end')
        self.entry_doc_serie.delete(0, 'end')
        self.entry_doc_numcontrato.delete(0, 'end')
        self.entry_doc_valor_total.delete(0, 'end')
        self.entry_doc_parcelas.delete(0, 'end')
        self.entry_info_pag_nr_parc.delete(0, 'end')
        self.entry_info_pag_forma_liq.delete(0, 'end')
        self.entry_info_pag_dt_venc.delete(0, 'end')
        self.entry_info_pag_valor_parc.delete(0, 'end')
        self.text_historico.delete('1.0', 'end')
        self.entry_itens_nota_prod_descr.delete(0, 'end')
        self.entry_itens_nota_centro.delete(0, 'end')
        self.entry_itens_nota_natureza.delete(0, 'end')
        self.entry_itens_nota_peso.delete(0, 'end')
        self.entry_itens_nota_quant2.delete(0, 'end')
        self.entry_itens_nota_valor_unit.delete(0, 'end')
        self.entry_itens_nota_valor_total.delete(0, 'end')
        
        self.entry_doc_num.insert(0, '')
        self.entry_doc_dt_emissao.insert(0, dta_atual.strftime("%d/%m/%Y"))
        self.entry_doc_serie.insert(0, 'U')
        self.entry_doc_numcontrato.insert(0, '')
        self.entry_doc_valor_total.insert(0, valor_decimal.strip())
        self.entry_doc_parcelas.insert(0, int(prazo))
        self.entry_info_pag_nr_parc.insert(0, int(prazo))
        self.entry_info_pag_forma_liq.insert(0, '')
        self.entry_info_pag_dt_venc.insert(0, dta_atual.strftime("%d/%m/%Y"))
        self.entry_info_pag_valor_parc.insert(0, valor_decimal.strip())
        self.text_historico.insert('1.0', '')
        self.entry_itens_nota_prod_descr.insert(0, '')
        self.entry_itens_nota_centro.insert(0,'')
        self.entry_itens_nota_natureza.insert(0, '')
        self.entry_itens_nota_peso.insert(0, valor_decimal.strip())
        self.entry_itens_nota_quant2.insert(0, valor_decimal.strip())
        self.entry_itens_nota_valor_unit.insert(0, valor_decimal.strip())
        self.entry_itens_nota_valor_total.insert(0, valor_decimal.strip())
        
        # Limpa a lista atual antes de inserir novos resultados
        self.LParcelasFinanceiras.delete(*self.LParcelasFinanceiras.get_children())
        self.LItens.delete(*self.LItens.get_children())

    def on_closing(self):
        if self.window_one.winfo_exists:
            self.window_one.destroy()  # Fechar a janela principal 
            self.window_one = None  # Initialize the attribute 
            self.treeview = None

    def on_closing_tela_negocios(self):
        self.janela_simulador_rel.destroy()  # Fechar a janela principal    
        self.janela_simulador_rel = None  # Initialize the attribute
        self.window_one.update_idletasks()  # Update the window to get correct dimensions
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 

    def on_closing_tela_premissas(self):
        self.janela_premissas.destroy()  # Fechar a janela principal    
        self.janela_premissas = None  # Initialize the attribute
        self.window_one.update_idletasks()  # Update the window to get correct dimensions
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 

    def  on_closing_tela(self, tela):
        # if tela is not None:
        tela.destroy()     
        tela = None  
    
        self.window_one.update_idletasks()  
        width = self.window_one.winfo_screenwidth()
        height = self.window_one.winfo_screenheight()
        self.window_one.geometry(f"{width}x{height}+0+0") 
       
    def toggle_button_state(self, button):
        # Check the current state and toggle it
        if button.cget("state") == "normal":
            button.config(state="disabled")  # Disable the button
        else:
            button.config(state="normal")  # Enable the button
class Formatos():

    def checar_data(self, data_string, formato='%Y-%m-%d'):
        try:
            # Tenta converter a string para um objeto de data
            data = datetime.strptime(data_string, formato)
            return True
        except ValueError:
            messagebox.showerror("Erro", 'Data Digitada Inválida')
            # Se ocorrer um erro, a data não é válida
            return False
    
    def calendario(self, event, target):
        # self.window_calendar = Tk()
        self.window_calendar = customtkinter.CTkToplevel(self.window_one)
        self.window_calendar.title('Calendário')
        calendario = tkcalendar.Calendar(self.window_calendar, locale='pt_br')
        calendario.pack()
       
        def get_data(event):
            dta = calendario.get_date()
            for widget in self.window_calendar.winfo_children():
                widget.destroy()

            self.window_calendar.destroy()  # Destroi
            self.window_calendar = None  # Reseta a referência do frame atual
            target.delete(0, "end")
            target.insert(0, dta.strip())

        calendario.bind('<<CalendarSelected>>', get_data)
        self.window_calendar.focus_force()
        self.window_calendar.grab_set()

    def justificar_texto(self, event, target):
        # Obtém o texto atual
        texto = target.get()  # Obtém o texto do início até o final

        # Limpa a textbox e insere o texto justificado
        target.delete(0, "end")  # Limpa a textbox
        lines = texto.splitlines()  # Divide o texto em linhas
        
        # Justifica cada linha
        justified = [" ".join(line.split()) for line in lines]  # Remove múltiplos espaços e reconstitui cada linha
        target.insert(0, "\n".join(justified))  # Insere as linhas justificadas
    
    def format_x_fx(self, valor):
        text = f"{valor:_.0f}"
        text = text.replace('.', ',').replace('_', '.')
        text = text + ' x'
        return text

    def format_x(self, event, target):
        if target.get() != '':
            text = float(target.get().replace(' x', '').replace('.', '').replace(',', '.')[:15])
            new_text = ''

            if event.keysym.lower() == "backspace":
                return

            new_text = self.format_x_fx(text)
            target.delete(0, "end")
            target.insert(0, new_text.strip())

    def format_mes_fx(self, valor):
        if isinstance(valor, str):
            try:
                valor = int(valor)
            except ValueError:
                return valor  # Retorna o valor original se não puder ser convertido para int
        
        text = f"{valor:_.0f}"
        text = text.replace("_", ".")
        return f"{text}º mês"

    def format_ano_fx(self, valor):
        text = f"{valor:_.0f}"
        text = text.replace('.', ',').replace('_', '.')
        text = text + ' Anos'
        return text
    
    def format_mes(self, event, target):
        if target.get() != '':
            text = float(target.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15])
            new_text = ''

            if event.keysym.lower() == "backspace":
                return

            new_text = self.format_mes_fx(text)
            target.delete(0, "end")
            target.insert(0, new_text.strip())

    def format_valor_fx(self, valor):
        if valor is None:
            valor = 0
        text = f"{valor:_.2f}"
        text = text.replace('.', ',').replace('_', '.')
        return text
    
    def format_valor(self, event, target):
         if target.get() != '':
            text = float(target.get().replace('.', '').replace(',', '.')[:15])
            new_text = ''

            if event.keysym.lower() == "backspace":
                return

            new_text = self.format_valor_fx(text)
            target.delete(0, "end")
            target.insert(0, new_text)
    
    def format_m2_fx(self, valor):
        text = f"{valor:_.2f}"
        text = text.replace('.', ',').replace('_', '.')
        text = text + ' m²'
        return text

    def format_m2(self, event, target):
        if target.get() != '':
            text = float(target.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
            new_text = ''

            if event.keysym.lower() == "backspace":
                return

            new_text = self.format_m2_fx(text)
            target.delete(0, "end")
            target.insert(0, new_text.strip())
    
    def format_per_fx(self, valor):
        text = f"{valor:.2%}"
        text = text.replace('.', ',')
        return text
    
    def format_per(self, event, target, target_destino):
        if target.get() != '':
            text = float(target.get().replace("%", "").replace(",", ".")[:7]) / 100
            parti = text
            new_text = ""

            if event.keysym.lower() == "backspace":
                return
            
            if float(parti) > 1:
                messagebox.showinfo('%', 'Percentual Não pode ser Maio que 100%!!!!')
                target.focus()
                parti = 0
                new_text = ''
                target.focus()
                if isinstance(target, ctk.CTkEntry):
                    target.select_range(0, 'end')  # Seleciona todo o texto 
            else:
                new_text = self.format_per_fx(text)
                target_destino.focus()
                if isinstance(target_destino, ctk.CTkEntry):
                    target_destino.select_range(0, 'end')  # Seleciona todo o texto
        else:
            new_text = ''
        
        target.delete(0, "end")
        target.insert(0, new_text.strip())
    
    def format_juros_am(self, event, target, entry_juros_aa):
        if entry_juros_aa.get() != '':
            i_aa = float(entry_juros_aa.get().replace("%", "").replace(",", ".")[:7]) / 100
            i_am = ((i_aa + 1) ** (1/12)) - 1
            
            i_am = self.format_per_fx(i_am)
            target.delete(0, "end")
            target.insert(0, i_am)

    def format_custo_projetos(self, event, janela):
        if self.entry_projetos_per_obra.get() != '':
            custo_obra = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
            per_custo_projeto = float(self.entry_projetos_per_obra.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_projeto = custo_obra * per_custo_projeto
            
            custo_projeto = self.format_valor_fx(custo_projeto)
            self.entry_projetos_valor_total.delete(0, "end")
            self.entry_projetos_valor_total.insert(0, custo_projeto)
    
    def format_custo_mkt(self, event, janela):
        if self.entry_mkt_per_vgv.get() != '':
            vgv_bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
            per_custo_mkt = float(self.entry_mkt_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_mkt = vgv_bruto * -per_custo_mkt
            
            custo_mkt = self.format_valor_fx(custo_mkt)
            self.entry_mkt_valor_total.delete(0, "end")
            self.entry_mkt_valor_total.insert(0, custo_mkt)

    def format_custo_overhead(self, event, janela):
        if self.entry_overhead_per_vgv.get() != '':
            vgv_bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
            per_custo_overhead = float(self.entry_overhead_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_overhead = vgv_bruto * -per_custo_overhead
            
            inicio_vendas = float(self.entry_vendas_inicio.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
            prazo_da_curva = self.Consulta_Prazo_Curvas(self.entry_vendas_curva.get(), janela) # fazer função para buscar curvas
            prazo_vendas = [prazo['Prazo_Curva'] for prazo in prazo_da_curva]
            nrper = float(self.entry_vendas_financiamento_prazo.get().replace(' x', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
            if isinstance(prazo_vendas, list) and len(prazo_vendas) > 0:
                nr_anos_projeto = inicio_vendas + prazo_vendas[0] + nrper
            else:
                nr_anos_projeto = inicio_vendas + 0 + nrper
            
            overhead_inicio = self.entry_vendas_inicio.get()
            overhead_curva = 'Over Head ' + str(int(nr_anos_projeto)) + ' meses'

            custo_overhead = self.format_valor_fx(custo_overhead)
            self.entry_overhead_valor_total.delete(0, "end")
            self.entry_overhead_valor_total.insert(0, custo_overhead)

            self.entry_overhead_inicio_desembolso.delete(0, "end")
            self.entry_overhead_inicio_desembolso.insert(0, overhead_inicio)
           
            self.entry_overhead_curva_overhead.delete(0, "end")
            self.entry_overhead_curva_overhead.insert(0, overhead_curva)

    def format_custo_obras(self, event, janela):
        if self.entry_obras_valor_m2.get() != '':
            custo_m2 = float(self.entry_obras_valor_m2.get().replace('.', '').replace(',', '.')[:15])
            area_empreendimento = float(self.entry_area_aproveitado.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
            custo_obra = area_empreendimento * -custo_m2
                        
            custo_obra = self.format_valor_fx(custo_obra)
            self.entry_obras_valor_total.delete(0, "end")
            self.entry_obras_valor_total.insert(0, custo_obra)
    
    def format_custo_posobras(self, event, janela):
        if self.entry_pos_obras_per_obras.get() != '':
            custo_obras = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
            per_custo_posobras = float(self.entry_pos_obras_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_posobras = custo_obras * per_custo_posobras
                        
            custo_posobras = self.format_valor_fx(custo_posobras)
            
            self.curva_de_obras = self.Consulta_Prazo_Curvas(self.entry_obras_curva_obras.get(), janela) 
            self.prazo_obras = float(float(self.curva_de_obras[0]['Prazo_Curva'])) 
            self.inicio_obras = float(self.entry_obras_inicio_desembolso.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
            posobras_inicio = self.format_mes_fx(self.prazo_obras + self.inicio_obras + 1)
            posobras_curva = 'Pós Obras 60 Meses'

            self.entry_pos_obras_valor_total.delete(0, "end")
            self.entry_pos_obras_valor_total.insert(0, custo_posobras)

            self.entry_pos_obras_inicio_desembolso.delete(0, "end")
            self.entry_pos_obras_inicio_desembolso.insert(0, posobras_inicio)

            self.entry_pos_obras_curva_obras.delete(0, "end")
            self.entry_pos_obras_curva_obras.insert(0, posobras_curva)

    def format_custo_admobras(self, event, janela):
        if self.entry_adm_per_obras.get() != '':
            custo_obras = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
            per_custo_admobras = float(self.entry_adm_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_admobras = custo_obras * per_custo_admobras
                        
            custo_admobras = self.format_valor_fx(custo_admobras)
            self.entry_adm_valor_total.delete(0, "end")
            self.entry_adm_valor_total.insert(0, custo_admobras)

            self.entry_adm_inicio_desembolso.delete(0, "end")
            self.entry_adm_inicio_desembolso.insert(0, self.entry_obras_inicio_desembolso.get())

            self.entry_adm_curva_obras.delete(0, "end")
            self.entry_adm_curva_obras.insert(0, self.entry_obras_curva_obras.get())
    
    def format_dre(self, event, janela):
        area_empreendimento = float(self.entry_area_aproveitado.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
        valor_venda_m2 = float(self.entry_vendas_vendas_preco_m2_com_comissao.get().replace('.', '').replace(',', '.')[:15])
        comissao_venda_per = float(self.entry_vendas_comissao_per.get().replace("%", "").replace(",", ".")[:7]) / 100
        comissao_negocio_per = float(self.entry_comissao_intermediacao.get().replace("%", "").replace(",", ".")[:7]) / 100
        if hasattr(self, 'combo_tpo_projeto'):
            if self.combo_tpo_projeto.get() != '':
                impostos_per = self.get_aliquota_imposto(self.combo_tpo_projeto.get())
                impostos_per = float(impostos_per[0])
            else:
                impostos_per = float(0)
        elif hasattr(self, 'entry_tpo_projeto'):
            if self.entry_nome_cenario.get() != '':
                impostos_per = self.get_aliquota_imposto(self.entry_tpo_projeto.get())
                impostos_per = float(impostos_per[0])
            else:
                impostos_per = float(0)
        else:
            impostos_per = float(0)

        urbanizador_per = float(self.entry_participacao_urbanizador.get().replace("%", "").replace(",", ".")[:7]) / 100
        parceiro_per = float(self.entry_total_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        investimento = self.entry_investimento_aporte.get()
        custo_investimento =  float(self.entry_investimento_valor.get().replace('.', '').replace(',', '.')[:15])
        custos_projetos = float(self.entry_projetos_valor_total.get().replace('.', '').replace(',', '.')[:15])
        custos_mkt = float(self.entry_mkt_valor_total.get().replace('.', '').replace(',', '.')[:15])
        custos_overhead = float(self.entry_overhead_valor_total.get().replace('.', '').replace(',', '.')[:15])
        custos_obras = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        custos_posobras = float(self.entry_pos_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
        custos_admobras = float(self.entry_adm_valor_total.get().replace('.', '').replace(',', '.')[:15])
        
        vgv_bruto = area_empreendimento * valor_venda_m2
        comissao_venda = vgv_bruto * comissao_venda_per
        vgv_liquido = vgv_bruto - comissao_venda
        impostos = vgv_liquido * impostos_per
        comissao_negocio = (vgv_liquido - impostos) * comissao_negocio_per
        receita_liquida = vgv_liquido - impostos - comissao_negocio
        vgv_parceiro = receita_liquida * parceiro_per
        receita_urbanizador = receita_liquida - vgv_parceiro
        if investimento == 'Sim':
            ebtda_valor = receita_urbanizador - custo_investimento + custos_projetos + custos_mkt + custos_overhead + custos_obras + custos_posobras + custos_admobras
        else:
            ebtda_valor = receita_urbanizador + custos_projetos + custos_mkt + custos_overhead + custos_obras + custos_posobras + custos_admobras
        
        if ebtda_valor != 0.0:
            ebtda_per = ebtda_valor / receita_urbanizador
        else:
            ebtda_per = 0

        indicador_tir_aa = 0
        indicador_tir_am = 0
        indicador_payback = 0
        
        if (custos_projetos + custos_obras) != 0.0:
            indicador_multiplicador = (vgv_bruto * urbanizador_per) / -(custos_obras) 
        else:
            indicador_multiplicador = 0

        indicador_exposicao_maxima = 0
        indicador_vpl_urbanizador = 0
        indicador_vpl_parceiro = 0
        
        self.entry_dre_vgv_bruto.delete(0, "end")
        self.entry_dre_comissao.delete(0, "end")
        self.entry_dre_vgv_liquido.delete(0, "end")
        self.entry_dre_impostos.delete(0, "end")
        self.entry_dre_comissao_negocio.delete(0, "end")
        self.entry_dre_receita_liquida.delete(0, "end")
        self.entry_dre_vgv_parceiro.delete(0, "end")
        self.entry_dre_receita_liquida_urbanizadora.delete(0, "end")
        self.entry_dre_ebtda_valor.delete(0, "end")
        self.entry_dre_ebtda_per.delete(0, "end")
        self.entry_indicadores_tir_aa.delete(0, "end")
        self.entry_indicadores_tir_am.delete(0, "end")
        self.entry_indicadores_payback.delete(0, "end")
        self.entry_indicadores_multiplicador_investimento.delete(0, "end")
        self.entry_indicadores_exposicaomax_caixa.delete(0, "end")
        self.entry_indicadores_vpl_urbanizadora.delete(0, "end")
        self.entry_indicadores_vpl_parceiro.delete(0, "end")

        self.entry_dre_vgv_bruto.insert(0, self.format_valor_fx(vgv_bruto))
        self.entry_dre_comissao.insert(0, self.format_valor_fx(comissao_venda))
        self.entry_dre_vgv_liquido.insert(0, self.format_valor_fx(vgv_liquido))
        self.entry_dre_impostos.insert(0, self.format_valor_fx(impostos))
        self.entry_dre_comissao_negocio.insert(0, self.format_valor_fx(comissao_negocio))
        self.entry_dre_receita_liquida.insert(0, self.format_valor_fx(receita_liquida))
        self.entry_dre_vgv_parceiro.insert(0, self.format_valor_fx(vgv_parceiro))
        self.entry_dre_receita_liquida_urbanizadora.insert(0, self.format_valor_fx(receita_urbanizador))
        self.entry_dre_ebtda_valor.insert(0, self.format_valor_fx(ebtda_valor))
        self.entry_dre_ebtda_per.insert(0, self.format_per_fx(ebtda_per))
        self.entry_indicadores_tir_aa.insert(0, self.format_per_fx(indicador_tir_aa))
        self.entry_indicadores_tir_am.insert(0, self.format_per_fx(indicador_tir_am))
        self.entry_indicadores_payback.insert(0, self.format_ano_fx(indicador_payback))
        self.entry_indicadores_multiplicador_investimento.insert(0, self.format_valor_fx(indicador_multiplicador))
        self.entry_indicadores_exposicaomax_caixa.insert(0, self.format_valor_fx(indicador_exposicao_maxima))
        self.entry_indicadores_vpl_urbanizadora.insert(0, self.format_valor_fx(indicador_vpl_urbanizador))
        self.entry_indicadores_vpl_parceiro.insert(0, self.format_valor_fx(indicador_vpl_parceiro))

    def format_pmt(self, event):
        if self.entry_vendas_lote_medio.get() != '':
            vlr_unidade = float(self.entry_vendas_lote_medio.get().replace('.', '').replace(',', '.')[:15])
            i_am = float(self.entry_vendas_juros_am.get().replace("%", "").replace(",", ".")[:7]) / 100
            prazo = float(self.entry_vendas_financiamento_prazo.get().replace("x", "").replace(",", ".")[:7])
            per_entrada = float(self.entry_vendas_entrada.get().replace("%", "").replace(",", ".")[:7]) / 100
            per_reforcos = float(self.entry_vendas_reforcos.get().replace("%", "").replace(",", ".")[:7]) / 100
            vlr_entrada = vlr_unidade * per_entrada
            vlr_reforcos = vlr_unidade * per_reforcos
            vlr_financiado = vlr_unidade - vlr_entrada - vlr_reforcos
           
            if prazo != 0.0:
                pmt_PRICE = npf.pmt(i_am, prazo, (vlr_financiado * -1), fv=0, when='end'  )
                pmt_sacoc = vlr_financiado / prazo
            else:
                pmt_PRICE = 0
                pmt_sacoc = 0
           
            pmt_PRICE = self.format_valor_fx(pmt_PRICE)
            self.entry_vendas_parcela_price.delete(0, "end")
            self.entry_vendas_parcela_price.insert(0, pmt_PRICE)
            
            pmt_sacoc = self.format_valor_fx(pmt_sacoc)
            self.entry_vendas_parcela_sacoc.delete(0, "end")
            self.entry_vendas_parcela_sacoc.insert(0, pmt_sacoc)

    def format_preco_comissao(self, event):
        if self.entry_vendas_preco_m2.get() != '':
            preco = float(self.entry_vendas_preco_m2.get().replace('.', '').replace(',', '.')[:15])
            comissao = float(self.entry_vendas_comissao_per.get().replace("%", "").replace(",", ".")[:7]) / 100
            area_unidade = float(self.entry_area_lote_medio.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
            preco_com_comissao = preco * (1 + comissao)
            tickt_medio = area_unidade *  preco_com_comissao

            preco_com_comissao = self.format_valor_fx(preco_com_comissao)
            self.entry_vendas_vendas_preco_m2_com_comissao.delete(0, "end")
            self.entry_vendas_vendas_preco_m2_com_comissao.insert(0, preco_com_comissao)
            
            tickt_medio = self.format_valor_fx(tickt_medio)
            self.entry_vendas_lote_medio.delete(0, "end")
            self.entry_vendas_lote_medio.insert(0, tickt_medio)
            
    def format_area_aproveitada(self, event):
        text = float(self.entry_area_aproveitamento.get().replace("%", "").replace(",", ".")[:7]) / 100
        parti = text

        if event.keysym.lower() == "backspace":
            return
        
        if float(parti) > 1:
            messagebox.showinfo('% Área Aproveitada', 'Percentual Não pode ser Maio que 100%!!!!')
            parti = 0
            new_text = ''
            self.entry_area_aproveitamento.focus()
            if isinstance(self.entry_area_aproveitamento, ctk.CTkEntry):
                self.entry_area_aproveitamento.select_range(0, 'end')  # Seleciona todo o texto 
            
        else:
            new_text = self.format_per_fx(text)
            if self.entry_area_total.get() != '':
                area_total = float(self.entry_area_total.get().replace(" m²", "").replace(".", "").replace(",", "."))
                area_aproveitada = area_total * text
            else:
                area_aproveitada = 0
            
            area_aproveitada = self.format_m2_fx(area_aproveitada)
            self.entry_area_aproveitado.delete(0, "end")
            self.entry_area_aproveitado.insert(0, area_aproveitada)

            self.entry_area_lote_padrao.focus()
            if isinstance(self.entry_area_lote_padrao, ctk.CTkEntry):
                self.entry_area_lote_padrao.select_range(0, 'end')  # Seleciona todo o texto 
        
        self.entry_area_aproveitamento.delete(0, "end")
        self.entry_area_aproveitamento.insert(0, new_text.strip())
        
    def format_cpf(self, event, target):
        text = target.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]

        target.delete(0, "end")
        target.insert(0, new_text)

    def format_cnpj(self, event, target):
    
        text = target.get().replace(".", "").replace("-", "")[:14]
        new_text = ""

        if event.keysym.lower() == "backspace": return
        
        for index in range(len(text)):
            
            if not text[index] in "0123456789": continue
            if index in [1, 4]: new_text += text[index] + "."
            elif index == 7: new_text += text[index] + "/"
            elif index == 11: new_text += text[index] + "-"
            else: new_text += text[index]

        target.delete(0, "end")
        target.insert(0, new_text)
    
    def format_medida_lote(self, event):
        TArea_Medida_Lote = self.entry_area_lote_padrao.get().strip()  # Get and strip whitespace
        TArea_Aproveitada = self.entry_area_aproveitado.get().strip()  # Get and strip whitespace
        if TArea_Medida_Lote:
            nrcarat = len(TArea_Medida_Lote)
            Caracter = ''
            Frente = ''
            Fundo = ''
            TArea_LoteMedio = 0.00

            for i in range(nrcarat):  # Iterate over the indices of the string
                char = TArea_Medida_Lote[i]  # Current character
                if char.lower() == "x":  # Check if character is "x" or "X"
                    Caracter = char
                else:
                    if Caracter.lower() == "x":
                        Fundo += char  # Concatenate fundo
                    else:
                        Frente += char  # Concatenate frente

            # Converting to float and formatting
            try:
                # Handle possible empty strings after replacing
                Frente_value = float(Frente.replace(",", ".")) if Frente.strip() else 0.0
                Fundo_value = float(Fundo.replace(",", ".")) if Fundo.strip() else 0.0
                
                TArea_LoteMedio = Frente_value * Fundo_value
                TArea_LoteMedio_formatted = "{:.2f}".format(TArea_LoteMedio)
            except ValueError:  
                TArea_LoteMedio_formatted = '0.0'
            
            if TArea_LoteMedio != 0.0:
                try:
                    nr_unidades = "{:.2f}".format(float(TArea_Aproveitada.replace(" m²", "").replace(".", "").replace(",", ".")) / TArea_LoteMedio)
                    
                except ZeroDivisionError:
                    nr_unidades = "N/A - Erro Divisão por Zero!!!"  # Handle the case of division by zero
                except ValueError:
                    nr_unidades = "N/A - Erro separador diferente de 'x' !!!"  # Handle conversion errors
            else:
                nr_unidades = "N/A - Erro separador diferente de 'x' !!!"

            # Update entry fields with formatted results
            self.entry_area_lote_medio.delete(0, "end")
            self.entry_area_lote_medio.insert(0, TArea_LoteMedio_formatted.replace(".", ",").strip())
            self.entry_area_nr_lotes.delete(0, "end")
            self.entry_area_nr_lotes.insert(0, nr_unidades.replace(".", ",").strip())
    
    def format_per_terreneiro(self, event):
        participacao_urbanizador = float(self.entry_participacao_urbanizador.get().replace("%", "").replace(",", ".")[:7]) / 100
        parti = participacao_urbanizador
        new_text = ''

        if event.keysym.lower() == "backspace":
            return
        
        if float(parti) > 1:
            messagebox.showinfo('% Urbanizador', 'Percentual Não pode ser Maior que 100%!!!!')
            parti = 0
            new_text = ''
            self.entry_participacao_urbanizador.focus()
            if isinstance(self.entry_participacao_urbanizador, ctk.CTkEntry):
                self.entry_participacao_urbanizador.select_range(0, 'end')  # Seleciona todo o texto
        else:
            self.entry_participacao_permuta.focus()
            if isinstance(self.entry_participacao_permuta, ctk.CTkEntry):
                self.entry_participacao_permuta.select_range(0, 'end')  # Seleciona todo o texto

            new_text = self.format_per_fx(participacao_urbanizador)
            participacao_terreneiro = self.format_per_fx(1 - participacao_urbanizador)

            self.entry_participacao_parceiro.delete(0, "end")
            self.entry_participacao_parceiro.insert(0, participacao_terreneiro.strip())

        self.entry_participacao_urbanizador.delete(0, "end")
        self.entry_participacao_urbanizador.insert(0, new_text.strip())
    
    def format_per_dif_aprazo(self, event):
        per_avista = float(self.entry_per_avista.get().replace("%", "").replace(",", ".")[:7]) / 100
        parti = per_avista
        new_text = ''

        if event.keysym.lower() == "backspace":
            return
        
        if float(parti) > 1 or float(parti) < 0 or float(parti) == 0:
            messagebox.showinfo('% A vista', 'Percentual Inválido, não pode ser 0 ou maior que 100%!!!!', parent=self.janela_premissas)
            parti = 0
            new_text = ''
            self.entry_per_avista.focus()
            if isinstance(self.entry_per_avista, ctk.CTkEntry):
                self.entry_per_avista.select_range(0, 'end')  # Seleciona todo o texto
            return
        else:
            self.entry_per_aprazo.focus()
            if isinstance(self.entry_per_aprazo, ctk.CTkEntry):
                self.entry_per_aprazo.select_range(0, 'end')  # Seleciona todo o texto

            new_text = self.format_per_fx(per_avista)
            per_aprazo = self.format_per_fx(1 - per_avista)

            self.entry_per_aprazo.delete(0, "end")
            self.entry_per_aprazo.insert(0, per_aprazo.strip())

        self.entry_per_avista.delete(0, "end")
        self.entry_per_avista.insert(0, new_text.strip())

    def format_per_total_participacao(self, event):
        admmkt_parceiro = float(self.entry_admmkt_parceiro.get().replace("%", "").replace(",", ".")[:7]) / 100
        per_permuta_fisica = float(self.entry_participacao_permuta.get().replace("%", "").replace(",", ".")[:7]) / 100
        parti = admmkt_parceiro
        new_text = ""

        if event.keysym.lower() == "backspace":
            return

        if float(parti) > 1:
            messagebox.showinfo('% Urbanizador', 'Percentual Não pode ser Maio que 100%!!!!')
            parti = 0
            new_text = ''
            self.entry_admmkt_parceiro.focus()
            if isinstance(self.entry_admmkt_parceiro, ctk.CTkEntry):
                self.entry_admmkt_parceiro.select_range(0, 'end')  # Seleciona todo o texto
        else:
            self.entry_investimento_valor.focus()
            if isinstance(self.entry_investimento_valor, ctk.CTkEntry):
                self.entry_investimento_valor.select_range(0, 'end')  # Seleciona todo o texto

        new_text = self.format_per_fx(admmkt_parceiro)
        self.entry_admmkt_parceiro.delete(0, "end")
        self.entry_admmkt_parceiro.insert(0, new_text.strip())
        
        participacao_urbanizador = float(self.entry_participacao_urbanizador.get().replace("%", "").replace(",", ".")) / 100 if self.entry_participacao_urbanizador.get().replace("%", "").replace(",", ".").strip() else 0.0 
        participacao_parceiro = float(self.entry_participacao_parceiro.get().replace("%", "").replace(",", ".")) / 100 if self.entry_participacao_parceiro.get().replace("%", "").replace(",", ".").strip() else 0.0 
        participacao_permuta = float(self.entry_participacao_permuta.get().replace("%", "").replace(",", ".")) / 100 if self.entry_participacao_permuta.get().replace("%", "").replace(",", ".").strip() else 0.0 
        
        participacao_total_urbanizador = (participacao_urbanizador * (1 - per_permuta_fisica)) + (participacao_parceiro * admmkt_parceiro)
        participacao_total_parceiro = (participacao_parceiro * (1 - admmkt_parceiro)) + (participacao_urbanizador * per_permuta_fisica)
        
        participacao_total_urbanizador = self.format_per_fx(participacao_total_urbanizador)
        participacao_total_parceiro = self.format_per_fx(participacao_total_parceiro)

        self.entry_total_urbanizadora.delete(0, "end")
        self.entry_total_urbanizadora.insert(0, participacao_total_urbanizador.strip())
        self.entry_total_parceiro.delete(0, "end")
        self.entry_total_parceiro.insert(0, participacao_total_parceiro.strip())
    
    def checar_cpf_cnpj(self, event, campo_entry, tipo_entry, target):
        entrada = campo_entry.get().replace(".", "").replace("-", "").replace("/", "").strip()  # Remove formatações
        tipo = tipo_entry.get()
        
        if tipo == "J" :
            if len(entrada) == 14 and entrada.isdigit():
                target.focus()
                target.select_range(0, 'end')
                target.icursor('end')
            else:
                messagebox.showinfo('Gestor Negócios', 'CNPJ Inválido, tente novamente!!!')
                return 
        elif tipo == "F" :
            if len(entrada) == 11 and entrada.isdigit():
                target.focus()
                target.select_range(0, 'end')
                target.icursor('end')
            else:
                messagebox.showinfo('Gestor Negócios', 'CPF Inválido, tente novamente!!!')
                return

    def format_cpf_cnpj(self, event, campo_entry, tipo_entry):
        campo = campo_entry.get()
        tipo = tipo_entry.get()
        
        nr_campos = len(campo)
        if tipo == "J" :
            if nr_campos in [2, 6]:
                campo += "."
            elif nr_campos == 10:
                campo += "/"
            elif nr_campos == 15:
                campo += "-"
            
        elif tipo == "F" :
            if nr_campos in [3, 7]:
                campo += "."
            elif nr_campos == 11:
                campo += "-"
            

        campo_entry.delete(0, "end")
        campo_entry.insert(0, campo.strip())  
    
    def checar_cep(self, event, campo_entry, target):
         # Remove quaisquer caracteres que não sejam dígitos
        cep = campo_entry.get()
        cep = ''.join(filter(str.isdigit, cep))
        # Verifica se o CEP tem exatamente 8 dígitos
        if len(cep) == 8 and cep.isdigit():
            target.focus()
            target.select_range(0, 'end')
            target.icursor('end')
        else:
            messagebox.showinfo('Gestor Negócios', 'CEP Inválido, tente novamente!!!')
            return
    
    def formatar_cep(self, 
                     event, 
                     entry_cep, 
                     entry_endereco, 
                     entry_endereco_bairro, 
                     entry_uf, 
                     entry_municipio
                     ):
        cep = entry_cep.get()
        # Remove quaisquer caracteres que não sejam dígitos
        cep = ''.join(filter(str.isdigit, cep))
        
        if len(cep) == 8:  # CEP deve ter 8 dígitos
            cep_format =  f"{cep[:5]}-{cep[5:]}"  # Formato: XXXXX-XXX
        else:
            messagebox.showinfo('Gestor Negócios', 'CEP Inválido, tente novamente.')
            return
        
        entry_cep.delete(0, "end")
        entry_cep.insert(0, cep_format.strip()) 
        
        cep = cep_format
        
        if not cep:
            customtkinter.CTkMessageBox.showinfo("Erro", "Informar um CEP válido!")
            entry_cep.focus()
        else:
            logradouro = self.consulta_cep(cep, "logradouro").upper()
            bairro = self.consulta_cep(cep, "bairro").upper()
            municipio_ds = self.consulta_cep(cep, "localidade").upper()
            uf = self.consulta_cep(cep, "uf").upper()
            
            entry_endereco.delete(0, "end")
            entry_endereco_bairro.delete(0, "end")
            entry_municipio.delete(0, "end")
            entry_uf.delete(0, "end")

            entry_endereco.insert(0, logradouro.capitalize())
            entry_endereco_bairro.insert(0, bairro.capitalize())
            entry_municipio.insert(0, municipio_ds.capitalize())
            entry_uf.insert(0, uf)

        entry_endereco.focus()
        entry_endereco.select_range(0, 'end')
        entry_endereco.icursor('end')       

    def check_email(self, event, entry_email):
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.search(self.regex, entry_email.get())):
            pass
            # messagebox.showinfo('Gestor Negócios', 'CNPJ Inválido, tente novamente!!!')
            # self.valida_email_cadastro = 'valido'
        else:
            messagebox.showinfo('Gestor Negócios', 'Email Inválido, tente novamente!!!')
            
    def verificar_cnpj(self, cnpj: str) -> bool:
        # Completa com zeros à esquerda caso não esteja com 14 dígitos
        cnpj = cnpj.zfill(14)
        
        if cnpj == "00000000000000":
            return False

        # Pega cada dígito do CNPJ informado
        d1 = int(cnpj[0])
        d2 = int(cnpj[1])
        d3 = int(cnpj[2])
        d4 = int(cnpj[3])
        d5 = int(cnpj[4])
        d6 = int(cnpj[5])
        d7 = int(cnpj[6])
        d8 = int(cnpj[7])
        d9 = int(cnpj[8])
        d10 = int(cnpj[9])
        d11 = int(cnpj[10])
        d12 = int(cnpj[11])
        d13 = int(cnpj[12])  # DV1 informado
        d14 = int(cnpj[13])  # DV2 informado

        # Cálculo do primeiro dígito verificador
        dv1 = (d1 * 6 + d2 * 7 + d3 * 8 + d4 * 9 + d5 * 2 + d6 * 3 +
            d7 * 4 + d8 * 5 + d9 * 6 + d10 * 7 + d11 * 8 + d12 * 9) % 11
        if dv1 == 10:
            dv1 = 0

        # Cálculo do segundo dígito verificador
        dv2 = (d1 * 5 + d2 * 6 + d3 * 7 + d4 * 8 + d5 * 9 + d6 * 2 +
            d7 * 3 + d8 * 4 + d9 * 5 + d10 * 6 + d11 * 7 +
            d12 * 8 + dv1 * 9) % 11
        if dv2 == 10:
            dv2 = 0

        # Comparação dos DVs informados
        return d13 == dv1 and d14 == dv2

    def validar_cpf(self, cpf: str) -> bool:
        # Completa com zeros à esquerda caso não esteja com 11 dígitos
        cpf = cpf.zfill(11)
        
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Cálculo do primeiro dígito verificador
        dv1 = 0
        dv2 = 0
        multiplicador = 2

        for i in range(9, 0, -1):  # De 9 até 1
            dv1 += int(cpf[i - 1]) * multiplicador
            dv2 += int(cpf[i - 1]) * (multiplicador + 1)
            multiplicador += 1

        dv1 = dv1 % 11
        if dv1 >= 2:
            dv1 = 11 - dv1
        else:
            dv1 = 0

        dv2 += dv1 * 2
        dv2 = dv2 % 11
        if dv2 >= 2:
            dv2 = 11 - dv2
        else:
            dv2 = 0

        # Validação final do CPF
        if cpf[-2:] == f"{dv1}{dv2}":
            return True
        else:
            return False
class Formularios():

    def OnDoubleClick(self, event):
        selected_item = self.list_g.selection()
        if selected_item:
            # Texto do item selecionado
            item_text = self.list_g.item(self.list_g.selection(), 'text')
            # Obtém os valores associados (como uma tupla)
            values = self.list_g.item(self.list_g.selection(), 'values')

            Tipo = values[3]
            Nome_da_Area = values[4]
            Cidade = values[5]
            UF = values[6]

            self.lista = self.Consulta_Negocio(UF, Cidade, Tipo, Nome_da_Area)
            if self.lista != []:
                self.simulador_estudos_rel()
            else:
                messagebox.showinfo("Informação", "Nenhum negócio encontrado.")
        else:
            messagebox.showwarning(
                "Seleção inválida", "Por favor, selecione um item.")

    def OnDoubleClick_modulo(self, event):
        janela = self.principal_frame
        coordenadas_relx = 0.5
        coordenadas_rely = 0.5
        coordenadas_relwidth = 0.20
        coordenadas_relheight = 0.07
        self.modulo = self.button_modulo(janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight)

    def OnDoubleClick_site(self, event):
        selected_item =  self.LSites.selection()
        if selected_item:
            # Get the text of the selected item
            item_text =  self.LSites.item(selected_item, 'text')
            # Get associated values as a tuple
            values =  self.LSites.item(selected_item, 'values')
            
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get(), self.window_one)
            Site = values[2]
        # Abre a URL no navegador padrão
        webbrowser.open(Site)

    def muda_barrinha(self, event, target):
        target.focus()
        # print(f"O tipo do widget é: {type(target)}")
        if isinstance(target, ctk.CTkEntry):
            target.focus()
            target.select_range(0, 'end')
            target.icursor('end')
            # target.set('')  # Use set() para limpar o valor do CTkEntry
        elif isinstance(target, ctk.CTkComboBox):
            target.focus()
            target.event_generate('<Down>')  # This simulates pressing the down arrow to open the dropdown
        elif isinstance(target, ctk.CTkTextbox):
            target.tag_add("sel", "1.0", "end")  # Select all text
            target.focus()  # Ensure the textbox is focused
    
    def muda_barrinha_dta(self, event, entry_dta, target):
        if self.checar_data(entry_dta.get(), formato='%d/%m/%Y') == False:
            entry_dta.focus()
        else:
            target.focus()
            # print(f"O tipo do widget é: {type(target)}")
            if isinstance(target, ctk.CTkEntry):
                target.focus()
                target.select_range(0, 'end')
                target.icursor('end')
                # target.set('')  # Use set() para limpar o valor do CTkEntry
            elif isinstance(target, ctk.CTkComboBox):
                target.focus()
                target.event_generate('<Down>')  # This simulates pressing the down arrow to open the dropdown
            elif isinstance(target, ctk.CTkTextbox):
                target.tag_add("sel", "1.0", "end")  # Select all text
                target.focus()  # Ensure the textbox is focused

    def obter_Empresa_ID(self, Empresa_DS, janela):
        if Empresa_DS !='':
            id_empresa = self.empresas_dict.get(Empresa_DS)  # Obtenha o ID correspondente
            if id_empresa:
                return id_empresa
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Empresa Incorreta, selecione novamente!!!', parent = janela)
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Empresa em Branco!!!', parent = janela)
            return

    def obter_tpo_programa_ID(self, Tpo_Programa_DS, janela):
        if Tpo_Programa_DS !='':
            id_tpo_programa = self.tpo_programa_dict.get(Tpo_Programa_DS)  # Obtenha o ID correspondente
            if id_tpo_programa:
                return id_tpo_programa
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Programa Incorreto, selecione novamente!!!', parent = janela)
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Programa em Branco!!!', parent = janela)
            return
    
    def obter_Situacao_Projeto_ID(self, Situacao_Projeto_DS, janela):
        if Situacao_Projeto_DS !='':
            id_situacao_projeto = self.projetos_situacao_dict.get(Situacao_Projeto_DS)  # Obtenha o ID correspondente
            if id_situacao_projeto:
                return id_situacao_projeto
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Situação do Projeto Incorreto, selecione novamente!!!', parent = janela)
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Situação Projeto em Branco!!!', parent = janela)
            return
    
    def obter_Tpo_Projeto(self, Tipo_Projeto_DS, janela):
        if Tipo_Projeto_DS !='':
            id_tpo_projeto = self.tpo_projeto_dict.get(Tipo_Projeto_DS)  # Obtenha o ID correspondente
            if id_tpo_projeto:
                return id_tpo_projeto
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Tipo do Empreendimento Incorreto, selecione novamente!!!', parent = janela)
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo do Empreendimento em Branco!!!', parent = janela)
            return
        
    def obter_Projeto_ID(self, Projeto_DS, janela):
        if Projeto_DS !='':
            id_projeto = self.projetos_dict.get(Projeto_DS)  # Obtenha o ID correspondente
            if id_projeto:
                return id_projeto
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Projeto Incorreto, selecione novamente!!!', parent = janela)
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Projeto em Branco!!!', parent = janela)
            return
        
    def obter_Unidade_ID(self, Unidade_DS, janela):
        id_unidade = self.unidade_negocios_dict.get(Unidade_DS)  # Obtenha o ID correspondente
        if id_unidade:
            return id_unidade
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Unidade de Negócio em Branco ou Incorreta!!!', parent = janela)
        return None
    
    def obter_FormaLiquidacao_ID(self, FormaLiquidacao_DS, janela):
        id_formaliquidacao = self.tpo_pagto_dict.get(FormaLiquidacao_DS)  # Obtenha o ID correspondente
        if id_formaliquidacao:
            return id_formaliquidacao
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Meio de Pagamento em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Frete_DS(self, Frete_ID, janela):
        ds_frete = self.frete_dict_1.get(Frete_ID)  # Obtenha o ID correspondente
        if ds_frete:
            return ds_frete
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Frete em Branco ou Incorreto!!!', parent = janela)
        return None

    def obter_Frete_ID(self, Frete_DS, janela):
        id_frete = self.frete_dict.get(str(Frete_DS))  # Obtenha o ID correspondente
        if id_frete:
            return id_frete
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Frete em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Centro_ID(self, Centro_DS, janela):
        id_centro = self.centro_dict.get(Centro_DS)  # Obtenha o ID correspondente
        if id_centro:
            return id_centro
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Centro de Resultado em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Spead_ID(self, Spead_DS, janela):
        id_spead = self.produto_dict.get(Spead_DS)  # Obtenha o ID correspondente
        if id_spead:
            return id_spead
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Spead em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_UnidadeMedida_ID(self, UnidadeMedida_DS, janela):
        id_unidademedida = self.unidade_medida_dict.get(UnidadeMedida_DS)  # Obtenha o ID correspondente
        if id_unidademedida:
            return id_unidademedida
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Unidade Medida em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Produto_ID(self, Produto_DS, janela):
        id_produto = self.produto_dict.get(Produto_DS)  # Obtenha o ID correspondente
        if id_produto:
            return id_produto
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Produto em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Natureza_ID(self, Natureza_DS, janela):
        id_natureza = self.natureza_dict.get(Natureza_DS)  # Obtenha o ID correspondente
        if id_natureza:
            return id_natureza
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Natureza Financeira em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Pessoa_ID(self, Pessoa_DS, janela):
        id_pessoa = self.nome_pessoa_dict.get(Pessoa_DS)  # Obtenha o ID correspondente
        if id_pessoa:
            return id_pessoa
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Cliente/Fornecedor em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_municipio_IBGE(self, Municipio_DS, janela):
        id_municipio = self.municipios_dict.get(Municipio_DS)  # Obtenha o ID correspondente
        if id_municipio:
            return id_municipio
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Município em Branco ou Incorreto!!!', parent = janela)
        return None

    def obter_banco(self, Banco_DS, janela):
        if Banco_DS:
            id_banco = self.bancos_dict.get(Banco_DS)  # Obtenha o ID correspondente
        else:
             messagebox.showinfo('Gestor Negócios', 'Erro - Banco em Branco ou Incorreto!!!', parent = janela)
             return
        
        if id_banco:
            return id_banco
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Banco em Branco ou Incorreto!!!', parent = janela)
        return None

    def obter_Orc_ID(self, Orc_DS, janela):
        id_orc = self.orcamentos_dict.get(Orc_DS)  # Obtenha o ID correspondente
        if id_orc:
            return id_orc
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Orcamento em Branco ou Incorreto!!!', parent = janela)
        return None

    def obter_Orc_Item_ID(self, Orc_Item_DS, janela):
        id_item_preco = self.item_precos_orcamentos_dict.get(Orc_Item_DS)  # Obtenha o ID correspondente
        if id_item_preco:
            return id_item_preco
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Item em Branco ou Incorreto!!!', parent = janela)
            return
        return None

    def obter_Periodicidade_ID(self, Periodicidade_DS, janela):
        id_periodicidade = self.periodicidades_dict.get(Periodicidade_DS)  # Obtenha o ID correspondente
        if id_periodicidade:
            return id_periodicidade
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Periodicidade em Branco ou Incorreto!!!', parent = janela)
        return None
    
    def obter_Indice_ID(self, Idx_DS, janela):
        id_idx = self.idx_dict.get(Idx_DS)  # Obtenha o ID correspondente
        if id_idx:
            return id_idx
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Índice em Branco ou Incorreto!!!', parent = janela)
        return None

    def obter_Nat_Gerencial_ID(self, DS_Nat_Gerencial, janela):
        id_natureza_gerencial = self.natureza_gerencial_dict.get(DS_Nat_Gerencial)  # Obtenha o ID correspondente
        if id_natureza_gerencial:
            return id_natureza_gerencial
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Natureza Gerencial em Branco ou Incorreto!!!', parent = janela)
        return None 
class Atualizar_Combo():
    
    # Atualização dos Combo
    def atualizar_unidade_medida(self, event, target):
        self.unidade_medida = self.get_unidade_medida()
        self.unidade_medida_dict = {nome: id for id, nome in self.unidade_medida}
        self.unidade_medida = [unidade[1] for unidade in self.unidade_medida]
        target.set_completion_list(self.unidade_medida)

    def atualizar_spead(self, event, target):
        self.spead = self.get_tpspead()
        self.spead_dict = {nome: id for id, nome in self.spead}
        self.spead = [spead[1] for spead in self.spead]
        target.set_completion_list(self.spead)

    def atualizar_bancos(self, event, target):
        self.bancos = self.get_bancos()
        self.bancos_dict = {nome: id for id, nome in self.bancos}
        self.bancos = [banco[1] for banco in self.bancos]
        target.set_completion_list(self.bancos)

    def atualizar_agencias(self, event, Empresa_ID, Banco_ID, target):
        self.agencias = self.get_agencias(Empresa_ID, Banco_ID)
        target.set_completion_list(self.agencias)

    def atualizar_contascorrente(self, event, Empresa_ID, Banco_ID, target):
        self.contascorrente = self.get_contascorrente(Empresa_ID, Banco_ID)
        target.set_completion_list(self.contascorrente)

    def atualizar_empresas(self, event, target):
        self.empresas = self.get_empresas()
        self.empresas_dict = {nome: id for id, nome in self.empresas}
        self.empresas = [empresa[1] for empresa in self.empresas]
        target.set_completion_list(self.empresas)

    def atualizar_projetos_situacao(self, event, target):
        self.projetos_situacao = self.get_projetos_situacao()
        self.projetos_situacao_dict = {nome: id for id, nome in self.projetos_situacao}
        self.projetos_situacao = {nome: nome for id, nome in self.projetos_situacao}
        target.set_completion_list(self.projetos_situacao)

    def atualizar_tpo_programa(self, event, target):
        self.tpo_programa = self.get_tpo_programa()
        self.tpo_programa_dict = {nome: id for id, nome in self.tpo_programa}
        self.tpo_programa = [tpo_programa[1] for tpo_programa in self.tpo_programa]
        target.set_completion_list(self.tpo_programa)

    def atualizar_tpo_projeto(self, event, target):
        self.tpo_projeto = self.get_tpo_projetos()
        self.tpo_projeto_dict = {nome: id for id, nome, imposto in self.tpo_projeto}
        self.impostos = {nome: imposto for id, nome, imposto in self.tpo_projeto}
        self.tpo_projeto = {nome: nome for id, nome, imposto in self.tpo_projeto}
        # self.tpo_projeto = [tpo_projetos[1] for tpo_projetos in self.centro_resultado]
        target.set_completion_list(self.tpo_projeto)
    
    def atualizar_tpo_pagto(self, event, target):
        self.tpo_pagto = self.get_tpo_pagto()
        self.tpo_pagto_dict = {nome: id for id, nome in self.tpo_pagto}
        self.tpo_pagto = [tpo_pagto[1] for tpo_pagto in self.tpo_pagto]
        target.set_completion_list(self.tpo_pagto)
    
    def atualizar_produto_fx(self, Empresa_ID):
        self.produtos = self.get_produtos(Empresa_ID)
        self.produto_dict = {nome: id for id, nome, tpo in self.produtos}
        self.produtos = [produto[1] for produto in self.produtos]

    def atualizar_produto(self, event, Empresa_ID, target):
        self.produtos = self.get_produtos(Empresa_ID)
        self.produto_dict = {nome: id for id, nome, tpo in self.produtos}
        self.produtos = [produto[1] for produto in self.produtos]
        target.set_completion_list(self.produtos)
    
    def atualizar_natureza_financeira(self, event, Empresa_ID, target):
        self.natureza_financeira = self.get_natureza_financeira(Empresa_ID)
        self.natureza_dict = {nome: id for id, nome, tpo in self.natureza_financeira}
        self.natureza_financeira = [natureza[1] for natureza in self.natureza_financeira]
        target.set_completion_list(self.natureza_financeira)
    
    def atualizar_natureza_gerencial(self, event, target):
        self.natureza_gerencial = self.get_natureza_gerencial()
        self.natureza_gerencial_dict = {nome: id for id, nome in self.natureza_gerencial}
        if self.natureza_gerencial and isinstance(self.natureza_gerencial[0], tuple):
           self.natureza_gerencial = [item[1] for item in self.natureza_gerencial]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.natureza_gerencial, key=str.lower))  # Ordena e configura
    
    def atualizar_centro_resultado(self, event, Empresa_ID, target):
        self.centro_resultado = self.get_centrosresultados(Empresa_ID)
        self.centro_dict = {nome: id for id, nome in self.centro_resultado}
        self.centro_resultado = [centro[1] for centro in self.centro_resultado]
        target.set_completion_list(self.centro_resultado)
    
    def atualizar_municipio(self, event, entry_uf, target):
        self.municipios = self.get_municipios(entry_uf)
        self.municipios_dict = {nome: id for id, nome in self.municipios}
        self.municipios = [municipio[1] for municipio in self.municipios]
        target.set_completion_list(self.municipios)
    
    def atualizar_municipio_fx(self, entry_uf):
        self.municipios = self.get_municipios(entry_uf)
        self.municipios_dict = {nome: id for id, nome in self.municipios}
        self.municipios = [municipio[1] for municipio in self.municipios]
        
    def atualizar_unidade_negocios(self, event, entry_empresa, target):
        self.unidade_negocios = self.get_unegocios(entry_empresa)
        self.unidade_negocios_dict = {nome: id for id, nome in self.unidade_negocios}
        self.unidade_negocios = [unidade[1] for unidade in self.unidade_negocios]
        target.set_completion_list(self.unidade_negocios)
    
    def atualizar_pessoa(self, event, entry_empresa, target):
        self.nome_pessoa = self.get_pessoas(entry_empresa)
        self.nome_pessoa_dict = {nome: id for id, nome in self.nome_pessoa}
        self.nome_pessoa = [pessoa[1] for pessoa in self.nome_pessoa]
        target.set_completion_list(self.nome_pessoa)
                
    def atualizar_nome_cenario(self, event, entry_empresa, entry_municipio, entry_uf, entry_tpo_projeto, target):
        ID_Empresa = entry_empresa
        self.nome_cenario = self.get_nome_cenario(ID_Empresa, entry_municipio, entry_uf, entry_tpo_projeto)
        completion_list = [area['Nome_da_Area'] for area in self.nome_cenario]
        target.set_completion_list(completion_list)
    
    def atualizar_curvas(self, event, Empresa_ID, target):
        self.nome_curva = self.get_nome_curvas(Empresa_ID)
        completion_list = [curva['Nome_Curva'] for curva in self.nome_curva]
        target.set_completion_list(completion_list)
    
    def atualizar_etapas_curvas(self, event, target):
        completion_list = self.get_etapas_curvas()
        target.set_completion_list(completion_list)
    
    def atualizar_sistema_amortizacao(self, event, target):
        completion_list = self.get_sistema_amortizacao() 
        target.set_completion_list(completion_list)
    
    def atualizar_periodicidade(self, event, target):
        self.periodicidades = self.get_periodicidade()
        self.periodicidades_dict = {nome: id for id, nome in self.periodicidades}
        if self.periodicidades and isinstance(self.periodicidades[0], tuple):
            self.periodicidades = [item[1] for item in self.periodicidades]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.periodicidades, key=str.lower))  # Ordena e configura
    
    def atualizar_idx(self, event, target):
        self.idx = self.get_idx()
        self.idx_dict = {nome: id for id, nome in self.idx}
        if self.idx and isinstance(self.idx[0], tuple):
            self.idx = [item[1] for item in self.idx]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.idx, key=str.lower))  # Ordena e configura

    def atualizar_frete(self, event, target):
        self.frete = self.get_frete() 
        self.frete_dict = {nome: id for id, nome in self.frete}
        self.frete = [frete[1] for frete in self.frete]
        target.set_completion_list(self.frete)

    def atualizar_status(self, event, Empresa_ID, target):
        self.status = self.get_status(Empresa_ID)
        target.set_completion_list(self.status)
    
    def atualizar_orcamentos(self, event, Empresa_ID, target):
        self.orcamentos = self.get_orcamentos(Empresa_ID)
        self.orcamentos_dict = {nome: id for id, nome in self.orcamentos}
        if self.orcamentos and isinstance(self.orcamentos[0], tuple):
            self.orcamentos = [item[1] for item in self.orcamentos]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.orcamentos, key=str.lower))  # Ordena e configura
    
    def atualizar_item_precos_orcamentos(self, event, entry_empresa, entry_orc, target):
        Empresa_ID = entry_empresa
        Orc_ID = entry_orc
        self.item_precos_orcamentos = self.get_precos_orc(Empresa_ID, Orc_ID)
        self.item_precos_orcamentos_dict = {nome: id for id, nome in self.item_precos_orcamentos}
        if self.item_precos_orcamentos and isinstance(self.item_precos_orcamentos[0], tuple):
            self.item_precos_orcamentos = [item[1] for item in self.item_precos_orcamentos]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.item_precos_orcamentos, key=str.lower))  # Ordena e configura
    
    def atualizar_projetos(self, event, target):
        self.projetos = self.get_projetos()
        self.projetos_dict = {nome: id for id, nome in self.projetos}
        if self.projetos and isinstance(self.projetos[0], tuple):
            self.projetos = [item[1] for item in self.projetos]  # Extrai o nome do projeto

        target.set_completion_list(sorted(self.projetos, key=str.lower))  # Ordena e configura    
class Icons():
    # Função para os farois
    def base64_to_farois(self, icon_tpo):
        # if icon_tpo == 'semafaro_azul':
        #     icon_base = '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'
        # elif icon_tpo == 'semafaro_vermelho':
        #     icon_base = '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'
        # elif icon_tpo == 'semafaro_verde':
        #     icon_base = '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 '
        # elif icon_tpo == 'semafaro_verde_conclusao':
        #     icon_base = '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'
        # elif icon_tpo == 'semafaro_amarelo':
        #     icon_base = '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'
        
        if icon_tpo == 'semafaro_azul':
            icon_base = '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'
        elif icon_tpo == 'semafaro_vermelho':
            icon_base = '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'
        elif icon_tpo == 'semafaro_verde':
            icon_base = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAgJSURBVEhLRZPJb53lGUd/zzt8w519HccBUxI7TuIECCEMUaChpaEqqCmoqkRVVVWlokqV+h90xV/TLrooErSCNJSWIQIaBZI4Axns2LFj+/r6Xt/hG9/h6YJFz+5szu4QZ8wCCGBgAedhNQBPQuikNAgCQDFAsNJxJAQxw1polZc5CaV05BmCAMB5MLEkJsD6kjg1CJUXXHJBJAS8AEsIy+yJCiDzhReIESgwwQp4eFYiBAQgnfdsKAy1c/DERAzyAABPbApI4RmWWJAEwM5qKRiuQJ7DZCgzFIlLLVsiUqCWbCooCRUhilFREOzA5IUQDM9gZhIkiDkHE0OCJADLnogBn/jBIO8vby8vb6+s9TcG+dCSK4ypVqsz04/urU3NTs3ONGZiH1RFVbJQJAAhIAgEKGZQzhk7H8kILIq8DCJtyPbMzp2N21eXvrm+ei2TGYUkKiquV3NbFN7medm935nQzRefOv3CsecPN+dihAoBPLQPtIhAxB6UsvHeVSggeO89SzwYrX357aWrK1eGGNsgFxUM092SjYz0w+5mqawOg1F3ZAb5VGXP4Ufnzxx/6fSB0y1MhIgirkivAMCDMmbPXjmnFVnkq4O1/977+urqdWppUeVhtrvd2/Jkjx4/Ftcr7//r/bX+WmISLVWz1lAss162MH3k5y//4tmZFx7Bo23skQ4wgADljonAXJIw3bLz2bXPrq7dUs0IMYUVXavExhfrmw9kLF1MH315oZM8ROhJCWaO41haIcfyYPPw71/7w9Hmk3PqoCoFl6AAInSg0grhc6S3t2/feHizOl2t1MOJoLaw99CpAycWmrMTvr6z2rl6+UoyGrErJZUmG7JNTDF0PA5qvpds/POT9za69y0KEEgBBAFAS7bINpK1m8uLokJK+JqOjj12ZK450yirUaKmw/ZMa7pdrTUqcb0SmnFSEyr2Iih9laVwBpxtdJav3voq5wG0ZXKwEPAZlGEUvf7Gw4379VDr0rdl5bHq3r1qT93WGlTfU5ucrDYmwqgVh8rbVlRti3olUY08jIZoOh15lySdxdtfbY1WHVKm0vtSlFRYmBLFVm8LcGyN8mjXWgErLr0giuNYayngA4lmENVkVJc1lcqTc8+cPfmjOteUoyiUYYW6o43bq9cLpCIgUiQQSAs/tOP1zsN6vT4Y9LWS7XbDSreddTvFzoDSkU9zlyv4wKOGGoZyfurwW6//6qdn3pisTxvjRKA5JhPaa0uLGTIHpu8WsuDc2900VfXKbj5KfTYww5Wd5aXO0rdbd1f6q71yN/HZuMiSUWKHvDDzxFvnfr0/nl9Z2TBMRskRm1RaqoXrva0c3oIteyUgGZJlMHJmUJQdl7nBRnrbRhRWo3rh7DAfpC7pJ93ueFBYMTt96PWXzx1sHf108eKFLy5s56O0QkxlRQdSymFSGpABE0gA0kMUUvRMcXdzbduMl3prl+5e7WR92Qgokt3BcKPb2+yOhmNfqex59Qfnjs6cuHT/+vkvPl3LesOAh4QyjAoZpVYWrAzAcFpJ4aBzoID0tbCbDUvNu1xupiPdnDgye/L4sZcq0dTmZtHveUkTPzzzxhPfe+6btVt/v/yfJdvdqZieNCaISE1kJiLZqrf3ekgBAFYQICEFxOTkVOLN0JdDsju++PzGN1+sLmbgM6/8eGH+qQj1115588TcqcXh2nuXLl7eut/RZU+7NA5KoXMjq8Fk0jcHZuY0JIGYnZDGV6EmEc1PPx7o0IUBWnXTilfM7l8/P//5vSsC8U9eOfv2L39z6tDzm2n/z/8+//H6rV5DjpvRIJBlFHldjXUj9KHK+KkDRzU0QTiGkAYRRAvx/ua+R1rT7Ch3Lpc8EmYt6Xx4+eOP73wmlToyvbBtdt/96B83dpbyJmURj1zqlGAdGAtTsB2Y+X0HZ6f2xwgI0jHkO396hySR8BRiYNP1nY1xMaaIvOTEpJbMvQd3Ejcu2v5vn3zw9dr1Ii5tUGYmASyFKoSqyeoEatWxfvP0a0/uPVJHTUEzgzhn642P3JCSy8mtv1x89/LWYhKXmSiheHdruyKjVtSoRtVBkvaSngkLDiCUCuPYekSotLkRbOP7+575489+tw+TdVQFtPdOQIO1tqQ89L7qvpOzTx9oP47EK2ZfZlN7a2HDdd368vB2t3gQt10Y5SElDTI1U0x4ahmKUj8dNF599sVHMBlBSRADEJLK3MlAlIQhxg52gPH5+5988PWHa9l6rscUukG+K2uhY+/yEuyCQAnPdVERpdSIeUgH2/Nvn/vtCXW0iqCCuoIyEB4gLiy0NMQlnAJylEv5/evbty5c++je7lKn6LgauwZlrhTWBkGU50VVxZVC0sDWuHHiwNNnT559YeLZJqIYkULAUCXIg8m7AiQtyHrWECx9hrTv+zc6N79cvnTxzler6XoZQYQs4JlJhXUzKCsZLUzNnTn+0qmF5/dhOoBso6kRECRDlIAHaMQ5AQQhoYlBDhqAsgnGfYzuJCtXVhZv3r252Vsn72UYWooP7194bv6JQ1OzbVGvoRojCqAVKwIxwQMe7AFKuPSwykstAgCwkCVAgHaZMn1kKVKPUsI5GMNgikJUaghjBCFkhJAAML7DEQAwmEDE3sB7WICEVwoEwWAGJEqggHewBCPZKiINTdASCgx4wAIACCCw/r9JZmIQpzmUAgjwnqRXpBhMKD0KZidYk4gByY6tI+vhAngA4rsiJKAAASdhAWIQoL0H6H9hd6BhJiR5nwAAAABJRU5ErkJggg=='
        elif icon_tpo == 'semafaro_verde_conclusao':
            icon_base = 'iVBORw0KGgoAAAANSUhEUgAAAuQAAALkCAIAAADIxrcyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAP+lSURBVHhe7P1ZkyPJlif4/c9RVTPA19i3zIjc95v3Zt5bdesuXTVV0y3TUyIUsoUzD3zhl+AnqC/CB1I4DyNCPpAyPWx2l7RUTW13qbvmvkYusWRGZGy+ADAz1XP4oGYGONwjMiMzFrjH+QkSGQ4H4IDBYHpM9ehRUlUYY4wxxiwqnr/BGGOMMWaRWLBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYoxxhhjFpoFK8YYY4xZaBasGGOMMWahWbBijDHGmIVmwYox94r0/9Idt5tHjXSX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'
        elif icon_tpo == 'semafaro_amarelo':
            icon_base = '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'
        

        # Corrigindo padding se necessário
        missing_padding = len(icon_base) % 4
        if missing_padding:
            icon_base += '=' * (4 - missing_padding)

        try:
            # Decodifica a imagem
            image_data = base64.b64decode(icon_base)
            image = Image.open(io.BytesIO(image_data))
            # original_image = Image.open(icon_path)
            resized_image =  image.resize((18, 18), Image.LANCZOS)  # Redimensionando para 32x32 pixels
            return ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print(f"Erro ao decodificar a imagem: {e}")
            return None  # Retorna None ou tratamento de erro apropriado
        
    # Função para converter uma imagem em Base64 para PhotoImage
    def base64_to_photoimage(self, icon_tpo):
        if icon_tpo == 'lupa':
            icon_base = "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"
        elif icon_tpo == 'save':
            icon_base = "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"
        elif icon_tpo == 'savedown':
            icon_base = "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"
        elif icon_tpo == 'trash':
            icon_base = "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"
        elif icon_tpo == 'anexar':
            icon_base = "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"
        elif icon_tpo == 'open_book':
            icon_base = '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'
        elif icon_tpo == 'three_points':
            icon_base = "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"
        elif icon_tpo == 'processo':
            icon_base = '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'
        elif icon_tpo == 'upload':
            icon_base = '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'
        elif icon_tpo == 'sair':
            icon_base = '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'
        elif icon_tpo == 'olho':
            icon_base = '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'
        elif icon_tpo == 'trespontos':
            icon_base = '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'
        elif icon_tpo == 'copia':
            icon_base = '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'
        elif icon_tpo == 'logo':
            icon_base = 'AAABAAgAICAQAAEABADoAgAAhgAAABAQEAABAAQAKAEAAG4DAAAgIAAAAQAIAKgIAACWBAAAEBAAAAEACABoBQAAPg0AACAgAAABACAAqBAAAKYSAAAYGAAAAQAgAIgJAABOIwAAFBQAAAEAIAC4BgAA1iwAABAQAAABACAAaAQAAI4zAAAoAAAAIAAAAEAAAAABAAQAAAAAAIACAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAgAAAgAAAAICAAIAAAACAAIAAgIAAAICAgADAwMAAAAD/AAD/AAAA//8A/wAAAP8A/wD//wAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA////////////////////////////////////j///////////j///////hwf/////////93//////+AAA//////////ePj////4cAAH////////9wiI////hgAAAP///////4eIj3j/+BAAAAB///////9wj4iPj4IAAAAAeP/////4MIiHf4hQAAd4gAf/////9wWHh3+IMAAH/4cHj////4MH83h/iHAASP/4AH////9wCPeIGIjwAH//+AB4///4cAiHeAeH+AB///gAB///9wAIh4gH9/gAf//4AACP/4cAeIeIB/ePgAeI8AAAj/+HcI+LhweIeIMAB4AAAI//9wCIiIgAeIj4AAAAAACP//hwiIuIAI+IiDAAAAB4////iPiIhwCPi49wAAAAj//////4i4gAaIiIh3cAeP//////+IeHeBiIuPd4AI////////+Ih3gI+IePcWj///////////h4OPhziPj/////////////hweIiI//////////////////////////////////////////////////////////////////////////////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAA//////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP////8oAAAAEAAAACAAAAABAAQAAAAAAMAA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b29vb1QhRU9XXBgCAgMNYG9vb2QfHj0mUyMCAiAwCy1nb29VCi4oJEYpBQhRYxgNYG9mIAYxKxcqQRIMYGMaAzBnWxAQPjgULzovCSVOCwAVZmIaGUpIERk8RxMCCAECImdnUVBLQA8QTEkzBwQCG2Jvb29lTTkcFUI/RCISG2Bvb29vb2FYMh01OzdSNGBvb29vb29vb2A2VlpZZm9vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb29vb28AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AACgAAAAgAAAAQAAAAAEAIAAAAAAAgBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////7+/v/8/Pz///////////////////////////////////////////////////////7+/v/R0dH/vr6+//Ly8v/////////////////////////////////////////////////////////////////////////////////z8/P/vb29//Ly8v/+/v7/////////////////////////////////////////////////yMjI/zw8PP8UFBT/kZGR//Pz8///////////////////////////////////////////////////////////////////////9vb2/6CgoP+Xl5f/9fX1//7//////////////////////////////////////////////8fHx/87Ozv/AQEB/wAAAP8jIyP/3t7e///////////////////////////////////////////////////////////////////////o6Oj/VVVV/9/f3//j7PD/xNXg//7+/v////////////////////////////39/f/Gxsb/Ozs7/wAAAP8AAAD/AAAA/w0NDf93d3f/9PT0////////////////////////////////////////////////////////////+Pj4/3p6ev87Ozv/y9LW/5m3yf+7z9r/9/f3//j4+P/////////////////8/Pz/xsbG/zg4OP8BAQH/AAAA/wAAAP8AAAD/AAAA/y4uLv/i4uL//v7+///////////////////////////////////////////////////////k5OT/S0tL/6urq//Y4ef/ja3B/+nu8f+rq6v/s7Oz//X4+v/7/P3/+/v7/8XFxf81NTX/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/CwsL/2dnZ//39/f//////////////////////////////////////////////////Pz8/21tbf8cHBz/0NDQ/97n7P+OrL7/y83O/6mpqf/t7e7/ssnX/9zl6//FxcX/MzMz/wMDA/8AAAD/AAAA/xcXF/8QEBD/Hx8f/yUlJf8FBQX/Nzc3/9ra2v/+/v7////////////////////////////////////////////Y2Nj/QUFB/xMTE//KzM3/v9DZ/4altv+jpab/e3t7//z9/f+buMn/w9DX/z4+Pv8DAwP/AAAA/wAAAP8AAAD/fHx8/319ff+3t7f/x8fH/ykpKf8HBwf/ZmZm//z8/P///////////////////////////////////////////3Z2dv8GBgb/PDw8/8XLz/9pj6X/epqs/5+hov91dXX//P39/5e1xv/CztX/OTk5/wICAv8AAAD/AAAA/wAAAP+CgoL/6+vr//T09P/o6Oj/eHh4/wkJCf86Ojr/zc3N///////////////////////////////////////Ly8v/PT09/wgICP+fn5//3+Xo/2CHnf95mqz/n6Gh/3V1df/8/f3/lbLD/8rW3f+NjY3/ERER/wAAAP8AAAD/MjIy/6+vr//v7+//9/f3//f39//Gxsb/EhIS/wEBAf90dHT//////////////////////////////////f39/4qKiv8AAAD/CgoK/729vf/m7PD/YYmf/4GjuP+goqP/R0dH/8/P0P+Trr//yNbe/93d3v8pKSn/AQEB/wAAAP9ubm7/9/f3//f39//39/f/9/f3/8jIyP8SEhL/AAAA/zExMf+/v7/////////////////////////////Dw8P/MDAw/wAAAP8KCgr/uLm5/7jK1P9ijqf/ia/F/6Cio/8PDw//mJiZ/6C3xf+CoLD/3OLl/5mZmf8ODg7/AAAA/25ubv/39/f/9/f3//f39//39/f/yMjI/xISEv8AAAD/AAAA/4iIiP/7+/v/////////////////+vr6/5qamv8DAwP/AAAA/xkZGf+4urz/f6K3/2GUsf+Su9L/oKOk/wQEBP+Pj4//4+ru/3ycrf/O2+L/09TU/y4uLv8CAgL/Y2Nj/+3t7f/39/f/9/f3//T09P+4uLj/EBAQ/wAAAP8AAAD/JSUl/729vf/////////////////Q0ND/RUVF/yAgIP8ODg7/j4+P/+js7v97pb3/aqLC/5nF3/+ho6T/BAQE/42Njf/3+fr/gaO3/4CmvP/j6e7/paWl/w0NDf8SEhL/hoaG/9LS0v/m5ub/29vb/zw8PP8DAwP/AAAA/wAAAP8EBAT/qKio/////////////////8zMzP9oaGj/h4eH/zAwMP+oqKj/8vf6/4Syy/90sNP/oM7p/6Gjpf8EBAT/ZmZm/9/g4v+GqsD/bp+7/8LZ5v/P0NH/Pz8//wEBAf8ODg7/HR0d/3R0dP+dnZ3/GBgY/wAAAP8AAAD/AAAA/wYGBv+pqan/////////////////+fn5/5ycnP8NDQ3/BwcH/6Wmpv/T5O7/hLjV/3y74P+i0u7/oaSl/wMD'
        
        # Corrigindo padding se necessário
        missing_padding = len(icon_base) % 4
        if missing_padding:
            icon_base += '=' * (4 - missing_padding)

        try:
            # Decodifica a imagem
            image_data = base64.b64decode(icon_base)
            image = Image.open(io.BytesIO(image_data))
            # Redimensionar se necessário, ajuste o tamanho conforme desejado
            largura_botao = 100  # ou qualquer tamanho desejado
            altura_botao = 100
            # largura_botao = int(image.width*100)  # ajuste a porcentagem conforme necessário
            # altura_botao = int(image.height*100)  # ajuste a porcentagem conforme necessário
            image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
            return CTkImage(image)
        except Exception as e:
            print(f"Erro ao decodificar a imagem: {e}")
            return None  # Retorna None ou tratamento de erro apropriado
              
    def images_base64(self):
        self.btsave_base64 = "R0lGODlhlAClAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAACUAKUAAAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnLlRmTI0MQDo3Mmzp8+fQIMKHUq0qBhlMTOhWVG0qdOnUKPqvIHUJNJ60LDWyyRGqtevYKEe3Ye0LNmzZtMKrLqQ7cB6aMLKnUuX51iLbguyxSqQ2I2hAQwACADAAGEAB3QSFuwz8WDBiw87Djy4sGTFkC3rnJzZ8GbMlRn3PMwTjcB6p1PvQ736dFa9sAdCG6gMaAwHPnIU+fFj9+7evH33Jn0AlPFQx40rR64cFPPlzZ1Hf568OXXpxjU5HizcZ6PZ+2aL/w9Pfnzq1whRq99HTPTOA7zjy59P/0dOnSvgaLKjCZR+/6BoAkeAA+6niYEG+tfffwU2GOCDofQnYYT8JQjHfYjJh4NPk7S23oetCQReQnyRF15jOPDmQ30sxlcEaQZYGCB/AMpoI40F4gggf3Dg4AMOPgL5449p1MifaDDM5wNpOnU4YkLoaXXWWm+l1hVP8NG34g9btsibaAcsCOCAZI5pZplomimmJm9sF5QPFmIYwG/xbdhTh+HxxVdVrJlIUJ+yCZRJTwd06eWWKyLKG3GZlHnjmjo+eiYodg4VA4Pavaeii5XulAmgBYH3GmtsvcYnWX/tFIB8inpZH4aXPv+YI6S0GkkrjRJ2GtQBmfBnRybbrVqfAz5l4hqIoD5pEHjE9GRofa2yKh+Yb4z5yay+ypimgdmOaQelRYWJI4YGKFlnsQSJKuJqs7HW56nhYQhAiptKq2WL28UgaYFq4totv7MG6INdYhQsBqzVDtjmTjHUG9+KDfS0grGquRsqaiNi3Je8zzrcYpcrvvjeG2KWmTAoJ/e6n8q/Asgyy/tdqRMaaUiCBk4MY4phlvj2FINN65rYLnrpqjYJlg+zGG2LoukbaY1QB4ytjTVWqoIYaExy884q++cenR3b5/OpFl8cIqBx7USvuYcmHR9Tm6lcB7d0Tzq1rdl+W6kBYmj/rfXOdO8M7XxuAnCXunkmHmie0Cgj57OGQv7xD9uJK2Gk/8oa9Yy1ajLwTjdPIkYaCM8IrKoeu0352KmBmt5bSKd+7+zxbQeDft1Wqy3nOqYpNbiKiSFJGmhIAjiZmepULtvz4VD4XSZeZaprBNWm6eCqp94lmLcaOLd/14JvYPiafA8H+XPz1ynNwx/MsO4ow2qv9kwaXnFDZfF0A/M/UND2fCKLW+8096jM/W5AoJAZ3xhRM5xthm7bWZ6rHvY8oQXNLRiMHZdcFTb65MtReaPb00C4OwN9DgAqYF8aGFE6MsFAVbuJXPZ+oCsAmMZirvsTWXjSAKVJqwKqaxXc/wAQA5L5KhO24pzdlFi3MnUKa1pzIBFxd6DK2QuIXvKJGKYUvbcMbYc7kQF9sKg9V3GPd91LYsnwtqb1+U2KvJrRG+TkQ9nVkGLwCpFeeLjBPnYwPljsWOWMaKFPeO+Q/Anf+QqUPk0YUkcnNFzWsAYrR0WQf7SrIZ5CJSKMocZ6OmnY5GSXvaYlSISXS6UB0dgtTVQqBlDMGteOaMU+zi9sxOqJsaRUturxcX51lFwAB9NIzKFSiSRM4oCemLWtvUdABCIX9kZ5x6J5kVQ8QcA0bTnB1YUSkZ0LIa6WyC3gzUxrjZBiEcckmhXQaZqSyyVPiNEua9JGfzNcERm5qf9PQw3xAIRk5Rp3l8zyJUhmkoxiJTknOD/yZp9k7JiuYkCMTlYJLRrkIDCTZko0osx0NNJdyxT2IJGekj8nhGUzGzHL/ixMMdhbmpJyEDGe/OwgGfvlliogw4d2M1jFXOPUQrjENDFToc9EnjS7STveFO5nJSobKAEgxm0CM1of9Oi+PPq7BJnThm8s3cpqKdMfdvB5T6rKbKbaw41mr4PDLGKCYCbOWkntkWI6KiWfma1a+tSh3LTXlgqnDFBhk2EzDCwgmcbXY560gE1UU6VgMLrhGe99snrhTt7J1BbhwD1sUetafsk/kLmtVaRZQSPZ2Ei8tpaRdgVFJGMJR2j/6sev/GRbWX8gA57kZT1T1WZ99tlZbyImlS7zV2Qhy5/vufI9wqvZGFoYv52sQHZA/GO9tlRTneRlRFPdH2BzW8b4aBYAqkXlAJm71aM6M5SW3IkENxpRV8lrL7QB42Ym6L+myqdy4xtq94wZUt6Zk7LEYyDX5NjQxHbsj90FgFuIxtY6YrK/GxwmQGOrXuSSMHMINUAMVHCA804RQWTd5rOyWy8E+DYhU61qP4tbH9Go4GR3TZBIX5ZcVS6ohj/hla/ekNHELlaxvEmVd2XjSf0CoK2j3Cl5edPbnfxARieLbDJ9p8RI7uqgNnVrEPnnpryEaKqitGUH/7gleQLg/3bK3NxjWznAASE0KDcwEBzcs7bF7tZLEXZLiZwM5VFa9Us8wUF21ltXOlMtR2lADBElnZPE5JlGStaJw7Q75S1VeckF2VM2txsfDAvWsz3BAQKnZj4CivNlT5vRg5TrH131Ocpi/kGgq/cnfDKVzfXyyQ3ecLLsGIdGoPgWgJrTH2YrB4HfQuB+Zm0cOLwh0zrZp2k3SNym3tcgVZkqz8bMpW73j0VAlgEO0ACkIInB3UASw4/aHSR6z3vd8V53DvTto3e/Owb1mxeNPaZtXb/YovfcSaE5PV4WubkuENdJn/VZ3gfTx8U7MXO4eSJjTP6vVdiO+Fzo1VNSBhKYmf8WtC8VPkbdDjwHhRO5Vw5waxaxmMZlXtzGEXvaj91cymHDQQMCLnOiHCAGKfrNthXbqqVx9+CqGS3Lgd3NsHUpBz+ioY+wnqKtD4nrufl61r3OdRqGHQdcx7raGT7w1H1awkVTT3B9ePJckxKAbacxZ+FJbsn9lT67rhJ4wttzCzf8qnlP/P9ofPO3xufboZb6fg1t88Ln85Y0Nu3J625qQO506XY/ssEzvq5BV1j0Wqq74rXbdFL71+pG9rzsotUqjIMaNjF2PegtX+pNzyeiwC8u2ye4+8q7KuXneRdpqx5MjR665IYyt98pPnzeJzbnCEEz4hWP5D+zCqIeczr/8R2P5IYbKvDJJzT2VN/69avI3Kd+PvNjX/7O/+/tpVLN3MvfMeLylJSwd3f011SdZ3GGF1hbYn+jd3vsknBT4XGXd4AQKIHm9wOqZ3jRx2kMB3m4V2SN518bVXKYV24ISIGhV3ClZYGz0yWB12SnQVoG6APSR3AhiHrwB4IT2F8iSHl2Z3twtyxOVlXCt3hE6HfYJWUlyH/MgygzuE3Ix2StUWHbJn4C6HtMl4I+ZYBV2Ec3WITkh316JHlE9Gu/10c62HLzZ4JkuIIPZYQDh375pX5W2IVpKHvld4e014ab8n84mIIfiGGdh39Q6IAAIFwxVYOYtFsdxIfVR4RLgLiGzAOHFkV4obd9jehy42eFRraDfIeDHBiG4laGgkWHWRh+2wV+zed8m/h3U3ho5gKHayWGUNZ+8XeHA9h9Arh7YaOAXlJfTWUoPohfb5F73NdwTciGoqiCFAeJtSiDE0RcYfOE5KF8LGeLsNdt4ld3w1dWzsiED4ONH2eKuOhU/1AXNE6WZoBlat5YjLTjfRoIgd63hYBXjk12eoqHAzyFdRWQImFHQ/m4IvTiAFySA/6TA1zyAAc5kAMJkLyBdT/gkA5JLwbZjw4pkD6AkLkBRPRScyhohvUiiJHnZIZIfmwjdDFwACh5ACuQkigZAEeXki55AAbQkkc3kwcQADFgkzcpkzCJkjYZGD65kzwplDB5kj0JAyn5ZA5AcjN0g4H3RWIoXlzIT43nPEV3lVFhAAJpYR3zifkVipn3cFg5lkUBJLl2fgfnguoHemETc2T5lkIBHwHoNsEIYxyHgSriljFwA3vZl3z5l37ZlzgQmIB5AzJQmIdJmHuZmIZZmP+K6ZiIyZdBNoHxIY3HIodbWEM3kAZvoB+eySOe6R+eqWcCQppwgDyhOZqoaVuluZquqSCu+QZpUENb6YxNBYZ5oX1Y+ANiySDJlmxiApw0Em2yljeLNm1GIpzTZpzMWU6NBpxy5BPTN4+kly6HpRNt1X/N0xNFMiscply0ti3rJWfkCTAEtDkFEmk8sZXD9ZH0uC7791dL0xNo0C/LxWiSIkKac0BFNSklhGw/0BO3iH4Z42RSeXedcgBUZJ/9+WGPQjKdCaG2pSbliUz+GUIqkGjIyBufaHqxs2a84WZiAJ1301Vy1juZ8AY+IAY3UJMnKWI3sG4k02pcVqIWWjf/nTJxgyOJZ7Z8/NMpaWCj94lltvIGaOCWtoEDnSk+J8pcXbMgRFaNy1gfdUk9p0GMricfEZZlmdNErnUjc/QVwwYpMGNIAJJl5OMrBRKlErehP2CZDbiWE9QpJMNVHzUgdGVXYSoXAHWh+8GfkcWmT8ZUYAhuYcYiZ+hmAXU+W6VlSkF0OwEDMRAGlBoDJvYTnGmhXdWlNKKebSqO8UGgeuJk7Hl4b8oTOGanDloj12YbkoAJw5AM85AP+jCryTAMmHBZP7FOQ0pUUyOohWZLNweSf7JWRdYiigpZbGRgL9UTYSAM+TCr0ZoPsjqt+TCtmBAGQVanOdI1eNo7aYoy/xraTXAIKJTYe6pDp0IlPuu1Wp7KE2EwDLSaDPlAD9Raq9GqD7Jqr/Mwq8OgrT6xpFpmpwgCBzDIP58IHp/0oZi0pWpkJvADQu+qEzAgCdfar9M6D/iqDNZKr/xKq5JwqQDQna5WSIE6rhHYglZqj65Cp93qn34qbPIKDf1Ks7eaDMJwq8gQq8PAs/X6DBg7DCFnUs3lYWwErGXYMVV6EFiahAsIAL7poAVmIK0Krxl7rf9aFGFQrfk6DwC7EzcgtVslqEzpJdIYiws7dR5Hp/YZnkqkK2JQrfTgryEXFDEgqxwrrV8rcXdjUv4pqKUaf2DYJ8YaRi1yc1tKK4okUP/iqj+zqq/R+gx7q7XTmgz2mgyTm2VslEh0I6gHCmHlWDE+KlN0Wmecs1pk0hMqUK0Y269SMQy1Oqu2Ki8rwK1qQqOsup44SKyvMXgMC2iouiYMaiFpsxPySq31mgz6gAk8YQAN8LzQC71uggz32q/2yrylsUqP1rgPCC2IG7qpca5/Z0vqWldFJS9hALT1Krv5MAw8MQEbEAIhsAEgML/1G2GY8LH0qrF7GyvCK556prv094kZtBMjWVYR5pveikxmGkl3G63zoL7+up4goAEaAAIbcMH0G2Hyyr5Ba2JoYL7HZG2+hnpaCr6iJqUti6pta1C20ikWO6sfOw/QIAz/PBQCGoDD9JvBIeBmwzCryhDBl5sPkqA/YpKnH6VjAtx+W7K0g1YPuomMyapVdWWwPFGt1RrE0eq+OwG/GKzBGhxhyCDBHpwMPcGfv/OuNccicEqN2ImDmZaqdSMj7xoG08qvQJwPyEDBGfzFGAwCE8AT8sqvGzure4sG22Km24K0hgeGiEOM2hkfyaojSFwgMKyvtnq1g9LFO/zHGbwBEQatsgq07EsPRaw2yMSp+0G2WTof5Rq+y9eKNBS8fnqm/pFpHYyvNNyv+mDDnFzBO3zBIRBhmSDDkTvEZgy22xswbOKjVkis0yiG4wa8OxFQdeO3b0AaN1C5Goux9MrF/9iJwzicwxqwwTwhDLosu+osJ4QUQourMCjrKq/su2D7e0HHwnNcV4K6tRAcucbsyzpBAeQ80DhMAYKMvEJcvZKLz4kkpIysKKrnlbBswBXHGwnMLTDDRHbwrpKQx60bwfOwyeFMzsE8zOdcr/3cuvlQvCNrTPbJylYVeOFGiMGKatX8v0vE0bpcq89AyAANAF5czn+cw8ScybtMrfZ6yjpBsgBcI1b8xt20tEUTxbvlsNvSagbyrphgq7Irq6P80w0gzhaswyAQykDr1Vc7D9i71EmUZekDCmrMe1timaOCmXXksjeKORydsfoQBiWWE/LyZF88zuIcYUSkAid5Nf/JW69rbUOAmi3NXI0qOEODu0eGO2WhSstS2zUsvdU0S8RDQQH0K9R9DMpDEcPRqtQjWyNYrSN2ANMCyKM7B9UeY2psu6oJstF2AcHPoNo/0QDkTNg5HMhCcQZDrNpMvbkSArh352lQRzRONs0tkrglpdzcCwB23M2N/RMU4MclTdxBgQn5irkMPVC947n3QlySWE/i+4Fbctu3SyvNGgMgndpA0QBe3MlCXc4UYNg7IQmxG607k9wv6yhPDQCByzwdCp+jZou8yRMLymWkqWQwIKs8rdbcLdw8vN8hMAEBh9rfLBp5Zp73CdvFh376EA0hQg/OnD1xHE5r9FUxzL7/wyCyEyDc3q0BBu0T4g3SSZ1oxCmk/CHSg/o/TrwP+rAP0QDFh2qqD37Tq8SoOFLHefuxQusTwL3hX6wB/n0Dg3y1mZYGR2y6azquf2aZS07TzhfHy3pAPdHBQPvZ5N0TwD3OO+zfW7C/0cqvyQzlJYNXoOCtjLxNhZrkhNhxiTXFsGW6/ZFpqK3S88DSyhPcGuAeOiEJEgy06ssIiVZtyp078ZxY85y2tM1Nto2qRDWkARqpsvrZQjyrvo0Y3U0BMYcGVzu30ZoM8iIGBIZcVKtTeygtxKriPXo9bUPdqPTOppNpYYCvlnu1NY7lPwGtvMy6+rq3YRtnEg7b04Ti//WQ4lGJg+W7VUhEJhPb4+yrvHRrKej8s8ZMrz8NADmwnxWaujuR4Iol0ftADyJZLxf45Drhm726IMkTSvJaq6yrvlkLFPz80dSqscMgLzFgJl1zMlwa2d1riyq75MTOsrQT5iSaxI3mUj1xA/WNx/iaD3emE2KQseqbt9GKbW8Q5XGG8QguH9AYH1Jt6GKYZtqVrI4yvN2iK2HQzRLctaDNE5hesw5PD3OuNj6m0Wuk2/VsfadanUq+GvpA6kVufWze5oHuq8+lPx0crRw7yrMqDICN7ny9v08/FQBM5gFi8/heH5VN7EHofEDPoMzsK9c9FV/uwZA7DzmLsXl78v/JcKkBYFJpGlnlnmzojYDfi/VJrg/LIM2aqCGoLiHmo+wGhSOacDo8UbFo382y+wz4qstdi+E+47dogleNXyHMDYELjuTRvYuurNl5bd79wR+CuhPx6u5IzdvzsL95+wyYsPIAQDKbOrDTFtf0V6gqjhpLTi4GOXu8Ad9xT1B6Ftg6EQaY4LFpjfRqrfxyNfJQs1wH3kMgyiU2xRaGXk8sjQN7R50B/52Pb56cAwd1+/0AgWlYsmTz9M0jKAyTGAANHTrEAQeURE0TQVWUSNFOxot2NHm0A+rNQxw/TJ70cfIkjodo9u2rty9azJgvMz08cLLCj5Q8VbJ0+MbiR6L/IDFetCgUDlFQE9E8hNoQRowwN6qqiApVjNCjEpVe/MS0aEWimkY6dIDS5M6eJg88nPRSrr5o++jWUwbVZFuVJxs8fDMWVCaPFjly/NhRE0U4NwJkhRwZx1eNZI0arYPxE2I7Zxve6Bva5MMAyuS+rFlz3w2coveaBNowTWHBnDMN9Vj74hvWkX0DmHxUd+XCiA3vfphWZduebx3eeElPLrSX+mDuu0lSrU+/gBUXv5j5OFPOtdHEePy7YQwci3F3fT/+clfPwF2vNPBwmEzUqGfWham3hg7g64edVgKsPKPkG2uz+Dh6Iw0fYnDOoQBuwCGNNyQKyTLhwIPDQfjI/0Oqvga4K9CH9D4zTTXr7KrOJqhyuu+voI7iCjwSCfuQRB+JWgo8pDT56DDDwqJtPsUmclCiNLTrq60KGyKmuroAXKa/LPeZZMaSUITNO4reW1BBsZQkriIdOUpSuONsA4nHNZNT6cAfcJgSAJdkUm0f6fahDsZ98vJSNBsbWurNwcDL8UzdxgIRUsMgHZHMHuWrD7TXTHIgTwBQe1EuAK+bCbUYojogB75iA4CyBy0dT7w0v6vovaNeNVLOS8ekqD7lVvI0BmVU21Iu6aKxrh667CIUVQdwKMkBwGpFCpTCOmyqsGyb2tYia5tKjFumOsq2Vom49bbab6k991pyO8fK7rM7n/W0IdMAjbFP/057iRgB1QMgvcfya8iA9AgOgGDIEm7oYIEdIlhhAJyTGACFK64wv4EhhnhFgAEQlt96Rj3tT32yHBm1pz5muWWXX4YZZknkavHFUE8rVdBQlWEoZp9/Bjroh8KoMmf+9imW39NQrivUTCTxWGipp546BjSqnAumZJXmOmuYjIZGmUn+pbpss9XDQRJl7pXJui1J7jpuueemu26778Y7b7335rtvv/8GPHDBBye8cMMPRzxxxRdnvHHHEB+HPHLJJ6e8cssvx9zxgAAAOw=="
        image_data = base64.b64decode(self.btsave_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.3)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.3)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.btsave_img = CTkImage(image)
        
        self.btsavedown_base64 = "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"
        image_data = base64.b64decode(self.btsavedown_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.8)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.8)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.btsavedown_img = CTkImage(image)
        
        self.bttrash_base64 = "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"
        image_data = base64.b64decode(self.bttrash_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.8)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.8)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.bttrash_img = CTkImage(image)

        self.btconsulta_base64 = "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"
        image_data = base64.b64decode(self.btconsulta_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.8)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.8)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.btconsulta_img = CTkImage(image)
        
        self.btanexar_base64 = "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"
        image_data = base64.b64decode(self.btanexar_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.8)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.8)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.btanexar_img = CTkImage(image)

        # Imagem Botão Cadastro ...        
        self.btcadastro_base64 = "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"
        image_data = base64.b64decode(self.btcadastro_base64)
        image = Image.open(io.BytesIO(image_data))
        largura_botao = int(image.width * 0.8)  # ajuste a porcentagem conforme necessário
        altura_botao = int(image.height * 0.8)  # ajuste a porcentagem conforme necessário
        image = image.resize((largura_botao, altura_botao), Image.LANCZOS)
        self.btcadastro_img = CTkImage(image)
        
    def load_icon(self, tipo, size=(64, 64)):  # Adiciona um parâmetro de tamanho
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if tipo == 'consultar':
            icon_path = os.path.join(base_dir, 'icon', 'search-13-48.ico')
        elif tipo == 'processar':
            icon_path = os.path.join(base_dir, 'icon', 'processo_4.ico')
        elif tipo == 'maps':
            icon_path = os.path.join(base_dir, 'icon', 'processo_4.ico')
        else:
            raise ValueError("Tipo de ícone inválido.")
        
        try:
            icon_image = Image.open(icon_path)
            icon_image = icon_image.resize(size)  # Redimensiona a imagem
        except FileNotFoundError:
            print(f"Erro: O arquivo {icon_path} não foi encontrado.")
            return None
        
        # Converter para CTkImage
        ctk_image = CTkImage(icon_image)
        return ctk_image
class Functions():
    
    # Drop Unidade de Medida
    def get_unidade_medida(self):
        strSql = "SELECT * FROM TB_TiposdeMedida ORDER BY TB_TiposdeMedida.TipodeMedida_Desc ASC"
        myresult = db._querying(strSql)
        unidade_medida = [(unidade['TipodeMedida_Diminutivo'], unidade['TipodeMedida_Desc']) for unidade in myresult]
        return unidade_medida
    
    # Drop Tipo Spead Fiscal
    def get_tpspead(self):
        strSql = "SELECT * FROM TB_TipoItem ORDER BY TB_TipoItem.TipoItem_Cod ASC"
        myresult = db._querying(strSql)
        spead = [(spead['TipoItem_ID'], spead['TipoItem_Desc']) for spead in myresult]
        return spead
    
    # Drop Natureza Financeira
    def get_bancos(self):
        strSql = "SELECT ID_Banco, DS_Banco FROM TB_Bcos ORDER BY DS_Banco"
        myresult = db._querying(strSql)
        bancos = [(banco['ID_Banco'], banco['DS_Banco']) for banco in myresult]
        return bancos
    
    # Drop Agências Bancárias
    def get_agencias(self, Empresa_ID, Banco_ID):
        conditions = []  # Lista para armazenar as condições
        conditions.append("cc.Empresa_ID = %s ")
        params = [Empresa_ID]
        if Banco_ID != '':
            conditions.append("cc.ID_Banco = %s ")
            params.append(Banco_ID)
        
        strSql = f"""
                    SELECT 
                        DISTINCT cc.ID_Agencia AS Agencia
                        FROM TB_Conta_Corrente cc
                    WHERE {' AND '.join(conditions)}
                """
        
        myresult = db.executar_consulta(strSql, params)
        agencias = [(agencia['Agencia']) for agencia in myresult]
        return agencias
    
    # Drop Contas Bancárias
    def get_contascorrente(self, Empresa_ID, Banco_ID):
        conditions = []  # Lista para armazenar as condições
        conditions.append("cc.Empresa_ID = %s ")
        params = [Empresa_ID]
        if Banco_ID != '':
            conditions.append("cc.ID_Banco = %s ")
            params.append(Banco_ID)
        
        strSql = f"""
                    SELECT 
                        cc.ID_Conta AS Conta
                        FROM TB_Conta_Corrente cc
                    WHERE {' AND '.join(conditions)}
                """
        
        myresult = db.executar_consulta(strSql, params)
        contas = [(conta['Conta']) for conta in myresult]
        return contas
    
    def get_natureza_financeira(self, Empresa_ID):
        strSql = """
                    SELECT 
                        nt.Nat_ID           AS Codigo, 
                        nt.Nat_Descricao    AS Nome, 
                        nt.Nat_Tipo         AS Tpo 
                        FROM TB_Natureza nt
                    WHERE 
                        nt.Nat_Tipo='A'
                        AND nt.Empresa_ID=%s
                    ORDER BY Nome
                """
    
        myresult = db.executar_consulta(strSql, Empresa_ID)
        naturezas = [(natureza['Codigo'], natureza['Nome'], natureza['Tpo']) for natureza in myresult]
        return naturezas
    
    def get_natureza_gerencial(self):
        strSql = """
                    select 
                        Nat_ID, 
                        Nat_Tipo, 
                        Nat_Desc 
                    from naturezas
                """
    
        myresult = db._querying(strSql)
        naturezas_gerencial = [(natureza['Nat_ID'], natureza['Nat_Desc']) for natureza in myresult]
        return naturezas_gerencial
    
    # Drop Produtos
    def get_produtos(self, Empresa_ID):
        strSql = """
                    SELECT 
                        pp.Produto_ID           AS Codigo, 
                        pp.Produto_Descricao    AS Nome, 
                        pp.Produto_Tipo         AS Tpo
                        FROM TB_Produtos AS pp
                    WHERE 
                        pp.Ativo='A'
                        AND pp.Empresa_ID = %s
                    ORDER BY pp.Produto_Descricao"""
        
        myresult = db.executar_consulta(strSql, Empresa_ID)
        produtos = [(produto['Codigo'], produto['Nome'], produto['Tpo']) for produto in myresult]
        return produtos
    
    # Drop Empresa
    def get_empresas(self):
        UserName = os.environ['Usr_login']
        
        if (UserName == 'Admin') or (UserName == 'admin') or (UserName == "ADMIN"):
            strSqL = """SELECT Pri_Cnpj, Pri_Descricao FROM TB_Empresas ORDER BY Pri_Descricao"""
            myresult = db._querying(strSqL)
        else:
            strSqL = """
                        SELECT 
                        distinct(per.Empresa_ID) AS Empresa_ID, 
                        emp.Pri_Cnpj             AS Pri_Cnpj,
                        emp.Pri_Descricao        AS Pri_Descricao, 
                        emp.Pri_EndUf            AS Pri_EndUf 
                        FROM usuarios usr
                        INNER JOIN TB_Permissoes per ON per.UsR_Login=usr.Usr_Login
                        INNER JOIN TB_Empresas   emp ON emp.Pri_Cnpj=per.Empresa_ID
                        WHERE usr.Usr_Login= %s ORDER BY emp.Pri_Descricao
                    """
            
            myresult = db.executar_consulta(strSqL, UserName)

        empresas = [(empresa['Pri_Cnpj'], empresa['Pri_Descricao']) for empresa in myresult]
        
        return empresas
    
    # Drop Projetos
    def get_projetos(self):
        UserName = os.environ['Usr_login']
        
        if (UserName == 'Admin') or (UserName == 'admin') or (UserName == "ADMIN"):
            strSql = """
                        SELECT pj.projeto_id, pj.projeto_ds, pj.projeto_empresa
                        FROM projetos_cronograma pj
                        WHERE pj.Projeto_Ativo=''
                        ORDER BY projeto_DS
                    """
            myresult = db._querying(strSql)
        else:
            strSql = """
                        SELECT DISTINCT(pp.Empresa_ID), pj.projeto_id, pj.projeto_ds, pj.projeto_empresa FROM TB_Permissoes pp
                        INNER JOIN usuarios            uu ON uu.Usr_Login=pp.UsR_Login
                        INNER JOIN projetos_cronograma pj ON pj.projeto_empresa=pp.Empresa_ID
                        WHERE pj.Projeto_Ativo<>'x'
                        AND pp.UsR_Login=%s
                        ORDER BY projeto_DS
                    """

            myresult = db.executar_consulta(strSql, UserName)

        projetos = [(projeto['projeto_id'], projeto['projeto_ds']) for projeto in myresult]
        
        return projetos
    
    # Drop Pessoas
    def get_pessoas(self, Empresa_ID):
        UserName = os.environ['Usr_login']
        strSql = """
                SELECT 
                    pp.Pessoas_CPF_CNPJ, 
                    pp.Pessoas_Descricao 
                    FROM TB_Pessoas AS pp 
                WHERE 
                    Empresa_ID= %s
                ORDER BY pp.Pessoas_Descricao"""
                    
        myresult = db.executar_consulta(strSql, Empresa_ID)
        pessoas = [(pessoa['Pessoas_CPF_CNPJ'], pessoa['Pessoas_Descricao']) for pessoa in myresult]
        return pessoas

    # Drop Centro Resultados
    def get_centrosresultados(self, Empresa_ID):
        strSql = """SELECT 
                        Cen_ID, 
                        Cen_Descricao 
                        FROM centrocusto cc 
                    WHERE
                        cc.Cen_Tipo='A'  
                        AND cc.Empresa_ID = %s
                    ORDER BY cc.Cen_Descricao"""

        myresult = db.executar_consulta(strSql, Empresa_ID)
        centros = [(centro['Cen_ID'], centro['Cen_Descricao']) for centro in myresult]
        return centros
    
    # Drop Status
    def get_status(self, ID_Empresa):
        strSqL = f"""SELECT Status FROM Status_Prospeccao
        WHERE Empresa_ID='{str(ID_Empresa)}' ORDER BY Status_Order, Status"""

        myresult = db._querying(strSqL)
        status = [(status['Status']) for status in myresult]
        return status
    
    # UF
    def get_uf(self):
        strSqL = 'SELECT UF FROM Estados WHERE Estado IS NOT NULL ORDER BY UF'
        myresult = db._querying(strSqL)
        ufs = [(uf['UF']) for uf in myresult]

        return ufs
    
    # Municipios
    def get_municipios(self, UF):
        strSql = f"""SELECT IBGE, Município FROM Municipios_IBGE WHERE UF='{
            str(UF)}' ORDER BY Município"""
        myresult = db._querying(strSql)
        municipios = [(municipio['IBGE'], municipio['Município'])
                      for municipio in myresult]

        return municipios
    
    # Drop Unidade Negocio
    def get_unegocios(self, Empresa_ID):
        UserName = os.environ['Usr_login']

        strSql = """
                SELECT 
                    uu.Unidade_ID, 
                    uu.Unidade_Descricao 
                    FROM TB_UnidadesNegocio AS uu
                WHERE  
                uu.Empresa_ID=%s 
                ORDER BY uu.Unidade_Descricao"""
        
        myresult = db.executar_consulta(strSql, Empresa_ID)
        unidades_negocios = [(un_negocio['Unidade_ID'], un_negocio['Unidade_Descricao']) for un_negocio in myresult]
        return unidades_negocios
    
    # Drop Orçamentos
    def get_orcamentos(self, Empresa_ID):
        strSql = """
                SELECT 
                    Empresa_ID,
                    CAST(Orc_ID AS CHAR) AS Orc_ID,
                    Orc_Descricao,
                    Orc_Status,
                    Orc_Observacao
                FROM orc_orcamentos 
                WHERE 
                    Orc_Status='A' 
                    AND Empresa_ID=%s
                 """
                
        myresult = db.executar_consulta(strSql, Empresa_ID)
        orcamentos = [(orcamento['Orc_ID'], orcamento['Orc_Descricao']) for orcamento in myresult]
        return orcamentos
    
    # Drop Item de Preços Orçamento
    def get_precos_orc(self, Empresa_ID, Orc_ID):
        conditions = []  # Lista para armazenar as condições
        conditions.append("Empresa_ID = %s ")
        params = [Empresa_ID]

        if Orc_ID != '':
            conditions.append("Orc_ID = %s ")
            params.append(Orc_ID)
        
        strSql = f"""
                    SELECT 
                    pp.Preco_ID, 
                    pp.Preco_Descricao, 
                    pp.Preco_Valor, 
                    pp.Unidade_ID, 
                    mm.TipodeMedida_Diminutivo
                FROM orc_precos pp
                    LEFT JOIN TB_TiposdeMedida mm ON mm.TipodeMedida_ID=pp.Unidade_ID
                    WHERE {' AND '.join(conditions)}
                 """
                
        myresult = db.executar_consulta(strSql, params)
        itens_orcamento = [(orcamento['Preco_ID'], orcamento['Preco_Descricao']) for orcamento in myresult]
        return itens_orcamento
    
    # Drop Tipo Projetos
    def get_tpo_projetos(self):
        strSql = "SELECT projeto_tipo_id, Tipo_Empreendimento, Per_Imposto FROM Tipo_Empreendimento WHERE Tipo_Empreendimento IS NOT NULL ORDER BY Tipo_Empreendimento"

        myresult = db._querying(strSql)
        tpo_projetos = [(tpo['projeto_tipo_id'], tpo['Tipo_Empreendimento'], tpo['Per_Imposto']) for tpo in myresult]
        return tpo_projetos
    
    # Drop Tipo Programa
    def get_tpo_programa(self):
        strSql = "SELECT projeto_status_id, projeto_status_ds FROM Projetos_Status ORDER BY projeto_status_ds"

        myresult = db._querying(strSql)
        projeto_result = [(projeto_status['projeto_status_id'], projeto_status['projeto_status_ds']) for projeto_status in myresult]
        return projeto_result
    
    # Drop Tipo Status do Projeto
    def get_projetos_situacao(self):
        strSql = "SELECT projetos_situacao_id, projetos_situacao_ds FROM Projetos_Situacao ORDER BY projetos_situacao_ds"

        myresult = db._querying(strSql)
        projetos_situacao = [(tpo['projetos_situacao_id'], tpo['projetos_situacao_ds']) for tpo in myresult]
        return projetos_situacao
    
    # Drop Tipo Pagtos
    def get_tpo_pagto(self):
        strSql = 'SELECT TipoPagamento_ID, TipoPagamento_Desc FROM TB_TiposPagamento ORDER BY TipoPagamento_Desc'
        
        myresult = db._querying(strSql)
        formas_pagto = [(forma['TipoPagamento_ID'], forma['TipoPagamento_Desc']) for forma in myresult]
        return formas_pagto
    
    def get_aliquota_imposto(self, tpo_projeto):
        strSql = """
                    SELECT 
                    Per_Imposto 
                    FROM Tipo_Empreendimento 
                    WHERE Tipo_Empreendimento = %s 
                    ORDER BY Tipo_Empreendimento"""
        
        myresult = db.executar_consulta(strSql, tpo_projeto)
        myresult = [aliquota['Per_Imposto'] for aliquota in myresult]
        return myresult

    # Drop Cenários
    def get_nome_cenario(self, Empresa_ID, Cidade, UF, Tpo_Projeto):
        conditions = []  # Lista para armazenar as condições
        conditions.append("Nome_da_Area <> ''")
        conditions.append("Empresa_ID = %s ")
        params = [Empresa_ID]

        if Cidade != '':
            conditions.append("Cidade = %s ")
            params.append(Cidade)

        if UF != '':
            conditions.append("UF = %s ")
            params.append(UF)

        if Tpo_Projeto != '':
            conditions.append("Tipo = %s ")
            params.append(Tpo_Projeto)

        strSql = f"""SELECT Nome_da_Area FROM Dados_Prospeccao
                     WHERE {' AND '.join(conditions)} ORDER BY Nome_da_Area"""
        myresult = db.executar_consulta(strSql, params)
        return myresult
    
    # Drop Curvas
    def get_nome_curvas(self, Empresa_ID):
        conditions = []  # Lista para armazenar as condições
        conditions.append("Empresa_ID = %s ")
        params = [Empresa_ID]

        strSql = f"""SELECT * FROM Curvas
                     WHERE {' AND '.join(conditions)} ORDER BY Nome_Curva"""
        
        myresult = db.executar_consulta(strSql, params)
        return myresult
    
    # Drop Etapas Curvas
    def get_etapas_curvas(self):
        strSql = 'SELECT * FROM Tipo_Periodo_Curva ORDER BY DS_Tipo_Periodo_Curva'
        myresult = db._querying(strSql)
        etapas = [(etapa['DS_Tipo_Periodo_Curva']) for etapa in myresult]
        return etapas
        
    # Drop Sistemas Amortização
    def get_sistema_amortizacao(self):

        strSql = 'SELECT Sistema_ID FROM Sistemas_Amortizacao WHERE Sistema_ID IS NOT NULL ORDER BY Sistema_ID'
        
        myresult = db._querying(strSql)
        sistema = [(sistema['Sistema_ID']) for sistema in myresult]

        return sistema
    
    # Drop Periodicidade
    def get_periodicidade(self):

        strSql = 'SELECT Periodi_ID, Periodi_Descricao FROM orc_periodicidade'
        
        myresult = db._querying(strSql)
        periodicidade = [(periodi['Periodi_ID'], periodi['Periodi_Descricao']) for periodi in myresult]

        return periodicidade
    
    # Drop Indices de Reajuste
    def get_idx(self):

        strSql = 'SELECT Idx_ID, Idx_DS FROM Orc_idx'
        
        myresult = db._querying(strSql)
        idx = [(indice['Idx_ID'], indice['Idx_DS']) for indice in myresult]

        return idx
    
    # Drop Frete
    def get_frete(self):
        frete_options = [
                        ('0', 'Contratação do frete por conta do remetente (CIF)'),
                        ('1', 'Contratação do frete por conta do destinatário (FOB)'),
                        ('2', 'Contratação do frete por conta de terceiros'),
                        ('3', 'Transporte próprio por conta do remetente'),
                        ('4', 'Transporte próprio por conta do destinatário'),
                        ('9', 'Sem ocorrência de transporte')  
                        ]
        myresult=frete_options
        fretes = [(frete[0], frete[1]) for frete in myresult]
        return myresult
    
    def getIRR_EXEC(self, AllFlows, Periods):
        try:
            # Calcula a taxa interna de retorno e ajusta para o período
            return (1 + npf.irr(AllFlows)) ** Periods - 1
        except Exception:
            # Retorna False em caso de erro
            return False
    
    def ult_dia_mes(self, v_data):
        if isinstance(v_data, str):
            v_data = datetime.strptime(v_data, '%Y-%m-%d')

        if not isinstance(v_data, datetime):
            v_data = datetime.now()

        next_month_first_day = (v_data.replace(day=28) + timedelta(days=4)).replace(day=1)
        last_day_of_month = next_month_first_day - timedelta(days=1)

        return last_day_of_month.strftime('%Y-%m-%d')
        
    def add_months(self, source_date, months):
        """Add a number of months to a date."""
        # Calculate the target year and month
        month = source_date.month - 1 + months  # Months are zero-indexed
        year = source_date.year + month // 12  # Calculate year by dividing total months by 12
        month = month % 12 + 1  # Total months must be converted back to 1-indexed month

        # Generate the new date, assuming the same day and handle potential overflow
        day = min(source_date.day, (datetime(year, month, 1) + timedelta(days=31)).day)
        return datetime(year, month, day)
    
    def usuario_autentic(self, strUsr, perm_modulo):
        try:
            # Se o usuário for Admin, conceda automaticamente permissões
            strUsr = os.environ.get('Usr_login')
            if strUsr == "Admin":
                return True
                        
            # Construir a consulta SQL
            vsSQL = """
            SELECT 
            Permissao_Modulo, 
            Permissao_Tipo 
            FROM TB_Permissoes
            WHERE UsR_Login = %s
            GROUP BY Permissao_Tipo, Permissao_Modulo
            ORDER BY Permissao_Tipo, Permissao_Modulo
            """

            # Executar a consulta
            resultados = db.executar_consulta(vsSQL, strUsr)
            # print(vsSQL, strUsr)
            # print(resultados)
            
            # Verificar se o usuário possui permissões
            if not resultados:
                messagebox.showinfo('Gestor Negócios', f"Usuário - {strUsr} - Não Tem Permissões Cadastradas!")
                return False

            permitido = False
            for row in resultados:
                
                if row['Permissao_Tipo'] == "Admin":
                    permitido = True
                    break
                elif row['Permissao_Modulo'] == "Todos":
                    permitido = True
                    break
                elif row['Permissao_Modulo'] == perm_modulo:
                    permitido = True
                    break

            if not permitido:
                messagebox.showinfo('Gestor Negócios', f"Usuário  - {strUsr} - Não Tem Permissões para Acessar!")

            return permitido

        except Exception as e:
            messagebox.showinfo('Gestor Negócios', f"Erro: {e}")
            return False

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind("<Enter>", self.schedule)
        self.widget.bind("<Leave>", self.hide)
        self.widget.bind("<ButtonPress>", self.hide)

    def schedule(self, event=None):
        self.unschedule()
        self.id = self.widget.after(500, self.show)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show(self):
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tip_window = tw = ttk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = ttk.Label(tw, text=self.text, justify=ttk.LEFT,
                         background="#ffffe0", relief=ttk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()