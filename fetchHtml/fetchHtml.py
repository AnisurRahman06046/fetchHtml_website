import requests
from bs4 import BeautifulSoup

def fetchHtml(webiste,parser):
    url = webiste
    r = requests.get(url)
    soup_data = BeautifulSoup(r.text,parser)
    return soup_data