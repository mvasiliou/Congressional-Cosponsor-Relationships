from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^senators/(?P<senator_id>[0-9]+)/$', views.senator_detail, name = 'senator_detail'),
    url(r'^senators/', views.senators_index, name = 'senators_index'),
    url(r'^bills/detail/(?P<bill_id>[0-9]+)/$', views.bill_detail, name = 'bill_detail'),
    url(r'^bills/(?P<congress>[0-9]+)/(?P<bill_range>[0-9]+)/$', views.bills_index, name='bills_index'),
    url(r'^bills/(?P<congress>[0-9]+)/$', views.bills_index, name='bills_index'),
    url(r'^bills/$', views.bills_index, name='bills_index'),

]