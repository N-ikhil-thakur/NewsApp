from django.urls import path
from .views import (
     homepage, 
     homepage_eng,
      newsPage, 
      newsPage_eng, 
      news_detail_page,
     news_detail_page_eng,
     searchNews,
     searchNewsEng
)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('en', homepage_eng, name='homepage_eng'),
    path('news/<str:newstype>', newsPage, name='news'),
    path('en/news/<str:newstype>', newsPage_eng, name='news_eng'),
    path('news/<str:newstype>/<int:id>',
         news_detail_page, name='news_detail'),
    path('en/news/<str:newstype>/<int:id>',
         news_detail_page_eng, name='news_detail_eng'),
     path('search' , searchNews , name="search_news"),
     path('en/search' , searchNewsEng , name="search_news_eng"),
]
