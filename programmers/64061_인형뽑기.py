def solution(board, moves):
    answer = 0 #터트려서 사라진 인형의 갯수
    arr_count = len(board[0])
    stack = []
    
    for i in range(len(moves)):
        for j in range(arr_count):
            if board[j][moves[i]-1] != 0:
                stack.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                moves[i] = 0
                break
        if len(stack) >=2 and stack[-1] == stack[-2]:
            answer+=2
            stack.pop()
            stack.pop()
                        
    return answer