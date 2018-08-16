a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
b=[str(x)for x in input()]
sum=0
for i in range(0,len(b)):
    if i>0 and a[b[i]] > a[b[i-1]]:
        sum=a[b[i]]-a[b[i-1]]
    else:
        sum+=a[b[i]]
print(sum)
