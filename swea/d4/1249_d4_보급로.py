# bfs 공부 및 dist부분은 gpt한테 물어봄
# dist를 쓰는 이유는 deque는 2차원 배열처럼 인덱싱이 불가능하기 때문에
# 큐에 넣는 것은 좌표 정보만 담고, 비용 계산을 위해서는 별도의 dist 배열을 만들었다

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 상, 하, 좌, 우
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    dist = [[float('inf')] * n for _ in range(n)]
    dist[x][y] = arr[x][y]

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue #무시하고 처음으로
            if dist[nx][ny] > dist[x][y]+arr[x][y]:
                dist[nx][ny] = dist[x][y] + arr[x][y]
                queue.append((nx,ny))
    
    return dist[n-1][n-1]

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]

    print(f"#{test_case} {bfs(0,0)}")