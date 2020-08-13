import sys
import threading
from collect import collect_ranking, collect_news
from esmodule import insert
from check import check_category
from extract import extract_keyword_textrank, make_nouns_list
from datetime import datetime


def run(es_flag=True, interval_second=600):

    timer = threading.Timer(interval_second, run, args=[es_flag, interval_second])
    timer.start()

    date = datetime.utcnow()
    ranking = collect_ranking()
    docs = []

    for rank, word in enumerate(ranking):
        category, related_search_word = check_category(word)
        news_titles, news_links = collect_news(word)
        nouns_list = make_nouns_list(word, news_links)
        related_keyword = extract_keyword_textrank(nouns_list)

        doc = dict()
        doc['ranking'] = rank + 1
        doc['word'] = word
        doc['category'] = category
        doc['related_search_word'] = related_search_word
        doc['related_keyword'] = related_keyword
        doc['news_title'] = news_titles[0]
        doc['timestamp'] = date
        docs.append(doc)

    print(docs)

    if es_flag:
        insert(docs)

    return docs


if __name__ == '__main__':
    es_flag = True

    if len(sys.argv) > 1:
        es_flag = (sys.argv[1] != 'False')

    run(es_flag)



