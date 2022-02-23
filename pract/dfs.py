#dfs

graph={
	 "A":["B","C","D"],
	 "B":["A","E"],
	 "C":["A","F"],
	 "D":["A","G"],
	 "E":["B"],	
	 "F":["C"],
	 "G":["D"]
	}
visited=[]

def dfs(start):
	visited.append(start)
	for i in graph[start]:
			if i not in visited:
			dfs(i)
dfs("A")
print(visited)
