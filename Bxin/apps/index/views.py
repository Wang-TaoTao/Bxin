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
            movies = Movie.objects.all()
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

        # 接收联想词

        # 校验并查询

        # 构造格式


        print("联想词")
        # 返回响应
        return http.JsonResponse({""})