import requests
from bs4 import BeautifulSoup


HEADERS = {
    'Referer': 'https://www.naver.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
URL_RANKING = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'
URL_NEWS = 'https://search.naver.com/search.naver?where=news&query='
ELEMENT_RANKING = 'span.item_title'
ELEMENT_NEWS = 'ul.type01 > li'


def collect_ranking():
    result = []
    ranking = crawling(URL_RANKING, ELEMENT_RANKING)
    
    for word in ranking[0:10]:
        result.append(word.text)

    return result


def collect_news(word):

    news = crawling(URL_NEWS + word, ELEMENT_NEWS)
    news_titles = []
    news_links = []

    for new in news[0:5]:
        title = new.select_one("a._sp_each_title").text
        link = new.select_one("a")['href']
        news_titles.append(title)
        news_links.append(link)

    return news_titles, news_links


def crawling(url, selector):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.select(selector)
    return result
