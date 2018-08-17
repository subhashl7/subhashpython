st1,st2=map(str,input().split())
h1=len(st1)
h2=len(st2)
count=0
if(h1==h2):
    for i in range(h1):
        if(st1[i]==st2[i]):
            count=count+0
        else:
            count=count+1
            if(count==1):
                print('yes')
            else:
                print('no')
