
nbS = 0
nbEdges = 0
graph = {}
k = 2

with open("./bz/3elt.graph",'r') as file:
	#content = file.readlines()
	#print(str(content))
	i = 0
	for l in file:
		if i == 0:
			nbS,nbEdges = [int(x) for x in l.split()]
			print("nbS : " + str(nbS))
			print("nbEdges : " + str(nbEdges))
		else:	
			graph[i] = [int(x) for x in l.split()]
		i+=1
	
	#print("graph : %s" % graph[1])



