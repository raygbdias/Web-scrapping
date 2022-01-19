from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen("https://www.tecmundo.com.br/busca?q=jogos")
bs = BeautifulSoup(url, 'html.parser')

dados = bs.find_all('h2', {'class':'tec--card__title'})
print (dados)
for i in dados:
    filhas = i.findChildren("a")
    print(filhas[0])
  #  print(filhas[1])
  #  print(filhas[2])
