from django.urls import path
from .views import homepage, newsPage, news_detail_page

urlpatterns = [
    path('', homepage, name='homepage'),
    path('news/<str:newstype>', newsPage, name='news'),
    path('news/<str:newstype>/<int:id>', news_detail_page, name='news_detail')
]
