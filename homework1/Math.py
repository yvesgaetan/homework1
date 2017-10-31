#1
from cmath import phase
a = complex(input())
y = abs(a)
x = phase(a)
print(y)
print(x)
#2
import math
from math import sqrt, asin, degrees
ab = int(input())
bc = int(input())
print(str(int(round(math.degrees(math.atan2(ab, bc)))))+'°')
#3
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i//9)**2)
#4
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))
#5
a = int(input())
b = int(input())
c = int(input())
print(pow(a,b))
print(pow(a,b,c))
#6
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a,b) + pow(c,d))
#8
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(i*(10**i-1)/9))
