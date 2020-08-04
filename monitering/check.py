import requests
from bs4 import BeautifulSoup

def check_category(item):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=" + item
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    category = []
    person_result = check_person(soup)
    tv_result = check_tv(soup)

    if person_result is not False:
        category += person_result
    elif check_movie(soup) is not False:
        category.append("영화")
    elif check_tv(soup) is not False:
        category.append(tv_result)
    else:
        category.append("Unknown")

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

    if not related_search:
        return result

    else:
        for i in related_search:
            result.append(i.text.strip())
        return result

