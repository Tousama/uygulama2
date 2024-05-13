# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:17:11 2024

@author: Muhammed
"""

point=(2,3)
target=(7,18)
def euclideanDistance(start,finish):
	x_distance = (start[0]-finish[0])**2
	y_distance = (start[1]-finish[1])**2
	return (x_distance+y_distance)**0.5

print(euclideanDistance(point,target))