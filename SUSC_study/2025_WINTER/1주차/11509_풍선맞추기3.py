# 런타임에러 -> sys.stdin.readline()사용해봄
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

height = [0] * 1000001 # 이게 문제였어!!! 다음에 질문해야지!!

for i in arr: # 4 5 2 1 4
    if height[i]>0:
        height[i]-=1
        height[i-1]+=1
    else:
        height[i-1]+=1
    # 0 1 2 3 4 5
    # 1     2

print(sum(height))
