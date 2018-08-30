N=input()
x=N.count('1')
y=N.count('0')
K=len(N)
if(K == x+y):
  print('yes')
else:
    print('no')
