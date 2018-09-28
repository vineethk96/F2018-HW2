#Problem 1 ECE 4984
#!/usr/bin/python3

import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("a")
	args = parser.parse_args()

	counter_i = 0
	counter_k = 0
	repeatedVal = False
	edges = []
	neighbors = []
	edgeCost = []

# 1) read from the input.txt file

	with open(args.a) as fin:
		
		n = fin.readline()
		print("total number of vertices: " + n)
		start = int(fin.readline())
		print("starting index: " + str(start))
		end = int(fin.readline())
		print("goal vertex: " + str(end))

		for line in fin:
			lineArray = line.split()
			newDict = {"i" : int(lineArray[0]), "j" : int(lineArray[1]), "wij": float(lineArray[2])}
			edges.append(newDict)
			del newDict

# 2) setup the 2D array

	board = []    
	for i in range(end): # create a list with nested lists
	    board.append([])
	    for n in range(end):
	    	board[i].append("inf") # fills nested lists with data
	board[0][start-1] = 0

# 3) iterate through each column & row
	while counter_k < end:			#k: (0 -> 109)
		while counter_i < end:		#i: (0 -> 109)

			if board[counter_k][counter_i] != "inf":

# 3a) find the neighbors of the vertex at counter_i
				for dictionary in edges:

					if int(dictionary["i"]) == (int(counter_i) + 1):
						#check for repeated neighbor values
						for vertex in neighbors:
							if dictionary == vertex:
								repeatedVal = True

						if not repeatedVal:
							neighbors.append(dictionary)
						else:
							repeatedVal = False

# 4) compute the cost per neighbor & pick the best
				for vertex in neighbors:

					if int(counter_k) == 0:
						edgeCostVal = int(vertex["wij"])
					else:
						edgeCostVal = int(vertex["wij"]) + int(board[counter_k][counter_i])

					edgeCost.append(edgeCostVal)

					if int(counter_k) + 1 < end:
						board[counter_k + 1][int(vertex["j"]) - 1] = edgeCostVal

						#for x in range(end - counter_k):
							#print(x)
							#board[counter_k + x + 1][int(vertex["j"]) - 1] = edgeCostVal

				del neighbors[:]
				del edgeCost[:]

			counter_i = counter_i + 1
		counter_i = 1
		counter_k = counter_k + 1


	currVertex = start
	counter_k = 0

	while currVertex != end:

		lowest = board[counter_k][0]

		for vertex in board[counter_k]:

			if vertex < lowest:
				lowest = vertex

		currVertex = lowest
		print(currVertex)

	#print(board)