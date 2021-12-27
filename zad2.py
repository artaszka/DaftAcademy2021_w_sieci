from dataclasses import dataclass
from typing import Set, Tuple
from requests.exceptions import HTTPError
import json
import requests
import bs4


@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int


def get_xkom_hotshot_product_data() -> HotShot:

    #try:
    url = 'https://www.x-kom.pl/'
    params = {'format': 'json', "Content-Type": "application/json; charset=utf-8"}
    headers = {"Content-Type": "application/json; charset=utf-8", 'user-agent': 'Chrome/96.0.4664.110'}
    r = requests.get(url, params=params, headers=headers)
    #data = json.loads(r)
    #print(data)
    #print('req_headers', r.request.headers)

    #print('CONTENT:', r.content)

    print('***********************************************************',)
    #print('headers', r.headers)
    print('status:', r.status_code)
    print('***********************************************************', )
    sup = bs4.BeautifulSoup(r.content, 'html.parser')
    print(sup.prettify())
    #
    # r.raise_for_status()
    # # access JSOn content
    #json_resp = r.json()
    # print("Entire JSON response")
    # #print(type(json_resp))
    #print(json_resp["url"])
    # print('JSON RESPONSE: ', json_resp)
    # for key, value in json_resp.items():
    #     print(key, ":", value)
    #except HTTPError as http_err:
        #print(f'HTTP error occurred: {http_err}')

    #except Exception as err:
        #print(f'Other error occurred: {err}')


get_xkom_hotshot_product_data()


"""
    Napisz funkcję która pobiera Gorący strzał z głównej strony https://www.x-kom.pl/.

    Tips:
        1. Sprawdź jak przeglądarka odpytuje API xkomu (konsola developerska w przeglądarce)
        2. Sprawdź czy na pewno masz wszystkie potrzebne nagłówki

    Przykład:
    >>> get_xkom_hotshot_product_data()
    HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100)
    """


def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:
    pass
    """
    Napisz funkcję która sprawdza czy którykolwiek ze słów kluczowych znajduje się w
    podanej nazwie. Zwróć set wszystkich słów kluczwych które występują w nazwie.


    Tips:
        1. Pamiętaj aby sprowadzić nazwę produktu do małych liter.

    Przykład:
    >>> get_matching_keywords("Telefon NoKia 3310", {"nokia", "sony"})
    {'nokia'}
    >>> get_matching_keywords("Telefon NoKia 3310plus", {"3310", "nokia"})
    {'nokia', '3310'}

    """


def check_xkom_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:
    pass
    """
    Napisz funkcję która zwróci dane produktu na gorącym strzale oraz wszystkie słowa
    kluczowe które zawierają się w nazwie produktu.

    Tips:
        1. Użyj tego co już zapiplementówałeś/aś

    Przykład:
    >>> check_xkom_hotshot(keywords={'owoce', 'warzywa'})
    (HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100), set())
    >>> check_xkom_hotshot(keywords={'nokia'})
    (HotShot(promotion_name='Telefon NoKia 3310', promotion_total_count=100), {'nokia'})
    """

