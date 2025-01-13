import math

N=int(input())

for i in range(0,N):
    a, b = map(int, input().split())
    combination = math.factorial(b) // (math.factorial(a) * math.factorial(b - a))
    print(combination)
