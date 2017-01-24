[TOC]

# P.S
`#-*- coding: UTF-8 -*-`
当你在 python 文件中想注释中文的时候就要加上这个 title

## EX4
>浮点数：浮点（英语：floating point，缩写为FP）是一种对于实数的近似值数值表现法，由一个有效数字（即尾数）加上幂数来表示，通常是乘以某个基数的整数次指数得到。

   记住 *=* 的名字是等于(equal)，它的作用是为东西取名。
## EX6
```python
x = "There are %d types of people." % 11 # why not just type 11? %d 指十进制整数
binary = "binary"
do_not = "don't"
y = "Those who know %s and Those who %s." %(binary, do_not) #%s 字符串采用 str()的显示

print x
print y

print "I said: %r." %x  # %r 指字符串 (采用 repr() 的显示)
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print  joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
```

>字符串：一段硬 code ，不想让计算机进行处理而直接输出的代码，字符串中可以包括**格式化支付 s%**

% 后面如果想添加多个变量则需将变量放入 `()`中，且用`,`隔开

Q:格式符 %s , %r 的区别?
>![ex](http://2.im.guokr.com/X6Z07qX7V-B1UQDcxAaGpW3-8nKAPW6c7HfQ7DTphq7EAAAAWwAAAEpQ.jpg)</br>
`%r = representation` 适用于 debug ，因为他会显示出原始数据(raw data)，方便程序员排查错误,而其他的字符是显示给用户看的。

Q:%d 与 %s 的区别？[概述](http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html)
>%s 字符串 (采用str()的显示)；%r 字符串 (采用repr()的显示)；

Q:%d 的意思？
>十进制整数.

tags:ankfied

## EX7
Q:
```python
print "." * 10 #输出结果是什么？
```

>.........

tags: ankfied

## EX9

新分行方法`"`实际上就是分行的意思,有三个`n`所有他能自动分成三行:
```python
print"""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
"""
```

Q:还有`\n = new line`的意思
>
```python
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
```

Q:什么是[转义字符](http://www.runoob.com/python/python-strings.html)？
>在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。

tags:ankfied

## EX10
此处的一题多解
Q: 如何用一个 print 打印出所有的变量:x,y,z?
>
```py
1. print x + y + z
2. print """
    %s %s %s
    """ %(X, Y,Z)
```
tags:ankfied

## EX11
```py
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy."%(age,height,weight)
```

Q:为什么要在 print 后面加 `,` ？
>因为这样的话 Print 之后就不会跳到新的一行，而是等你输入 age 之后 enter 才跳入下一行

Q:raw_input 与 input 的区别？
>关于输入的内容:`input`只能输入数值型且能计算数值,e:int;float，而`raw_input` 则是 string 型的，只会完整的输出字符串。

Q:So, you're '35' old, '6 `\'`20"' tall and '120' heavy. 为什么中间会有个`\'`呢？
>因为print 中用的符号是`%r`如果用的是`%s` 就不会出现斜杠了

tags:ankfied

## EX13
```python
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#print 另一种方法
print """
T %s?
Y %s?
Y %s?
Y %s? """ %(script,first,second,third)
```

Q:`print "The script is called:", script`这后面放`script`是什么个意思??
>`script`实质上就是一个变量,他具体是什么名字真心不重要,因为真正决定他显示出来是什么样子是在Terminal中决定的.

将`raw_input()`与`argv`结合在一起

```python
from sys import argv
x = raw_input("Stupid")
y = raw_input("Fire")
z = raw_input("Mocaccino")
x,y,z = argv
print "The file-name is called:", x
print "It's discribe my best favorite is:", y
print "The second is :", z
```

1. 手动逐行显示x,y,z定义的内容
2. 全部显示print的内容
3. argv = argument variable “参数变量”

tags:ankfied

## EX14
```py
from sys import  argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where Do you live? %s" % user_name
live = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright ,so you said %r about liking me.
You live in %r. Not sure where that is .
And you have a %r computer. Nice.
""" %(likes, live , computer)
```

###NOTES

1. 通过定义变量 `prompt` 来省略重复的话语
2. 如果我想用来……，我该怎么做
3. `input`与`raw_input`的区别,例子如下:

```python
print "And How old are you?"
year = input(prompt)
```

    输出的结果是(如果你当中不填写东西的话),也就是一个无效的值
    > File "ex14.py", line 18, in <module>
    >       </br>year = input(prompt)
    > File "<string>", line 0   
    >    ^
    ></br>SyntaxError: unexpected EOF while parsing

    而`raw_input`则是允许空值的,这大概就是`raw_input`的好处吧,尽管`input()`会将`()`的内容计算出结果.


tags:Ankfied


## EX15
```py
from sys import argv #从系统中导入参数变量

script, filename = argv # 设置两个参数变量，脚本、文件名

txt = open(filename) # 令 txt 为打开文件名的指令

print "Here's your file %r:" % filename #输出文件名(representation 形式)
print txt.read()  # 阅读该文档并输出到 terminal 上

print "I'll also ask you to type the filename again:" #打印这句话
file_again = raw_input ("> ") # 在 raw_input 前提前打印“>_"

txt_again = open(file_again)

print txt_again.read()
```

### NOTICE

- function 与 method 的区别[FR](http://stackoverflow.com/questions/155609/difference-between-a-method-and-a-function) <mark>*Que*</mark>
    + A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.
    + A method is a piece of code that is called by a name that is associated with an object. In most respects it is identical to a function except for two key differences:
        + A method is implicitly passed the object on which it was called.
        + A method is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).


- 得到文件名字更好的方法
    - 我只想到了 `filename = ex15_sample.txt`
    - `filename = "/Users/KZhi/Desktop/Sublime/Python/ex15_sample.txt"` 麻烦


```py
from sys import argv

script, filename = argv

with open (filename, "rb") as txt:  
    print (txt.read())
```
Q:`with-as` 语法的意思?
>是打开某文件，并关闭。`with`语句指定 txt 为*变量* 再打印 txt.read() 只读的内容，再说一句，文件打开之后一定要关闭掉

Q: 如何用 `with-as` 打开多个项目？
```python
    with open("x.txt") as f1, open('xxx.txt') as f2:
    do something with f1,f2
```

- "r" 的内容就如 EX16 中所讲的一般，以只读方式打开文件。

tags:ankfied, question
## EX16 字符写入文件

### Code
```py
#-*- coding: UTF-8 -*-
from sys import argv

script, filename = argv


print "We're going to erase %r. " %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."


raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #打开，并可读写

print "Truncating the file. Goodbye!"
target.truncate() #将文件内容清空

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally, we close it."
target.close()
```

Q:为何这里可以直接 target.write()?
> 因为前面已经定义了 target = open(filename,'w')


### NOTE
Q:如何用一个 target.write() 将 line1 line2 line3 打印出来
> target.write(line1 + "\n" + line2 + "\n" + line3)

`open`有不同的模式打开,如下表:

|模式<a name="openmode"></a>|描述|
|---|----|
|r|以读写方式打开文件,可读取文件信息|
|w|以写方式打开文件，可向文件写入信息。如文件存在，则清空该文件，再写入新内容|
|a|以追加模式打开文件（即一打开文件，文件指针自动移到文件末尾），如果文件不存在则创建|
|r+|以读写方式打开文件，可对文件进行读和写操作。|
|w+|消除文件内容，然后以读写方式打开文件。|
|a+|以读写方式打开文件，并把文件指针移到文件尾。|

tags:ankfied
## EX17 复制文件操作

###Code
```py
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s"%(from_file, to_file)

# we could do these two on one line too, how?

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

input.close()
output.close()
```

###NOTE

Q:如何使下文两行合并为一行？
```python
input = open(from_file)
indata = input.read()
```
> 方法如下
```python
indata = open(from_file).read()
```
Q:`from os.path import exists` 的含义是什么？
>用来判断文件是否存在

Q:将文件内容清空的指令是什么？
>x.truncate()

Q:`%d` 是什么意思？
> - % 表示为格式符，其中可以包含一个**类型码**，用以控制<mark>显示的类型</mark>.
> - %d 十进制整数

Q:如何显示一个变量的字节？
>len(x),sample:`print "The input file is %r bytes long" % len(indata)`


Q:如何判断一个文件是否存在？
>exists(x),sample:`print "Does the output file exist? %r" %exists(to_file)
`

Q:为何要写`output.close()` ？
>The problem is <font color="red">_python does not actually write the file to disk until you execute "output.close()"._ </font>When you end your session, if you forgot to do "output.close()" it will write it to disk for you (it has all the time for me at least). But in my case, it was the same python "session" in which I was trying to both write the file, and then use it.

Q:如何用一行代码来复制文件内容？

```py
# 1
import shutil
shutil.copyfile('test.txt', 'copy.txt')

# 2
with open ('copy.txt','wb') as indata:
    indate.wirte(open('test.txt','rb').read())
```
关于 `shutil` 的 [further reading](https://docs.python.org/3/library/shutil.html)

Q: `open('copy.txt','wb')` 中的 `'wb'` 是什么意思？
> 'wb' = the file is opened for writing in binary mode.

Q: 为何在 windows 系统下最好用 `wb` 而不是 `w` 来打开文件?
>在 Unix sys(Linux, Mac OS), 二进制模式没用，他们对待 text 文件就像对待其他文件一样。而在 windows 系统中，text files are written with slightly modified line endings。 当处理真实的二进制文件(exe, jpg) 时，会造成很严重的问题。因此，当打开那些并不是 test 文件时，应该使用 `wb` 或 `rb`。只有在处理 text file 时 才使用 `w` or `b`。[更多模式](#openmode)。结论就是：无论在什么系统打代码最好都用 wb 格式或 rb 格式

Q: 如何在 terminal 中查询文件内容
>cat -- concatenate and print files 但实际的最大作用是打印文件内容到屏幕上。

tag:ankfied
## EX18：函数
```py
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#ok, that *args is acutally pointless, we can just do this

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

#this just takes one argument

def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
```

###Note
Q:`def` 什么意思?
> def 告诉 python 创建一个函数

Q:函数名称是以字符和下划线 _ 组成的嘛?
> 可以使用下划线来定义函数名称。

Q:函数名称是不是紧跟着园括号() ?圆括号之间可以用来做什么？
> 定义参数

Q:圆括号内多个参数是否以什么符号隔开?
> 逗号

Q:参数名称可否有重复?
> 不可以

Q:如何检查函数定义是否没有问题？

4. 函数定义是以 def 开头的嘛?
6. 紧跟着参数的是不是括号和冒号): ?
7. 紧跟着函数定义的代码是否使用了4个空格的缩进( indent )?
8. 函数结束的位置是否取消了缩进(" dedent")?

Q: 运行一个函数时,检查的四个要点:
>
1. 调运函数时是否使用了函数的名称?
2. 函数名称是否紧跟着`(` ?
3. 括号后有无参数? 多个参数是否以逗号隔开?
4. 函数是否以`)` 结尾?

阅读5遍下面的这几句话:"'运行函数( run)'\'调用函数( call)'\'使用函数( use)'是同一个意思".

tag:ankfied
## EX19
```python
def cheese_and_crackers(cheese_count, boxes_of_crackers):# 定义函数为 cheese_ 并设置其含有两个变量
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) # 简单定义1,2 变量为20,30

print "OR, we can use variables from our script:"
amount_of_cheese = 10 # 定义其为 10
amount_of_crackers = 50 # 定义其为 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 给予该函数两个变量(之前定义的)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # 在函数内进行运算。

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # 给予 cheese_and_crackers 两个参数,进行计算并运行函数
```

```python
coding:UTF-8
# 1
def stupid_computer (cpu,keyborad):
    print "What's your cpu are? :%s " %cpu
    print "What kind of keyborad you like? %s" %keyborad

print "We do like computers.And now i'm ganna ask you some questions"

ARM = "binbo"
ban = "Shit"

stupid_computer(ARM, ban)

# 2
def favor_of_grils (height, hobby, weight):
    print "My dream girls height is %r" %height
    print "My dream girls hobby is %s" %hobby
    print "My dream girls weight is %s" %weight

print "So, may I ask you 'what's your favor of girls? "

favor_of_grils("170cm", 'sports+books', '52k')

# 3
#运用 raw_input 到函数内的参数
def filetransfer (orginal, type):
    print "Confirm again!  Your files are: %r " %orginal
    print "And transfer to %r? " %type

from_file = raw_input("Which file you wanna copy? ")
to_file = raw_input("And copy to where? ")

filetransfer(from_file,to_file)

# 4 复制文件
#将函数编程真正意义上的 copy 行为
def file_trans (orginal,target):
    with open (target, 'wb') as indate:
        indate.write(open(orginal, 'rb').read())

from_file = raw_input("You want copy from? ")
raw_input("Yes Please.")
to_file = raw_input("To here ")

file_trans(from_file,to_file)
print "DONE!"

# 5 复制文件
import shutil

def file_trans_2(target,orginal):
    shutil.copyfile(target,orginal)

from_file = raw_input("You want copy from? ")
raw_input("Yes Please.")
to_file = raw_input("To here ")

file_trans_2(to_file,from_file)
print "DONE!"

# 6 复制文件
from sys import argv

scropt, from_file, to_file = argv

def file_trans_3(input, output):
    indate = open(from_file).read()
    output = open(to_file, 'wb').write(indate)

file_trans_3(from_file, to_file)

print "Transction complete!"


#7 写入文件
from sys import argv

script, filename = argv

def file_wirtting(target):
    print "Opening the file %r ..." %target
    target = open(target, 'wb').write(line1 + "\n" + line2 + "\n" + line3)

line1 = raw_input("Your 1st line :")
line2 = raw_input("Your 2nd line:")
line3 = raw_input("Your 3rd line:")

file_wirtting(filename)

## mistake
from sys import argv

script, filename = argv

def file_wirtting(target):
    print "Opening the file %r ..." %target
    target.open(target, 'wb').write(line1 + "\n" + line2 + "\n" + line3)

line1 = raw_input("Your 1st line :")
line2 = raw_input("Your 2nd line:")
line3 = raw_input("Your 3rd line:")
之前为什么错了，因为 x 不能直接 x.wirte or truncate 因为这个是在 open 之后的操作


```
Q:为什么不直接 file = open(target, 'ab+').truncate()，然后接 file.write(line1...)
> 因为当 file = open(target,'ab+') 时，file 就包含了这个指令即以追加方式打开输入的 target 文件，如果以 file = open(target, 'ab+').truncate(). 则定义 file 为以追加方式打开 target 文件并清空。 file.write() = file = open(target, 'ab+').truncate().write()

Q: 如何函数内的参数想包含英文或中文怎么办?
> 加`'x'` 即可

Q: 为函数参数(中英文) 加`''` 为什么不加 `" "`?他们的在哪里？
> 事实上并没有区别，唯一的区别在于如果你的 def 中是%r 则在 terminal 中 `"x"` 显示的会是`'x'`。

tag:ankfied

## EX20
```py
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

current_line = 1
print_a_line(current_line, current_file)
```

Q:`f.readline()` 是什么意思？
>逐行读出


Q:[什么是`seek()` function?](http://stackoverflow.com/questions/11696472/seek-function)
>A seek() operation moves that pointer to some other part of the file so you can read or write at that place.

Q:seek 的句法是？
```python
fp.seek(offset, from_what)
```

Q:分别解释当中的各部分
>`fp` 是你正在处理的文件指针(file pointer);`offset` 是指你会移动多少字节;`from_what` defines your point of reference:

Q:`fp.seek(offset,from_what)`中的`from_what` 的可使用常量有哪些？分别代表什么意思？ 如果省略参数又是什么意思？
>
- **0**:means your reference point is the **beginning** of the file，若省略，则也代表0
- **1**: means your reference point is the **current** file position
- **2**: means your reference point is the **end** of the file.

Q:为什么使用 fp.seek() 函数呢？
>因为当你在管理文件的时候，你所正在处理的文件中的指针必定在某个位置。当刚打开时，可能处于开头，当随着你的操作可能就移动了。
>Never forget that when managing files, there'll always be a position inside that file where you are currently working on. When just open, that position is the beginning of the file, but as you work with it, you may advance.

>`seek` will be useful to you when you need to `walk` along that open file, just as a path you are traveling into.

Q:具体解释下 **+=** 的运用
>a += b ---> a = a + b

## EX21 函数可以返回东西
### Code
```py
def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a + b # 赋予 add 函数其值

def subtract(a, b):
    print "Subtracting %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d " %(a, b)
    return a / b

print "let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2, 10)

print "Age : %d, height :%d, weight: %d, iq: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))#需要 4 个已知的量，打印顺序从右到左，先打印 divide 函数

print "That becomes: ", what, "can you do it by hand?"
```

### NOTES
Q:解出`what = add(age, subtract(height, multiply(weight, divide(iq, 2))))` what 的值，已知, Age : 35, height :74, weight: 180, iq: 60
> what = -4391

# 第一部分的总结
|字符|名称|意义|
|:-:|:-:|:-:|
|print|打印|将内容打印出来|
|#|注释|不运行的内容，仅用来注释该行代码|
|<=|小于等于号|数学运算符号|
|>=|大于等于号|数学运算符号|
|%|格式化字符|控制显示的内容|
|%s|s=string|输出字符串给用户|
|%r|r=representation|显示原始数据(raw data),方便程序员排查错误|
|%d|d=decimal|十进制|
|float| 浮点数|一种对实数的近似值数值表现法|
|string|字符串|你想要展示给别人的，或者你需要从程序中“导出“的一小段字符”。|
|print """|打印多行|打印出多行字符串|
|\|转义字符|若在字符串中需使用特殊字符，python 用反斜杠
|\n|n= new line| 创建新行|
|\t|t = tab|缩进|
|raw_input()|输入|括号内可放提示，读取控制台的输入|
|input()|输入|`def input(prompt):return(eval(raw_input()))`|
|from sys import `argv`| 参数变量(argument variable)|变量包含了你传递给 Python 的参数|
|from `sys` import argv|模组(module)|导入进来的功能|
|x = open(file)| 打开|从 Open 获得的东西是一个 file|
|y.open('x.txt','rb')|以读写方式打开，可读取文件信息|
|y.open('x.txt','wb')|以写模式打开|若文件存在则覆盖其内容再读写，若不存在则创建内容|
|y.open('x.txt','ab+')|以读写反思打开文件|文件指针放置末尾|
|f.readline()|逐行阅读|
|fp.seek(offset, from_what)|
|x.truncate()|清空|将括号内的文件内容清空|
|from os.path import `exists`|存在 命令|将文件名字字符串作为参数，如果文件存在，则返回 True ，否则为 False.|
|terminal cat|concatenate and print files|打印文件内容到屏幕上|
|def|定义函数|告诉 python 创建一个函数|
|a += b|a = a + b|
|return|回传|将结果回传给初始变量|

## EX25
`file.split()` 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个字符串

`str.split(str="", num=string.count(str))`

参数
- str -- 分隔符，默认为空格
- num -- 分割次数

返回值
返回分割后的字符串列表

`return sorted()` built-in function that build a new sorted list from an iterable.可以用来排序数字和字母。

`List.pop([i])` removes and returns tha last item in the list if the i=0.

>
```python
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
```

若在 terminal 中输入的时候为 `words = "'All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.'"`
则使用 print_last_word(word) 函数的时候，得到的 就是 `wait`，`-1` 的意思就是把倒数第一个字符拿到前面来。


Q:如何从一个 x.py 文件中一次性导入所有的函数？
> from x.py import *

Q:如何书写一个断 字符 的函数？以`break_words`为函数名称，以 `' '` 为间隔
>
```py
def break_words(stuff):
    words = stuff.split(' ')
    return words
```

Q:已得到 `words = 'All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.'` ,创造一个函数用来排序
>
```py
def sort_words(words):
    return sorted(words)
```

Q: 如何打印 字符串 中的第一个字符 或 最后一个字符？
>
```py
def print_first_word(words):
    word_0 = words.opp(0), word_1 = words.opp(-1)
    print word
```
