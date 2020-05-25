import peewee
import requests
import string
from bs4 import BeautifulSoup

from Model.Empresa import Empresa



def createTables():
    try:
        Empresa.create_table()
        print("Tabela Empresa Criada")
    except peewee.OperationalError:
        print("Table Empresa Já Existe")

def listaEmpresas():
    arrLetras = list(string.ascii_uppercase)
    arrNumeros = list(map(str, list(range(0, 10))))
    arrLetraNumero = arrLetras + arrNumeros
    urlPorLetra = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Letra="

    qtdTotalEmpresas = 0
    arrEmpresas = []
    for letraNumero in arrLetraNumero:
        url = urlPorLetra + str(letraNumero)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        lst1 = soup.find_all(class_ = "GridRow_SiteBmfBovespa GridBovespaItemStyle")
        lst2 = soup.find_all(class_ = "GridAltRow_SiteBmfBovespa GridBovespaAlternatingItemStyle")
        lstTotal = lst1 + lst2

        qtdEmpresasLetra = 0
        for empresa in lstTotal:
                qtdEmpresasLetra = qtdEmpresasLetra + 1
                qtdTotalEmpresas = qtdTotalEmpresas + 1
                result = {"razaoSocial": empresa.a.text,
                          "codigoCVM": empresa.a['href'].replace("ResumoEmpresaPrincipal.aspx?codigoCvm=", ""),
                          "link": empresa.a['href'],
                          "nomePregao": empresa.find_all("td")[1].text,
                          "segmento": empresa.find_all("td")[2].text.replace('\xa0', '')}
                arrEmpresas.append(result)

    return arrEmpresas


def coletaDadosEmpresa(codigoCVM):
    print(listaEmpresas())

def principal():
    listaEmpresa = listaEmpresas()
    qtdEmpresa = len(listaEmpresa)
    print("Total de Empresas: ", qtdEmpresa)
    cont = 0

    for emp in listaEmpresa:
        print("Salvando Empresa " + emp['razaoSocial'])

        objeEmp = Empresa()
        objeEmp.codigoCvm = emp['codigoCVM']
        objeEmp.razaoSocial = emp['razaoSocial']
        objeEmp.linkCadastroEmpresa = emp['link']
        objeEmp.nomePregao = emp['nomePregao']
        objeEmp.segmentoBolsa = emp['segmento']
        objeEmp.saveNotExists()
        cont = cont + 1
        print(str(cont) + " / " + str(qtdEmpresa))
#createTables()
principal()