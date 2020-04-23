

import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',user='root',password='mysql',database='bxin',charset='utf8')
# 获取游标
cur = conn.cursor()

# 从mysql获取图片地址
sql = 'select name,image from tb_movie;'
# url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg'
row_count = cur.execute(sql)

result_list = []

i=1
# 获取并构造数据格式
for line in cur.fetchall():

    result_list.append({
        "name":'{}'.format(i),
        "image_url":line[1],
    })
    i+=1


# print(result_list)

# 下载图片
import urllib.request
for i in result_list:

    url = i['image_url']
    filename = './utils/images2/{}.jpg'.format(i['name'])

    urllib.request.urlretrieve(url=url, filename=filename)