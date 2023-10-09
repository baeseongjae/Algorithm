N = int(input())
P = list(map(int, input().split()))
total = 0
answer = 0

P.sort()
for item in P:
    total += item
    answer += total


print(answer)
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값