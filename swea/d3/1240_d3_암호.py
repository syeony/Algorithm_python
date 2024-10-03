import sys
sys.stdin = open("/Users/ohseungyeon/Documents/GitHub/Algorithm/swea/d3/1240_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    row, col = map(int, input().split()) 

    arr = [list(map(int, input().strip())) for _ in range(row)] 
    new_arr = []
    new2_arr = []

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                new_arr = arr[i]
                break
    
    for i in range(col-1,-1,-1):
        if new_arr[i] == 1:
            new2_arr = new_arr[i-55:i+1]
            break
    
    new3_arr = []
    sum = 0

    for i in range(0,8):
        new3_arr.append(''.join(map(str, new2_arr[i*7:(i*7)+7])))
        if new3_arr[i] == '0001101': new3_arr[i] = 0
        elif new3_arr[i] == '0011001': new3_arr[i] = 1
        elif new3_arr[i] == '0010011': new3_arr[i] = 2
        elif new3_arr[i] == '0111101': new3_arr[i] = 3
        elif new3_arr[i] == '0100011': new3_arr[i] = 4
        elif new3_arr[i] == '0110001': new3_arr[i] = 5
        elif new3_arr[i] == '0101111': new3_arr[i] = 6
        elif new3_arr[i] == '0111011': new3_arr[i] = 7
        elif new3_arr[i] == '0110111': new3_arr[i] = 8
        elif new3_arr[i] == '0001011': new3_arr[i] = 9

        sum += new3_arr[i]

    fomula = (new3_arr[0]+new3_arr[2]+new3_arr[4]+new3_arr[6])*3+new3_arr[1]+new3_arr[3]+new3_arr[5]+new3_arr[7]
    
    if fomula % 10 == 0:
        print(f"#{test_case} {sum}")
    else:
        print(f"#{test_case} 0")
