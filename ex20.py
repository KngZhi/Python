#coding:UTF-8
from sys import argv

script, input_file = argv #调用两个参数变量

def print_all(f): #定义`print_all` 函数包含一个 f 变量
	print f.read() # 打印 f 中的全部内容

def rewind(f): #定义 rewind 函数包含一个 f 变量
	f.seek(0) # seek 函数指针略过两个字节

def print_a_line(line_count, f):
	print line_count, f.readline() #读出当前行
	line_count += 1
	print line_count, f.readline()
	line_count += 1
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) #将当前文件的指针放置为开始

print "Let's print three lines:"

current_line = 2
print_a_line(current_line, current_file)

