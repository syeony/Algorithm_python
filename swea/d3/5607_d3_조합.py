import math

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

T = int(input())

for test_case in range(1,T+1):
    n,r = map(int,input().split())
    result = combination(n,r)
    print(f"#{test_case} {result}")

