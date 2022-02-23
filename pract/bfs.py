#bfs

graph={
	 "A":["B","C","D"],
	 "B":["A","E"],
	 "C":["A","F"],
	 "D":["A","G"],
	 "E":["B"],	
	 "F":["C"],
	 "G":["D"]
	}
	
def bfs(start):
	queue=[start]
	exp=[]
	while queue:
		n=queue.pop(0)
		if n not in exp:
			exp.append(n)
			neighbour=graph[n]
			for a in neighbour:
				queue.append(a)
			
	print(exp)
	return
bfs("A")
