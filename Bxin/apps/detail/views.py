from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View
# 商品详情页
from Bxin.settings import logger
from apps.index.models import Movie,MovieDetail


# 电影详情页
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
            'movie': movie,
            'moviedetail': moviedetail,
        }

        # 返回响应
        return render(request, 'detail.html', context)




# 电影详情页热播电影
class HotMovieView(View):

    def get(self, request, movie_id):

        # 查询电影信息
        try:
            movie = Movie.objects.order_by('-score')[:2]
        except Exception as e:
            logger.error(e)
            return render(request, '404.html')

        # 构造数据格式
        hot_movie = []
        for mo in movie:

            hot_movie.append({
                'movie_id':mo.id,
                'name':mo.name,
                'score':mo.score,
            })

        print(hot_movie)
        # 返回响应
        return http.JsonResponse({'code': 200, 'errmsg': 'OK', 'hot_movie': hot_movie})