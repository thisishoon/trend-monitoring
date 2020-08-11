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

    nouns_over_2char = []
    for noun in nouns:
        if len(noun) < 2 or noun == word:
            continue
        else:
            nouns_over_2char.append(noun)

    count = Counter(nouns_over_2char).most_common(10)
    related_keyword = [i[0] for i in count]

    return related_keyword
