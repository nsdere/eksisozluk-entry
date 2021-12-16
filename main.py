import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

URL = "https://eksisozluk.com/isvicre--35513"
entries = []

# finding the max_page
page = requests.get(URL + "?p=" + str(1), headers={'User-Agent': 'Chrome'})
soup = BeautifulSoup(page.content, 'html.parser')
list = soup.find(class_='pager')
max_page = re.findall('"([^"]*)"', str(list))[2]

# scraping entries
for page in range(1, int(max_page)):
    page = requests.get(URL + "?p=" + str(page), headers={'User-Agent': 'Chrome'})
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find_all('div', class_='content')
    list_copy = list.copy()
    for l in list_copy:
        entries.append(l.get_text().rstrip().lstrip())

df = pd.DataFrame(entries)
df