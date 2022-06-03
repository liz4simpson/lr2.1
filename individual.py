import math
print("Введите 3 стороны: ")
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
s = math.sqrt(p*(p-a)+(p-b)*(p-c))
print("Полупериметр равен: ", p)
print("Площадь равна: ", s)
