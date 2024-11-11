T = int(input())

for tc in range(1,T+1):
    n, p = map(int,input().split())
    sum = 0

    for i in range(1,n+1):
        sum+=i
        if sum == p:
            sum-=1
    
    print(sum)