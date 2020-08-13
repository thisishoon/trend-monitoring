from elasticsearch import Elasticsearch
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError

def insert(dicts):
    es = Elasticsearch("localhost:9200")
    for dict in dicts:
        try:
            res = es.index(index='trend', doc_type='naver', body=dict)
        except ConnectionError as ce:
            print("ElasticSearch is not running")
        except NewConnectionError as nce:
            print("ElasticSearch is not running2")
