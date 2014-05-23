#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binClock.py
#  
#  Copyright 2013 ryan <ryan@porta-penguin>
#
#  This one's going out to my chums Ben, Michael, and The Girl!
#  Last revision: 07/06/10

import os
import platform
import time
from datetime import datetime

binGrid = [[0]*4 for i in range(6)]
grid = [[0]*4 for i in range(6)]

def main():
	while True:
		tick()
	return 0
	
def tick():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
	for i in range(0,6):
		timeArray = []
		hour = datetime.now().hour
		hourTens = getBin(hour / 10)
		hourOnes = getBin(hour % 10)
		
		mint = datetime.now().minute
		mintTens = getBin(mint / 10)
		mintOnes = getBin(mint % 10)
		
		sec = datetime.now().second
		secTens = getBin(sec / 10)
		secOnes = getBin(sec % 10)
		
		timeArray.extend((hourTens, hourOnes, mintTens, mintOnes, secTens, secOnes))
		
		for j in range(0,4):
			binGrid[i][j] = timeArray[i][j]
	buildDisplay()	
	printGrid()	
	time.sleep(1)
	
def printGrid():
	grid[0][0] = '   '
	grid[0][1] = '   '
	grid[2][0] = '   '
	grid[4][0] = '   '
	for i in range(0,4):
		print str(2**(3-i)) + ' >',
		for j in range(0,6):
			print grid[j][i],
		print '\n'
		#print '---------------------------'
	print '     ^   ^   ^   ^   ^   ^'
	print '     H   h   M   m   S   s'
	
def getBin(x):
    return (bin(x)[2:]).zfill(4)
    
def buildDisplay():
	for i in range(0,6):
		for j in range(0,4):
			if binGrid[i][j] == '1':
				grid[i][j] = '[X]'
			else:
				grid[i][j] = '[ ]'

if __name__ == '__main__':
	main()