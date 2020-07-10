from django.shortcuts import render
from .models import NewsType, News, Links


# Create your views here.
from django.shortcuts import render

from news.models import News, NewsType

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
    news_types = NewsType.objects.all()
    links = Links.objects.all()[0]

    news_types_with_news = {}
    for items in NewsType.objects.all():
        news_types_with_news[items] = items.news.all().order_by(
            '-pub_date')[:5]
    return render(request, 'visitor/home.html', {
        'news_types': news_types,
        'news_types_with_news': news_types_with_news,
        'page_type': 'Homepage', 'links': links})


def homepage_eng(request):
    news_types = NewsType.objects.all()
    links = Links.objects.all()[0]
    news_types_with_news = {}
    for items in NewsType.objects.all():
        news_types_with_news[items] = items.news.all().order_by(
            '-pub_date')[:5]
    return render(request, 'visitor/home_eng.html', {
        'news_types': news_types,
        'news_types_with_news': news_types_with_news,
        'page_type': 'Homepage', 'links': links})


def newsPage(request, newstype):
    news_types = NewsType.objects.all()
    links = Links.objects.all()[0]
    newstype = NewsType.objects.get(title_eng=newstype)
    newses_list = News.objects.filter(news_type=newstype).order_by('-pub_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(newses_list, 9)

    try:
        newses = paginator.page(page)
    except PageNotAnInteger:
        newses = paginator.page(1)
    except EmptyPage:
        newses = paginator.page(paginator.num_pages)

    return render(request, 'visitor/news.html', {
        'newstype': newstype, 'page_type': newstype, 'news_types': news_types, 'newses': newses, 'links': links})


def newsPage_eng(request, newstype):
    news_types = NewsType.objects.all()
    links = Links.objects.all()[0]
    newstype = NewsType.objects.get(title_eng=newstype)
    newses_list = News.objects.filter(news_type=newstype).order_by('-pub_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(newses_list, 9)

    try:
        newses = paginator.page(page)
    except PageNotAnInteger:
        newses = paginator.page(1)
    except EmptyPage:
        newses = paginator.page(paginator.num_pages)

    return render(request, 'visitor/news_eng.html', {
        'newstype': newstype, 'page_type': newstype, 'news_types': news_types, 'newses': newses, 'links': links})


def news_detail_page(request, newstype, id):
    newses = NewsType.objects.get(title_eng=newstype)
    news = newses.news.get(id=id)
    links = Links.objects.all()[0]
    news_types = NewsType.objects.all()
    news_type = newses
    return render(request, 'visitor/news_detail.html', {"news_type": news_type, 'page_type': news_type, 'news': news, 'news_types': news_types,  'links': links})


def news_detail_page_eng(request, newstype, id):
    newses = NewsType.objects.get(title_eng=newstype)
    news = newses.news.get(id=id)
    links = Links.objects.all()[0]
    news_types = NewsType.objects.all()
    news_type = newses
    return render(request, 'visitor/news_detail_eng.html', {"news_type": news_type, 'page_type': news_type, 'news': news, 'news_types': news_types, 'links': links})
