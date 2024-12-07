# 시간초과

a = int(input())
b = list(map(int,input().split()))
c = []

for i in range(a-1):
    for j in range(i+1,a):
        if b[j]>b[i]:
            c.append(str(b[j]))
            break
    else:
        c.append('-1')

c.append('-1')

print(' '.join(c))