import sys
sys.stdin = open("/Users/ohseungyeon/Documents/GitHub/Algorithm/swea/d3/1220_input2.txt", "r")

for test_case in range(1,11):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):

            if arr[i][j] == 1:
                if i < n-1:
                    if arr[i+1][j] == 2:
                        pass
                    else:
                        arr[i][j] = 0
                        arr[i+1][j] = 1
                if i == n-1:
                    arr[i][j] = 0

            if arr[n-1-i][j] == 2:
                if n-1-i > 0:
                    if arr[n-2-i][j] == 1:
                        pass
                    else:
                        arr[n-1-i][j] = 0
                        arr[n-2-i][j] = 2
                if n-1-i == 0:
                    arr[n-1-i][j] = 0

    for i in range(n):
        for j in range(1,n):
            if arr[j-1][i] == 1 and arr[j][i] == 2:
                count += 1
    
    print(f"#{test_case} {count}")