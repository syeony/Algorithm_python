N = int(input())
sum = 0
i=0

while sum<=N:
    i = i + 1
    sum = sum + i

if sum>N:
    print(i-1)
else:
    print(i)