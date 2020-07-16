from django.contrib import admin

from .models import NewsType, News, Links
# Register your models here.

from django.urls import reverse
from django.shortcuts import redirect

class NewsAdmin(admin.ModelAdmin):
    model = News
    ordering= ("-pub_date",)
    search_fields = ("title" , "title_eng" , "pub_date",)
    

class NewsInline(admin.StackedInline):
    model = News
    ordering = ("-pub_date",)
    extra = 0


class NewsTypeAdmin(admin.ModelAdmin):
    inlines = [NewsInline, ]
    list_display = ['title', 'title_eng']
    search_fields = ("title_eng",)
    ordering = ("id",)



admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(Links)
admin.site.register(News , NewsAdmin)
