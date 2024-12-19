# 메모리 초과

import sys
input = sys.stdin.readline

n,l = map(int,input().split())
arr = [] # 범위
max_num = 0

for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
    max_num = max(max_num,b)

arr = sorted(arr, key=lambda x: x[0])

p = ['.' for _ in range(max_num)] # 웅덩이

for i in range(len(arr)):
    p[arr[i][0]:arr[i][1]] = ['M'] * (arr[i][1]-arr[i][0])

count = 0
for i in range(max_num): # 메모리 초과
    if p[i] == 'M':
        for j in range(l):
            p[i+j] = '.'
        count += 1

print(count)
