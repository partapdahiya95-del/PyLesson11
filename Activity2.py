rows = int(input("enter a number"))
number = 1
print("Floyd,s triangle is a right angled triangle with characters.")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end="")
        number = number + 1
    print()