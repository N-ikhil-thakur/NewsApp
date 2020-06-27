from django.shortcuts import render

from news.models import News, NewsType


def homepage(request):
    news_types = NewsType.objects.all()

    news_types_with_news = {}
    for items in NewsType.objects.all():
        news_types_with_news[items.title] = items.news.all().order_by(
            '-pub_date')[:5]
    return render(request, 'visitor/home.html', {
        'news_types': news_types,
        'news_types_with_news': news_types_with_news,
        'page_type': 'Homepage'})


def newsPage(request, newstype):
    news_types = NewsType.objects.all()
    newstype = NewsType.objects.get(title=newstype)
    return render(request, 'visitor/news.html', {
        'newstype': newstype, 'page_type': newstype, 'news_types': news_types})
