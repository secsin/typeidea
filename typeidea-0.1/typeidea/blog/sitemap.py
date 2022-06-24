# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/12 12:40
# @File : sitemap
# @Project : typeidea
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reverse('post-detail', args=[obj.pk])
