# 시간초과

n = int(input())
li = []

for i in range(1,n+1):
    li.append(i)

while len(li) > 1:
    del li[0]
    temp = li[0]
    del li[0]
    li.append(temp)

print(li[0])