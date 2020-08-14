from elasticsearch import Elasticsearch
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError


def insert_to_es(docs, index_name):
    es = Elasticsearch("localhost:9200")
    result = []
    for doc in docs:
        try:
            res = es.index(index=index_name, doc_type='naver', body=doc)
            result.append(res['result'])
        except ConnectionError as ce:
            print("ElasticSearch is not running")
        except NewConnectionError as nce:
            print("ElasticSearch is not running2")
    return result[0]