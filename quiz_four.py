"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
import sys
year = int(input("请输入年： "))
month = int(input("请输入月： "))
day = int(input("请输入日： "))

number = 0
month_day = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30}
# 判断是不是闰年
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    month_day['2'] = 29

for key,value in month_day.items():    
    if month > int(key):
        number += value
    else:
        break
number += day
print("这是今年的第% d 天"% number)



