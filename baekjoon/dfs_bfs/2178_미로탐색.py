N, M = map(int,input().split())

arr = [list(map(int,input().strip())) for _ in range(N)]

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = []
    q.append((x,y))

    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))

    for i in range(N):
        print(arr[i])
        
    return arr[N-1][M-1]


print(bfs(0,0))