from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'videostore.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rentaldvd/', include('rentaldvd.urls', namespace='api-polls', app_name='rentaldvd')),
    url(r'^api/auth/', include('accounts.urls', namespace='api-auth')),
]
