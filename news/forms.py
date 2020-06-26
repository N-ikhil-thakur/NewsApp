from django import forms

from .models import News, NewsType


class NewsForm(forms.ModelForm):

    class meta:
        model = News
        fields = '__all__'


class NewsTypeForm(forms.ModelForm):

    class Meta:
        model = NewsType
        fields = '__all__'
