from tremo.check import check_category


def test_check_category():
    category, related_search = check_category('김태희')
    assert '영화배우' in category

    category, related_search = check_category('놀면 뭐하니?')
    assert '예능' in category

    category, related_search = check_category('다만 악에서 구하소서')
    assert '영화' in category

    category, related_search = check_category('윤은혜')
    assert '탤런트' in category
