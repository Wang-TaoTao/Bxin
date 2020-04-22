from django.shortcuts import render

# Create your views here.
from django.views import View


class DetailView(View):

    '''电影详情页显示'''

    def get(self,request):

        context = {}

        return render(request,'detail.html',context=context)