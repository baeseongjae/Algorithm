N = int(input())
arr = []
def hanoi(n, start, end):
    if n == 1:
        arr.append((start, end))
        return
    
    hanoi(n-1, start, 6-start-end)
    arr.append((start, end))
    hanoi(n-1, 6-start-end, end)

hanoi(N, 1, 3)
print(len(arr))

for item in arr:
    print(item[0], item[1])