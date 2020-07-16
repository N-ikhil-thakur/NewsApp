from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import JsonResponse, HttpResponse


from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im = im.convert("RGB")
    im_io = BytesIO() 
    im.save(im_io, 'JPEG' ,quality=80 , optimize=True) 
    new_image = File(im_io, name=image.name)
    return new_image

class NewsType(models.Model):
    title = models.CharField(
        max_length=100, default='समाचार को प्रकार', verbose_name='समाचार को प्रकार')
    title_eng = models.CharField(
        max_length=100, default="Type Of News ", verbose_name='Type Of News')

    def __str__(self):
        return f'{self.title}'


class News(models.Model):
    news_type = models.ForeignKey(
        NewsType, on_delete=models.CASCADE, related_name='news')

    title = models.CharField(
        max_length=250, verbose_name='शिर्षक', default="शिर्षक भेटिएन")
    title_eng = models.CharField(
        max_length=250, null=True, verbose_name='Title', default="No Title")

    description = models.TextField(
        verbose_name='विवरण', default="विवरण भेटिएन")
    description_eng = models.TextField(
        null=True, verbose_name='Description', default="No description")

    display_picture = models.ImageField(default='image_placeholder.png', null=True, blank=True)

    editor = models.CharField(
        max_length=100, default='सहयोगी समाचार', verbose_name='सम्पादक')

    editor_eng = models.CharField(
        max_length=100, default="Sahayogi News", verbose_name='Editor')
    pub_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name_plural = ("All Newses")

    def save(self, *args, **kwargs):
            if self.display_picture:
                new_image = compress(self.display_picture)
                self.display_picture = new_image
            else:
                self.display_picture = "image_placeholder.png"
            super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} ====> {self.title_eng}'
    



class Links(models.Model):
    title = "Social Media Links"
    youtube = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and Links.objects.exists():
            return
        return super(Links, self).save(*args, **kwargs)
