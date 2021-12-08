from bs4 import BeautifulSoup
import requests
import urllib
import os
WIKI = 'https://ru.wikipedia.org/wiki/'

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
