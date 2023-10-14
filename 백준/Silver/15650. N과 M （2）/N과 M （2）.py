N, M = map(int, input().split())
answer = []

def back(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
    
    for i in range(start, N+1):
        if i not in answer:
            answer.append(i)
            back(i+1)
            answer.pop()

back(1)

# 중복되는 수열 여러번 출력 X
