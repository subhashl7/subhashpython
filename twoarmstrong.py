a,b = map(int,input().split())
for x in range(a,b):
	temp=x
	num=0
	while x!=0:
		y=x%10
		x=x//10
		num += y**3
	if(num == temp):
		print(temp,end=" ")
