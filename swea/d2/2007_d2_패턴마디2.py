T = int(input())

for tc in range(1,T+1):
    n = input()
    for i in range(1,10):
        if n[:i] == n[i:i*2]:
            print(f"#{tc} {i}")
            break