import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
c = [-1] * a
stack = [0] 

for i in range(1,a):
    while stack and b.count(b[stack[-1]])<b.count(b[i]):
        c[stack.pop()] = b[i]
    stack.append(i)

print(*c) 