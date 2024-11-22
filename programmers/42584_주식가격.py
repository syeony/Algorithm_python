def solution(prices):
    answer = []
    
    for i in range(0,len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)
        
    answer.append(0)
                    
    return answer