# 2차원 배열에서 가로세로 바꾸는걸 zip으로 저장하는 법 찾아서 적용해봤음

import sys
sys.stdin = open("/Users/ohseungyeon/Documents/GitHub/Algorithm/swea/d3/1216_input.txt", "r")


for test_case in range(1,11):
    n = int(input())
    arr = [list(input()) for _ in range(100)] #행
    arr2 = list(map(list, zip(*arr))) #열
    max = 0

    for i in range(100):
        for j in range(100):
            for change in range(j+1,101):

                row_arr = arr[i][j:change]
                if row_arr == row_arr[::-1]:
                    if len(row_arr) > max:
                        max = len(row_arr)
                
                col_arr = arr2[i][j:change]
                if col_arr == col_arr[::-1]:
                    if len(col_arr) > max:
                        max = len(col_arr)
                
            
    print(f"#{test_case} {max}")