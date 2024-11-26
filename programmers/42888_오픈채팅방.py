# 시간초과

def solution(record):
    answer = []
    ID = []
    name = []
    
    for i in record:
        arr = list(i.split())
        if arr[0] == 'Enter' and arr[1] not in ID:
            ID.append(arr[1])
            name.append(arr[2])
        elif arr[0] == 'Leave':
            pass
        else: # Change
            name[ID.index(arr[1])] = arr[2]
            
    for i in record:
        arr = list(i.split())
        if arr[0] == 'Enter':
            answer.append(f"{name[ID.index(arr[1])]}님이 들어왔습니다.")
        elif arr[0] == 'Leave':
            answer.append(f"{name[ID.index(arr[1])]}님이 나갔습니다.")
        else: # Change
            pass

    return answer