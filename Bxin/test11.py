detail_all = ['\n        导演: 吕克·贝松\n        编剧: 吕克·贝松\n        主演: 让·雷诺 / 娜塔莉·波特曼 / 加里·奥德曼 / 丹尼·爱罗 / 彼得·阿佩尔·马图斯维奇 / 弗兰克·赛格 / 麦温 / 乔治·马丁 / 罗伯特·拉萨多 / 亚当·布斯奇 / 马里奥·托迪斯科 / 萨米·纳塞利\n        类型: 剧情 / 动作 / 犯英语 / 意大利语 / 法语\n        上映日期: 1994-09-14(法国)\n        片长: 110分钟(剧场版) / 133分钟(国际版)\n        又名: 杀手莱昂 / 终极追ofessional\n        IMDb链接: tt0110413\n\n']

try:
    temp = {}
    direct = detail_all[0].split('\n')[1]

    temp['direct'] = "".join(direct).split(":")[1]

    etc = detail_all[0].split('\n')[2]
    temp['etc'] = "".join(etc).strip().split(":")[1]
    #
    performer = detail_all[0].split('\n')[3]
    print(performer)
    temp['performer'] = "".join(performer).strip().split(":")[1].split("类型")[0]
    #

    address = detail_all[0].split('\n')[5]
    temp['address'] = "".join(address).strip().split(":")[1]

    # language = detail_all.strip().split('\n')[6]
    # temp['language'] = "".join(language).strip().split(":")[1]
    #
    # types= detail_all.strip().split('\n')[3].split("类型:")[1]
    # temp['types'] = "".join(types).strip()


    #


except Exception as e:
    print(e)

# print(directs)
# print(etc)
# print(etcs)

print(temp)