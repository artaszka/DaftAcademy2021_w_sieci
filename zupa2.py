import requests
import bs4
from typing import Set
import urllib


def get_recepie_links(keyword: str) -> Set[str]:
    url = 'https://www.kwestiasmaku.com/szukaj?search_api_views_fulltext='
    keyword = urllib.parse.quote_plus(keyword)
    url += keyword
    lista = set()
    print(type(lista))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT b.1: WOW64)'}
    page = requests.get(url, headers=headers)
    url2 = bs4.BeautifulSoup(page.content, 'html.parser')
    main = url2.find(class_='view-content')
    #print(main.prettify())
    items = main.find_all('h2')
    for a in main.find_all('div', about=True):
        begin = 'https://www.kwestiasmaku.com'
        end = a['about']
        adres = begin+end
        lista.add(adres)
    print(type(lista))
    print(lista)


get_recepie_links("placki")




"""
    Napisz funkcję która pobierze linki do przepisów z wyszukiwania o zadanym słowie kluczowym
    ze strony https://www.kwestiasmaku.com

    Tips:
        1. Zobacz jak budowane jest zapytanie wyszukujące
        2. Zobacz w jakim kontenerze znajdują się wyniki wyszukiwania
        3. Ugotuj zupe na podstawie przepisu wonsz w sieci :))

    Przykład:
    >>> get_recepie_links("placki")
    {'https://www.kwestiasmaku.com/przepis/placki-kukurydziane',
     'https://www.kwestiasmaku.com/przepis/placki-twarogowe',
     'https://www.kwestiasmaku.com/przepis/placki-z-batatow',
     'https://www.kwestiasmaku.com/przepis/placki-z-ciecierzycy',
     'https://www.kwestiasmaku.com/przepis/placki-z-dyni',
     'https://www.kwestiasmaku.com/przepis/placki-z-kalafiora',
     'https://www.kwestiasmaku.com/przepis/placki-ziemniaczane'}
    """