import pytest
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from datetime import datetime


def test_connect_naver_datalab():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver?entertainment=2&groupingLevel=4&marketing=-2&news=-2&sports=-2&where=main'

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.content, 'html.parser')
    assert res.status_code == 200


# def test_connect_es():
#     es = Elasticsearch("localhost:9200")
#     doc = {
#         'author': 'Jihoon Kang',
#         'text': 'ElasticSearch Test',
#         'timestamp': datetime.utcnow()
#     }
#     res = es.index(index="test", body=doc)
#
#     assert res['result'] == 'created'
