from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    (r'^$', 'apps.home.views.index'),
)
