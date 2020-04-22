from django.shortcuts import render

from django.views import View

from Bxin.settings import logger
from .models import Movie, MovieDetail

class IndexView(View):

    def get(self,request):

        # 接收参数
        # movie_id = request.GET.get('movie_id')

        # 校验参数并查询
        try:
            movie = Movie.objects.filter(id=487)
        except Exception as e:
            logger.error(e)


        # try:
        #     movie_detail = MovieDetail.objects.filter(id=1)
        # except Exception as e:
        #     logger.error(e)
        # 构造数据
        result_list = []
        for mo in movie:

            context = {}

            result_list.append({
                "name":mo.name,
            })

        context = {
            "name":result_list,
        }

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


