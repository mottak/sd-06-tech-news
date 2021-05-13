import requests
from parsel import Selector
import time

tech_mundo_url = "https://www.tecmundo.com.br/novidades"


def fetch(url):
    time.sleep(1)
    try:
        website = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    else:
        response_status = website.status_code
        if response_status == 200:
            return website.text
        elif response_status != 200:
            return None


def scrape_noticia(html_content):
    selector = Selector(text=html_content, base_url=html_content)
    url = selector.css("head > link[rel=canonical]::attr(href)").get()
    title = selector.css("h1#js-article-title::text").get()
    timestamp = ""
    writer = ""
    shares_count = ""
    comments_count = ""
    summary = ""
    sources = ""
    categories = ""
    # timestamp = selector.css("time[datetime]")
    print(url)
    print(title)

    # pass
    #     {
    #   "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm",
    #   "title": "Musk: Tesla está muito perto de carros totalmente autônomos",
    #   "timestamp": "2020-07-09T11:00:00",
    #   "writer": "Nilton Kleina",
    #   "shares_count": 61,
    #   "comments_count": 26,
    #   "summary": "O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado.",
    #   "sources": ["Venture Beat"],
    #   "categories": [
    #     "Mobilidade Urbana/Smart Cities",
    #     "Veículos autônomos",
    #     "Tesla",
    #     "Elon Musk"
    #   ]
    # }


scrape_noticia(
    fetch(
        "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    )
)


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
