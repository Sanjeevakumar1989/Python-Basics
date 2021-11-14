
#<---Keyword list--->
import keyword
print(keyword.kwlist)

#<---simple addition--->
a = 25
b = 22
d = 34
c = a+b+d
print(c)

#<--- two input from user and add function --->
Num1 = float(input("Enter the number1: "))
Num2 = float(input("Enter the number2:   "))
print(type(Num1))
print(Num1+Num2)

#<--- Multiple variable using single line input from user--->
a1,a2,a3=input("enter 3 names: ").split(',')
print("Name 1:", a1)
print("Name 2 :", a2)
print("Name 3 :", a3)

#<--- How do join strings --->
para = ['22','24','45']
print(type(para))
print(','.join(para))
print(para[0])

#<---Input para get from user-->
para = []
print("Enter the para: ")
while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)
output1 = '\n'.join(para)
print(output1)

