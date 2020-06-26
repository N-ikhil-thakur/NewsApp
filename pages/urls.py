from django.urls import path
from .views import homepage, newsPage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('news/<str:newstype>', newsPage, name='news')
]
