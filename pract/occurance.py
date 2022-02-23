l=[1,2,3,4,5,6,7,8,9]
n=int(input("enter number to search:"))
f=0
for i in l:
	if i==n:
		f=1
		break
		
if f==0:
	print("number not found")

else:
	print("number found")

