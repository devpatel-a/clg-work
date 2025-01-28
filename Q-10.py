#Find if area of rectangle is greater than its perimeter
l=float(input("Enter length of rectangle: "))
b=float(input("Enter breadth of rectangle: "))
a=l*b
p=2*(l+b)
print("Area",a)
print("Perimeter",p)
if a>p:
    print("Area of rectangle is greater than its perimeter")
elif a<p:
    print("Perimeter of rectangle is greater than its area")
else:
    print("Area of rectangle is equal to its perimeter")