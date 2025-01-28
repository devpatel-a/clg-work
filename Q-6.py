#Check number of didgits is a given number
a=int(input("Enter an integer between 0 to 99999: "))
if 0<=a<=9:
    print("1 digit number")
elif 9<a<=99:
    print("2 digit number")
elif 99<a<=999:
    print("3 digit number")
elif 999<a<=9999:
    print("4 digit number")
elif 9999<a<=99999:
    print("5 digit number")
else:
    print("Invalid number")