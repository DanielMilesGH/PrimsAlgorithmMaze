import os
import mazeDrawSideBySideWeb
import random
import dijkstra
import pygame as pyg
import asyncio

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
test = mazeDrawSideBySideWeb.MazeDrawyer(1500,1000,10,eval(txt))
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

async def main():
	pyg.init()
	genCounter=0
	edgeCounter=0
	bestCounter=0
	pathCounter=0
	test.WINDOW.fill((200, 157, 128))
	sz = 5
	color = (0,0,0)
	hitBias=False
	hitBiasB=False
	while True:
		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				exit()
		if edgeCounter < len(test.edgeList)//2 + 1:
			x1 = test.edgeList[edgeCounter][0] * sz + 10
			y1 = test.edgeList[edgeCounter][1] * sz + 10
			x2 = test.edgeList[edgeCounter][2] * sz + 10 
			y2 = test.edgeList[edgeCounter][3] * sz + 10

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			x1 = test.edgeList[edgeCounter][0] * sz + 10 + 750
			y1 = test.edgeList[edgeCounter][1] * sz + 10
			x2 = test.edgeList[edgeCounter][2] * sz + 10 + 750
			y2 = test.edgeList[edgeCounter][3] * sz + 10

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)

			x1 = test.edgeList[-edgeCounter][0] * sz + 10
			y1 = test.edgeList[-edgeCounter][1] * sz + 10
			x2 = test.edgeList[-edgeCounter][2] * sz + 10 
			y2 = test.edgeList[-edgeCounter][3] * sz + 10

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			x1 = test.edgeList[-edgeCounter][0] * sz + 10 + 750
			y1 = test.edgeList[-edgeCounter][1] * sz + 10
			x2 = test.edgeList[-edgeCounter][2] * sz + 10 + 750
			y2 = test.edgeList[-edgeCounter][3] * sz + 10

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			edgeCounter+=1

		elif bestCounter < len(bestPath):
			x1 = bestPath[bestCounter][0] * sz + 10
			y1 = bestPath[bestCounter][1] * sz + 10
			x2 = bestPath[bestCounter][2] * sz + 10 
			y2 = bestPath[bestCounter][3] * sz + 10
			color = (255,255,0)

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			
			x1 = bestPath[bestCounter][0] * sz + 10 + 750
			y1 = bestPath[bestCounter][1] * sz + 10
			x2 = bestPath[bestCounter][2] * sz + 10 + 750
			y2 = bestPath[bestCounter][3] * sz + 10
			color = (255,255,0)
			colorB = (255,255,0)

			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			bestCounter+=1
		elif pathCounter < len(pathDraw):
# 			pyg.time.wait(1)
	    	# Get the starting and ending coordinates of the edge
			x1 = pathDraw[pathCounter][0] * sz + 10
			y1 = pathDraw[pathCounter][1] * sz + 10
			x2 = pathDraw[pathCounter][2] * sz + 10 
			y2 = pathDraw[pathCounter][3] * sz + 10

	   		# Draw the edge on the screen	
			# color = (distances[(edge[0], edge[1])]% 255, distances[(edge[0], edge[1])]*1.5 % 255, 0)
			color = (255,0,0)
			if not hitBias:
				if (pathDraw[pathCounter][0], pathDraw[pathCounter][1]) == randomEnd:
					hitBias=True
			if not hitBiasB:
				if (pathDrawB[pathCounter][0], pathDrawB[pathCounter][1]) == randomEnd:
					hitBiasB=True
			if hitBiasB:
				colorB = (200,100,100)
			
			pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)
			x1 = pathDrawB[pathCounter][0] * sz + 10 + 750
			y1 = pathDrawB[pathCounter][1] * sz + 10
			x2 = pathDrawB[pathCounter][2] * sz + 10 + 750
			y2 = pathDrawB[pathCounter][3] * sz + 10
			pyg.draw.line(test.WINDOW, colorB, (x1, y1), (x2, y2), 3)
			pathCounter+=1
			# draw the best path
			for i in range(len(bestPath)):
				x1 = bestPath[i][0] * sz + 10
				y1 = bestPath[i][1] * sz + 10
				x2 = bestPath[i][2] * sz + 10 
				y2 = bestPath[i][3] * sz + 10
				color = (255,255,0)

				pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)

				x1 = bestPath[i][0] * sz + 10 + 750
				y1 = bestPath[i][1] * sz + 10
				x2 = bestPath[i][2] * sz + 10 + 750
				y2 = bestPath[i][3] * sz + 10
				color = (255,255,0)

				pyg.draw.line(test.WINDOW, color, (x1, y1), (x2, y2), 3)


		if genCounter%40==0:
			await asyncio.sleep(0)
			pyg.display.update()
		if genCounter == 50_000:
			genCounter=1
		genCounter+=1
		# else:
		# 	print(len(test.edgeList))
		# 	print(edgeCounter)

asyncio.run(main())
