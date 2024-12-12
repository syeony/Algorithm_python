# 시간초과 -> 찾아본 결과 <투포인터>라는 개념 찾았음

import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))
sum = 0
cnt = 0
cnt_arr = []

for i in range(len(arr)):
    for j in range(i,len(arr)):
        sum += arr[j]
        cnt += 1
        if sum >= s:
            cnt_arr.append(cnt)
            sum,cnt = 0, 0
            break

print(min(cnt_arr))