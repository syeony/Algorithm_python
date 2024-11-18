# gpt한테 딕셔너리 사용법 많이 물어봄
# 그러나 시간초과

def solution(N, stages):
    answer = []
    dic = {}
        
    for i in range(1,N+1):
        mo, ja = 0, 0
        for j in range(len(stages)):
            if stages[j] >= i:
                if stages[j] > i:
                    pass
                elif stages[j] == i:
                    ja += 1
            if stages[j] >= i:
                mo += 1
        dic[i] = ja/mo if mo != 0 else 0 # 런타임에러 해결
            
    sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse = True)) 
    
    # print(sorted_dic)
    
    answer = list(sorted_dic.keys())
    
    return answer