from konlpy.tag import Komoran
from newspaper import Article, ArticleException
from collections import Counter
from krwordrank.word import KRWordRank


def extract_keyword_textrank(input_list):
    min_count = 5
    max_length = 10
    wordrank_extractor = KRWordRank(min_count=min_count, max_length=max_length)
    beta = 0.85
    max_iter = 10
    texts = input_list

    keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

    stopwords = {'뉴스', '기자', '기사', '평점', '주연', '방송', '편성표'}

    passwords = {word: score for word, score in sorted(
        keywords.items(), key=lambda x: -x[1])[:100] if not (word in stopwords)}

    related_keyword = list(passwords.keys())

    if len(related_keyword) > 15:
        return related_keyword[:15]
    else:
        return related_keyword


def make_news_contents(search_word, news_links):
    komoran = Komoran()
    news_contents = []
    stopwords = ['하', '있', '없', '되', '보']

    for news_link in news_links:
        article = Article(news_link, language='ko')
        try:
            article.download()
            article.parse()
            content = article.text
        except ArticleException:
            continue

        news_content = ""
        word_tag = komoran.pos(content)

        for word, morph in word_tag:
            if word not in stopwords and word not in search_word:
                if morph in ['VA', 'VV']:
                    news_content += (word + '다' + ' ')
                elif morph in ['NNP', 'NNG', 'NP'] and len(word) > 1:
                    news_content += (word + ' ')

        news_contents.append(news_content)

    return news_contents