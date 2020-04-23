from django import http
from django.shortcuts import render

from django.views import View

from Bxin.settings import logger
from .models import Movie, MovieDetail

class IndexView(View):

    def get(self,request):

        # 接收参数
        movie_name = request.GET.get('movie_name')
        movie_name = "肖申克的救赎"

        # 校验参数并查询
        try:
            movie = Movie.objects.filter(name__contains=movie_name)
        except Exception as e:
            logger.error(e)

        for mo in movie:
            print(mo.image)

        context = {}




        # context = {
        #     "name":movie.name,
        #     # "direct":movie_detail.direct,
        #     # "performer":movie_detail.performer,
        #     # "time":movie_detail.time,
        #     # "type":movie_detail.type,
        #     # "score":movie_detail.score,
        #     "cinecism":movie.desc,
        #     "image_url":movie.image,
        # }


        return render(request,'index.html',context=context)



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