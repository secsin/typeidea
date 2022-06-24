# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/13 11:02
# @File : serializers
# @Project : typeidea
from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Comment
        fields = ['id', 'target', 'content', 'nickname', 'website', 'email', 'created_time']
