#### LIBRARIES ####

import pandas as pd
import numpy as np
from openpyxl import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

#### WEBSCRAPPING ####

url = "https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/TaxasJurosMensalPorMes?$top=100&$format=json&$select=Modalidade,InstituicaoFinanceira,TaxaJurosAoAno,anoMes"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

base = pd.read_json(url)

base1 = pd.json_normalize(base['value'])
baseFinal = pd.DataFrame(base1)
#teste = baseFinal.loc[baseFinal["InstituicaoFinanceira"] == "CAIXA ECONOMICA FEDERAL"]

#### FORM ####

BankList = list(["NENHUM"])
BankList1 = list(set(baseFinal["InstituicaoFinanceira"]))
BankList.extend(BankList1)
BankList.sort()
#BankList = dict.fromkeys(BankList)

MethodList = list(["NENHUM"])
MethodList1 = list(set(baseFinal["Modalidade"]))
MethodList.extend(MethodList1)
#MethodList = dict.fromkeys(BankList)

class financiamento:

    def __init__(self):
    
        root = Tk()
        root.geometry('600x650')

        self.v = StringVar()
        self.x = StringVar()
        self.y = StringVar()
        self.z = StringVar()
        self.p = StringVar()
        self.t = StringVar()
        self.TaxaJurosAno = StringVar()
        self.ParcelasTotal = StringVar()
        self.FinanciamentoTotal = StringVar()

        root.title('Simulador de Financiamento Habitacional')
        Label(root, text = "Método de Cálculo").pack(anchor=W, pady = 5, padx = 10)
        Radiobutton(root, text='SAC', variable=self.v, value="SAC", tristatevalue=0).pack(anchor=W, padx = 10)
        Radiobutton(root, text='PRICE', variable=self.v, value="PRICE", tristatevalue=0).pack(anchor=W,pady = 5, padx = 10)
        Label(root, text = "Banco").pack(anchor=W, pady = 5, padx = 10)
        ttk.Combobox(root,values = BankList, textvariable=self.x, width = 300).pack(anchor=W,pady = 5, padx = 10)
        Label(root, text = "Modelo de Cáclulo").pack(anchor=W, pady = 5, padx = 10)
        ttk.Combobox(root,values = MethodList, textvariable=self.y, width = 300).pack(anchor=W,pady = 5, padx = 10)
        Label(root, text = "Taxa de Juros (formato 0.00)").pack(anchor=W, pady = 5, padx = 10)
        Entry(root, textvariable = self.z).pack(anchor=W, pady = 5, padx = 10)
        Label(root, text = "Montante a ser Captado").pack(anchor=W, pady = 5, padx = 10)
        Entry(root, textvariable = self.p).pack(anchor=W, pady = 5, padx = 10)
        Label(root, text = "Meses de Duração do Financiamento").pack(anchor=W, pady = 5, padx = 10)
        Entry(root, textvariable = self.t).pack(anchor=W, pady = 5, padx = 10)
        Label(root, text = "Taxa de Juros Anual").pack(anchor=W, pady = 5, padx = 10)
        TaxaJuros = Label(root, textvariable = self.TaxaJurosAno).pack(anchor=W, pady = 5, padx = 10)
        Label(root, text = "Primeira Parcela").pack(anchor=W, pady = 5, padx = 10)
        ParcelaMensal = Label(root, textvariable = self.ParcelasTotal).pack(anchor=W, pady = 5, padx = 10)
        Label(root, text = "Total do Financiamento").pack(anchor=W, pady = 5, padx = 10)
        FinanciamentoValor = Label(root, textvariable = self.FinanciamentoTotal).pack(anchor=W, pady = 5, padx = 10)
                        # create the button
        btCalcularPagamento = Button(root, text = "Calcular",
                                          command = self.CalcularPagamento).pack()
        root.mainloop()

#### CALCULOS ####

    def CalcularPagamento(self):

        calculo = self.v.get()
        banco = self.x.get()
        metodo = self.y.get()

        if banco == "NENHUM":
            juros = float(self.z.get())
        else:
            juros = baseFinal.loc[(baseFinal["InstituicaoFinanceira"] == banco) & 
                                  (baseFinal["Modalidade"] == metodo) & 
                                  (baseFinal["anoMes"] == max(baseFinal.anoMes))]
            juros = float(juros.TaxaJurosAoAno)/100

        total = int(self.p.get())
        meses = int(self.t.get())



    #total = float(250000)
    #meses = int(420)
    #juros = float(0.0941)
        juros_mes = (1+juros)**(22/252)-1
        if calculo == "PRICE":
            parcela = total*((1+juros_mes)**meses*juros_mes/((1+juros_mes)**meses-1))
        elif calculo == "SAC":
            parcela = total/meses + total*juros_mes

        info=pd.DataFrame([[banco], [metodo], [calculo], [total], [meses], [juros], [juros_mes], [parcela]],
                      index=["Banco", "Método de Cálculo", "Modelo de Cálculo", "Montante","Período","Juros Ano","Juros Mês","Parcela"],
                      columns=["Dados"])

        if calculo == "PRICE":
            data=[[0, total, total/meses, parcela, total*juros_mes, total-parcela+total*juros_mes]]
        elif calculo == "SAC":
            data=[[0, total, total/meses, total/meses + total*juros_mes, total*juros_mes, total-parcela+total*juros_mes]]

        tabela_price = pd.DataFrame(data,
                                    columns=["Periodo", 
                                             "Montante", 
                                             "Parcela", 
                                             "Amortizacao", 
                                             "Juros", 
                                             "Saldo_devedor"])

        for i in range(1,(meses+1)):
            if calculo == "PRICE":
                data=[{'Periodo': i,'Montante': total,'Parcela': total/meses,'Amortizacao': parcela,'Juros': juros_mes * tabela_price.iloc[i-1][5],'Saldo_devedor': tabela_price.iloc[i-1][5] + juros_mes * tabela_price.iloc[i-1][5] - parcela}]
                data=pd.DataFrame(data)
                tabela_price = pd.concat([tabela_price,data])
            elif calculo == "SAC":
                data=[{'Periodo': i,'Montante': total,'Parcela': total/meses,'Amortizacao': total/meses + juros_mes * tabela_price.iloc[i-1][5],'Juros': juros_mes * tabela_price.iloc[i-1][5],'Saldo_devedor': tabela_price.iloc[i-1][5] + juros_mes * tabela_price.iloc[i-1][5] - total/meses + juros_mes * tabela_price.iloc[i-1][5]}]
                data=pd.DataFrame(data)
                tabela_price = pd.concat([tabela_price,data])        
        
        Total_Financiamento = sum(tabela_price.Amortizacao)

        self.TaxaJurosAno.set('{:.1%}'.format(juros, '10.2f'))
        self.ParcelasTotal.set('R${:,.2f}'.format(parcela, '10.2f'))
        self.FinanciamentoTotal.set('R${:,.2f}'.format(Total_Financiamento, '10.2f'))

        with pd.ExcelWriter('output.xlsx') as writer:  
            info.to_excel(writer, sheet_name='Dados')
            tabela_price.to_excel(writer, sheet_name='Tabela')

financiamento()
