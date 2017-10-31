#1
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = list(product(a, b))
for i in x:
    print (i, end=' ')
#2
from itertools import permutations
a = list(map(str, input().split()))
s = a[0]
x = list(permutations(s, int(a[1])))
x.sort()
for i in x:
    print(''.join(i))
#3
from itertools import combinations
from operator import itemgetter

a = list(map(str, input().split()))
s = sorted(a[0])
for z in range(1, int(a[1]) + 1):

    x = sorted(list(combinations(s, z)))
    for i in x:
        print(''.join(i))
#4
from itertools import combinations_with_replacement
a = list(map(str, input().split()))
x = sorted(a[0])
y = sorted(list(combinations_with_replacement(x, int(a[1]))))
z=list()
for i in y:
    print(''.join(i))
#5
from itertools import groupby
a = input()
for key, group in groupby(a):
    print ((len(list(group)), int(key)), end=' ')
#6
from itertools import combinations

N = int(input()); a = input().split(); K = int(input())
com = list(combinations(a,K))
r = [1 for i in range(len(com)) if 'a' in com[i]]
print(sum(r)/len(com))
#7
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
final = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(final))