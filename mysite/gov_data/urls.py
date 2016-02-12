from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^senators/(?P<id>[0-9]+)/$', views.senator_detail, name = 'senator_detail'),
    url(r'^senators/', views.senators_index, name = 'senators_index'),
    url(r'^bills/(?P<bill_id>[0-9]+)/$', views.bill_detail, name = 'bill_detail'),
    url(r'^bills/', views.bills_index, name='bills_index'),
]