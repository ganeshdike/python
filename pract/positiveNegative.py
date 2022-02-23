l=[1,-2,3,-4,5,-6,7,-8,9]
pos=0
neg=0
for i in l:
	if(i<0):
		neg=neg+1
	else:
		pos=pos+1
		
print(l)
print(pos)
print(neg)
