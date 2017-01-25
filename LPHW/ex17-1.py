#-*- coding: UTF-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file).read()#打开,并阅读()的内容

print "The input file is %d bytes long" % len(from_file)

print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, Control-Z to abort."
raw_input()

to_file = open(to_file, 'w').write(input)#open().write()打开()并写入()的内容
print "The file:"
print "Alright, all done."
