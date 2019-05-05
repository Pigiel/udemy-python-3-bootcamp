# Object Oriented Programming
## Homework Assignment
### Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

```py
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return ((self.coor2[0]- self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5
    
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
```
```sh
# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
```
```sh
li.distance()
9.433981132056603
```
```sh
li.slope()
1.6
```
### Problem 2
Fill in the class

```py
class Cylinder:
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return 2 * (Cylinder.pi * self.radius**2) + (2 * Cylinder.pi * self.radius * self.height)
```
```sh
# EXAMPLE OUTPUT
c = Cylinder(2,3)
```
```sh
c.volume()
56.52
```
```sh
c.surface_area()
94.2
```