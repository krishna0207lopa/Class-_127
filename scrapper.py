import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

star_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
request = requests.get(star_url)
print(request)

soup = BeautifulSoup(request.text, "html.parser")

star_table = soup.find("table")

temp_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_name = []
Distance = []
Mass = []
Radius = []
Luminosity = []

for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])

value = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius,Luminosity)),columns= ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(value)

value.to_csv("Stars_data.csv")