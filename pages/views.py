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
