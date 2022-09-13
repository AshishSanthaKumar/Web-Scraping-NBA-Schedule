from bs4 import BeautifulSoup
import requests

url = 'https://www.basketball-reference.com/leagues/NBA_2023_games-october.html'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

october = soup.find('tbody')
match = october.find('tr')
match_day = match.find('th').text
match_time = match.find('td').text
visiting_team = match.find('td', class_='left').text

print(match_day, match_time, visiting_team)
