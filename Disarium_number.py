def s(n):
    summ=0
    a=len(str(n))
    while n>0:
        r=n%10
        summ=summ+r**a
        a-=1
        n=n//10
    return summ
n=int(input())
print(n==s(n))