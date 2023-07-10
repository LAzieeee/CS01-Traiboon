#1
number = int(input())
x = 0
for i in range(number + 1):
    x += i
print(x)

#2
number = int(input())
for i in range(10):
    print(f"{number} * {i + 1} = ", number * ( i + 1 ))

#3
number = int(input())
for i in range(1, number):
    if i % 2 != 0:
        print(i)


#4
number = int(input())
x = ""
for i in range(number):
    print(x + "*") 
    x += "*"
