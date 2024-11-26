# 시간초과 dictionary 사용하여 해결

def solution(record):
    answer = []
    id_name = {}
    
    for i in record:
        arr = list(i.split())
        if arr[0] == 'Enter':
            id_name[arr[1]]=arr[2]
        elif arr[0] == 'Change':
            id_name[arr[1]]=arr[2]
            
    for i in record:
        arr = list(i.split())
        if arr[0] == 'Enter':
            answer.append(f"{id_name[arr[1]]}님이 들어왔습니다.")
        elif arr[0] == 'Leave':
            answer.append(f"{id_name[arr[1]]}님이 나갔습니다.")

    return answer