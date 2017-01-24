from sys import argv

script , input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count, f.readline()

current_file = open(input_file)

print "Let's print all the whole file:\n"
print_all(current_file)

print "Let's rewind, kind of like a tape."

rewind(current_file)

print "Let's type the file line by line meanwhile the lines"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)