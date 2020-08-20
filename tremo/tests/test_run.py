from tremo.run import run, repeat


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
