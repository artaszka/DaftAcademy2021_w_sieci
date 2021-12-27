from dataclasses import dataclass
import bs4
import requests


@dataclass
class Contact:
    email: str
    phone: str
    address: str
    instagram: str


def get_daftcode_contact_info() -> Contact:
    url = 'https://daftcode.pl/'
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    dane = soup.find(id="___gatsby")
    items = dane.find_all(class_="footer__item-link")
    print(items)
    email = items[0].text
    print(email)

    phone = items[1].a.text
    print(phone)

    address = items[2].a.text
    print(address)

    link = dane.find(class_="social__icon social__icon--instagram")['href']
    instagram = link
    print(instagram)

    contact = Contact(email=email, phone=phone, address=address, instagram=instagram)

    return contact
get_daftcode_contact_info()

"""
    Napisz funkcję która pobierze z głównej strony Dafta (https://daftcode.pl/)
    dane:
        * Adres email
        * Telefon
        * Adres
        * Link do instagrama

    Tips:
        1. Ugotuj zupę
    """