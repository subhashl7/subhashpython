a,k=map(int,input().split())
n=0
for num in range(a,k+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            n=n+1
print(n)
