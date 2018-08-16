def main():
 N = int(input())
 factorial=1
 if(N == 0):
   print("1")
 elif(N>0):
   for i in range(1,N+1):
       factorial = factorial*i
   print(factorial)

if __name__ == '__main__':
    main()
