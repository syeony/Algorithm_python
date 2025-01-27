# 메모이제이션 적용
# gpt 도움

n = int(input())

def t(n,memo): # 3
    if n == 0 or n == 1:
        return 1
    
    if n in memo: # 이미 계산된 값이 있다면
        return memo[n] # 바로 반환해서 불필요한 계산 방지
    
    result = 0
    for i in range(n):
        result+= (t(i,memo)*t(n-1-i,memo))

    memo[n]=result
    return result

memo={}

print(t(n,memo))