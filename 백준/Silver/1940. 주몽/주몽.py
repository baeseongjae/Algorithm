import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int,input().split()))

sortArr = sorted(arr)
i=0
j=n-1
cnt = 0

while i<j:
    if sortArr[i]+sortArr[j] > m:
        j-=1
    elif sortArr[i]+sortArr[j] == m:
        cnt+=1
        i+=1
        j-=1
    elif sortArr[i]+sortArr[j] < m:
        i+=1 

print(cnt)