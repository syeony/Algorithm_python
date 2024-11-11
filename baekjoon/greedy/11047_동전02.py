N, K = map(int,input().split())
arr = []
K_sum = K
num = 0

for i in range(N):
    n = int(input())
    arr.append(n)

for i in range(N-1,-1,-1):
    if K_sum>=arr[i]:
        count = K_sum // arr[i]
        num += count
        K_sum -= arr[i] * count

print(num)