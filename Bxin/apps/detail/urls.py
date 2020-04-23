
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # 电影详情页
    url(r'^index/detail/(?P<movie_id>\d+)/$',views.DetailView.as_view(),name='detail'),

]
