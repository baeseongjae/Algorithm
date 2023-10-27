N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxValue = - int(1e9)
minValue = int(1e9)

def DFS(add, sub, mul, div, total, i):
    global maxValue, minValue

    if i == N:
        maxValue = max(maxValue, total)
        minValue=  min(minValue, total)
        return
    # 연산자 삽입
    if add:
        DFS(add-1, sub, mul, div, total+arr[i], i+1)
    if sub:
        DFS(add, sub-1, mul, div, total-arr[i], i+1)
    if mul:
        DFS(add, sub, mul-1, div, total*arr[i], i+1)
    if div:
        DFS(add, sub, mul, div-1, int(total/arr[i]), i+1)
            

DFS(add, sub, mul, div, arr[0], 1)
print(maxValue)
print(minValue)
# 연산자 우선순위 무시
# 1 2 3 4 5 6
# + + - * /

# N개의 수와 N-1개의 연산자가 주어질때 만들수있는 결과가 최대인것과 최소인것 구하기
# 완전탐색