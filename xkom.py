from dataclasses import dataclass
from typing import Set, Tuple
from bs4 import BeautifulSoup
import requests
# import json
# import re
@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int

def get_xkom_hotshot_product_data() -> HotShot:


     # Napisz funkcję która pobiera Gorący strzał z głównej strony https://www.x-kom.pl/.
     # Tips:
     #     1. Sprawdź jak przeglądarka odpytuje API xkomu (konsola developerska w przeglądarce)
     #     2. Sprawdź czy na pewno masz wszystkie potrzebne nagłówki
     # Przykład:
     # >>> get_xkom_hotshot_product_data()
     # HotShot(promotion_name='ASUS TUF GAMING Z590-PLUS\xa0(Socket 1200)', promotion_total_count=100)


    url = "https://www.x-kom.pl/"
    h = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=h)    # print(r)  # <Response [200]>
    soup = BeautifulSoup(r.content, 'html.parser')
    response = soup.find_all('script')
    for r in response:
        if len(str(r).splitlines()) > 0:
            for rl in r:
                if "window.__INITIAL_STATE__" in rl:
                    dane = rl
    for d in dane.split(','):
        if 'promotionName' in d:
            n = d.split(':')[1][1:-1:]
        if 'promotionTotalCount' in d:
            c = int(d.split(':')[1])
    return HotShot(n, c)
def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:
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
    words = set(name.split(' '))
    words_lower = set([w.lower() for w in words])
    keyword_lower = set([k.lower() for k in keywords])
    final_set = set()
    for kl in keyword_lower:
        for wl in words_lower:
            if kl in wl:
                final_set.add(kl)
            else:
                continue
    return final_set
def check_xkom_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:
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
    hs = get_xkom_hotshot_product_data()
    mk = get_matching_keywords(hs.promotion_name, keywords)
    return hs, mk
test1 = get_xkom_hotshot_product_data()
print(test1)
test2 = get_matching_keywords('Pamięć RAM DDR4 Kingston FURY 16GB (2x8GB) 3600MHz CL17 Beast RGB', {'DDR4', 'pamięć', 'HDD'})
print(test2)
test3 = check_xkom_hotshot({'DDR4', 'pamięć', 'HDD'})
print(test3)