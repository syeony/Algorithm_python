T = int(input())

for tc in range(1,T+1):
    n = input()
    print(f"#{tc}", end=' ')
    if n == n[::-1]:
        print(1)
    else:
        print(0)