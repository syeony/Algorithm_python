import sys
sys.stdin = open("/Users/ohseungyeon/Documents/GitHub/Algorithm/swea/d4/1210_input.txt", "r")

for test_case in range(1,11):
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]
    X = 0
    Y = 99

    # 2 찾아내기
    for i in range(100):
        if arr[Y][i] == 2:
            X = i
            break

    while True:
        if Y-1 >= 0:
            Y -= 1
            if X-1 >= 0 and arr[Y][X-1] == 1:
                for i in range(X-1,-1,-1):
                    if arr[Y][i] == 1:
                        X -= 1
                    else:
                        break
            elif X+1 <= 99 and arr[Y][X+1] == 1:
                for i in range(X+1,100):
                    if arr[Y][i] == 1:
                        X += 1
                    else:
                        break
        else:
            break
    
    print(f"#{test_case} {X}")

        
