# 1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client
# 2. 创建FastDFS客户端实例
client = Fdfs_client('client.conf')
# 3. 调用FastDFS客户端上传文件方法 将所有电影图片上传到fastdfs的stroger
for i in range(2,251):
    ret = client.upload_by_filename('/home/python/Desktop/Bxin_project/Bxin/Bxin/utils/images2/{}.jpg'.format(i))
    # 4.将图片上传信息打印出来，便于访问。
    print(ret)




