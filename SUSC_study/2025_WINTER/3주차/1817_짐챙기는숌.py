n, m = map(int,input().split())

if n==0:
    print(0)
else:
    arr = list(map(int, input().split()))
    sum=0
    cnt=1
    for i in range(n):
        if sum+arr[i]<=m:
            sum+=arr[i]
        else:
            cnt+=1
            sum=arr[i]

    print(cnt)
