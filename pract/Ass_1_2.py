print("number is prime or not");
no=int(input("Enter number:"))
k=0
for i in range(2,no):
	if(no%i==0):
		k=1
		break
if(k==1):
	print("number not Prime...")
else:
	print("number is Prime...")

