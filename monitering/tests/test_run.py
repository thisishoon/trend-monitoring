from monitering.run import run, repeat


def test_run():
    docs = run()
    assert len(docs) == 10

    for doc in docs:
        assert 'word' in doc.keys()
        assert 'ranking' in doc.keys()
        assert 0 < doc.get('ranking') & doc.get('ranking') <= 10
        assert 'category' in doc.keys()
