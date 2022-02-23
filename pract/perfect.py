no=int(input("Enter Number:"))
sum=0
for i in range(1,no-1):
	if(no%i==0):
		sum=sum+i
		
if(sum==no):
	print("Perfect number...")
	
else:
	print("not Perfect number...")
