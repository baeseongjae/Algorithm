N, M = map(int, input().split())
answer = []

def back():
    #배열 길이 확인
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N+1):
        # 중복확인
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()

back()
