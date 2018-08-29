N,K = input().split()
N,K = int(N),int(K)
N = N ^ K
K = N ^ K
N = N ^ K
print(N,K)
