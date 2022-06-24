# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author : SecSin
# @Time : 2022/6/13 11:07
# @File : apis
# @Project : typeidea
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response

from django.http import JsonResponse

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    """评论相关接口"""
    # permission_classes = [IsAdminUser]  # 写入时权限校验
    parser_classes = [JSONParser, FormParser]
    """视图集"""
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    # 搜索
    search_fields = ('id', 'title')

    # 添加链接
    @action(methods=['post'], detail=False)
    def add_link(self, request, *args, **kwargs):
        href = request.data.get('href', None)
        if href:
            print(href)
            obj = Link.objects.filter(href=href).first()
            if obj:
                return JsonResponse({
                    'status': '1001',
                    'msg': '已经存在此友链'
                })
            else:
                # user = request.user
                # print(user)
                serializer = LinkSerializer(data=request.data)
                # print(serializer)
                print(request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        'status': '1000',
                        'msg': '添加成功'
                    })
                else:
                    # print(serializer.errors)
                    return JsonResponse({
                        'status': '1002',
                        'msg': '插入数据不合法'
                    })
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        pass

    # 删除链接
    @action(methods=['delete'], detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        count = 0
        delete_id = request.data.get('id', None)
        print(delete_id)
        if not delete_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        for i in delete_id.split(','):
            obj = Link.objects.filter(id=i).first()
            if obj:
                obj.delete()
                count = count + 1
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return JsonResponse({
            'code': 200,
            'msg': '删除成功',
            'num': count
        })

    # 修改信息
    @action(methods=['put'], detail=False)
    def edit_link(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        if id:
            obj = Link.objects.filter(id=id).first()
            # print(request.data)
            serializer = LinkSerializer(instance=obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(update_fields=['title', 'href', 'created-time', 'id'])
                return JsonResponse({
                    'code': 200,
                    'msg': '更新成功',
                })
            else:
                return JsonResponse({
                    'code': 201,
                    'msg': '更新失败',
                })
        else:
            return Response(status.HTTP_204_NO_CONTENT)

