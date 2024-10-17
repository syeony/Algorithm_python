# 2시간 고민 후 답 참고

def omok(arr):
    # 행, 열, 대각선1, 대각선2
    dx = [0,1,1,1] 
    dy = [1,0,1,-1]
    
    for start_x in range(n):
        for start_y in range(n):
            if arr[start_x][start_y] == 'o':
                for d in range(4):
                    x=start_x
                    y=start_y
                    count = 0
                    while 0<=x<n and 0<=y<n and arr[x][y] == 'o':
                        count += 1
                        x += dx[d]
                        y += dy[d]
                    if count >= 5:
                        return 'YES'
    return 'NO'

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)] #행

    print(f"#{test_case} {omok(arr)}")