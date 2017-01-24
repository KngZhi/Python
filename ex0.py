from os import listdir

filename = '/Users/KZhi/pictures'
m = listdir(filename)

h=[]

for x in m:
	if x[-3:]=='jpg':
		h.append(x)
print h