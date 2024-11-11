# 시간초과

N, K = map(int,input().split())
arr = []
K_sum = K
num = 0

for i in range(N):
    n = int(input())
    arr.append(n)

for i in range(N-1,-1,-1):
    if K>=arr[i]:
        while True:
            K_sum -= arr[i]
            if K_sum<0:
                K_sum += arr[i]
                break
            num += 1

print(num)