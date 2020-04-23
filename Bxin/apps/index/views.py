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
            movie = MovieDetail.objects.filter(name__contains=movie_name)
        except Exception as e:
            logger.error(e)

        for mo in movie:
            print(mo.name)

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


