"""
暂停三秒输出
"""
# 使用time模块的sleep()函数

from time import sleep

dic = {'1':"我",'2':"爱",'3':"你"}
for key,value in dic.items():
    print(key , value)
    sleep(3)