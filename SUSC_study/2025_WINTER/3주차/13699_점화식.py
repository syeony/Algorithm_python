# 3은 잘 나오는데 왜 25는 안나오지?

n = int(input())

def t(n): # 3
    if n == 0 or n == 1:
        return 1
    
    result = 0
    for i in range(n): # 0 1 2
        result+= (t(i)*t(n-1-i))

    return result

print(t(n))