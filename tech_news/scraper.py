import time
import requests
from requests.exceptions import ReadTimeout, HTTPError


# Requisito 1
def fetch(url):
    time.sleep(1)
    response = ''

    try:
        response = requests.get(url, timeout=3)
    except ReadTimeout:
        return None
    try:
        response.raise_for_status()
    except HTTPError:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
