import pymysql
from Bxin.settings import logger


'''图片上传到fastdfs并且将返回的file_id存入mysql的image_file_id字段'''


# 建立连接
conn = pymysql.connect(host='localhost', port=3306,user='root', password='mysql', database='bxin', charset='utf8')
# 游标
cur = conn.cursor()


##  1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client
#  2. 创建FastDFS客户端实例
client = Fdfs_client('client.conf')
#  3. 调用FastDFS客户端上传文件方法 将所有电影图片上传到fastdfs的stroger
for i in range(1,251):
    ret = client.upload_by_filename('/home/python/Desktop/Bxin_project/Bxin/Bxin/static/images2/{}.jpg'.format(i))
    #  4.将图片上传信息打印出来，便于访问。
    print(ret)
    print(ret['Remote file_id'])

    try:
        value_ = ret['Remote file_id']

        sql = "update tb_movie set image_file_id = '%s' where id='%i';" % (value_,i)

        row_count = cur.execute(sql)
        conn.commit()
    except Exception as e:
        logger.error(e)
        print("有异常")
        break


    print("success")

# 关闭连接
cur.close()
conn.close()
