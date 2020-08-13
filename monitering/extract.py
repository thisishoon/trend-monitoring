from konlpy.tag import Okt, Twitter
from newspaper import Article, ArticleException
from collections import Counter
from krwordrank.word import KRWordRank, summarize_with_keywords


def extract_keyword_frequency(word, news_links):
    okt = Okt()
    result = ""
    for news_link in news_links:
        article = Article(news_link, language='ko')
        article.download()
        try:
            article.parse()
            content = article.text
            result += content
        except ArticleException as ae:
            continue

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


def extract_keyword_textrank(nouns_list):

    min_count = 5
    max_length = 10
    wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)
    beta = 0.85
    max_iter = 10
    texts = nouns_list

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    stopwords = {'영화', '뉴스', '기자', '이슈', '기사', '평점', '주연', '방송', '편성표'}

    passwords = {word: score for word, score in sorted(
        keywords.items(), key=lambda x: -x[1])[:100] if not (word in stopwords)}

    related_keyword = list(passwords.keys())

    if len(related_keyword) > 10:
        return related_keyword[:10]
    else:
        return related_keyword


def make_nouns_list(word, news_links):
    okt = Okt()
    result = []

    for news_link in news_links:
        article = Article(news_link, language='ko')

        try:
            article.download()
            article.parse()
            content = article.text
        except ArticleException as ae:
            continue

        if content == '':
            continue
        else:
            nouns = okt.nouns(content)
            str = " ".join(noun for noun in nouns if len(noun) > 1 and noun != word)
            result.append(str)

    return result
