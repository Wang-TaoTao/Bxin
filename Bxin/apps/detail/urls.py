
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    # 电影详情页
    url(r'^detail/(?P<movie_id>\d+)/$',views.DetailView.as_view(),name='detail'),

    # 电影详情页热播电影
    url(r'^hot/(?P<movie_id>\d+)/$',views.HotMovieView.as_view(),name='hot'),

]
