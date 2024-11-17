from collections import deque

n = int(input())
deque = deque()

for i in range(1,n+1):
    deque.append(i)

while len(deque) > 1:
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)


print(deque[0])