import json

from django import http
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from Bxin.settings import logger
from .models import Movie, MovieDetail
import jieba


# 首页电影
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
                "id":mo.id,
                "name":mo.name,
                "score":mo.score,
                "image_file_id":mo.image_file_id,
            })


        context = {

            'contents': result_list,
        }

        # print(context)

        # 返回结果
        return render(request, 'index.html', context)




# 联想词
class AssWrodView(View):

    def get(self, request):


        # 接收用户输入的字符串
        str_name = request.GET.get('search')

        print(str_name)

        # 分词
        str_list = jieba.cut_for_search(str_name)

        # 查询
        for str_ in str_list:

            try:
                movie = Movie.objects.filter(name__contains=str_)[:3]

            except Exception as e:
                logger.error(e)
                return

        data = []
        # 遍历查出相似电影名
        for mo in movie:

            data.append({
                "id":mo.id,
                "name":mo.name,
            })

        print(data)
        # 返回响应
        return http.JsonResponse({'code':200,'errmsg':'OK','data':data})