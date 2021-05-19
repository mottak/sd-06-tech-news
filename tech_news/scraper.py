import requests
import time
from requests.exceptions import HTTPError, ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    """Carrega e retorna os dados da URL de parâmetro"""

    time.sleep(1)
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
    """Preenche um dicinário a partir das informações
    de uma notícia extraídas a partir do seu HTML"""

    selector = Selector(html_content)

    return {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css(
            ".tec--timestamp__item time::attr(datetime)"
        ).get(),
        "writer": selector.css(".tec--author__info__link::text").get().strip(),
        "shares_count": int(
            selector.css(".tec--toolbar__item *::text")[0]
            .get()
            .strip()
            .split()[0]
        ),
        "comments_count": int(
            selector.css(".tec--toolbar__item *::text")[2]
            .get()
            .strip()
            .split()[0]
        ),
        "summary": "".join(
            selector.css(".tec--article__body p:nth-child(1) *::text").getall()
        ),
        "sources": [
            source.strip()
            for source in selector.css(".z--mb-16 .tec--badge::text").getall()
        ],
        "categories": [
            category.strip()
            for category in selector.css(
                ".tec--badge--primary *::text"
            ).getall()
        ],
    }


# Requisito 3
def scrape_novidades(html_content):
    """Retorna URLs das páginas de notícias"""
    if html_content == "":
        return []
    else:
        selector = Selector(html_content)
        list_urls = selector.css(
            "div.tec--card__info h3 a::attr(href)"
        ).getall()
    return list_urls


# Requisito 4
def scrape_next_page_link(html_content):
    """Retorna Link da próxima página"""
    selector = Selector(html_content)
    url_next_page = selector.xpath(
        "//*[@id='js-main']/div/div/div[1]/div[2]/a/@href"
    ).get()
    if url_next_page == "":
        return None
    else:
        return url_next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
