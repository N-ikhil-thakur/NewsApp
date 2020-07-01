from django.contrib import admin
from .models import NewsType, News, Links
# Register your models here.


class NewsAdmin(admin.StackedInline):
    model = News
    extra = 0


class NewsTypeAdmin(admin.ModelAdmin):
    model = NewsType
    list_display = ['title', 'title_eng']
    inlines = [NewsAdmin, ]


admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(Links)
