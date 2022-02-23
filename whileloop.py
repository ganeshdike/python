i=int(input('enter number...'))
rev=0;
idigit=0;
while i!=0:
	idigit=i%10;
	rev=(rev*10)+idigit
	i=int(i/10)
print(rev)
