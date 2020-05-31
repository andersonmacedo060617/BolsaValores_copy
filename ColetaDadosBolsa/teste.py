from bs4 import BeautifulSoup
import requests
import re

page = requests.get("http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Letra=A")
soup = BeautifulSoup(page.content, 'html.parser')
teste = soup.find_all(class_ = "GridRow_SiteBmfBovespa GridBovespaItemStyle")
teste2 = soup.find_all(class_ = "GridAltRow_SiteBmfBovespa GridBovespaAlternatingItemStyle")
teste3 = teste + teste2
print(len(teste3))

for empresa in teste3:
    #print(empresa.find_all("td"))
    result = {"razaoSocial": empresa.a.text, "codigoCVM": empresa.a['href'].replace("ResumoEmpresaPrincipal.aspx?codigoCvm=", ""),
              "nomePregao": empresa.find_all("td")[1].text, "segmento": empresa.find_all("td")[2].text.replace('\xa0', '')}
    print(empresa)