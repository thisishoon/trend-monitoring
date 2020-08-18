from elasticsearch import Elasticsearch, helpers
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

    return result


def insert_es_bulk(docs, index_name='trend', path='localhost:9200'):
    es = Elasticsearch(path)
    try:
        result = helpers.bulk(es, docs, index=index_name)
        return result
    except ElasticsearchException:
        print('ElasticSearch is not running')
        return False


def generate_data(docs):
    for doc in docs:
        yield {
            "_index": "test_bulk",
            '_source': doc
        }
