from django.shortcuts import render

from news.models import News, NewsType


def homepage(request):
    return render(request, 'visitor/home.html', {})


def newsPage(request, newstype):
    newstype = NewsType.objects.get(title=newstype)
    return render(request, 'visitor/news.html', {'newstype': newstype})
