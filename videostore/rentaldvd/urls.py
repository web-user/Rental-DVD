from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^api/$', views.RentalRestAPIView.as_view(), name='dvd_api'),
    url(r'^api/(?P<id>\d+)/$', views.RentalAPIDetailView.as_view()),
    url(r'^dvd/(?P<id>[0-9]+)/$', views.DvdDetailView.as_view(), name='detail'),

    url(r'^$', views.DvdListView.as_view(), name='home'),

]

app_name = 'rentaldvd'

urlpatterns = format_suffix_patterns(urlpatterns)