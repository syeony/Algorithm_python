#바뀐점:enumerate()사용
#기존에는 dic={장르:[플레이수,플레이수,...]}였다면
#이코드는 dic={장르:[[플레이수,인덱스],[플레이수,인덱스],...]}로 저장해나감
#기존코드와 다르게 play수가 겹쳐도 인덱스를 정확하게 찾을 수 있음

def solution(genres, plays):
    answer = []
    dic = {}

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = []
        dic[genre].append([play, index])
    
    for genre in dic:
        dic[genre].sort(key=lambda x: x[0], reverse=True)
    
    dic = dict(sorted(dic.items(), key=lambda item: sum(play for play,index in item[1]), reverse=True))
    
    for key,value in dic.items():
        answer.append(value[0][1])
        if len(value) > 1:
            answer.append(value[1][1])
    
    return answer
