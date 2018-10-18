from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^dvd/(?P<id>[0-9]+)/$', views.DvdDetailView.as_view(), name='detail'),
    url(r'^api/$', views.RentalRestApi.as_view(), name='dvd_api'),
]

app_name = 'rentaldvd'

urlpatterns = format_suffix_patterns(urlpatterns)