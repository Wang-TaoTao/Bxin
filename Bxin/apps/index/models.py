from django.db import models

# Create your models here.

from django.db import models

# 电影模型类
class Movie(models.Model):
    """电影"""


    name = models.CharField(max_length=80, verbose_name='电影名称')
    score = models.CharField(max_length=10, verbose_name='电影评分')
    desc = models.CharField(max_length=50,null=True,verbose_name='一句话影评')
    image = models.CharField(max_length=80, verbose_name='图片地址')
    image_file_id = models.ImageField(null=True, verbose_name='图片file_id')
    detail_link = models.CharField(max_length=80,verbose_name='详情页链接')




    class Meta:
        db_table = 'tb_movie'
        verbose_name = '电影信息'





# 电影详情页模型类
class MovieDetail(models.Model):

    '''详情页'''
    name = models.CharField(max_length=80, verbose_name='电影名称')
    score = models.CharField(max_length=10, verbose_name='电影评分')
    direct = models.CharField(max_length=30, verbose_name='导演')
    etc = models.CharField(max_length=80, verbose_name='编剧')
    performer = models.CharField(max_length=256, verbose_name='主演')
    types = models.CharField(max_length=50, verbose_name='类型')
    address = models.CharField(max_length=50, verbose_name='地区')
    language = models.CharField(max_length=80, verbose_name='语言')
    date = models.CharField(max_length=256, verbose_name='上映日期')
    # 外键关联
    for_key = models.ForeignKey(Movie,null=True,on_delete=models.CASCADE, verbose_name='index')



    class Meta:
        db_table = 'tb_detail'
        verbose_name = '电影详情信息'
