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


def check_category(item):
    res = requests.get(URL_CATEGORY + item, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    category = []
    person_result = check_person(soup)
    movie_result = check_movie(soup)
    tv_result = check_tv(soup)

    if person_result:
        category += person_result
    elif movie_result:
        category.append(NAME_MOVIE)
    elif tv_result:
        category.append(tv_result)
    else:
        category.append(NAME_UNKNOWN)

    related_search = check_related_search(soup)

    return category, related_search


def check_person(soup):
    try:
        query = soup.select("#people_info_z > div.cont_noline > div > dl > dd.name > span ")[-1].text
    except Exception as e:
        return False
    else:
        return query.split(', ')


def check_movie(soup):
    try:
        query = soup.select_one("#_au_movie_info > div.section_head > h2").text
    except Exception as e:
        return False
    else:
        return True


def check_tv(soup):
    try:
        query = soup.select_one("div.broadcast_detail > div.top_info > dl > dd ").text.strip()
    except Exception as e:
        return False
    else:
        return query


def check_related_search(soup):
    related_search = soup.select("#nx_related_keywords > dl > dd.lst_relate._related_keyword_list > ul li")
    result = []

    if related_search:
        for i in related_search:
            result.append(i.text.strip())
        return result

    else:
        return result

