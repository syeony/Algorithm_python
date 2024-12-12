# 큰 수를 찾아서 그 수 기준 시계, 반시계 회전
# 틀림

import sys
input = sys.stdin.readline

a,b=map(int,input().split())
arr = list(map(int,input().split()))

max_num = max(arr)
max_index = arr.index(max_num)

sum1 = 0
cnt1 = b
for i in range(max_index):
    sum1 += arr[i]
    cnt1 -= 1
sum1 += (max_num*cnt1)

sum2 = 0
cnt2 = b
for j in range(a-1,max_index-1,-1):
    sum2 += arr[j]
    cnt2 -= 1
sum2 += (max_num*cnt2)

print(max(sum1,sum2))