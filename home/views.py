# Create your views here.
#-*- encoding: utf-8 -*-

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator

import urllib, urllib2, json, simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.middleware.csrf import get_token

import requests
from allauth.socialaccount import providers
from allauth.socialaccount.providers.facebook.provider import FacebookProvider
from allauth.socialaccount.providers.facebook.views import fb_complete_login

from allauth.socialaccount.providers.twitter.provider import TwitterProvider
from allauth.socialaccount.providers.twitter.views import TwitterAPI

from allauth.socialaccount.providers.weibo.provider import WeiboProvider

from allauth.socialaccount.models import (SocialLogin, SocialToken, SocialAccount)
from allauth.socialaccount.helpers import complete_social_login, render_authentication_error
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import settings, random
from home.models import IndexBanner, IndexFashion, IndexNews, IndexRecommend, IndexSale, IndexHot, IndexMap
from account.models import User
from rest_framework.views import APIView
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.template import RequestContext
from datetime import datetime, timedelta
from django.db.models import Q
import pytz
import base64
import time

def slice_list(list_list, s_count):
	result = []
	s_list = []
	count = 1
	for item in list_list:
		s_list.append(item)
		if count % s_count == 0:
			result.append(s_list)
			s_list = []
		count += 1

	return result

def home(request):
	timestamp = time.time()
	banners = IndexBanner.objects.all()
	fashions = IndexFashion.objects.all()
	recommends = IndexRecommend.objects.all()
	news = IndexNews.objects.all()
	sale_result = IndexSale.objects.all()
	hot_result = IndexHot.objects.all()
	hot_blog = IndexFashion.objects.all()[:4]
	map_result = IndexMap.objects.all()
	return render_to_response("home/index.html", locals(), context_instance=RequestContext(request))

def hot_detail(request):
	timestamp = time.time()
	hot_result = IndexHot.objects.all()
	store_list = IndexMap.objects.all()
	return render_to_response("home/hot_detail.html", locals(), context_instance=RequestContext(request))

def hot_works(request):
	timestamp = time.time()
	hot_result = IndexHot.objects.all()
	store_list = IndexMap.objects.all()
	product = range(50)
	paginator = Paginator(product, 15)
	product = paginator.page(1)
	return render_to_response("home/hot_works.html", locals(), context_instance=RequestContext(request))

def hot_news(request):
	timestamp = time.time()
	product = range(50)
	paginator = Paginator(product, 10)
	news = paginator.page(1)
	return render_to_response("home/hot_news.html", locals(), context_instance=RequestContext(request))

def hot_sales(request):
	timestamp = time.time()
	sales = range(50)
	paginator = Paginator(sales, 10)
	sales = paginator.page(1)
	return render_to_response("home/hot_sales.html", locals(), context_instance=RequestContext(request))