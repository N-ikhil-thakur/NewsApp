from django.contrib import admin
from .models import NewsType, News
# Register your models here.


class NewsAdmin(admin.StackedInline):
    model = News
    fields = ('title', 'body', 'display_picture', 'editor', 'pub_date')
    extra = 10


class NewsTypeAdmin(admin.ModelAdmin):
    model = NewsType
    list_display = ['title']
    inlines = [NewsAdmin, ]


admin.site.register(NewsType, NewsTypeAdmin)
