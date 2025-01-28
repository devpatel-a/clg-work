#Print largest or smallest out of 3 numbers
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
if a==b==c:
    print(a,"=",b,"=",c)
elif a>=b>=c:
    print(a,"is largest and",c,"is smallest")
elif a>=c>=b:
    print(a,"is largest and",b,"is smallest")
elif b>=a>=c:
    print(b,"is largest and",c,"is smallest")
elif b>=c>=a:
    print(b,"is largest and",a,"is smallest")
elif c>=a>=b:
    print(c,"is largest and",b,"is smallest")
elif c>=b>=a:
    print(c,"is largest and",a,"is smallest")