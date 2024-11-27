#gpt도움
#하지만 테케15개중 2,14번 실패
#이유분석:동일한 play 값이 여러 번 등장하는 경우 잘못된 인덱스를 반환할 수 있음
#생각해낸 방법:play랑 index를 같이 저장하자 -> enumerate()를 사용

def solution(genres, plays):
    answer = []
    
    #genres=plays리스트 딕셔너리 하나 만들어서
    dic={}
    for genre,play in zip(genres,plays):
        if genre not in dic:
            dic[genre] = []
        dic[genre].append(play)
    
    #plays리스트 정렬
    for i in dic:
        dic[i].sort(reverse=True)
        
    #plays리스트 합계가 큰순으로 dic 정렬
    dic = dict(sorted(dic.items(), key=lambda item:sum(item[1]), reverse=True))
    
    #각각 최대 두개까지만 answer에 저장
    for key,value in dic.items():
        answer.append(plays.index(value[0]))
        if len(value) > 1:
            answer.append(plays.index(value[1]))
    
    return answer