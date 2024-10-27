# 왜 쉽게 풀 생각을 못했을까
# 너무 dfs, bfs만 생각한듯

T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    arr = list(map(int,input().split()))
    max = 0
    
    for i in range(0,n-1):
        for j in range(i+1,n):
            mul = arr[i]*arr[j]
            if mul > max and list(str(mul)) == sorted(str(mul)):
                max = mul

    if max == 0:
        max = -1

    print(f"#{test_case} {max}")
