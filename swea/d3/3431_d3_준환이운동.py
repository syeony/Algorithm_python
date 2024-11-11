T = int(input())

for test_case in range(1,T+1):
    L, U, X = map(int,input().split())
    result = 0

    if L<=X<=U:
        result = 0
    elif X<L:
        result = L-X
    elif X>U:
        result = -1
    
    print(f"#{test_case} {result}")