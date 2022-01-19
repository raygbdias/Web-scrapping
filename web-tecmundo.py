from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://www.tecmundo.com.br/busca?q=jogos")
bs = BeautifulSoup(url, 'html.parser')

dados = bs.find_all('h2', {'class':'tec--card__title'})
#print (dados)
for i in dados:
    nomes = i.findChildren("a")
    print(nomes[0].text)
    link = i.findChildren("a")
    print(link[0]["href"] )
    
    url = urlopen(link[0]["href"])
    bs = BeautifulSoup(url, 'html.parser')
    data = bs.find_all('div', {'class':'tec--article__body-grid'})
    print (data)
    