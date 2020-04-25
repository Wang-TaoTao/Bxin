
from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [

    # 首页展示
    url(r'^$',views.IndexView.as_view(),name='index'),

    # 联想词
    url(r'^index/assword/$',views.AssWrodView.as_view(),name='asword'),

]
