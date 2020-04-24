import json

from django import http
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from Bxin.settings import logger
from .models import Movie, MovieDetail


class IndexView(View):
    """提供首页电影"""

    def get(self, request):

        try:
            movies = Movie.objects.all()[:10]
        except Exception as e:
            logger.error(e)
            return
        result_list = []

        for mo in movies:

            result_list.append({
                "name":mo.name,
                "score":mo.score,
                "image_file_id":mo.image_file_id,
            })


        context = {

            'contents': result_list,
        }

        print(context)

        # 返回结果
        return render(request, 'index.html', context)




# 联想词
class AssWrodView(View):

    def get(self, request):

        # 接收参数
        asword = '我'
        # 校验并查询参数
        try:
            word = Movie.objects.filter(name__contains=asword).order_by('name')
        except Exception as e:
            logger.error(e)
            return http.HttpResponseNotFound('关键字不存在')

        # 构造数据
        result_list = []
        for item in word:

            result_list.append({
                "name":item.name,
            })
        print(result_list)
        # 返回数据
        return http.JsonResponse(result_list)