T = int(input())

def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    bubble(arr)

    print(f"#{tc}", end=' ')

    for item in arr:
        print(item, end=' ')
    print()