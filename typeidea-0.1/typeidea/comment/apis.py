# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/13 11:07
# @File : apis
# @Project : typeidea
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    """评论相关接口"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]  # 写入时权限校验

    def filter_queryset(self, queryset):
        target = self.request.query_params.get('target')
        # print(target)
        if target:
            queryset = queryset.filter(target=target)
        return queryset
