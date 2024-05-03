from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

 

url = 'https://www.webull.com/quote/crypto'

# Request in case 404 Forbidden error

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url,headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')

name_i = 0
sym_i = 1
i = 2

data = soup.findAll("div",attrs={"class": "table-cell"})
data_name= soup.findAll("p",attrs={"class":"tit bold"})
data_sym = soup.findAll("p",attrs={"class":"txt"})

 

for crypto in range(0,5):
    name = data_name[name_i].text
    symbol = data_sym[sym_i].text.replace("USD","")
 
 
    price = data[i].text
    per_change = data[i+1].text
    clean_price = float(price.replace(',',''))
    cor_price = data[i+3].text

 
    name_i += 1
    sym_i += 2
    i += 10


    print('Rank:', name_i)
    print('Name:', name)
    print('Symbol:', symbol)
    print('Current price: $', price, sep='')
    print('Percent of change in the last 24 hrs:', per_change) 
    print('Corresponding price: $', cor_price, sep='')
    print()