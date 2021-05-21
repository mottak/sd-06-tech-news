from tech_news.database import find_news


# Requisito 10
def top_5_news():
    all_news = find_news()
    pop_news = []
    for news in all_news:
        the_pop_news = news["comments_count"] + news["shares_count"]
        fresh_pop_new = {
            "title": news["title"],
            "url": news["url"],
            "populary": the_pop_news,
        }
        pop_news.append(fresh_pop_new)

    def sorted_news(e):
        return e['populary']

    pop_news.sort(key=sorted_news, reverse=True)
    return [(news["title"], news["url"]) for news in pop_news][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
