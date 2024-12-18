# gpt가 도와줌
# 접근방법: 10이 몇번 곱해지는지, 즉 2와 5의 쌍의 개수
# 5로 나누면서 카운팅

import sys
input = sys.stdin.readline

n = int(input())
count = 0

while n>=5:
    count += n//5
    n//=5

print(count)