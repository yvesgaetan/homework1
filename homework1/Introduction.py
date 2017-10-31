#1
if __name__ == '__main__':
    x = 'Hello, World!'
    print(x)
#2
if __name__ == '__main__':
    n = int(input())
def x(n):
    if n%2 == 0:
        if 2<=n<=5:
            return ('Not Weird')
        if 6<=n<=20:
            return ('Weird')
        if n>20:
            return ('Not Weird')
    else:
        return('Weird')
print (x(n))
#3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a + b)
print (a - b)
print (a*b)
#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a//b)
print (a/b)
#5
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print (i**2)
#6
def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
    if year%100==0:
        leap = False
    if year%400==0:
        leap = True
    return leap
#7
if __name__ == '__main__':
    n = int(input())
    y = range(1,n+1)
    print (*y, sep='')
