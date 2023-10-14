N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

def back(tmp):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(N):
        if arr[i] not in answer and tmp <= arr[i]:
            answer.append(arr[i])
            back(arr[i])
            answer.pop()

arr.sort()
back(arr[0])