from django.db import models
import datetime


class NewsType(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class News(models.Model):
    news_type = models.ForeignKey(
        NewsType, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=250)
    body = models.TextField()
    display_picture = models.ImageField(
        default='image.png', null=True, blank=True)
    editor = models.CharField(max_length=100, default='SahayogiNews')
    pub_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title
