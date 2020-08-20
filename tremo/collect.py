import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def collect_ranking():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'
    result = []
    ranking = crawling(url, 'span.item_title')
    
    for word in ranking[0:10]:
        result.append(word.text)

    return result


def collect_news(word):
    news_url = "https://search.naver.com/search.naver?where=news&query=" + word
    news = crawling(news_url, 'ul.type01 > li')

    news_titles = []
    news_links = []

    for new in news[0:5]:
        title = new.select_one("a._sp_each_title").text
        link = new.select_one("a")['href']
        news_titles.append(title)
        news_links.append(link)

    return news_titles, news_links


def crawling(url, selector):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.select(selector)
    return result
