jug1=3
jug2=4
t=2

def jugslover(amt1,amt2):
	print(amt1,amt2)
	
	if(amt1==t and amt2==0) or (amt1==0 and amt2==t):
		return
		
	elif amt2==jug2:
		jugslover(amt1,0)
		
	elif amt1!=0:
		if amt1<=jug2-amt2:
			jugslover(0,amt1+amt2)
		elif amt1>jug2-amt2:
			jugslover(amt1-(jug2-amt2),amt2+(jug2-amt2))
			
	else:
		jugslover(jug1,amt2)

jugslover(0,0)
