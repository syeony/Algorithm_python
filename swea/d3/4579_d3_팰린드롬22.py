# 답 봄

T = int(input())

for tc in range(1,T+1):
    n = input()
    reversed_n = n[::-1]
    result = 'Not exist'

    for i in range(len(n)):
        if n[i] == reversed_n[i]:
            continue
        if n[i] == '*' or reversed_n[i]=='*':
            result = 'Exist'
            break
        else:
            break
    else:
        result = 'Exist'
    
    print(f"#{tc} {result}")