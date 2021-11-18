# <---whileloop--->

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
n = 20
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
i = 2
while i <= 50:
    if i == 25:
        break
    print(i)
    i += 1

# <---range--->

print(list(range(5)))
print(list(range(5, 20)))
print(list(range(5, 20, 2)))
print(list(range(0, 21, 3)))


# <---forloop--->
for i in range(10):
    print(i)

for i in range(0, 15, 3):
    print(i)

# <---nestedforloop--->

for i in range(6):
    for j in range(i):
        print('*', end="")
    print("")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(65, 70, 1):
    for j in range(char (i)):
        print("*", end="")
    print("")
