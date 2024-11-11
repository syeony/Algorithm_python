n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(arr,x,y):
    q = []
    q.append((x,y))

    arr[x][y] = 0
    num = 1

    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] 

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                num+=1
                arr[nx][ny] = 0
                q.append((nx,ny))
    
    return num
            
        
num_arr = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            num_arr.append(bfs(arr,i,j))

num_arr.sort()
print(len(num_arr))
for i in range(len(num_arr)):
    print(num_arr[i])