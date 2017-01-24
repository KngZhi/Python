from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print "Copying the %s to %s" % (from_file, to_file)
print "And, the file is %r byte" %len(from_file)
print "Is this file exists? %r" %exists(to_file)
print "Let's go!"

input = open(from_file).read()
to_file = open(to_file, 'a+').write(input)

print "Done!"
