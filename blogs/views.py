from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blogs import models
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.core import serializers
import json


# 这个函数主要是把查询的内容渲染到 index.html页面去
def index(request):

    blog_index = models.Article.objects.all().order_by('-id')
    context = {
        'blog_index': blog_index,
    }
    return render(request, 'index.html', context)


def getCate(id):
    """
    获取分类名称
    @param id: 分类id
    @return:
    """
    number_data = models.Category.objects.filter(id=id)
    for x in number_data:
        return x.name

    return ''


def article(request):
    """
    返回josn数据提供给前端
    @param request:
    @return:
    """
    # 和前端约定的返回格式
    result = {"resCode": '0', "message": 'success', "data": []}

    # 获取所有文章，对应SQL：select * from Article
    all_article = models.Article.objects.all()

    # 第一种方法，序列化为 Python 对象，结果result["data"]的数据结构不太符合要求
    # result["data"] = serializers.serialize('python', all_article)
    # return JsonResponse(result)

    # 第二种方法，将model对象逐个转为dict字典，然后设置到data的list中
    for server in all_article:
        server = model_to_dict(server)
        server['category_name'] = getCate(server['category'])
        server['tags'] = serializers.serialize('python', server['tags'])  # 外键模型对象需要序列化，或者去除不传递
        result["data"].append(server)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")
    # return JsonResponse(result)


def get_category(request):
    # 和前端约定的返回格式
    result = {"resCode": '0', "message": 'success', "data": []}

    # 获取所有文章，对应SQL：select * from Article
    all_article = models.Category.objects.all()
    # 将model对象逐个转为dict字典，然后设置到data的list中
    for server in all_article:
        server = model_to_dict(server)
        result["data"].append(server)

    # return HttpResponse("Hello world")
    return JsonResponse(result)


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
