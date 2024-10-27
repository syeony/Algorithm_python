for test_case in range(1,11):
    n = int(input())

    a, b = map(int,input().split())

    result = a ** b
    print(f"#{test_case} {result}")