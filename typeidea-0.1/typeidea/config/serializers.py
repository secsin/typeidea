# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/13 11:02
# @File : serializers
# @Project : typeidea
from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    # created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # 自定义字段
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')  # 只读不写

    class Meta:
        model = Link
        fields = ['id', 'title', 'href', 'weight', 'created_time', 'owner']

    def create(self, validated_data):
        return Link.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.href = validated_data.get('href', instance.href)
        instance.created_time = validated_data.get('created_time', instance.created_time)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
