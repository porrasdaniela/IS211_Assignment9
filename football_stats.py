
# football_stats.py

import requests
from bs4 import BeautifulSoup

# URL for CBS stats page
url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2021-season-regular-category-touchdowns"

# Make a GET request to fetch the page content
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the main stats table on the page
table = soup.find('table', class_='TableBase-table')

# Extract and print the top 20 players stats
players = table.find_all('tr')[1:21]

# Print the header for the table
print("{:<25} {:<20} {:<10} {:<15}".format('Player', 'Position', 'Team', 'Touchdowns'))

# Loop through the players and extract relevant details
for player in players:
    stats = player.find_all('td')

    if len(stats) >= 4:
        player_number = stats[0].text.strip()
        team = stats[1].text.strip()
        position_and_name = stats[2].text.strip()
        touchdowns = stats[3].text.strip()

        # separating the position and name
        if 'QB' in position_and_name:
            position = 'QB'
            name = position_and_name.replace('QB', '').strip()
        elif 'RB' in position_and_name:
            position = 'RB'
            name = position_and_name.replace('RB', '').strip()
        elif 'WR' in position_and_name:
            position = 'WR'
            name = position_and_name.replace('WR', '').strip()
        else:
            position = 'Unknown'
            name = position_and_name.strip()

        # Print the player data with proper formatting
        print("{:<25} {:<20} {:<10} {:<15}".format(name, position, team, touchdowns))