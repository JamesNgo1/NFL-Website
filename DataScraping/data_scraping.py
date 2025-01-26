import requests
from bs4 import BeautifulSoup as soup
import csv 

"""
Beautiful soup is used for parsing html or xml documents . It helps extract specific data web pages like
titles , linkes or any other HTML elements

"""


passing_qb_page = requests.get('https://www.nfl.com/stats/player-stats/')


""" convert to beautiful soup object """
webpage = soup(passing_qb_page.content, features='html.parser')

passing_qb_data = []

for row in webpage.tbody.find_all('tr'):
    cols = row.find_all('td')
    
    # Player name | Pass Yards | yds / att | att | cmp | cmp % | td | int | rate | 1st | 1st% | 20 yd plays | 40 yard plays | long pass play | sacks | sack yards

    # Loop through each <td> element to get the text (or you can process it as needed)
    data = []
    for col in cols:
       
        data.append(col.get_text().strip())

    finalData.append(data)

#print(len(finalData))
print(finalData)

qb_passing_file = 'qbPassing'

for row in finalData:
    print(row)
    print()






