#<---If condition--->
age = int(input("Enter the age: "))
name = input("Enter the name : ")
if age >= 18:
    print(name, 'is eligible because', age, ' years is old')
else:
    print(name, 'is not eligible because', age, ' years is old')

num = int(input("Enter the number: "))
if num % 2 == 0:
    print(num, "is even number")
else:
    print(num, "is odd number")

#<---elif condition--->

days = int(input("Enter the days: "))
if days == 0:
    print("No fine amount")
elif days >= 1 and days <= 5:
    print("Fine amount is: ", days * 1)
elif days > 5 and days <= 10:
    print("Fine amount is: ", days * 5)
elif days > 10 and days <= 30:
    print("Fine amount is: ", days * 10)
else:
    print("Membership is Cancelled")

#<---Nested if condition--->
m1 = int(input("Enter the mark-1: "))
m2 = int(input("Enter the mark-2: "))
m3 = int(input("Enter the mark-3: "))
m4 = int(input("Enter the mark-4: "))
m5 = int(input("Enter the mark-5: "))
total = m1 + m2 + m3 + m4 + m5
average = total / 5.0
print("Total :", total)
print("Average :", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Result : pass")
    if average >= 90 and average  <= 100:
        print("Grade : Grade A")
    elif average  > 80 and average  <= 89:
        print("Grade : Grade B")
    elif average  > 70 and average  <= 79:
        print("Grade : Grade C")
    else:
        print("Grade : Grade D")
else:
    print("Result : fail")
    print("Grade : No Grade")
