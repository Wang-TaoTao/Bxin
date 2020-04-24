from django.shortcuts import render

# Create your views here.
from django.views import View
# 商品详情页
from Bxin.settings import logger
from apps.index.models import Movie,MovieDetail


class DetailView(View):

    def get(self,request,movie_id):

        # 获取当前movie信息
        try:
            movie = Movie.objects.get(id=movie_id)
        except Exception as e:
            logger.error(e)
            return render(request, '404.html')

        # 获取当前movie详情信息
        try:
            moviedetail = MovieDetail.objects.filter(name__contains=movie.name)
        except Exception as e:
            logger.error(e)
            return render(request, '404.html')



        # 渲染页面
        context = {
            'categories': '1',
            'breadcrumb': '2',
            'movie': movie,
            'moviedetail': moviedetail,
        }

        return render(request, 'detail.html', context)

