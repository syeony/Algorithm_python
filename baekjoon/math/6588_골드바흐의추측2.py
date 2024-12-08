# 문제 이해가 안되서 찾아본 블로그 (문제 이해용으로만 봄 답은 안봄)
# https://greentea31.tistory.com/24

import sys
input = sys.stdin.readline

sosu = [True] * 1000001 # 처음엔 모든 수가 전부 소수라고 가정
sosu[0],sosu[1]=False,False # 0,1은 제외

for i in range(2,1000001):
    if i*i > 1000000: break
    if sosu[i] == False: continue
    for j in range(i*i,1000001,i): # 2-> 4,6,8,10,...제외 (2로 나눠지니까 소수가 아님)
        sosu[j] = False

n = int(input())
partition = 0
partition_arr = []

for i in range(n):
    num = int(input())
    for i in range(num):
        if sosu[i] == True and sosu[num-i] == True:
            if (i or num-i) not in partition_arr:
                partition_arr.append(i)
                partition_arr.append(num-i)
                partition += 1
        else:
            continue
    print(partition)
    partition = 0
    partition_arr = []