from sys import argv
script, test = argv
txt = open(test)

print "Here's the file %r:" %test
print txt.read()
print txt.close()