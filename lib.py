from bs4 import BeautifulSoup
import requests
import os
import json
import re
from PIL import Image
from io import BytesIO
import urllib.request

WIKI = 'https://ru.wikipedia.org/w/api.php?action=query&formatversion=2&prop=pageimages%7Cpageterms&format=json&titles=' # Адрес википедии

def save_chemical_form_of(drug_name):
    parsed_page = BeautifulSoup((requests.get(WIKI+drug_name)).text, "html.parser")
    image_link = (list(filter(lambda x: x['alt'] == 'Изображение химической структуры', parsed_page.findAll('img', alt=True)))[0])['src']
    urllib.request.urlretrieve('https:'+image_link, './pics/'+drug_name+".png")    

def remove_pics_from_folder(path):
    os.remove(path)

def return_chemical_form_of(drug_name):
    parsed_page = BeautifulSoup((requests.get(WIKI+drug_name)).text, "html.parser")
    image_link = (list(filter(lambda x: x['alt'] == 'Изображение химической структуры', parsed_page.findAll('img', alt=True)))[0])['src']
    return requests.get('https:'+image_link).content

# Использовать эту функцию для загрузки картинки
def get_picture_of(drug_name: str) -> bytes:
    regexp = r'\d*px'
    link = json.loads((requests.get(WIKI+drug_name)).text)['query']['pages'][0]['thumbnail']['source']
    link = re.sub(regexp, '300px', link)
    return (urllib.request.urlopen(link)).read()

def show_picture(picture: bytes) -> None:
    (Image.open(BytesIO(picture))).show()
