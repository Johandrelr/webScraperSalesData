# Scipt to test scraping method for properties for sales https://nye.obos.no/
# The script scrapes data per building of a project
# find project -> Housing selector -> choose building -> look for iframe link in devTools
# v2 does not handle buildings sold out or still to be lauched.

import bs4 
from selenium import webdriver
import time
import pandas as pd

webDriverPath = '\\chromedriver\\chromedriver.exe'
dataFrames = []
buildings = []


# build a class for storing building data (buildings to be scraped)
class building:
    def __init__(self, projectName, buildingName, url) -> None:
        self.projectName = projectName
        self.buildingName = buildingName
        self.url = url
    def setdf(self,df):
        self.df = df


# create list of buildings from CSV
urls = pd.read_csv('CSV Input\\urlsList_Obos.csv')

# itterate through csv and create buildings
for x in urls.index: 
    buildings.append(building(urls['projectName'][x],urls['buildingName'][x],urls['url'][x]))


# function to Create tables from urls
def getTableFromUrl(building):
    url = building.url
    driver = webdriver.Chrome(webDriverPath)
    driver.get(url)
    time.sleep(5)   # need a better solution then this 
    
    html = driver.page_source
    
    soup = bs4.BeautifulSoup(html,'html.parser')
    
    tables = soup.find_all('table')
    
    df1 = pd.read_html(str(tables[0]),flavor='html5lib')
    df1 = df1[0]
    df1['Building Name'] = building.buildingName
    return df1
    
# loop through buildings and scrape tables from url
for j in range(len(buildings)):
    buildings[j].setdf(getTableFromUrl(buildings[j]))


# merge data frames and export to 1 csv
dfs = []
for k in range(len(buildings)):
    dfs.append(buildings[k].df)

# Combine data frames and add date and time of scraped data
appended_data = pd.concat(dfs)
appended_data['Date-Time'] = pd.Timestamp.today()

# export to csv and add date to the name
appended_data.to_csv('CSV Output\\obosScrapedData' + '_'+str(pd.Timestamp.today().strftime('%Y-%m-%d'))+'.csv')


