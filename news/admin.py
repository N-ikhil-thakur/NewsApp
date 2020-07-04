from django.contrib import admin

from .models import NewsType, News, Links
# Register your models here.

from django.urls import reverse
from django.shortcuts import redirect


class NewsAdmin(admin.StackedInline):
    model = News
    extra = 0


class NewsTypeAdmin(admin.ModelAdmin):
    inlines = [NewsAdmin, ]
    list_display = ['title', 'title_eng']


admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(Links)
