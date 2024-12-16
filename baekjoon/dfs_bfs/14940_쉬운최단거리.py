import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
goal = []

flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal.append(i)
            goal.append(j)
            flag = True
            break
    if flag:
        break

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    q = []
    q.append((x,y))

    visited[x][y] = 0

    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] 

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    
    return visited
            
        
visited=bfs(goal[0],goal[1])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()