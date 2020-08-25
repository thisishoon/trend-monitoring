from datetime import datetime
from tremo.run import run, repeat, make_document


def test_run():
    docs = run(elastic_search=False)
    assert len(docs) == 10

    for doc in docs:
        assert 'word' in doc.keys()
        assert 'ranking' in doc.keys()
        assert 0 < doc.get('ranking') & doc.get('ranking') <= 10
        assert 'category' in doc.keys()


def test_repeat():
    timer, alive_flag = repeat(elastic_search=False, interval_second=600)

    assert alive_flag is True  # 반복을 위한 timer 실행중인 상태
    timer.cancel()
    timer.join(5)
    assert timer.is_alive() is False


def test_make_document():
    rank = 1
    word = 'Btv'
    category = 'Media Service'
    related_search_word = ['SK', 'SK Broadband', 'Intern', 'Media', 'Network']
    related_keyword = ['SW', 'Backend', 'AIPlatformSquad', 'ProductCOE']
    news_title = 'Kang Jihoon will converted to full-time employee as manager'
    date = datetime.utcnow()

    doc = make_document(rank, word, category, related_search_word, related_keyword, news_title, date)

    assert type(doc) is dict
    assert len(doc) != 0
    assert doc is not None
