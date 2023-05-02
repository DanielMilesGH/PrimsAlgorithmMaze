import pygame as pyg
from pygame.locals import *
import sys
import math
import dijkstra
import os
import random
import asyncio

WHITE = (255,255,255)
RED = (255, 0, 0)

class MazeDrawyer:
	pyg.init()
	def __init__(self, width, height, gridSpace, edgeList):
		self.WINDOW_WIDTH = width
		self.WINDOW_HEIGHT = height
		self.GRID_SPACE = gridSpace
		self.coordList = []
		self.edgeList = edgeList
		self.WINDOW = pyg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

		# print(self.edgeList)



	def draw(self, WINDOW, pathDraw, pathDrawB, randomStart, randomEnd, bestPath, bestPathB, i):
		# making the backgroudn vaguely pink
		self.WINDOW.fill((200, 157, 128))
		# drawing straight lines across to make grid
		# horizontal
		# for i in range(self.WINDOW_WIDTH // self.GRID_SPACE):
		# 	pyg.draw.line(self.WINDOW, WHITE, (i*self.GRID_SPACE, 0), (i*self.GRID_SPACE, self.WINDOW_HEIGHT+self.GRID_SPACE))
		# # vertical
		# for i in range(self.WINDOW_HEIGHT // self.GRID_SPACE):
		# 	pyg.draw.line(self.WINDOW, WHITE, (0, i*self.GRID_SPACE), (self.WINDOW_WIDTH+self.GRID_SPACE, i*self.GRID_SPACE))

		sz=5
		# print(len(self.edgeList))
		# print(len(distances))
		for event in pyg.event.get():
			if event.type == QUIT:
				pyg.quit()
				sys.exit()
		color = (0,0,0)
		# pyg.time.wait(1)
		x1 = self.edgeList[i][0] * sz + 10
		y1 = self.edgeList[i][1] * sz + 10
		x2 = self.edgeList[i][2] * sz + 10 
		y2 = self.edgeList[i][3] * sz + 10

		pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)

		x1 = self.edgeList[i][0] * sz + 10 + 750
		y1 = self.edgeList[i][1] * sz + 10
		x2 = self.edgeList[i][2] * sz + 10 + 750
		y2 = self.edgeList[i][3] * sz + 10

		pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
		# pyg.draw.line(self.WINDOW, (255,55,55), (x1, y1), (x2, y2), 4)
		pyg.display.update()

		hitBias = False
		hitBiasB = False
		'''
		for i in range(len(pathDraw)):
			for event in pyg.event.get():
				if event.type == QUIT:
					pyg.quit()
					sys.exit()
			# pyg.time.wait(1)
	    	# Get the starting and ending coordinates of the edge
			x1 = pathDraw[i][0] * sz + 10
			y1 = pathDraw[i][1] * sz + 10
			x2 = pathDraw[i][2] * sz + 10 
			y2 = pathDraw[i][3] * sz + 10

	   		# Draw the edge on the screen	
			# color = (distances[(edge[0], edge[1])]% 255, distances[(edge[0], edge[1])]*1.5 % 255, 0)
			color = (255,0,0)
			if not hitBias:
				if (pathDraw[i][0], pathDraw[i][1]) == randomEnd:
					hitBias=True
			if hitBias:
				color = (200,100,100)
			# print(color)
			# try:
			# 	color = (255, distances[(x1, y1)], 0)
			# except:
			# 	color = (0,0,0)
			pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
			# pyg.draw.rect(self.WINDOW, (255,255,255), 
			# 	          pyg.Rect(randomEnd[0]*sz+10,
			# 	          	       randomEnd[1]*sz+10, sz,sz))
			# pyg.draw.rect(self.WINDOW, (255,255,255), 
			# 	          pyg.Rect(randomStart[0]*sz+10,
			# 	          	       randomStart[1]*sz+10, sz,sz))

			x1 = pathDrawB[i][0] * sz + 10 + 750
			y1 = pathDrawB[i][1] * sz + 10
			x2 = pathDrawB[i][2] * sz + 10 + 750
			y2 = pathDrawB[i][3] * sz + 10

	   		# Draw the edge on the screen	
			# color = (distances[(edge[0], edge[1])]% 255, distances[(edge[0], edge[1])]*1.5 % 255, 0)
			color = (255,0,0)
			if not hitBiasB:
				if (pathDrawB[i][0], pathDrawB[i][1]) == randomEnd:
					hitBiasB=True
			if hitBiasB:
				color = (200,100,100)
			# print(color)
			# try:
			# 	color = (255, distances[(x1, y1)], 0)
			# except:
			# 	color = (0,0,0)
			pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
			# pyg.draw.rect(self.WINDOW, (255,255,255), 
			# 	          pyg.Rect(randomEnd[0]*sz+10,
			# 	          	       randomEnd[1]*sz+10, 15,15))
			# pyg.draw.rect(self.WINDOW, (255,0,255), 
			# 	          pyg.Rect(randomStart[0]*sz+10,
			# 	          	       randomStart[1]*sz+10, 15,15))
			for edge in bestPath:
			# pyg.time.wait(1)
				x1 = edge[0] * sz + 10
				y1 = edge[1] * sz + 10
				x2 = edge[2] * sz + 10 
				y2 = edge[3] * sz + 10
				color = (255,255,0)

				pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
				
				x1 = edge[0] * sz + 10 + 750
				y1 = edge[1] * sz + 10
				x2 = edge[2] * sz + 10 + 750
				y2 = edge[3] * sz + 10
				color = (255,255,0)

				pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)

			if not counter%55:
				pyg.display.update()
			counter+=1	# defining rounding down to nearest GRID_SPACE
		pyg.display.update()
'''

	def roundDown(self, x):
		return self.GRID_SPACE * math.floor(x/self.GRID_SPACE)

	def setCoordList(self, coordList):
		self.coordList = coordList

	def drawMaze(self):
		pos = (0,0)
		coordList = []
		drawing = True
		self.draw(self.WINDOW)

		while drawing:
			for event in pyg.event.get():
				if event.type == QUIT:
					pyg.quit()
					sys.exit()
			pyg.display.update()
''
# incase i want to test this module
if __name__ == "__main__":
	os.system("java Prim 145 195")
	file = open("tree.txt")
	txt = file.read()
	file.close()
	randomStart = (random.randint(25,50),
				   random.randint(25,50))
	randomEnd = (random.randint(120, 140),
				   random.randint(120, 140))

	solverBiased = dijkstra.Dijkstra(eval(txt), 
							   start=randomStart,
							   end=randomEnd,
							   bias=10)
	solvedUnBiased= dijkstra.Dijkstra(eval(txt), 
							   start=randomStart,
							   end=randomEnd,
							   bias=False)
	distancesB, prevsB = solverBiased.runSearch()
	distances, prevs = solvedUnBiased.runSearch()

	pathDraw = solvedUnBiased.toDraw
	pathDrawB = solverBiased.toDraw
	test = MazeDrawyer(1500,1000,10,eval(txt))
	# get best path
	bestPath = []
	currVtx = randomEnd
	while prevs[currVtx] != None:
		bestPath.append((currVtx[0], currVtx[1], 
			            prevs[currVtx][0], 
			            prevs[currVtx][1]))
		currVtx = prevs[currVtx]
	bestPathB = []
	currVtx = randomEnd
	while prevsB[currVtx] != None:
		bestPathB.append((currVtx[0], currVtx[1], 
			            prevsB[currVtx][0], 
			            prevsB[currVtx][1]))
		currVtx = prevsB[currVtx]

	print(bestPath)
	test.draw(test.WINDOW)

	while True:
		for event in pyg.event.get():
			if event.type == QUIT:
				exit()
