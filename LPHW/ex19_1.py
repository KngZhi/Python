def chair_and_table(chair_count, table_count):
	print """
	You have %d chairs!
	You have %d tables!
	Pales, you got enought for a party!
	Get a blanket , plus.\n
	""" % (chair_count, table_count)
print "We can just give the function numbers directly:"
chair_and_table(20, 31)

print "OR, we can use variables from our script:"
chair_count = raw_input()
table_count = raw_input()

chair_and_table(int(chair_count), int(table_count))