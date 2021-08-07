"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
输出指定个数的斐波那契数列
"""

number = int(input("输出斐波那契数列的个数为： "))
list = [0,1]
for i in range(number):
    list[i + 1] = list[i - 1] + list[i]
    x = list[i + 1]
    list.append(x)
print(list[0:number])
