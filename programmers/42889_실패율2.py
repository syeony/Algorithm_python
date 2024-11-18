# 참고 : https://study-hub.tistory.com/10
# 문제를 잘못이해했었음
# 사람들이 스테이지에 도전한만큼 사람들 수가 줄어드는 걸 생각못했음

def solution(N, stages):
    answer = []
    dic = {}
    player_count = len(stages)
        
    for i in range(1,N+1):
        if player_count == 0:
            dic[i] = 0
        else:
            dic[i] = stages.count(i)/player_count
            player_count -= stages.count(i)
            
    answer = sorted(dic, key=lambda x: dic[x], reverse = True)
    
    return answer