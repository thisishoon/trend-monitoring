import requests
from bs4 import BeautifulSoup
from datetime import datetime
from newspaper import Article
from check import check_category
from extract import extract_related_keyword

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def collect_ranking():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'
    date = datetime.utcnow()
    dicts = []

    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('span.item_title')

    for i in range(0, 10):
        dict = {}
        word = data[i].get_text()

        result = check_category(word)

        main_title, news_links = collect_news(word)
        related_keyword = extract_related_keyword(word, news_links)


        dict['ranking'] = i+1
        dict['word'] = word
        dict['category'] = result[0]
        dict['related_word'] = result[1]
        dict['keyword'] = []
        dict['news_title'] = main_title
        dict['timestamp'] = date
        dicts.append(dict)

    return dicts

def collect_news(word):
    news_url = "https://search.naver.com/search.naver?where=news&query=" + word
    news_res = requests.get(news_url, headers=HEADERS)
    soup = BeautifulSoup(news_res.text, 'html.parser')

    news = soup.select("ul.type01 > li")
    main_title = news[0].select_one("a._sp_each_title").text
    news_links = []
    print("--------------")
    for new in news[0:3]:
        title = new.select_one("a._sp_each_title").text
        link = new.select_one("a")['href']
        news_links.append(link)

    return main_title, news_links
