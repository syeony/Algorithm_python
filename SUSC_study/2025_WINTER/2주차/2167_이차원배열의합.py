n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
k=int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    sum=0
    for q in range(i-1,x):
        for w in range(j-1,y):
            sum+=arr[q][w]
    print(sum)