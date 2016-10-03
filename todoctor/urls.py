from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main_page, name='main_pade'),
    url(r'^results/$', views.results, name='results'),
    url(r'^coupon/$', views.coupon, name='coupon'),
]
