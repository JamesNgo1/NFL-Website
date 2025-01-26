import requests
from bs4 import BeautifulSoup as soup
import csv 
"""
Beautiful soup is used for parsing html or xml documents . It helps extract specific data web pages like
titles , linkes or any other HTML elements

"""


def scrape_url(url, header_rows , csv_file):

    page = requests.get(url)

    webpage = soup(page.content, features='html.parser')

    data_array = []

    # web scrape the web page URL , load in given array
    for row in webpage.tbody.find_all('tr'):
        cols = row.find_all('td')
        
        # Player name | Pass Yards | yds / att | att | cmp | cmp % | td | int | rate | 1st | 1st% | 20 yd plays | 40 yard plays | long pass play | sacks | sack yards

        # Loop through each <td> element to get the text (or you can process it as needed)
        data = []
        for col in cols:
        
            data.append(col.get_text().strip())

        data_array.append(data)
    
    for data in data_array:
        print(data)
        print()
    write_to_csv(header_rows,csv_file,data_array)



def write_to_csv(header_rows , csv_file , array_data):
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        file.write = csv.writer(file)

        file.write.writerow(header_rows)

        for row in array_data:
            file.write.writerow(row)