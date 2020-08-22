import requests
from datetime import datetime
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

URL_CATEGORY = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query='

NAME_MOVIE = '영화'
NAME_UNKNOWN = 'unknown'

ELEMENT_CATEGORY_PERSON = '#people_info_z > div.cont_noline > div > dl > dd.name > span '
ELEMENT_CATEGORY_MOVIE = '#_au_movie_info > div.section_head > h2'
ELEMENT_CATEGORY_TV = 'div.broadcast_detail > div.top_info > dl > dd '
ELEMENT_RELATED_SEARCH_WORD = '#nx_related_keywords > dl > dd.lst_relate._related_keyword_list > ul li'


def check_category(item):
    res = requests.get(URL_CATEGORY + item, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    category = []

    person = soup.select(ELEMENT_CATEGORY_PERSON)
    if person:
        category += person[-1].text.split(', ')

    movie = soup.select_one(ELEMENT_CATEGORY_MOVIE)
    if movie:
        category.append(NAME_MOVIE)

    tv = soup.select_one(ELEMENT_CATEGORY_TV)
    if tv:
        category.append(tv.text.strip())

    if not category:
        category.append(NAME_UNKNOWN)

    related_search = check_related_search(soup)

    return category, related_search


def check_related_search(soup):
    related_search = soup.select(ELEMENT_RELATED_SEARCH_WORD)
    result = []

    if related_search:
        for i in related_search:
            result.append(i.text.strip())
        return result

    else:
        return result

