# 절반만 맞음
# 틀린이유 분석: 꼭 1,2에서만 대결해야되는줄 알았음 그러나 중간에 만나 대결할 가능성을 생각 못했음
# 틀림확인 예시: 8,7,8 -> 3

def solution(n,a,b):
    answer = 0
    
    #1,2,3,4,5,6,7,8
    #4-2-1 7-4-2
    
    c=max(a,b)
    
    while True:
        c = c/2
        answer += 1
        if c<=1:
            break

    return answer