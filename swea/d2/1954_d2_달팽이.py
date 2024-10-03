# 답 참고

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    
    # 우, 하, 좌, 상
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    present = 0
    value = 1
    i,j=0,0

    while value <= N*N:
        arr[i][j] = value
        value+=1

        nx, ny = i+dx[present], j+dy[present]

        # 가려는 곳이 끝이거나 값이 채워져있을 때
        if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny]!=0:
            present = (present+1)%4
            nx, ny = i+dx[present], j+dy[present]

        i,j = nx, ny

    print(f"#{test_case}")
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print("")