# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/9 20:57
# @File : custom_site
# @Project : typeidea

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea管理'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
