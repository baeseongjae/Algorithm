import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targetArr = list(map(int, input().split()))
dict = {}
arr.sort()

for item in arr:
    if item not in dict:
        dict[item] = 1
    else:
        dict[item] += 1

for item in targetArr:
    start = 0
    end = len(arr)-1
    result = 0
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < item:
            start = mid + 1
        elif arr[mid] > item:
            end = mid - 1
        # 타겟값이 존재한다면 딕셔너리 확인하여 개수반환
        elif arr[mid] == item:
            result = dict.get(item)
            break
    print(result)

    # 이분탐색하다가
    # arr[mid] 값이랑 타겟값이 같으면
    # 앞뒤로 전부 확인
    # or 딕셔너리 활용해서 해당키의 값 개수 반환.
