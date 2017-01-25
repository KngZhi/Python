# coding:UTF-8
def add(a,b):
	print "Adding %d + %s" %(a,b)
	return a + b

def subtract(a, b):
	print "Subtracting %d - %d" %(a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %s" %(a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %s " %(a, b)
	return a / b

print "let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age : %d, height :%d, weight: %d, iq: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))#需要 4 个已知的量，打印顺序从右到左，先打印 divide 函数

print "That becomes: ", what, "can you do it by hand?"

print what = divide(iq,2) / weight - height + age