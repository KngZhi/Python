from sys import argv

sript, ex15_sample = argv
txt = open(ex15_sample)

print "Here's your file %r:" % ex15_sample
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input(">>>")
txt_again = open(file_again)
print txt_again.read()
