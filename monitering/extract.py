from konlpy.tag import Okt
from newspaper import Article
from collections import Counter


def extract_related_keyword(word, news_links):
    okt = Okt()
    result = ""
    for news_link in news_links:
        article = Article(news_link, language='ko')
        article.download()
        article.parse()
        content = article.text
        result += content

    nouns = okt.nouns(result)

    for k, v in enumerate(nouns):
        if len(v) < 2 or v == word:
            nouns.pop(k)

    count = Counter(nouns)
    related_keyword = count.most_common(10)

    return related_keyword
