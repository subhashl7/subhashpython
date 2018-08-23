N,K=map(int,input().split())
list=[int(x) for x in input().split()]
h=0
for i in range(0,K):
  h=h+list[i]
print(h)
