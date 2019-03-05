
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

from account.views import *

urlpatterns = format_suffix_patterns(patterns('',
	url("^detail", "home.views.hot_detail", name="hot_detail"),
	url("^news", "home.views.hot_news", name="hot_news"),
	url("^works", "home.views.hot_works", name="hot_works"),
	url("^sales", "home.views.hot_sales", name="hot_sales"),
))