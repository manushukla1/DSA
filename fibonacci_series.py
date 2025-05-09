"""def fibo (n):
    if n == 1 :
        return 0
    if n == 2 :
        return 1
    return ((fibo(n-1)+fibo(n-2)))
n = int(input("Enter a number:"))
for i in range (1, n +1 ):
    print (fibo(i))
"""


def fib(n):
    a = 0
    b = 1
    #print(a)
    #print(b)

    for i in range (n):
        c = a+b
        a = b
        b = c
        print(c)

userinp = int(input("give number:"))
fib(userinp)