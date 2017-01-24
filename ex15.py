#-*- coding: UTF-8 -*-
from sys import argv

sript, ex15_sample = argv#引入一个包, 并以两个变量从左到右的顺序来解包
txt = open(ex15_sample)#`open`一般对应打开的是文件这个对象

print "Here's your file %r:" % ex15_sample#将文件名字输出
print txt.read()#进行只读
print txt.close()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")#用户输入文件名

txt_again = open(file_again)#打开文件对象
print txt_again.read()#对文件进行读取
print txt.close