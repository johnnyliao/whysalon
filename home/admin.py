#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from home.models import IndexBanner, IndexFashion, IndexNews, IndexRecommend, IndexSale, IndexHot, IndexMap
from salmonella.admin import SalmonellaMixin

class IndexBannerAdmin(SalmonellaMixin, admin.ModelAdmin):
	list_display = ['name', 'image_tag']

class IndexFashionAdmin(SalmonellaMixin, admin.ModelAdmin):
	list_display = ['title', 'image_tag']

class IndexNewsAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title"]
    #salmonella_fields  = ["banner", "movie", "brand"]

class IndexRecommendAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title", "image_tag"]

class IndexSaleAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title", "image_tag"]

class IndexHotAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title", "image_tag"]

class IndexＭapAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["title", "llat", "llong"]

#admin.site.register(S3Data, S3DataAdmin)
admin.site.register(IndexBanner, IndexBannerAdmin)
admin.site.register(IndexFashion, IndexFashionAdmin)
admin.site.register(IndexNews, IndexNewsAdmin)
admin.site.register(IndexRecommend, IndexRecommendAdmin)
admin.site.register(IndexSale, IndexSaleAdmin)
admin.site.register(IndexMap, IndexMapAdmin)