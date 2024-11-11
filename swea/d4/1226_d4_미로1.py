# 백준 2178과 유사한 문제

for tc in range(1,11):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(16)]

    # 상하좌우
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    def bfs(x,y):
        q=[]
        q.append((x,y))
        answer = 0

        while q:
            x,y = q.pop(0)

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if arr[nx][ny] == 1:
                    continue
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = 4
                    q.append((nx,ny))
                elif arr[nx][ny] == 3:
                    answer = 1
                    break
        return answer
            

    print(f"#{tc} {bfs(1,1)}")
