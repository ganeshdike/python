arr=1,2,3,4,5,6,7,8,9
no=int(input('enter input'))
for j in range(no,2,-1):
	for i in range((j-1),1,-1):
		if j%i==0:
			break
	if(i==2 and j!=4):
		print(j,"prime")
	
	else:
		print(j,"not prime")
		
