import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from .models import Product, Comment


def index(request, *args, **kwargs):
    try:
        sentiments = Comment.objects.values()
        sentiments = list(sentiments)
        keys = {
            'id': '序列',
            'c_id': '评论ID',
            'p_id': '商品id',
            'p_name': '商品',
            'c_time': '评论时间',
            'short': '评论内容',
            'sentiment': '情感倾向',
            'add_time': '爬取时间'
        }
        context = {
            'results': json.dumps(sentiments, ensure_ascii=False),
            'keys': json.dumps(keys, ensure_ascii=False),
        }
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponseNotFound(f"<h1 style='color:red'>{e}</h1>")
 