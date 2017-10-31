#1
def swap_case(s):
    aa =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bb = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for ii in s:
        if ii in aa:
            y = aa.index('ii')
            s.replace(aa[y],bb[y])
    for qq in s:
        if qq in bb:
            zz = bb.index('qq')
            s.replace(bb[zz], aa[zz])
    print (swap_case(s))
#2
def split_and_join(line):
    a = line.split(" ")
    b = "-".join(a)
    return b
#3
def print_full_name(a, b):
    print("Hello" + " " + a + " " + b + "! You just delved into python.")
#4
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string
#5
def count_substring(string, sub_string):
    a = 0

    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            a += 1
    return a
#6
if __name__ == '__main__':
    s = input()
    s.split()
    inum = False
    ialpha= False
    idigit = False
    ilower= False
    iupper=False
    for i in s:
        if i.isalnum()==True:
            inum=True
        if i.isalpha()==True:
            ialpha=True
        if i.isdigit()==True:
            idigit=True
        if i.islower()==True:
            ilower=True
        if i.isupper()==True:
            iupper=True
    print (inum)
    print (ialpha)
    print (idigit)
    print (ilower)
    print (iupper)
#7
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
#8
def wrap(string, max_width):
    s = textwrap.fill(string,max_width)
    return (s)
#9
N, M = map(int,input().split())
for i in range(1,N,2):
    print("{}".format(".|." * i).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N-2,-1,-2):
    print("{}".format(".|." * i).center(M, "-"))
#10
def print_formatted(n):
    a = len(str(bin(n)).replace('0b', ''))

    for i in range(1, n + 1):
        b = bin(int(i)).replace('0b', '').rjust(a, ' ')
        c = oct(int(i)).replace('0o', '', 1).rjust(a, ' ')
        d = hex(int(i)).replace('0x', '').upper().rjust(a, ' ')
        e = str(i).rjust(a, ' ')
        print(e, c, d, b)
#11
import string
alpha = string.ascii_lowercase

n = int(input())
L = []

for i in range(n):
    s = "-".join(alpha[i:n])
    L.append(s[::-1]+s[1:])

width = len(L[0])

for i in range(n-1, 0, -1):
    print(L[i].center(width, "-"))

for i in range(n):
    print(L[i].center(width, "-"))
#12
def capitalize(string):
    return ''.join((c.upper() if i == 0 or string[i - 1] == ' ' else c) for i, c in enumerate(string))
#13
def minion_game(s):
    V = frozenset("AEIOU")
    n = len(s)
    ksc = sum(q for c, q in zip(s, range(n, 0, -1)) if c in V)
    ssc = n * (n + 1) // 2 - ksc
    if ksc > ssc:
        print("Kevin {:d}".format(ksc))
    elif ssc > ksc:
        print("Stuart {:d}".format(ssc))
    else:
        print("Draw")
#14
def merge_the_tools(string, k):
    length = len(string)
    t = length // k
    for i in range(0, length, k):
        t0 = string[i:i + k]
        a = []

        t0.split()
        for ab in t0:
            if ab not in a:
                a += (ab)
        print("".join(a))