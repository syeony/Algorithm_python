def dfs(c): #깊이우선
    v[c] = 1
    ans_dfs.append(c)

    for i in adj[c]:
        if not v[i]:
            dfs(i)

def bfs(s): #너비우선
    q=[]

    ans_bfs.append(s)
    v[s] = 1
    q.append(s)

    while q: #q가 있을때
        c = q.pop(0) #선입선출

        for i in adj[c]:
            if not v[i]:
                ans_bfs.append(i)
                q.append(i)
                v[i] = 1


N, M, V = map(int,input().split())
adj = [[] for _ in range(N+1)]

for i in range(M): #노드의 개수가 아닌 간선의 개수로
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1,N+1): #노드가 1부터 N개까지 있기 때문에
    adj[i].sort()

ans_dfs = []
v = [0] * (N+1)
dfs(V)

ans_bfs = []
v = [0] * (N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)