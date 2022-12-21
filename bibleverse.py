import requests 
from bs4 import BeautifulSoup

url = "https://dailyverses.net/random-bible-verse"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

bible_verses = soup.findAll('span', attrs={"class":"v1"})
for verse in bible_verses:
    print(verse.text)


