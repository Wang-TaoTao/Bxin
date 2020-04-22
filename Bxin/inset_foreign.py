
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql',database='Bxin', charset='utf8')

# 获取游标对象
cursor = conn.cursor()


# sql = 'insert into tb_detail where '