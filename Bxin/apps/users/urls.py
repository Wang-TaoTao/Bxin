
from django.conf.urls import url


from . import views

urlpatterns = [

    # 注册
    url(r'^register/$',views.RegisterView.as_view(),name='register'),
    # 登录
    url(r'^login/$',views.LoginView.as_view(),name='login'),

]