from django.shortcuts import render
from json import load


def index(request):
    return render(request, "news/index.html")


def news(request, post_id):
    article = get_post(post_id)
    date = {"time": article['created'], "text": article['text'], "title": article['title']}
    return render(request, "news/news.html", date)


def get_post(id_post):
    with open("hypernews/news.json", "r") as articles_file:
        articles = load(articles_file)
        for article in articles:
            if article["link"] == id_post:
                return article

