N = int(input())
t1=0
t2=1
for x in range(0,N):
    nextterm = t1+t2
    t1=t2
    t2=nextterm
    print(t1,end=' ')
