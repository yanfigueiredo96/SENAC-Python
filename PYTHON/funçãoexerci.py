# import math

# def fundelt (x,b,a,c):
#     delta= -b **2 + 4 *a*c 
#     delta2= b **2 + 4 *a*c
#     return delta , delta2

# x1 = b + 
# x2 = b - 

# print(fundelt(5,2,6,8))
import math

def RaizQuad (a,b,c):
    delta = -b**2 + 4*a*c
    x1 = (b+ math.sqrt (delta))/2*a
    x2 = (b- math.sqrt (delta))/2*a

    return [x1,x2]

print (RaizQuad (1,2,3))
