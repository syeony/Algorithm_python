T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    mok = a//b
    na = a%b
    print(f"#{test_case} {mok} {na}")