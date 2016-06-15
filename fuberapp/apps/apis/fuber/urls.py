from django.conf.urls import patterns, url
from apps.apis.fuber import views

urlpatterns = patterns(
    '',
    url(r'^start/trip$', views.StartTripApi.as_view(), name="start-trip"),
    url(r'^end/trip/(?P<pk>[0-9]+)$', views.EndTripApi.as_view(), name="end-trip"),
    url(r'^cabs$', views.CabsApi.as_view(), name="cabs"),
    url(r'^booking/history$', views.BookingHistoryApi.as_view(), name="booking-history"),
)
