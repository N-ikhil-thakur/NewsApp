from django.shortcuts import render
from .models import NewsType, News


# Create your views here.
from django.shortcuts import render

from news.models import News, NewsType

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    newses_list = News.objects.filter(news_type=newstype)
    page = request.GET.get('page', 1)

    paginator = Paginator(newses_list, 9)

    try:
        newses = paginator.page(page)
    except PageNotAnInteger:
        newses = paginator.page(1)
    except EmptyPage:
        newses = paginator.page(paginator.num_pages)

    return render(request, 'visitor/news.html', {
        'newstype': newstype, 'page_type': newstype, 'news_types': news_types, 'newses': newses})


def news_detail_page(request, newstype, id):
    newses = NewsType.objects.get(title=newstype)
    news = newses.news.get(id=id)
    newses_suggestions = newses.news.order_by('-pub_date')[:6]
    news_types = NewsType.objects.all()
    news_type = newstype
    return render(request, 'visitor/news_detail.html', {"news_type": news_type, 'page_type': news_type, 'news': news, 'news_types': news_types, 'news_suggestions': newses_suggestions})
