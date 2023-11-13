T = int(input())

def solution():
    tc = input()
    arr = list(map(int, input().split()))
    cnt = [0] * 101
    answer = 0

    for item in arr:
        cnt[item] += 1
    maxCnt = max(cnt)

    for i in range(100, -1, -1):
        if cnt[i] == maxCnt:
            answer = i
            break

    print(f"#{tc} {answer}")

for i in range(T):
    solution()