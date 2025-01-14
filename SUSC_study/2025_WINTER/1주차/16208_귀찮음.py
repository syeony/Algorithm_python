t = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
answer = 0

for i in range(t-1):
    answer+=(arr[i]*(s-arr[i]))
    s-=arr[i]

print(answer)