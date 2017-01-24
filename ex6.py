# -*- coding: UTF-8 -*-

x = "There are %d types of people." % 11
binary = "binary"
do_not = "don't"
y = "Those who know %s and Those who %s." %(binary, do_not)
# 定义x 然后定义"binary"&"do_not"然后用y将两个词连接起来
print x
print y

print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print  joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e