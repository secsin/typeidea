from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

from .models import Post, Tag, Category
from config.models import SideBar


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        print(context)
        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'postlist'
    template_name = 'blog/list.html'


# 标签页的处理，重写两个方法，分别获取上下文数据传入模板以及获取指定Model或QuerySet数据
class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.kwargs中的数据是从url定义中拿到
        tag_id = self.kwargs.get('tag_id')
        # 获取对象实例，如果获取不到就抛出404错误
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """ 重写querset，根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


# 分类页的处理，重写两个方法，分别获取上下文数据传入模板以及获取指定Model或QuerySet数据
class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        """ 重写querset，根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class PostDetailView(CommonViewMixin, DetailView):
    template_name = 'blog/detail.html'
    queryset = Post.latest_posts()
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


# class PostListView(ListView):
#     queryset = Post.latest_posts()
#     paginate_by = 1
#     context_object_name = 'postlist'  # 如果不设置此项，在模板中需要使用object_list变量
#     template_name = 'blog/list.html'


# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#     # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id)
#     if tag_id:
#         postlist, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         postlist, category = Post.get_by_category(category_id)
#     else:
#         postlist = Post.latest_posts()
#     context = {
#         'category': category,
#         'tag': tag,
#         'postlist': postlist,
#         'sidebars': SideBar.get_all()
#     }
#     context.update(Category.get_navs())
#     return render(request, 'blog/list.html', context=context)


# def post_detail(request, post_id=None):
#     # return HttpResponse('detail')
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#
#     context = {
#         'post': post,
#         'sidebars': SideBar.get_all()
#     }
#     context.update(Category.get_navs())
#     return render(request, 'blog/detail.html', context=context)
