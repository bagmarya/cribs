
import requests
import json
from bs4 import BeautifulSoup

page = requests.get('https://www.hitelectro.ru/catalog/Elektrika/Datchiki_dvijeniya/Svetilniki_ulichnyie_s_datchikami')
soup = BeautifulSoup(page.text, 'html.parser')
with open('page.html', 'w') as file:
    file.write(soup.prettify())
