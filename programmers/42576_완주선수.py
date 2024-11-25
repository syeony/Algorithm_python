# 시간초과

def solution(participant, completion):
    answer = ''
    
    for i in participant:
        if participant.count(i) != completion.count(i):
            answer = i
            break
        else:
            continue
        # if i not in completion:
        #     answer = i
                
    return answer