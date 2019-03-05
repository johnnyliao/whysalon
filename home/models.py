#-*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.contenttypes import generic
from mezzanine.core.fields import RichTextField
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.sites.models import Site

import urlparse, settings
from django.utils import simplejson

class IndexBanner(models.Model):
    banner = models.ImageField(_(u"banner"), upload_to='home/banner')
    name = models.CharField(_(u"Banner名稱"), max_length=30)
    link = models.CharField(_(u"Banner連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)
    
    def __unicode__(self):
        return self.name

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.banner.url + '" />'

    image_tag.allow_tags = True
    
    class Meta:
        verbose_name = _(u"首頁Banner資訊")
        verbose_name_plural = _(u"首頁Banner列表")

class IndexFashion(models.Model):
    fashion = models.ImageField(_(u"圖片"), upload_to='home/fashion')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.fashion.url + '" />'

    image_tag.allow_tags = True

    class Meta:
        verbose_name = _(u"首頁流行趨勢")
        verbose_name_plural = _(u"首頁流行趨勢列表")

class IndexNews(models.Model):
    title = models.CharField(_(u"標題"), max_length=999)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)
    updated = models.DateTimeField(_(u"建立時間"), auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"首頁最新消息")
        verbose_name_plural = _(u"首頁消息列表")

class IndexRecommend(models.Model):
    recommend = models.ImageField(_(u"圖片"), upload_to='home/recommend')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.recommend.url + '" />'

    image_tag.allow_tags = True

    class Meta:
        verbose_name = _(u"首頁網友推薦")
        verbose_name_plural = _(u"首頁網友推薦列表")


class IndexSale(models.Model):
    sale = models.ImageField(_(u"圖片"), upload_to='home/sale')
    title = models.CharField(_(u"標題"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.sale.url + '" />'

    image_tag.allow_tags = True

    class Meta:
        verbose_name = _(u"首頁優惠活動")
        verbose_name_plural = _(u"首頁優惠活動列表")


class IndexHot(models.Model):
    hot = models.ImageField(_(u"圖片"), upload_to='home/hot')
    title = models.CharField(_(u"設計師名稱"), max_length=30)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)
    detail = RichTextField(_(u"詳細內容"), max_length=9999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.hot.url + '" />'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = _(u"首頁熱門設計師")
        verbose_name_plural = _(u"首頁熱門設計師列表")

class DesignerDemo (models.Model):
    photo = models.ImageField(_(u"圖片"), upload_to='home/designer_demo')
    designer = models.ManyToManyField("IndexHot", verbose_name=_(u"設計師"), related_name='index_hot_photo')


    def image_tag(self):
        return '<img style="width:100px;height:100px" src="' + self.photo.url + '" />'

    image_tag.allow_tags = True

    class Meta:
        verbose_name = _(u"設計師作品")
        verbose_name_plural = _(u"設計師作品列表")

class IndexMap(models.Model):
    map_img = models.ImageField(_(u"圖片"), upload_to='home/map')
    llat = models.CharField(_(u"經度"), max_length=30)
    llong = models.CharField(_(u"緯度"), max_length=30)
    title = models.CharField(_(u"店名"), max_length=30)
    des = models.CharField(_(u"簡介"), max_length=999, null=True, blank=True)
    link = models.CharField(_(u"點擊連結"), max_length=999, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"首頁據點")
        verbose_name_plural = _(u"首頁據點列表")
