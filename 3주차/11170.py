N=int(input())
for i in range(0,N):
    a,b=map(int,input().split())
    sum=0
    for j in range(a,b+1):
        arr = list(map(int,str(j)))
        sum+=arr.count(0)
    print(sum)
