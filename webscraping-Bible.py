import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


#webpage = 'https://ebible.org/asv/JHN{}'
random_chapter = random.randrange(1, 22)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else: 
    random_chapter = str(random_chapter)
print(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('span',class_='p')

print(page_verses)

