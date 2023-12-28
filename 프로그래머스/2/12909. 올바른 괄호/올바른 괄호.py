def solution(s):
    answer = True
    stack = []
    
    for item in s:
        if item == '(':
            stack.append(item)
        elif item == ')':
            # 스택에 남아있다면
            if len(stack):
                stack.pop();
            else:
                return False;
    
    if len(stack):
        answer = False
            
    return answer