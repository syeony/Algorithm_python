def bfs(s):
    q = []

    q.append(s)
    adj.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)

        for i in adj[c]:
            if not v[i]:
                q.append(i)
                ans_bfs.append(i)
                v[i] = 1

    return v.count(1)-1

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1,n+1):
    adj[i].sort()

ans_bfs = []
v = [0] * (n+1)
print(bfs(1))