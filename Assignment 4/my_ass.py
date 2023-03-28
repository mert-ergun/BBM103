import requests

url = 'https://piazza.com/class/l8eydbtphjf56m/post/38'
response = requests.get(url)
html = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table')

sum = 0
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        sum += int(cell.text)
    
print(sum)