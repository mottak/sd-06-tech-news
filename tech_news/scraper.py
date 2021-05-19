import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
    except requests.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    timestamp = selector.css("#js-article-date::attr(datetime)").get()
    get_writer = selector.css(".tec--author__info__link::text").get()
    writer = get_writer.strip() if get_writer else None
    # <<<<<<<
    get_shares_count = selector.css(
        "#js-author-bar > nav > div:nth-child(1)::text"
    ).re_first(r"\d+")
    share_count = int(get_shares_count) if get_shares_count else 0
    # >>>>>>> pedaço de código feito pela Daniele Perse
    comments_count = int(
        selector.css("#js-comments-btn::attr(data-count)").get()
    )
    get_summary = selector.css(
        ".tec--article__body p:first-child *::text"
    ).getall()
    summary = "".join(get_summary)
    get_sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in get_sources]
    get_categories = selector.css("#js-categories > a *::text").getall()
    categories = [category.strip() for category in get_categories]
    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": share_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return news


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    news = selector.css(
        "h3.tec--card__title a.tec--card__title__link::attr(href)"
    ).getall()
    return news


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page = selector.css("a.tec--btn::attr(href)").get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = "https://www.tecmundo.com.br/novidades"
    news = []
    while len(news) < amount:
        news_page = fetch(url)
        news_list = scrape_novidades(news_page)
        for news_item in news_list:
            news_url = fetch(news_item)
            news.append(scrape_noticia(news_url))
            if len(news) == amount:
                create_news(news)
                return news
        url = scrape_next_page_link(news_page)
