T = int(input())

for tc in range(1,T+1):
    n = list(input().strip())
    result = ''

    for i in range(len(n)):
        if n[i] == '*' or n[-1-i] == '*':
            result = 'Exist'
            break
        else:
            if n[i] != n[-1-i]:
                result = 'Not exist'
                break
    
    if n[0] != n[-1] and (n[0]!='*' and n[-1]!='*'):
        result = 'Not exist'

    print(f"#{tc} {result}")