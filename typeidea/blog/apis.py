# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/13 11:07
# @File : apis
# @Project : typeidea
from rest_framework import viewsets


from .models import Post, Category, Tag
from .serializers import (
    PostSerializer, PostDetailSerializer, CategorySerializer,
    CategoryDetailSerializer, TagSerializer, TagDetailSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """文章相关接口"""
    serializer_class = PostSerializer
    queryset = Category.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]  # 写入时权限校验

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        tag_id = self.request.query_params.get('tag')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if tag_id:
            queryset = queryset.filter(tag_id=tag_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """分类相关接口"""
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """标签相关接口"""
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)
