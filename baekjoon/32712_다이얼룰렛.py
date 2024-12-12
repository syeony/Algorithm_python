# 실패

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
arr = list(map(int,input().split()))

if a>b:
    max_arr = max(arr[:b])
else:
    max_arr = max(arr)

sum = 0

for i in arr:
    if i == max_arr:
        break
    else:
        sum += i
        b-=1

sum += (b*max_arr)

print(sum)