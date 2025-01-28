#Check if its leap year or not
a=int(input("Enter year: "))
if a>0 and a%4==0:
    print(a,"is leap year")
elif a>0 and a%4!=0:
    print(a,"is not a leap year")
else:
    print("Enter a valid year")