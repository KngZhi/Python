# -*- coding: UTF-8 -*-
formatter = "%r %r %r %r"
#以下就是将括号中的内容打印出来,L6中则就是其本身
#
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)#
print formatter %(
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight."
	)
print formatter % ('nani', "sing", "some", "song")

#加分习题
#2. 在L15中可见,''与""在print时性质是一样的