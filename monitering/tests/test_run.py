import threading
from monitering.run import run, repeat


def test_run():
    docs = run(elastic_search=False)
    assert len(docs) == 10

    for doc in docs:
        assert 'word' in doc.keys()
        assert 'ranking' in doc.keys()
        assert 0 < doc.get('ranking') & doc.get('ranking') <= 10
        assert 'category' in doc.keys()


# To do Issue : why timer is alive after timer cancle()?
def test_repeat():
    timer, alive_flag = repeat(elastic_search=False, interval_second=600)

    assert alive_flag is True
    timer.cancel()
