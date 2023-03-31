from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    #DIA MES DE REFERENCIA
def dmreferenciatrue(data):
    converDate = datetime.strptime(data, "%Y-%m-%d")
    converstr = datetime.strftime(converDate, "%d/%m/%Y")
    return converstr

def dmreferenciafalse(data):
    converDate = datetime.strptime(data, "%Y-%m-%d")
    converstr = datetime.strftime(converDate, "%B/%Y")
    return converstr


    # VLR TOTAL EM US
def valorus(value):
    valorformatado = 'US '+ locale.currency(float(value), symbol=False, grouping=True)
    return valorformatado


     # VALOR TOTAL MENSAL
def valormes(value):
    valorformatado = locale.currency(float(value), grouping=True)
    return valorformatado


    # DATA PROCESSADA
def dataProcessada(data):
    convDate = "{dia}/{mes}/{ano} - {hora}".format(
    dia=data[8:10],
    mes=data[5:7],
    ano=data[0:4],
    hora=data[11:16])
    return convDate

    # REGRA DE COBRANÇA
def regra_cobranca(value):
    if value == True:
        return 'APLICADA'
    else:
        return 'NÃO APLICADA'
