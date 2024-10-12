for test_case in range(1,11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    row_arr = []
    col_arr = []
    count = 0

    for i in range(8):
        for j in range(0,8-n+1):
            for x in range(n):
                row_arr.append(arr[i][j+x])
                if len(row_arr) == n:
                    join = ''.join(row_arr)
                    if join == join[::-1]:
                        count+=1
                    row_arr=[]
    
                col_arr.append(arr[j+x][i])
                if len(col_arr) == n:
                    join = ''.join(col_arr)
                    if join == join[::-1]:
                        count+=1
                    col_arr=[]
                
    
    print(f"#{test_case} {count}")