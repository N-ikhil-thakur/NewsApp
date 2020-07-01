from django.urls import path
from .views import homepage, homepage_eng, newsPage, newsPage_eng, news_detail_page, news_detail_page_eng

urlpatterns = [
    path('', homepage, name='homepage'),
    path('en', homepage_eng, name='homepage_eng'),
    path('समाचार/<str:newstype>', newsPage, name='news'),
    path('news/<str:newstype>', newsPage_eng, name='news_eng'),
    path('समाचार/<str:newstype>/<int:id>',
         news_detail_page, name='news_detail'),
    path('news/<str:newstype>/<int:id>',
         news_detail_page_eng, name='news_detail_eng'),

]
