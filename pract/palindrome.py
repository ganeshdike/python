no=int(input("Enter Number:"))
print(no)
n=no
rev=0
while n>0:
	di=n%10
	print(di)
	rev=(rev*10)+di
	n=int(n/10)
	
	
if rev==no:
	print("number is palindrome::")
	
else:
	print("number is not palindrome::")
	
