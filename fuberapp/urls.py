from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.apis import urls as apis_urls
from apps.home import urls as home_urls


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # API Urls
    url(r'^api/', include(apis_urls)),
    # Home urls
    url(r'^', include(home_urls)),
)
