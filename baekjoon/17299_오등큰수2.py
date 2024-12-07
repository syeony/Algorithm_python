import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
c = [-1] * a
stack = [0]
cnt = [0] * 1000001
for i in b:
    cnt[i] += 1

for i in range(1,a):
    while stack and cnt[b[stack[-1]]]<cnt[b[i]]:
        c[stack.pop()] = b[i]
    stack.append(i)

print(*c) 