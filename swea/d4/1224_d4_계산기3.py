# 조금 고민하다 답 봄
# https://glory-summer.tistory.com/86

for tc in range(1,11):
    n = int(input())
    str = input()
    stack = []
    result = ''

    for i in str:
        if i.isdigit(): #숫자이면
            result += i
        else:
            if i =='(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    
    while stack: #남김없이 다 꺼냄
        result += stack.pop()

    stack = [] 
    for i in result:
        if i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(i))

    print(f"#{tc} {stack[-1]}")