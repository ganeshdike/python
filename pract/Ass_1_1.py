print("matha table upto given tabl:")
n=int(input("Enter limit"));
for i in range(1,11):
	for j in range(1,n+1):
		print(i,"X",j,"=",i*j,end="\t")
	print()
	
	
	
#output:

#dell@ubuntu:~/python/pract$ gedit Ass_1_1.py
#dell@ubuntu:~/python/pract$ python3 Ass_1_1.py
#matha table upto given tabl:
#Enter limit3
#1 X 1 = 1	 1 X 2 = 2	    1 X 3 = 3	
#2 X 1 = 2	 2 X 2 = 4	    2 X 3 = 6	
#3 X 1 = 3	 3 X 2 = 6	    3 X 3 = 9	
#4 X 1 = 4	 4 X 2 = 8	    4 X 3 = 12	
#5 X 1 = 5	 5 X 2 = 10	    5 X 3 = 15	
#6 X 1 = 6	 6 X 2 = 12	    6 X 3 = 18	
#7 X 1 = 7	 7 X 2 = 14	    7 X 3 = 21	
#8 X 1 = 8	 8 X 2 = 16	    8 X 3 = 24	
#9 X 1 = 9	 9 X 2 = 18	    9 X 3 = 27	
10 X 1 = 10	 10 X 2 = 20    10 X 3 = 30
