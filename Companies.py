from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find('table')

soup.find_all('table')

soup.find_all('table')[1]

# soup.find('table', class_ = 'wikitable sortable')

soup.find('table', class_ = 'wikitable sortable jquery-tablesorter')


table = soup.find_all('table')[1]

print(table)

world_titles = table.find_all('th')

world_titles

world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)

import pandas as pd

df = pd.DataFrame(columns = world_table_titles)

df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data
    
df 

df.to_csv(r'C:\Users\myamy\OneDrive\Documents\Web_scraping_output\Companies_1.csv', index = False)
