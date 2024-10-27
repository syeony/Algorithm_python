T = int(input())

for test_case in range(1,T+1):
    h,w=map(int,input().split())
    arr = [list(input().strip()) for _ in range(h)]
    n = int(input())
    m = list(input().strip())
    
    # u,d,r,l
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    rocket = ''
    x_direction = 0
    y_direction = 0
    x_position = 0
    y_position = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '^' or arr[i][j] == 'v' or arr[i][j] == '<' or arr[i][j] == '>':
                x_position = i
                y_position = j
                if arr[i][j] == '^':
                    x_direction = dx[0]
                    y_direction = dy[0]
                if arr[i][j] == 'v':
                    x_direction = dx[1]
                    y_direction = dy[1]
                if arr[i][j] == '<':
                    x_direction = dx[3]
                    y_direction = dy[3]
                if arr[i][j] == '>':
                    x_direction = dx[2]
                    y_direction = dy[2]

    for i in range(len(m)):
        if m[i] == 'S':
            while(1):
                pass
        if m[i] == 'U':
            pass
        if m[i] == 'D':
            pass
        if m[i] == 'L':
            pass
        if m[i] == 'R':
            pass
