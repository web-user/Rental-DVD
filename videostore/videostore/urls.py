from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'videostore.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('rentaldvd.urls', namespace='api-polls', app_name='rentaldvd')),
    url(r'^api/auth/', include('accounts.urls', namespace='api-auth')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)