def main():
 a = int(input())
 factorial=1
 if(a == 0):
   print("The factorial of 0 is 1")
 elif(a>0):
   for i in range(1,a+1):
       factorial = factorial*i
   print(factorial)

if __name__ == '__main__':
    main()
