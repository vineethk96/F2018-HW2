#Problem 1 ECE 4984
#!/usr/bin/python3

edges = []
neighbors = []
routeTaken = []

totalWeight = 0
end = 0
neighborExistsBool = False

def minimum(neighbors, edges):
#search for the appropriate dictionary entry

	neighborExistsBool = False

	for currVertex in neighbors:

		if currVertex == 110:
			return neighbors

		#search through the "database" for possible neighbors
		for dictionary in edges:

			if int(currVertex) == int(dictionary["i"]):		#found the currVertex
				
				#check to see if the neighbor exists already
				for existNeighbor in neighbors:
					if int(dictionary["j"]) == int(existNeighbor):
						neighborExistsBool = True

				#add neighbor to the list
				if neighborExistsBool == False:
					neighbors.append(dictionary["j"])
				else:
					neighborExistsBool = False

	minimum(neighbors, edges)



if __name__ == '__main__':

	# 1) read from the input.txt file

	with open('input1.txt') as fin:
		
		n = fin.readline()
		print("total number of vertices: " + n)
		start = fin.readline()
		print("starting index: " + start)
		end = fin.readline()
		print("goal vertex: " + end)

		for line in fin:
			lineArray = line.split()
			newDict = {"i" : int(lineArray[0]), "j" : int(lineArray[1]), "wij": float(lineArray[2])}
			edges.append(newDict)
			del newDict

	# data has been succesfully imported from the text file

	# Implement recursive algorithm to find the shortest distance between the
	# start to the end

	# repeat till we reach the end of the maze

	neighbors.append(start)
	
	for dictionary in edges:

		if int(start) == int(dictionary["i"]):		#found the currVertex
			neighbors.append(dictionary["j"])		#append the correlated neighbors

	neighbors = minimum(neighbors, edges)

	backtrace = end
	#print("backtrace: " + backtrace)
	#print("start: " + start)

	
	#time to backtrace the optimal route
	while int(backtrace) != int(start):
		for index in neighbors:							#search through all the neighbors
			for dict1 in edges:							#find the corresponding edges to the current neighbor
				if int(index) == int(dict1["i"]):					#if the current neighbor is found within the edges
					#print(str(index))
					if int(backtrace) == int(dict1["j"]):			#the final value is the neighbor
						routeTaken.append(int(backtrace))
						backtrace = index
				if int(backtrace) == int(index):
					break
			if int(backtrace) == int(index):
				break

routeTaken.reverse()
print(routeTaken)