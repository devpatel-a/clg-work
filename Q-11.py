## Check if 3 points are on same line or not
x1=float(input("Enter x-coordinate of 1st point"))
y1=float(input("Enter y-coordinate of 1st point"))
x2=float(input("Enter x-coordinate of 2nd point"))
y2=float(input("Enter x-coordinate of 2nd point"))
x3=float(input("Enter x-coordinate of 3rd point"))
y3=float(input("Enter x-coordinate of 3rd point"))
a=x1*(y2-y3)-y1*(x2-x3)+(x2*y3-x3*y2)
if a==0:
    print("Given points are on same line")
else:
    print("Given points are not on same line")