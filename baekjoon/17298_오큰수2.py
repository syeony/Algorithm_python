import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
c = [-1] * a
stack = [0] # 스택을 사용하면 시간을 줄일 수 있다

for i in range(1,a):
    while stack and b[stack[-1]]<b[i]:
        c[stack.pop()] = b[i]
    stack.append(i)

print(*c) # 새롭게 알게된거