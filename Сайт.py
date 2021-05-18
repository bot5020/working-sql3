import requests
from bs4 import BeautifulSoup as bea

s = requests.get("https://ria.ru/world/")
html = bea(s.content, 'html.parser')
tmp= html.find('a',attrs={'class' : 'list-item__title color-font-hover-only'})

print(tmp.text)
