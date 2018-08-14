n1=int(input())
n2=[int(x) for x in input().split()]
s=sorted(n2)
if(n1%2==0):
    y=((h1)-1)//2
    x=b-1
    z=(s(y)+s(x))/2
    print(z)
else:
    y=(n1)//2
    print(s[y])
