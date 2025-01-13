T = int(input())

for tc in range(1,T+1):

    dx=[0,0,1,-1,1,-1,1,-1]
    dy=[1,-1,0,0,1,-1,-1,1]

    
    n = int(input())
    arr = [list(map(input().strip())) for _ in range(n)]

    