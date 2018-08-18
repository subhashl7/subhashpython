N=input()
s=0
r=0
new=[]
list=[int(x) for x in input().split()]
while(s==0):
    l=list[s]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        print(l,end=" ")
        new.insert(r,l)
        r+=1
    elif((new==[])and(list==[])):
        print('unique')
    if(list==[]):
        break

