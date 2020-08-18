import requests
from elasticsearch import Elasticsearch
from datetime import datetime
from tremo.esmodule import insert_to_es


def test_connect_naver_datalab():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    res = requests.get(url, headers=HEADERS)
    assert res.status_code == 200


def test_connect_es():
    docs = list()
    docs.append({'author': 'thisishoon'})
    docs.append({'author': 'jihoon kang'})
    results = insert_to_es(docs, index_name='test', path='localhost:9200')
    assert type(results) == list
    # for result in results:
    #     assert result == 'created'

    results = insert_to_es(docs, index_name='test2', path='localhost:9100')
    assert type(results) == list