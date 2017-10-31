#1
a = input()
m = list(map(int, input().split()))
sum = 0
for i in range(int(input())):
    b, c = input().split()
    for j in range(len(m)):
        if int(b) == m[j]:
            sum = sum + int(c)
            m.remove(m[j])
            break
print(sum)
#2
from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n + 1):
    d[input()].append(str(i))

for i in range(m):
    print(' '.join(d[input()]) or -1)
#3
from collections import namedtuple
n, s = int(input()), namedtuple('Student', input())
print("%.2f" % (sum(int(s(*input().split()).MARKS) for _ in range(n)) / n))
#4
from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    item_name,item_price=input().rsplit(' ',1)
    if item_name not in d:
        d[item_name]=int(item_price)
    else:
        d[item_name]=d[item_name]+int(item_price)

for i in d.items():
    print(*i)
#5
from collections import OrderedDict
words = OrderedDict()
for i in range(int(input())):
    eachword = input().strip()
    words[eachword] = words.get(eachword, 0) + 1
print (len(words))
print (*words.values())
#6
from collections import deque
d = deque()
for i in range(int(input())):
    eval('d.{0}({1})'.format(*input().split()+['']))
print (' '.join(map(str,d)))
#7
from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = deque(map(int, input().split()))
    for e in range(n-1):
        if s[0] >= s[1]:
            s.popleft()
        elif s[-1] >= s[-2]:
            s.pop()
    if len(s) > 1:
        print ('No')
    else:
        print ('Yes')
#8
import sys

if __name__ == "__main__":
    s = input().strip()
from collections import Counter, OrderedDict
x = sorted(Counter(s).items(), key = lambda x: (-x[1], x[0]))
for i,n in x[:3]:
    print (i, n)
