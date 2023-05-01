import heapq
import math
class Dijkstra:
	def __init__(self, edgeLst, bias=False, start=(0,0), end=(100,100)):
		self.edgeLst = edgeLst
		self.graph = {}
		self.toDraw = []
		self.initalizeGraph()
		self.bias = bias
		self.start = start	
		self.end = end
	def initalizeGraph(self):
		for edge in self.edgeLst:
			# first go 01 to 23
			if (edge[0], edge[1]) not in self.graph.keys():
				self.graph[(edge[0], edge[1])] = {(edge[2], edge[3]):1}
			# otherwise, add the edge to the lst
			else:
				# access the first dict location, then append neighbor to nested dict
				self.graph[(edge[0], edge[1])][(edge[2], edge[3])] = 1

		for edge in self.edgeLst:
			# now go 23 to 01
			if (edge[2], edge[3]) not in self.graph.keys():
				self.graph[(edge[2], edge[3])] = {(edge[0], edge[1]):1}
			# otherwise, add the edge to the lst
			else:
				# access the first dict location, then append neighbor to nested dict
				self.graph[(edge[2], edge[3])][(edge[0], edge[1])] = 1

	def runSearch(self):
		distances = {vtx: float('infinity') for vtx in self.graph}
		prevs = {vtx: None for vtx in self.graph}
		distances[self.start] = 0
		pq = [(0, self.start)]
		while len(pq)>0:
			currDist, currVtx = heapq.heappop(pq)
			if currDist > distances[currVtx]:
				continue

			for neighbor, weight in self.graph[currVtx].items():
				if not self.bias:
					dist = currDist + weight
				else:
					dist = currDist + weight + self.manhattan(neighbor, self.end)**self.bias
				# only consider if its better than other dists
				if neighbor==self.bias:
					bias=False
				if dist < distances[neighbor]:
					distances[neighbor] = dist
					prevs[neighbor] = currVtx
					heapq.heappush(pq, (dist, neighbor))
					# if this happened, add edge to the toDraw
					self.toDraw.append((currVtx[0], currVtx[1], neighbor[0], neighbor[1]))

		return distances, prevs
	def manhattan(self, a, b):
		return sum(abs(val1-val2) for val1, val2 in zip(a,b))
if __name__ == "__main__":
	file = open("tree.txt")
	txt = file.read()
	file.close()

	test = Dijkstra(eval(txt))

	print(len(eval(txt)))
	print()
	print(len(test.graph.keys()))

	# print(test.runSearch())
	test.runSearch()
	distances, prevs = 	test.runSearch()
	print(prevs)
