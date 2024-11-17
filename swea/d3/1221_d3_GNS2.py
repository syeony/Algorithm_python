# 딕셔너리 사용

T = int(input())

for tc in range(1,T+1):
    _ = input()
    arr = list(input().split())

    GNS = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    def a(data):
        return GNS[data]
    
    arr.sort(key=a)
    
    print(f"#{tc}")
    print(' '.join(arr))