from elasticsearch import Elasticsearch


def insert(dicts):
    es = Elasticsearch("localhost:9200")
    for dict in dicts:
        res = es.index(index='trend', doc_type='naver', body=dict)
        print(res['result'])
