# 내 풀이: 팩토리얼 계산 해준다음 0의 개수 일일히 세기
# 답은 맞을텐데 왜 틀렸습니다로 뜰까?
# 일단 gpt한테 물어본 결과 이것보다 더 효율적인 답을 알려주긴 했음

import sys
input = sys.stdin.readline

n = int(input())
multiply = 1

if n == 0:
    multiply = 0
else:
    for i in range(1,n+1):
        multiply *= i

multiply = str(multiply)
sum = 0
for i in range(len(multiply)-1,-1,-1):
    if multiply[i] == '0':
        sum+=1
    else:
        break

print(sum)