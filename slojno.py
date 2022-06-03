a3 = int(input("Введите а3: "))
a2 = int(input("Введите а2: "))
a1 = int(input("Введите а1: "))
b3 = int(input("Введите b3: "))
b2 = int(input("Введите b2: "))
b1 = int(input("Введите b1: "))

c3 = a3 + b3 + ((a2 + b2 + (a1 + b1)//10)//10)
c2 = (a2 + b2 + (a1 + b1) // 10) % 10
c1 = (a1 + b1) % 10

print(c3, c2, c1)
