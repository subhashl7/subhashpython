n0,h0=map(int,input().split())
n1,h1=map(int,input().split())
x0=(n0*60)+h0
y0=(n1*60)+h1
y1=x0-y0
x1=y1//60
y1%=60
print(x1,y1,sep=" ")
