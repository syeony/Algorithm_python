
def name(word):
    global end
    
    if not word[0].isupper():
        return False
    
    if word[-1] in end:
        word = word[:-1]
    
    for i in word[1:]:
        if not i.islower():
            return False
        
    return True

    # if word[0].isupper() and word[1:].islower():
    #     return True
    
    # return False


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    full = ''
    sentence_count=0
    end = ['.','?','!']

    while sentence_count<n:
        sentence = input()
        full+=sentence

        for i in end:
            sentence_count += sentence.count(i)

    result = []
    cnt = 0

    for word in full.split(): 
        if name(word):
            cnt += 1
        
        if word[-1] in end:
            result.append(cnt)  
            cnt = 0
    
    print(f"#{tc}",end=' ')
    for i in range(len(result)):
        print(result[i],end=' ')
    print()
