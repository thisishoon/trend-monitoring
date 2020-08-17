from elasticsearch import Elasticsearch
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError
from elasticsearch import ElasticsearchException


def insert_to_es(docs, index_name='trend', path='localhost:9200'):
    es = Elasticsearch(path)
    result = []

    for doc in docs:
        try:
            res = es.index(index=index_name, body=doc)
            result.append(res['result'])
        except ElasticsearchException:
            print('ElasticSearch is not running')
        except ConnectionError:
            print("ElasticSearch is not working")
        except NewConnectionError:
            print("ElasticSearch is not working2")

    return result

