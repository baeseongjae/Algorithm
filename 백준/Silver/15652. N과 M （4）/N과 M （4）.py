N, M = map(int, input().split())
answer = []

def back(tmp):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        if tmp <= i:
            answer.append(i)
            back(i)
            answer.pop()

back(1)