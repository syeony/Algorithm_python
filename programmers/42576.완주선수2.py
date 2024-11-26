# 고고님 코드 보고 sort로 접근하니까 시간초과 안남
# count가 시간 많이 잡아먹는듯

def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()
    
    if len(completion) != len(participant):
        completion.append("0")
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
                
    return answer