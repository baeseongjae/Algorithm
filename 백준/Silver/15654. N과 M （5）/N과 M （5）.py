N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
arr.sort()

def back():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(N):
        if arr[i] not in answer:
            answer.append(arr[i])
            back()
            answer.pop()

back()