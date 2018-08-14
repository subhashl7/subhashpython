n,a,d=map(int,input().split())
y=0
for i in range(0,n+1):
    y=y+(a+(i-1)*d)
print(y)
