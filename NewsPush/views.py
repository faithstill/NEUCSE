# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import models
from treeView.models import treeView
from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Create your views here.
# something wrong
def index(request):
    news_list = models.NewsPost.objects.all()
    nodes = treeView.objects.all()
    now = datetime.now()
    limit = 3  # 每页显示的记录数
    paginator = Paginator(news_list, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        news_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        news_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        news_list = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render(request, 'NewsPush/index.html', {'news_list': news_list, 'nodes': nodes, 'now': now})

def news_content_page(request,news_list_id):
    news = models.NewsPost.objects.get(pk=news_list_id)
    nodes = treeView.objects.all()
    return render(request,'NewsPush/news_content_page.html',{'news': news, 'nodes': nodes})
