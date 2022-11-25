import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://vy-homefinder.herokuapp.com/embed/ygjLxNggKLyT8WEs5?initialWidth=556&childId=homefinder-frame&parentTitle=Ulvenkroken%2C%20salgstrinn%202%20%7C%20OBOS&parentUrl=https%3A%2F%2Fnye.obos.no%2Fny-bolig%2Fboligprosjekter%2Foslo%2Fbjerke%2Fulvenkroken%2Fulvenkroken-salgstrinn-2%2F'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print(page.status_code)


# print('Classes of each table:')
# for table in soup.find_all('table'):
#     print(table.get('class'))

tables = soup.find_all('table')

df1 = pd.read_html(str(tables[0]),flavor='html5lib')
df1 = df1[0]

print(df1)

