from turtle import *
from random import randrange


def matrix_to_graph(list1, length):
	g = dict()
	for i in range(length):
		g[i] = []
	for index in range(length):
		for i in range(length):
			if list1[index][i] == 1 and index != i:
				g[index].append(i)
	return g

position = {}
def draw(g):
	penup()
	visted = []
	global position

	#sets position for nodes and writes it
	for i in g.keys():
		a = True
		while a:
			a = False
			x = randrange(-400, 400)
			y = randrange(-200, 200)
			for j in position.keys():
				if 10000 > (position[j][0]-x)**2 + (position[j][1]-y)**2:
					a = True
					break 
		setposition(x, y)
		position[i] = [x, y]
		write(i)

	#draw edges
	for i in g.keys():
		visted.append(i)
		for j in g[i]:
			if j not in visted:
				penup()
				setposition(position[i])
				pendown()
				setposition(position[j])
	

def bfs(qraph, start):
	pencolor('green')
	pensize(3)
	global position
	queue = [start]
	visted = []
	while queue:
		node = queue.pop(0)
		visted.append(node)
		for i in graph[node]:
			if i not in visted and i not in queue:
				queue.append(i)
				penup()
				setposition(position[node])
				pendown()
				setposition(position[i])

	mainloop()
		


number_of_nodes = int(input("Enter number of nodes:"))
print("Enter adjacency matrix")
graph = []
for i in range(number_of_nodes):
	temp = [int(x) for x in input().split()]
	graph.append(list(temp))
graph = matrix_to_graph(graph, number_of_nodes)
#speed(10)
draw(graph)
bfs(graph, 0)

