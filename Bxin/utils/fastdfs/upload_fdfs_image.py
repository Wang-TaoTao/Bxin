import pymysql

# 建立连接
conn = pymysql.connect(host='localhost', user='root', password='mysql', database='bxin', charset='utf8')

# 游标
cur = conn.cursor()

##  1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client
# 2. 创建FastDFS客户端实例
client = Fdfs_client('client.conf')
# 3. 调用FastDFS客户端上传文件方法 将所有电影图片上传到fastdfs的stroger
for i in range(2,251):
    ret = client.upload_by_filename('/home/python/Desktop/Bxin_project/Bxin/Bxin/static/images2/{}.jpg'.format(i))
    # 4.将图片上传信息打印出来，便于访问。
    print(ret)


    sql = "insert into tb_movi(image_file_id) values(ret[Remote file_id])"

    row_count = cur.execute(sql)

    cur.close()

    conn.close()


# ret = {
#     'Group name': 'group1',
#     'Remote file_id': 'group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg',
#     'Status': 'Upload successed.',
#     'Local file name': '/Users/zhangjie/Desktop/kk.jpeg',
#     'Uploaded size': '69.00KB',
#     'Storage IP': '192.168.103.158'
# }




