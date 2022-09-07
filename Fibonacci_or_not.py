n=int(input())
def fib(n):
    lst=[]
    a=0
    b=1
    while b<=n:
        lst.append(a)
        lst.append(b)
        a,b=b,a+b
    return lst
if n in fib(n): print(True)
else: print(False)