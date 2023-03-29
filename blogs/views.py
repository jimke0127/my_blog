from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blogs import models


def hello(request):
    return HttpResponse('Hello django!')


def orm(request):
    # 第一种方法：
    # models.Article.objects.create(title='增加标题一', category_id=3, body='增加内容一', user_id=1)
    # 第二种方法：添加数据，实例化表类，在实例化里传参为字段和值
    # obj = models.Article(title='增加标题二', category_id=3, body='增加内容二', user_id=1)
    # 写入数据库
    # obj.save()
    # 第三种方法：将要写入的数据组合成字典，键为字段值为数据
    dic = {'title': '增加标题三', 'category_id': '4', 'body': '增加内容三', 'user_id': '1'}
    # 添加到数据库，注意字典变量名称一定要加**
    models.Article.objects.create(**dic)

    return HttpResponse('orm')
