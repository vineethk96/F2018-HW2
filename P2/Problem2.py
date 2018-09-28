#Problem 2 ECE 4984
#!/usr/bin/python3

from collections import defaultdict
from heapq import *

def minimum(edges, neighbors, i):

	sortedList = [neighbors[0]]
	
	minimum = neighbors[0]["wij"]

	for newVertex in neighbors:
		if minimum > newVertex["wij"]:
			sortedList.insert(0, neighbors)

	return sortedList[0]


def dijkstra(edges, start, end, n):
	
	costToCome = []
	openList = []
	visitedList = [start]
	neighbors = []
	repeatedVal = False
	lowest = {}
	possDirections = []
	routeTaken = []
	costRoute = []
	runAgain = False
	firstRun = True

	# fill the cost to come list
	for x in range(int(n)):
		if x == start-1:
			costToCome.append(0)
		else:
			costToCome.append(float('inf'))

	while len(openList) != 0 or firstRun:			#not int(end) in visitedList or not runAgain:
		firstRun = False

		#find new neighbors
		currVertex = visitedList[len(visitedList) - 1]	#=2
		
		for dictionary in edges:
			if dictionary["i"] == currVertex:			#=2,1,1
														#=2,3,1.2
														#=2,5,2

				# make sure the value isn't already listed as a neighbor
				
				for value in visitedList:
					if dictionary["j"] == value:
						repeatedVal = True
				

				if repeatedVal:
					repeatedVal = False
				else:
					openList.append(dictionary["j"])
					possDirections.append(dictionary)

		# new neighbors have been found

		# now search for the lowest weight
		minimum = 100
		'''
		print()
		print("possDirections:")
		print(possDirections)
		'''

		for possRoutes in possDirections:
			if possRoutes["wij"] < minimum:
				runAgain = False
				minimum = possRoutes["wij"]
				quickestRoute = possRoutes
			elif possRoutes["wij"] == minimum:
				runAgain = True
				minimum = possRoutes["wij"]
				quickestRoute = possRoutes
				# run one more time
		'''
		print("route:")
		print(quickestRoute)
		'''

		totalWeight = quickestRoute["wij"] + costToCome[quickestRoute["i"]-1]

		if costToCome[quickestRoute["j"]-1] > totalWeight:
			#print("totalWeight is less")
			costToCome[quickestRoute["j"]-1] = totalWeight

		'''
		print("openList: ")
		print(openList)
		print("visitedList: ")
		print(visitedList)
		print("costToCome: ")
		print(costToCome)
		'''

		possDirections.remove(quickestRoute)
		openList.remove(quickestRoute["j"])
		visitedList.append(quickestRoute["j"])


	backtrace = end
	#print("backtrace: " + backtrace)
	#print("start: " + start)

	
	#time to backtrace the optimal route
	while int(backtrace) != int(start):
		for index in visitedList:							#search through all the neighbors
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
	routeTaken.insert(0, start)
	for step in routeTaken:
		costRoute.append(costToCome[step - 1])
	print()
	print()
	print(routeTaken)
	print(costRoute)


if __name__ == '__main__':

	edges = []

# 1) read from the input.txt file

	with open('input_1.txt') as fin:
		
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



	dijkstra(edges, start, end, n)
