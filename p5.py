s={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
r=[str(x)for x in input()]
sum=0
for i in range(0,len(r)):
    if i>0 and s[r[i]] > s[r[i-1]]:
        sum=s[r[i]]-s[r[i-1]]
    else:
        sum+=s[r[i]]
print(sum)
