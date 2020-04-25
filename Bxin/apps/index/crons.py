import os
import time

from django.template import loader

from Bxin import settings
from Bxin.settings import logger
from apps.index.models import Movie



def generate_static_index_html():

    '''生成静态主页html文件'''

    print('%s: generate_static_index_html' % time.ctime())

    # 查询所有电影
    try:
        movies = Movie.objects.all()
    except Exception as e:
        logger.error(e)
        return
    result_list = []

    for mo in movies:
        result_list.append({
            "id": mo.id,
            "name": mo.name,
            "score": mo.score,
            "image_file_id": mo.image_file_id,
        })
    # 构造数据
    context = {

        'contents': result_list,
    }


    template_index = loader.get_template('index.html')

    html_text = template_index.render(context)

    file_path = os.path.join(settings.STATICFILES_DIRS[0],'index.html')
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(html_text)

