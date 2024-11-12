# SuperbowlChampion_stats.py

import requests
from bs4 import BeautifulSoup

# URL for Super Bowl Champions fetch from Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

# Make a GET request to fetch the page content
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the main stats table on the page
table = soup.find('table', class_='wikitable sortable')

if table:
    rows = table.find_all('tr')
    headers = [header.text.strip() for header in rows[0].find_all('th')]

    print("{:<10} {:<30} {:<15} {:<15} {:<30}".format(*headers))
    for row in rows[1:]:
        cols = [col.text.strip() for col in row.find_all('td')]
        if cols:
            print("{:<10} {:<30} {:<15} {:<15} {:<30}".format(*cols))
else:
    print("Could not find the table. The structure of the page may have changed.")