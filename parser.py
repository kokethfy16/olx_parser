from bs4 import BeautifulSoup  
import requests

def parse():
    url = 'https://www.olx.ua/elektronika/telefony-i-aksesuary/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    new_news = []
    news = []

    news = soup.findAll('a', class_='marginright5 link linkWithHash detailsLink linkWithHashPromoted')

    for i in range(len(news)):
    	if news[i].find('strong') is not None:
        	new_news.append(news[i].text)
    
    for item in new_news:
    	print(f'{item}')

parse()


