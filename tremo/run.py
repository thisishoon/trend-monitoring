import threading
from .collect import collect_ranking, collect_news
from .esmodule import insert_to_es, insert_es_bulk
from .check import check_category
from .extract import extract_keyword_textrank, make_news_contents
from datetime import datetime


def run(elastic_search=True):
    date = datetime.utcnow()
    ranking = collect_ranking()
    docs = []

    for rank, word in enumerate(ranking):
        print(str(rank+1) + '   collecting')
        category, related_search_word = check_category(word)
        news_titles, news_links = collect_news(word)
        news_contents = make_news_contents(word, news_links)
        related_keyword = extract_keyword_textrank(news_contents)

        doc = dict()
        doc['ranking'] = rank + 1
        doc['word'] = word
        doc['category'] = category
        doc['related_search_word'] = related_search_word
        doc['related_keyword'] = related_keyword
        doc['news_title'] = news_titles[0]
        doc['timestamp'] = date
        doc['score'] = (10-rank)*10
        docs.append(doc)

    print(docs)

    if elastic_search:
        # insert_to_es(docs)
        insert_es_bulk(docs, index_name='trend')

    return docs


def repeat(elastic_search=True, interval_second=100):
    timer = threading.Timer(interval_second, repeat, args=[elastic_search, interval_second])
    timer.start()
    run(elastic_search)

    return timer, timer.is_alive()

