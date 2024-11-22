# 통과못함

def solution(n, k, cmd):
    answer = ['O'] * n
    n_arr = []
    present_position = k
    deleted_arr=[] # 삭제된 [행번호] 저장
    
    for i in range(n):
        n_arr.append(i)
            
    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            present_position += int(cmd[i][2:])
        elif cmd[i][0] == 'U':
            present_position -= int(cmd[i][2:])
        elif cmd[i] == 'C':
            deleted_arr.append(present_position)
            if present_position == n_arr[-1]:
                present_position -= 1
                n_arr.pop()
            else:
                n_arr.pop()
        elif cmd[i] == 'Z': # pop사용
            position = deleted_arr.pop()
            if position <= present_position:
                present_position += 1
            n_arr.append(n_arr[-1]+1)            
            
    deleted_arr.sort()
    for i in range(n):
        if len(deleted_arr)>0 and deleted_arr[0] == i:
            deleted_arr.pop(0)
            answer[i] = 'X'
    
    return ''.join(answer)