#1
if __name__ == '__main__':
    N = int(input())
    final=""
    lst = list()
    for line in range(N):
        i = input().split()
        command = i[0]
        arg = i[1:]
        if command == 'print':
            print(lst)
        else:
            n = final+'.'+command+'('+','.join(arg)+')'
            eval('lst'+n)
#2
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    ar=[]

for i in range(0,len(integer_list)):

   ar.append(int(integer_list[i]))

t=tuple(ar)

print hash(t)
#3
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    final = []
a = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        for k in range(z +1):
            if i+j+k != n:
                final.append([])
                final[a] = [ i , j, k ]
                a+=1
print (final)
#4
if __name__ == '__main__':
    students =[]
    y = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a = []
        students += [[name , score]]
    for i,n in students:
        a+=[n]
    q = sorted(set(a))[1]
    for i,n in students:
        if n == q:
            y+=[i]
    for o in sorted(y):
        print(o)
#6
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

tot = student_marks[query_name]
avg = sum(tot) / len(tot)
print("{0:.2f}".format(avg))
