import math
a=float(input("Digite valor de A: "))
b=float(input("Digite valor de B: "))
c=float(input("Digite valor de C: "))
delta = b**2 -4*a*c

x1 = (-b + math.sqrt(delta))/2*a

x2 = (-b - math.sqrt(delta))/2*a

print(x1)
print(x2)


