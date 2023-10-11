import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))

sumArr = []


sumArr.append(arr[0])

for i in range(1,n):
    sumArr.append(sumArr[i-1] + arr[i])

for _ in range(m):
    i, j = map(int,input().split())
    if i==1:
        print(sumArr[j-1])
    else:
        print(sumArr[j-1]-sumArr[i-2])
    

