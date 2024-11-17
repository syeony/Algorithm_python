T = int(input())

def dfs(v,count):
    global max_count
    visit[v] = 1

    for i in li[v]:
        if visit[i] == 0:
            dfs(i,count+1)

    visit[v] = 0
    max_count = max(max_count,count)

for tc in range(1,T+1):
    n,m = map(int,input().split())
    li = [[] for _ in range(n+1)]
    
    for i in range(m):
        x,y = map(int, input().split())
        li[x].append(y)
        li[y].append(x)
    
    visit = [0] * (n+1)
    count, max_count = 0,0
    
    for i in range(n+1):
        dfs(i,1)

    print(f"#{tc} {max_count}")