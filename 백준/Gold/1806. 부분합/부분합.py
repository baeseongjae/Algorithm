import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
j = 0
minValue = 10 ** 5
total = arr[i]

while j < N:
    if total < S:
        j += 1
        if j >= N:
            break
        total += arr[j]

    elif total >= S:
        minValue = min(j-i+1, minValue)
        total -= arr[i]
        i += 1

if minValue == 10**5:
    print(0)
else:
    print(minValue)
