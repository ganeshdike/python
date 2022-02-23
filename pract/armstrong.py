
for i in range(1,500):
	no=i
	sum1=0
	while no>0:
		digit=no%10
		sum1=sum1+(digit*digit*digit)
		no=no/10
	
	if sum1==i:
		print(i)
