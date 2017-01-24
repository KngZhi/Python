def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACT %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(25, 2)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d\n" % (age, height, weight, iq)

print "Here is a puzzle"

x = divide(iq, 2)
y = multiply(weight, x)
z = subtract(height, y)
s = add(age, z)
what = height + age - weight * (iq / 2)
#s = add(age,subtract(height,multiply(weight,divide(iq,2)))
print "That becomes: ", what, "Can you do it by hand?"
