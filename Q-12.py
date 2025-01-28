#Find if a point is inside or on or outside the circle with given center and radius
x=float(input("Enter x coordinate of center of circle: "))
y=float(input("Enter y coordinate of center of circle: "))
r=float(input("Enter radius of circle: "))
x1=float(input("Enter x coordinate of the point: "))
y1=float(input("Enter y coordinate of the point: "))
d=((x-x1)**2 + (y-y1)**2)**(1/2)
if d>r:
    print("Point is outside the circle")
elif d==r:
    print("Point is on the circle")
else:
    print("Point is inside the circle")