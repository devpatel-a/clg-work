#Accept marks of 3 subjects and print total and averageand assign grade to him
a=float(input("Enter marks in 1st subject(0-100): "))
b=float(input("Enter marks in 2nd subject(0-100): "))
c=float(input("Enter marks in 3rd subject(0-100): "))
t=a+b+c
print("Total marks obtained=",t)
avg=t/3
print("Average of 3 subjects is=",avg)
if 0<=a<=39:
    print("Grade in subject a is F")
elif 40<=a<=44:
    print("Grade in subject a is P")
elif 45<=a<=49:
    print("Grade in subject a is C")
elif 50<=a<=54:
    print("Grade in subject a is B")
elif 55<=a<=59:
    print("Grade in subject a is B+")
elif 60<=a<=69:
    print("Grade in subject a is A")
elif 70<=a<=79:
    print("Grade in subject a is A+")
elif 80<=a<=100:
    print("Grade in subject a is O")
else:
    print("Enter valid marks")
if 0<=b<=39:
    print("Grade in subject b is F")
elif 40<=b<=44:
    print("Grade in subject b is P")
elif 45<=b<=49:
    print("Grade in subject b is C")
elif 50<=b<=54:
    print("Grade in subject b is B")
elif 55<=b<=59:
    print("Grade in subject b is B+")
elif 60<=b<=69:
    print("Grade in subject b is A")
elif 70<=b<=79:
    print("Grade in subject b is A+")
elif 80<=b<=100:
    print("Grade in subject b is O")
else:
    print("Enter valid marks")
if 0<=c<=39:
    print("Grade in subject c is F")
elif 40<=c<=44:
    print("Grade in subject c is P")
elif 45<=c<=49:
    print("Grade in subject c is C")
elif 50<=c<=54:
    print("Grade in subject c is B")
elif 55<=c<=59:
    print("Grade in subject c is B+")
elif 60<=c<=69:
    print("Grade in subject c is A")
elif 70<=c<=79:
    print("Grade in subject c is A+")
elif 80<=c<=100:
    print("Grade in subject c is O")
else:
    print("Enter valid marks")