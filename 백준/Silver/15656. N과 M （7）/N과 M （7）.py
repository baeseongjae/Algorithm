N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

def back():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(N):
        answer.append(arr[i])
        back()
        answer.pop()

arr.sort()
back()