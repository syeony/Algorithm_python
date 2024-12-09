def solution(n, words):
    answer = []
    arr = []
    
    last_word = words[0][-1]
    arr.append(words[0])
    
    for i in range(1,len(words)):
        if (words[i] not in arr) and (last_word == words[i][0]):
            arr.append(words[i])
            last_word = words[i][-1]
        else:
            a = (i+1)%n
            b = (i+1)//n
            if a == 0:
                answer.append(n)
                answer.append(b)
            else:
                answer.append(a)
                answer.append(b+1)
            break
    else:
        answer.append(0)
        answer.append(0)
            
    return answer