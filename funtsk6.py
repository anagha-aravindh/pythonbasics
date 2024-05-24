# factusingfunction
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))
# fibo
def fib(num):
    a=0
    b=1
    i=0
    while i<n:
        print(a,end=" , ")
        c=a+b
        a=b
        b=c
        i+=1
n=int(input("enter the limit:"))
fibon=fib(n)
print(fib)
# sumofn
def sum(n):
    t=0
    for i in range(1,n+1):
        t+=i
    return t
n=int(input("enter a no:"))
print(sum(n))