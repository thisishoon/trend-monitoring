import threading
import requests
import logging
import pprint
from .collect import collect_ranking, collect_news
from .es_module import insert_to_es, insert_es_bulk
from .check import check_category
from .extract import extract_keyword_textrank, make_news_contents
from datetime import datetime


def run(elastic_search=False):
    date = datetime.utcnow()
    ranking = collect_ranking()
    docs = []

    for rank, word in enumerate(ranking):
        print(str(rank + 1) + '   collecting')
        category, related_search_word = check_category(word)
        news_titles, news_links = collect_news(word)
        news_contents = make_news_contents(word, news_links)
        related_keyword = extract_keyword_textrank(news_contents)

        doc = make_document(rank, word, category, related_search_word, related_keyword, news_titles[0], date)

        docs.append(doc)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(docs)

    if elastic_search:
        insert_es_bulk(docs, index_name='trend', path=elastic_search)

    return docs


def repeat(elastic_search=False, interval_second=600):
    logging.basicConfig(filename='./error.log', level=logging.ERROR)
    timer = threading.Timer(interval_second, repeat, args=[elastic_search, interval_second])
    timer.start()

    try:
        run(elastic_search)
    except Exception as e:
        logging.error(str(e))
    except (requests.exceptions.RequestException, ConnectionResetError) as e:
        logging.error(str(e))

    return timer, timer.is_alive()


def make_document(rank, word, category, related_search_word, related_keyword, news_titles, date):
    doc = dict()

    doc['ranking'] = rank + 1
    doc['word'] = word
    doc['category'] = category
    doc['related_search_word'] = related_search_word
    doc['related_keyword'] = related_keyword
    doc['news_title'] = news_titles[0]
    doc['timestamp'] = date
    doc['score'] = (10 - rank) * 10

    return doc
