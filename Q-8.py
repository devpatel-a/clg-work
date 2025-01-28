#Check if triangle is valid or not sum of 3 angles of triangle is 180 degree
a=float(input("Enter 1st angle: "))
b=float(input("Enter 2nd angle: "))
c=float(input("Enter 3rd angle: "))
if a+b+c==180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")