import requests
from bs4 import BeautifulSoup
from datetime import datetime
from check import check_category

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


def collect_ranking():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'

    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('span.item_title')

    now = datetime.now()

    print(now.year, now.month, now.day, now.hour, now.minute)

    for i in range(0, 10):
        item = data[i].get_text()

        print(i + 1, item)
        result = check_category(item)
        print("유형", result[0])
        print("연관검색어", result[1])

        collect_news(item)


def collect_news(item):
    news_url = "https://search.naver.com/search.naver?where=news&query=" + item
    news_res = requests.get(news_url, headers=HEADERS)
    soup = BeautifulSoup(news_res.text, 'html.parser')

    news = soup.select("ul.type01 > li")
    print("--------------")
    for new in news[0:3]:
        title = new.select_one("a._sp_each_title").text

        # source = new.select_one("span._sp_each_source").text
        # time = new.select_one("dd.txt_inline").select_one("span.bar").next_sibling
        # time = str(time)[1:-1]

        print(title)

    print("--------------")
