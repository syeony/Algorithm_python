# 빈 값을 어떻게 처리하냐가 관건이었음
# max행을 구해서 처리해줌

T = int(input())

for tc in range(1, T + 1):
    arr = [list(input().strip()) for _ in range(5)]
    max_len = max(len(i) for i in arr)  

    print(f"#{tc}", end=' ')

    for j in range(max_len):  
        for i in range(5):    
            if j < len(arr[i]): 
                print(arr[i][j], end='')

    print("") 