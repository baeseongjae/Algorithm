N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
targetArr = list(map(int, input().split()))

def binarySearch(arr, targetArr):

    for target in targetArr:
        start = 0
        end = len(arr) - 1
        answer = 0

        while start <= end:
            mid = (start + end) // 2
            if target < arr[mid]:
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            elif target == arr[mid]:
                answer = 1
                break
        print(answer)

binarySearch(arr, targetArr)