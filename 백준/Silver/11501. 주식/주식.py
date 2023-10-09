T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxValue = 0
    answer = 0

    for i in range(N-1, -1, -1):
        if maxValue < arr[i]:
            maxValue = arr[i]
        else:
            answer += maxValue - arr[i]
    print(answer)