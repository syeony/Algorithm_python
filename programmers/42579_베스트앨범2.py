#바뀐점:enumerate()사용
#기존에는 dic={장르:[플레이수,플레이수,...]}였다면
#이코드는 dic={장르:[[플레이수,인덱스],[플레이수,인덱스],...]}로 저장해나감
#기존코드와 다르게 play수가 겹쳐도 인덱스를 정확하게 찾을 수 있음

def solution(genres, plays):
    answer = []
    
    # 딕셔너리 생성
    dic = {}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = []
        # (재생 수, 고유 인덱스) 형태로 저장
        dic[genre].append([play, index])
    
    # 장르별 재생 수를 기준으로 정렬
    for genre in dic:
        # 재생 수 내림차순, 동일 재생 수일 경우 인덱스 오름차순으로 정렬
        dic[genre].sort(key=lambda x: x[0], reverse=True)
    
    # 장르 총 재생 수를 기준으로 정렬
    dic = dict(sorted(dic.items(), key=lambda item: sum(play for play,index in item[1]), reverse=True))
    
    # 각 장르에서 최대 두 곡 선택
    for key,value in dic.items():
        answer.append(value[0][1])
        if len(value) > 1:
            answer.append(value[1][1])
    
    return answer
