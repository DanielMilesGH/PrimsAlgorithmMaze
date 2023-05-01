import pygame as pyg
from pygame.locals import *
import sys
import math
import dijkstra
import os
import random

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



	def draw(self, WINDOW):
		# making the backgroudn vaguely pink
		self.WINDOW.fill((255, 157, 128))
		# drawing straight lines across to make grid
		# horizontal
		# for i in range(self.WINDOW_WIDTH // self.GRID_SPACE):
		# 	pyg.draw.line(self.WINDOW, WHITE, (i*self.GRID_SPACE, 0), (i*self.GRID_SPACE, self.WINDOW_HEIGHT+self.GRID_SPACE))
		# # vertical
		# for i in range(self.WINDOW_HEIGHT // self.GRID_SPACE):
		# 	pyg.draw.line(self.WINDOW, WHITE, (0, i*self.GRID_SPACE), (self.WINDOW_WIDTH+self.GRID_SPACE, i*self.GRID_SPACE))

		sz=5
		print(len(self.edgeList))
		print(len(distances))
		counter=0
		for edge in self.edgeList:
			for event in pyg.event.get():
				if event.type == QUIT:
					pyg.quit()
					sys.exit()
			# pyg.time.wait(1)
			x1 = edge[0] * sz + 10
			y1 = edge[1] * sz + 10
			x2 = edge[2] * sz + 10 
			y2 = edge[3] * sz + 10
			color = (0,0,0)

			pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
			# pyg.draw.line(self.WINDOW, (255,55,55), (x1, y1), (x2, y2), 4)
			if not counter%1000:
				pyg.display.update()
			counter+=1
		counter=0

		hitBias = False

		for edge in pathDraw:
			for event in pyg.event.get():
				if event.type == QUIT:
					pyg.quit()
					sys.exit()
			# pyg.time.wait(1)
	    	# Get the starting and ending coordinates of the edge
			x1 = edge[0] * sz + 10
			y1 = edge[1] * sz + 10
			x2 = edge[2] * sz + 10 
			y2 = edge[3] * sz + 10

	   		# Draw the edge on the screen	
			# color = (distances[(edge[0], edge[1])]% 255, distances[(edge[0], edge[1])]*1.5 % 255, 0)
			color = (255,0,0)
			if not hitBias:
				if (edge[0], edge[1]) == randomEnd:
					hitBias=True
			if hitBias:
				color = (200,100,100)
			# print(color)
			# try:
			# 	color = (255, distances[(x1, y1)], 0)
			# except:
			# 	color = (0,0,0)
			pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)
			pyg.draw.rect(self.WINDOW, (255,255,255), 
				          pyg.Rect(randomEnd[0]*sz+10,
				          	       randomEnd[1]*sz+10, 15,15))
			pyg.draw.rect(self.WINDOW, (255,0,255), 
				          pyg.Rect(randomStart[0]*sz+10,
				          	       randomStart[1]*sz+10, 15,15))

			for edge in bestPath:
			# pyg.time.wait(1)
				x1 = edge[0] * sz + 10
				y1 = edge[1] * sz + 10
				x2 = edge[2] * sz + 10 
				y2 = edge[3] * sz + 10
				color = (255,255,0)

				pyg.draw.line(self.WINDOW, color, (x1, y1), (x2, y2), 3)

			# pyg.draw.line(self.WINDOW, (255,55,55), (x1, y1), (x2, y2), 4)
			if not counter%111:
				pyg.display.update()
			counter+=1	# defining rounding down to nearest GRID_SPACE
		pyg.display.update()

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

# incase i want to test this module
if __name__ == "__main__":
	os.system("java Prim 280 195")
	file = open("tree.txt")
	txt = file.read()
	file.close()
	randomStart = (random.randint(0,50),
				   random.randint(0,50))
	randomEnd = (random.randint(250,270),
				   random.randint(150,190))

	solver = dijkstra.Dijkstra(eval(txt), 
							   start=randomStart,
							   end=randomEnd,
							   bias=10)

	distances, prevs = solver.runSearch()
	pathDraw = solver.toDraw
	test = MazeDrawyer(1500,1000,10,eval(txt))
	# get best path
	bestPath = []
	currVtx = randomEnd
	while prevs[currVtx] != None:
		bestPath.append((currVtx[0], currVtx[1], 
			            prevs[currVtx][0], 
			            prevs[currVtx][1]))
		currVtx = prevs[currVtx]
	print(bestPath)
	test.draw(test.WINDOW)

	while True:
		for event in pyg.event.get():
			if event.type == QUIT:
				exit()
