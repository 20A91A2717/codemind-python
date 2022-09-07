x,y=map(int,input().split())
h=0
for i in range(1,y+1):
    if x%i==0 and y%i==0:
        h=i
print(h)