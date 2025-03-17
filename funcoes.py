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
        
        ID_Unidade = self.entry_informacoes_unidade_negocio.get()
        Dta_Registro = datetime.now() #aJUSTAR PARA DATA DO DIA DO REGISTRO
        Usr = os.environ.get('Usr_login')
        
        CEP = ''
        Endereco = ''
        EndNr = ''
        EndCompl = ''
        EndBairro = ''
        
        TPer_Desconto_VPL = float(self.entry_taxa_desconto.get().replace("%", "").replace(",", ".")[:7]) / 100

        Dta_Documento = datetime.now().strftime("%Y-%m-%d")
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
            messagebox.showerror("Erro", f"Ocorreu um erro ao incluir a parcela: {str(e)}")

    def incluir_itens_click(self):
        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.')
            return

        documento_valor_total = float(self.entry_doc_valor_total.get().replace('.', '').replace(',', '.')[:15])

        if self.entry_itens_nota_prod_descr.get() != '':
            item_produto = self.entry_itens_nota_prod_descr.get()
        else:
            messagebox.showerror("Erro", "Preencher o Produto!")
            return
        
        if  self.entry_itens_nota_centro.get() != '':
            item_centro = self.entry_itens_nota_centro.get()
        else:
            messagebox.showerror("Erro", "Preencher o Centro Resultado!")
            return
        
        if self.entry_itens_nota_natureza.get() != '':
            item_natureza = self.entry_itens_nota_natureza.get()
        else:
            messagebox.showerror("Erro", "Preencher a Natureza Financeira!")
            return
        
        ID_Produto = self.obter_Produto_ID(item_produto)
        ID_CR = self.obter_Centro_ID(item_centro)
        ID_Nat = self.obter_Natureza_ID(item_natureza)
        
        if self.entry_itens_nota_peso.get() != '': 
            item_peso = float(self.entry_itens_nota_peso.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Peso em branco, Preecher pelo menos com zero!")
            return
        
        if self.entry_itens_nota_quant2.get() != '':
            item_quantidade = float(self.entry_itens_nota_quant2.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Quantidade em branco, Preecher com valor!")
            return
        
        if self.entry_itens_nota_valor_unit != '':
            item_valor_unitario = float(self.entry_itens_nota_valor_unit.get().replace('.', '').replace(',', '.')[:15])
        else:
            messagebox.showerror("Erro", "Valor Unitário em branco, Preecher com valor!")
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
            messagebox.showinfo("Erro", "Documento já existe, com Itens Cadastrado!")
            
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
                messagebox.showerror("Erro", "Soma dos Itens não pode ser Maior que o Valor Total do Documento!")
                self.entry_itens_nota_prod_descr.focus()  # Set focus to the product ID input       

    def incluir_itens(self):
        item_peso = float(self.entry_itens_nota_peso.get().replace('.', '').replace(',', '.')[:15])
        item_quantidade = float(self.entry_itens_nota_quant2.get().replace('.', '').replace(',', '.')[:15])
        item_valor_unitario = float(self.entry_itens_nota_valor_unit.get().replace('.', '').replace(',', '.')[:15])
        item_valor_total = float(self.entry_itens_nota_valor_total.get().replace('.', '').replace(',', '.')[:15])
        
        if item_valor_total == 0:
            messagebox.showinfo('Gestor Negócios', 'Erro Valor Total do Item não pode ser Zero!!!.')
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
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get())
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
        Frete = self.obter_Frete_ID(self.combo_frete.get()) 
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
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.')
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
            messagebox.showinfo("Info", "Documento Não Pode ser Excluídos, existem Baixas Financeiras!")
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
            messagebox.showwarning("Seleção Inválida", "Por favor, selecione um item para excluir.")
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
            messagebox.showinfo("Info", "Item da Nota já gravado, só pode ser excluído toda a nota!")
            cursor.close()
            return
        
        self.LItens.delete(Nr_Item[0])
        
        cursor.close()  # Close the cursor

    def consulta_lcto(self):
        Modulo_Financeiro = self.entry_tipo_lcto_descr.get()

        if self.combo_empresa.get() != '': 
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
            return
        
        if self.combo_pessoa.get() != '':
            ID_Fornecedor = self.obter_Pessoa_ID(self.combo_pessoa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.combo_unidade_negocio.get() != '':
            ID_Unidade = self.obter_Unidade_ID(self.combo_unidade_negocio.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Cliente/Fornecedor em Branco!!!.')
            return
        
        if self.entry_doc_num.get() != '':
            Nr_Documento = self.entry_doc_num.get()
        else:
            messagebox.showinfo('Gestor Negócios', 'Nr do Documento em Branco!!!.')
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
            messagebox.showinfo('Gestor Negócios', 'Documento Não Existe!!!.')
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
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa em Branco!!!.')
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

    def Consulta_Prazo_Curvas(self, curva):
        Empresa_ID = self.obter_Empresa_ID(self.combo_empresa.get())

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
        self.curva_de_investimentos = self.Consulta_Prazo_Curvas(self.entry_investimento_curva_investimento.get()) 
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
        self.curva_de_adto = self.Consulta_Prazo_Curvas(self.entry_adto_parceiro_curva_adto.get()) 
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
        self.curva_de_vendas = self.Consulta_Prazo_Curvas(self.entry_vendas_curva.get()) 
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
        self.curva_de_projetos = self.Consulta_Prazo_Curvas(self.entry_projetos_curva_projeto.get()) 
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
        self.curva_de_mkt = self.Consulta_Prazo_Curvas(self.entry_mkt_curva_mkt.get()) 
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
        self.curva_de_obras = self.Consulta_Prazo_Curvas(self.entry_obras_curva_obras.get()) 
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

        self.curva_de_financiamento = self.Consulta_Prazo_Curvas(self.entry_financiamento_curva_liberacao.get()) 
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
        self.entry_informacoes_maps.delete(0, 'end')
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
        text = f"{valor:_.0f}"
        text = text.replace('.', ',').replace('_', '.')
        text = text + 'º mês'
        return text

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

    def format_custo_projetos(self, event):
        if self.entry_projetos_per_obra.get() != '':
            custo_obra = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
            per_custo_projeto = float(self.entry_projetos_per_obra.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_projeto = custo_obra * per_custo_projeto
            
            custo_projeto = self.format_valor_fx(custo_projeto)
            self.entry_projetos_valor_total.delete(0, "end")
            self.entry_projetos_valor_total.insert(0, custo_projeto)
    
    def format_custo_mkt(self, event):
        if self.entry_mkt_per_vgv.get() != '':
            vgv_bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
            per_custo_mkt = float(self.entry_mkt_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_mkt = vgv_bruto * -per_custo_mkt
            
            custo_mkt = self.format_valor_fx(custo_mkt)
            self.entry_mkt_valor_total.delete(0, "end")
            self.entry_mkt_valor_total.insert(0, custo_mkt)

    def format_custo_overhead(self, event):
        if self.entry_overhead_per_vgv.get() != '':
            vgv_bruto = float(self.entry_dre_vgv_bruto.get().replace('.', '').replace(',', '.')[:15])
            per_custo_overhead = float(self.entry_overhead_per_vgv.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_overhead = vgv_bruto * -per_custo_overhead
            
            inicio_vendas = float(self.entry_vendas_inicio.get().replace('º mês', '').replace('.', '').replace(',', '.')[:15]) # tirar caracteres
            prazo_da_curva = self.Consulta_Prazo_Curvas(self.entry_vendas_curva.get()) # fazer função para buscar curvas
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

    def format_custo_obras(self, event):
        if self.entry_obras_valor_m2.get() != '':
            custo_m2 = float(self.entry_obras_valor_m2.get().replace('.', '').replace(',', '.')[:15])
            area_empreendimento = float(self.entry_area_aproveitado.get().replace(' m²', '').replace('.', '').replace(',', '.')[:15])
            custo_obra = area_empreendimento * -custo_m2
                        
            custo_obra = self.format_valor_fx(custo_obra)
            self.entry_obras_valor_total.delete(0, "end")
            self.entry_obras_valor_total.insert(0, custo_obra)
    
    def format_custo_posobras(self, event):
        if self.entry_pos_obras_per_obras.get() != '':
            custo_obras = float(self.entry_obras_valor_total.get().replace('.', '').replace(',', '.')[:15])
            per_custo_posobras = float(self.entry_pos_obras_per_obras.get().replace("%", "").replace(",", ".")[:7]) / 100
            custo_posobras = custo_obras * per_custo_posobras
                        
            custo_posobras = self.format_valor_fx(custo_posobras)
            
            self.curva_de_obras = self.Consulta_Prazo_Curvas(self.entry_obras_curva_obras.get()) 
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

    def format_custo_admobras(self, event):
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
    
    def format_dre(self, event):
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
            messagebox.showinfo('% Urbanizador', 'Percentual Não pode ser Maio que 100%!!!!')
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

    def button_maps(self, janela, coordenadas_relx, coordenadas_rely, coordenadas_relwidth, coordenadas_relheight, tipo):
        self.btn_consultar = customtkinter.CTkButton(janela, text='Maps',fg_color='transparent', text_color="black", command=self.Acessar_Maps)  # Tamanho desejado
        self.btn_consultar.pack()
        self.btn_consultar.place(relx=coordenadas_relx, rely=coordenadas_rely, relwidth=coordenadas_relwidth, relheight=coordenadas_relheight)

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
            
            ID_Empresa = self.obter_Empresa_ID(self.combo_empresa.get())
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

    def obter_Empresa_ID(self, Empresa_DS):
        if Empresa_DS !='':
            id_empresa = self.empresas_dict.get(Empresa_DS)  # Obtenha o ID correspondente
            if id_empresa:
                return id_empresa
            else:
                messagebox.showinfo('Gestor Negócios', 'Erro - Empresa Incorreta, selecione novamente!!!')
                return None
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Empresa em Branco!!!')
            return

    def obter_Unidade_ID(self, Unidade_DS):
        id_unidade = self.unidade_negocios_dict.get(Unidade_DS)  # Obtenha o ID correspondente
        if id_unidade:
            return id_unidade
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Unidade de Negócio em Branco ou Incorreta!!!')
        return None
    
    def obter_FormaLiquidacao_ID(self, FormaLiquidacao_DS):
        id_formaliquidacao = self.tpo_pagto_dict.get(FormaLiquidacao_DS)  # Obtenha o ID correspondente
        if id_formaliquidacao:
            return id_formaliquidacao
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Meio de Pagamento em Branco ou Incorreto!!!')
        return None
    
    def obter_Frete_DS(self, Frete_ID):
        ds_frete = self.frete_dict_1.get(Frete_ID)  # Obtenha o ID correspondente
        if ds_frete:
            return ds_frete
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Frete em Branco ou Incorreto!!!')
        return None

    def obter_Frete_ID(self, Frete_DS):
        id_frete = self.frete_dict.get(str(Frete_DS))  # Obtenha o ID correspondente
        if id_frete:
            return id_frete
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Tipo de Frete em Branco ou Incorreto!!!')
        return None
    
    def obter_Centro_ID(self, Centro_DS):
        id_centro = self.centro_dict.get(Centro_DS)  # Obtenha o ID correspondente
        if id_centro:
            return id_centro
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Centro de Resultado em Branco ou Incorreto!!!')
        return None
    
    def obter_Spead_ID(self, Spead_DS):
        id_spead = self.produto_dict.get(Spead_DS)  # Obtenha o ID correspondente
        if id_spead:
            return id_spead
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Spead em Branco ou Incorreto!!!')
        return None
    
    def obter_UnidadeMedida_ID(self, UnidadeMedida_DS):
        id_unidademedida = self.unidade_medida_dict.get(UnidadeMedida_DS)  # Obtenha o ID correspondente
        if id_unidademedida:
            return id_unidademedida
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Unidade Medida em Branco ou Incorreto!!!')
        return None
    
    def obter_Produto_ID(self, Produto_DS):
        id_produto = self.produto_dict.get(Produto_DS)  # Obtenha o ID correspondente
        if id_produto:
            return id_produto
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Produto em Branco ou Incorreto!!!')
        return None
    
    def obter_Natureza_ID(self, Natureza_DS):
        id_natureza = self.natureza_dict.get(Natureza_DS)  # Obtenha o ID correspondente
        if id_natureza:
            return id_natureza
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Natureza Financeira em Branco ou Incorreto!!!')
        return None
    
    def obter_Pessoa_ID(self, Pessoa_DS):
        id_pessoa = self.nome_pessoa_dict.get(Pessoa_DS)  # Obtenha o ID correspondente
        if id_pessoa:
            return id_pessoa
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Cliente/Fornecedor em Branco ou Incorreto!!!')
        return None
    
    def obter_municipio_IBGE(self, Municipio_DS):
        id_municipio = self.municipios_dict.get(Municipio_DS)  # Obtenha o ID correspondente
        if id_municipio:
            return id_municipio
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Município em Branco ou Incorreto!!!')
        return None

    def obter_banco(self, Banco_DS):
        id_banco = self.bancos_dict.get(Banco_DS)  # Obtenha o ID correspondente
        if id_banco:
            return id_banco
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Banco em Branco ou Incorreto!!!')
        return None

    def obter_Orc_ID(self, Orc_DS):
        id_orc = self.orcamentos_dict.get(Orc_DS)  # Obtenha o ID correspondente
        if id_orc:
            return id_orc
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Orcamento em Branco ou Incorreto!!!')
        return None

    def obter_Orc_Item_ID(self, Orc_Item_DS):
        id_item_preco = self.item_precos_orcamentos_dict.get(Orc_Item_DS)  # Obtenha o ID correspondente
        if id_item_preco:
            return id_item_preco
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Item em Branco ou Incorreto!!!')
            return
        return None

    def obter_Periodicidade_ID(self, Periodicidade_DS):
        id_periodicidade = self.periodicidades_dict.get(Periodicidade_DS)  # Obtenha o ID correspondente
        if id_periodicidade:
            return id_periodicidade
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Periodicidade em Branco ou Incorreto!!!')
        return None
    
    def obter_Indice_ID(self, Idx_DS):
        id_idx = self.idx_dict.get(Idx_DS)  # Obtenha o ID correspondente
        if id_idx:
            return id_idx
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Índice em Branco ou Incorreto!!!')
        return None

    def obter_Nat_Gerencial_ID(self, DS_Nat_Gerencial):
        id_natureza_gerencial = self.natureza_gerencial_dict.get(DS_Nat_Gerencial)  # Obtenha o ID correspondente
        if id_natureza_gerencial:
            return id_natureza_gerencial
        else:
            messagebox.showinfo('Gestor Negócios', 'Erro - Natureza Gerencial em Branco ou Incorreto!!!')
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

    def atualizar_empresas(self, event, target):
        self.empresas = self.get_empresas()
        self.empresas_dict = {nome: id for id, nome in self.empresas}
        self.empresas = [empresa[1] for empresa in self.empresas]
        target.set_completion_list(self.empresas)

    def atualizar_tpo_projeto(self, event, target):
        self.tpo_projeto = self.get_tpo_projetos()
        self.tpo_projeto_dict = {nome: id for id, nome, imposto in self.tpo_projeto}
        self.impostos = [aliquota['Per_Imposto'] for aliquota in self.tpo_projeto]
        self.tpo_projeto = [(tpo_projeto['Tipo_Empreendimento']) for tpo_projeto in self.tpo_projeto]
        target.set_completion_list(self.tpo_projeto)
    
    def atualizar_tpo_pagto(self, event, target):
        self.tpo_pagto = self.get_tpo_pagto()
        self.tpo_pagto_dict = {nome: id for id, nome in self.tpo_pagto}
        self.tpo_pagto = [tpo_pagto[1] for tpo_pagto in self.tpo_pagto]
        target.set_completion_list(self.tpo_pagto)
    
    def atualizar_produto_fx(self, Empresa_DS):
        self.produtos = self.get_produtos(Empresa_DS)
        self.produto_dict = {nome: id for id, nome, tpo in self.produtos}
        self.produtos = [produto[1] for produto in self.produtos]

    def atualizar_produto(self, event, Empresa_DS, target):
        self.produtos = self.get_produtos(Empresa_DS)
        self.produto_dict = {nome: id for id, nome, tpo in self.produtos}
        self.produtos = [produto[1] for produto in self.produtos]
        target.set_completion_list(self.produtos)
    
    def atualizar_natureza_financeira(self, event, Empresa_DS, target):
        self.natureza_financeira = self.get_natureza_financeira(Empresa_DS)
        self.natureza_dict = {nome: id for id, nome, tpo in self.natureza_financeira}
        self.natureza_financeira = [natureza[1] for natureza in self.natureza_financeira]
        target.set_completion_list(self.natureza_financeira)
    
    def atualizar_natureza_gerencial(self, event, target):
        self.natureza_gerencial = self.get_natureza_gerencial()
        self.natureza_gerencial_dict = {nome: id for id, nome in self.natureza_gerencial}
        if self.natureza_gerencial and isinstance(self.natureza_gerencial[0], tuple):
           self.natureza_gerencial = [item[1] for item in self.natureza_gerencial]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.natureza_gerencial, key=str.lower))  # Ordena e configura
    
    def atualizar_centro_resultado(self, event, Empresa_DS, target):
        self.centro_resultado = self.get_centrosresultados(Empresa_DS)
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
        ID_Empresa = self.obter_Empresa_ID(entry_empresa)
        self.nome_cenario = self.get_nome_cenario(ID_Empresa, entry_municipio, entry_uf, entry_tpo_projeto)
        completion_list = [area['Nome_da_Area'] for area in self.nome_cenario]
        target.set_completion_list(completion_list)
    
    def atualizar_curvas(self, event, target):
        Empresa_ID = None  # Initialize to None
        if hasattr(self, 'entry_empresa') and self.entry_empresa is not None:
            Empresa_ID = self.obter_Empresa_ID(self.entry_empresa.get())
        elif hasattr(self, 'combo_empresa') and self.combo_empresa is not None:
            Empresa_ID = self.obter_Empresa_ID(self.combo_empresa.get())
            
        if Empresa_ID is not None:
            self.nome_curva = self.get_nome_curvas(Empresa_ID)
            completion_list = [curva['Nome_Curva'] for curva in self.nome_curva]
            target.set_completion_list(completion_list)
        else:
            messagebox.showinfo('Gestor Negócios', 'Empresa não foi encontrada. Verifique se combo_empresa ou entry_empresa estão disponíveis.')
    
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

    def atualizar_status(self, event, Empresa_DS, target):
        Empresa_ID = self.obter_Empresa_ID(Empresa_DS)
        self.status = self.get_status(Empresa_ID)
        target.set_completion_list(self.status)
    
    def atualizar_orcamentos(self, event, entry_empresa, target):
        Empresa_ID = self.obter_Empresa_ID(entry_empresa)
        self.orcamentos = self.get_orcamentos(Empresa_ID)
        self.orcamentos_dict = {nome: id for id, nome in self.orcamentos}
        if self.orcamentos and isinstance(self.orcamentos[0], tuple):
            self.orcamentos = [item[1] for item in self.orcamentos]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.orcamentos, key=str.lower))  # Ordena e configura
    
    def atualizar_item_precos_orcamentos(self, event, entry_empresa, entry_orc, target):
        Empresa_ID = self.obter_Empresa_ID(entry_empresa)
        Orc_ID = self.obter_Orc_ID(entry_orc)
        self.item_precos_orcamentos = self.get_precos_orc(Empresa_ID, Orc_ID)
        self.item_precos_orcamentos_dict = {nome: id for id, nome in self.item_precos_orcamentos}
        if self.item_precos_orcamentos and isinstance(self.item_precos_orcamentos[0], tuple):
            self.item_precos_orcamentos = [item[1] for item in self.item_precos_orcamentos]  # Extrai o nome do orçamento

        target.set_completion_list(sorted(self.item_precos_orcamentos, key=str.lower))  # Ordena e configura

class Icons():
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
        self.btsave_base64 = "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"
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
    
    def get_natureza_financeira(self, Empresa_DS):
        Empresa_ID = self.obter_Empresa_ID(Empresa_DS)
        strSql = """SELECT 
                        nt.Nat_ID           AS Codigo, 
                        nt.Nat_Descricao    AS Nome, 
                        nt.Nat_Tipo         AS Tpo 
                        FROM TB_Natureza nt
                    WHERE 
                        nt.Nat_Tipo='A'
                        AND nt.Empresa_ID=%s
                    ORDER BY Nome"""
    
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
    def get_produtos(self, Empresa_DS):
        Empresa_ID = self.obter_Empresa_ID(Empresa_DS)
        strSql = """SELECT 
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
                    WHERE usr.Usr_Login= %s ORDER BY emp.Pri_Descricao"""
            
            myresult = db.executar_consulta(strSqL, UserName)

        empresas = [(empresa['Pri_Cnpj'], empresa['Pri_Descricao']) for empresa in myresult]
        
        return empresas
    
    # Drop Empresa
    def get_pessoas(self, entry_empresa):
        Empresa_ID = self.obter_Empresa_ID(entry_empresa)
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
    def get_centrosresultados(self, Empresa_DS):
        Empresa_ID = self.obter_Empresa_ID(Empresa_DS)
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
        WHERE Empresa_ID='{str(ID_Empresa)}' ORDER BY Status_Order"""

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
    def get_unegocios(self, entry_empresa):
        Empresa_ID = self.obter_Empresa_ID(entry_empresa)
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
    def get_orcamentos(self, entry_empresa):
        Empresa_ID = entry_empresa
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
    def get_precos_orc(self, entry_empresa, entry_orc_id):
        Empresa_ID = entry_empresa
        Orc_ID =  entry_orc_id
        conditions = []  # Lista para armazenar as condições
        conditions.append("Empresa_ID = %s ")
        params = [Empresa_ID]

        if entry_orc_id != '':
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
        return myresult
    
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
