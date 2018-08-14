a = int(input())
b = [int(x) for x in input().split()]
n = sorted(b)
for y in range(a):
    print(n[y],end=" ")
