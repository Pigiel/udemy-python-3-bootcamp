#!/usr/bin/env python3

class Line():

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return ((self.coor2[0]- self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5
		# Different solution
		# x1,y1 = self.coor1
		# x2,y2 = self.coor2
		# return ((x2-x1)**2 + (y2-y1)**2)**0.5

	def slope(self):
		return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
		# Different solution
		# x1,y1 = self.coor1
		# x2,y2 = self.coor2
		# return (y2-y1)/(x2-x1)

print('\n## Problem 1 ##\n')
print('coordinate1 = (3,2)')
coordinate1 = (3,2)
print('coordinate2 = (8,10)')
coordinate2 = (8,10)

print('\nli = Line(coordinate1,coordinate2)\n')
li = Line(coordinate1,coordinate2)
print('li.distance()')
print(li.distance())
print('li.slope()')
print(li.slope())

class Cylinder():

	pi = 3.14

	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return Cylinder.pi * self.radius**2 * self.height

	def surface_area(self):
		return 2 * (Cylinder.pi * self.radius**2) + (2 * Cylinder.pi * self.radius * self.height)

print('\n## Problem 2 ##\n')
print('c = Cylinder(2,3)\n')
c = Cylinder(2,3)

print('c.volume()')
print(c.volume())
print('c.surface_area()')
print(c.surface_area())