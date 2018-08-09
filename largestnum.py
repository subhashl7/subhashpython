#subbu#largestnumber
a,b,c = map(int,raw_input().split())
if(a>b and a>c):
	ptint('a is largest num')
elif(b>a and b>c):
	print('b is largest num')
else:
	print('c is largest num')
