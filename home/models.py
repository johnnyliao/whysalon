#-*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.contenttypes import generic

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.sites.models import Site

import urlparse, settings
from cart.models import Brand
from django.utils import simplejson

class IndexBanner(models.Model):
    banner = models.ImageField(_(u"banner"), upload_to='home/banner')
    name = models.CharField(_(u"Banner名稱"), max_length=30)
    link = models.CharField(_(u"Banner連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.banner.url + '" />'

    class Meta:
        verbose_name = _(u"首頁Banner資訊")
        verbose_name_plural = _(u"首頁Banner列表")

class IndexFashion(models.Model):
    fashion = models.ImageField(_(u"圖片"), upload_to='home/fashion')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.fashion.url + '" />'

    class Meta:
        verbose_name = _(u"首頁流行趨勢")
        verbose_name_plural = _(u"首頁流行趨勢列表")

class IndexNews(models.Model):
    title = models.CharField(_(u"標題"), max_length=999)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"首頁最新消息")
        verbose_name_plural = _(u"首頁消息列表")

class IndexRecommend(models.Model):
    recommend = models.ImageField(_(u"圖片"), upload_to='home/recommend')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.recommend.url + '" />'

    class Meta:
        verbose_name = _(u"首頁網友推薦")
        verbose_name_plural = _(u"首頁網友推薦列表")


class IndexSale(models.Model):
    sale = models.ImageField(_(u"圖片"), upload_to='home/sale')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.sale.url + '" />'

    class Meta:
        verbose_name = _(u"首頁優惠活動")
        verbose_name_plural = _(u"首頁優惠活動列表")

class IndexHot(models.Model):
    hot = models.ImageField(_(u"圖片"), upload_to='home/hot')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.hot.url + '" />'

    class Meta:
        verbose_name = _(u"首頁熱門設計師")
        verbose_name_plural = _(u"首頁熱門設計師列表")

class IndexMap(models.Model):
    llat = models.CharField(_(u"經度"), max_length=30)
    llong = models.CharField(_(u"緯度"), max_length=30)
    title = models.CharField(_(u"店名"), max_length=30)
    des = models.CharField(_(u"說明"), max_length=999, null=True, blank=True)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"首頁據點")
        verbose_name_plural = _(u"首頁據點列表")