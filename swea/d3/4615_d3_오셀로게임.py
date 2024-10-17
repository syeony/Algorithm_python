# 오목판정 먼저 보고 이거 보니까 할만했음
# gpt 도움 조금 받았음

def othello(arr,x,y,dol):

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for d in range(8):
        arr2 = []
        start_x = x
        start_y = y

        while True:
            start_x += dx[d]
            start_y += dy[d]

            if not (0<=start_x<N and 0<=start_y<N):
                break

            if arr[start_x][start_y] == 0:
                break

            if arr[start_x][start_y] != dol:
                arr2.append((start_x,start_y))
            elif arr[start_x][start_y] == dol:
                for flip_x, flip_y in arr2:
                    arr[flip_x][flip_y] = dol
                break
            

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2

    for i in range(M):
        x,y,dol = map(int,input().split())
        x -= 1
        y -= 1
        arr[x][y] = dol
        othello(arr,x,y,dol)
    
    black_count = sum(row.count(1) for row in arr)
    white_count = sum(row.count(2) for row in arr)
    
    print(f"#{test_case} {black_count} {white_count}")
