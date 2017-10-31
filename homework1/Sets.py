#1
def average(array):
    x = set(array)
    return(sum(x)/len(x))
#2
if __name__ == '__main__':
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    a = line2.split()
    b = line4.split()
    nline2=set(list(map(int, a)))
    nline4=set(list(map(int, b)))
    inter = nline2.intersection(nline4)
    uni = nline2.union(nline4)
    for i in inter:
        if i in uni:
            uni.remove(i)
    final=sorted(uni)
    for i in final:
        print(i)
#3
n = input()
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
h = 0
for i in arr:
    if i in a:
        h+=1
    else:
        if i in b:
            h-=1
print (h)
#4
n = input()
aa = set()
for i in range(int(n)):
    i = input()
    aa.add(i)
print(len(aa))
#5
n = input()
m = set(map(int, input().split()))
d = int(input())
for line in range(d):
    i = input().split()
    command = i[0]
    if command == 'pop':
        m.pop()
    if command == 'remove':
        m.remove(int(i[1]))
    if command  == 'discard':
        m.discard(int(i[1]))
x = sum(m)
print(x)
#6
n = int(input())
m = set(map(int, input().split()))
y = int(input())
z = set(map(int, input().split()))
a = m.union(z)
print(len(a))
#7
a = int(input())
b = set(map(int, input().split()))
c = int(input())
d = set(map(int, input().split()))
inter=b.intersection(d)
print(len(inter))
#8
a = int(input())
b = set(map(int, input().split()))
c = int(input())
d = set(map(int, input().split()))
m = b.difference(d)
print(len(m))
#9
a = int(input())
b = set(map(int, input().split()))
c = int(input())
d = set(map(int, input().split()))
m = b.symmetric_difference(d)
print(len(m))
#10
m = int(input())
A = set(map(int, input().split()))
n = int(input())

for i in range(n):
    c, args = input().split()
    B = set(map(int, input().split()))
    eval('A.'+c+'(B)')

print (sum(A))
#11
n = int(input())
lst = list(map(int, input().split()))
final = set(lst)
print(((sum(final)*n)-(sum(lst)))//(n-1))
#12
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print(A.issubset(B))
#13
a = set(map(int, input().split()))
b = int(input())
c = set(map(int, input().split()))
d = set(map(int, input().split()))
x = a.issuperset(c)
y = a.issuperset(d)
if x == True and y == False:
    print(False)
if x== False and y == True:
    print(False)
if x == True and y == True:
    print(True)
if x == False and y == False:
    print(False)
