def fact(n):
    fac=[]
    for i in range(1,n//2+1):
        if n%i==0:
            fac.append(i)
    return fac
n=int(input())
if sum(fact(n))>n:
    print(True)
else: print(False)