# 답 보고 dictionary 이용

def solution(participant, completion):
    answer = ''
    dic = {}
    
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        
    for i in completion:
        dic[i] -= 1
        
    for key,value in dic.items(): # 이거 쓰는 법 외워놓기
        if value != 0:
            answer = key
                
    return answer