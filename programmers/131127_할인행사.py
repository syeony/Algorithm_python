def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-10+1):
        discount2 = discount[i:i+10]
        for x in range(len(want)):
            if discount2.count(want[x]) != number[x]:
                # print(discount2, want[x], number[x])
                break
        else:
            answer += 1
                
                    
    return answer