from django.contrib import admin

from .models import NewsType, News, WebsiteInfo , DevelopersInfo
# Register your models here.

from django.urls import reverse
from django.shortcuts import redirect

class NewsAdmin(admin.ModelAdmin):
    model = News
    ordering= ("-pub_date",)
    search_fields = ("title" , "title_eng" , "pub_date", "id" , "display_picture" ,)
    

class NewsInline(admin.StackedInline):
    model = News
    ordering = ("-pub_date",)
    extra = 0


class NewsTypeAdmin(admin.ModelAdmin):
    inlines = [NewsInline, ]
    list_display = ['title', 'title_eng']
    search_fields = ("title_eng",)
    ordering = ("id",)

class Uploaded_Images(admin.ModelAdmin):
    def link(self):
        return mark_safe("<a href='%s'>edit</a>" % 'owner/filebrowser/browse')


admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(WebsiteInfo)
admin.site.register(News , NewsAdmin)
admin.site.register(DevelopersInfo)
