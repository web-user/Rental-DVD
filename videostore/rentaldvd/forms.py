from .models import Dvd
from django.forms import ModelForm
from django import forms
import django_filters


class DvdApiFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(name='title')

    class Meta:
        model = Dvd
        fields = ('title',)


