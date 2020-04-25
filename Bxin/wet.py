
import jieba
# 分词
str_name = '肖申克的救赎'
str_list = jieba.cut_for_search(str_name)

for str_ in str_list:

    print(str_)