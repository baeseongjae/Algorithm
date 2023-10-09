# 모든 로프 사용할 필요 X,
# 임의로 몇개만 골라도 됨.
N = int(input())
arr = []
answer = 0 # 버틸수있는 최대무게
k = 0

for i in range(N):
    arr.append(int(input()))

arr.sort()

answer = arr[-1] # 1개 사용시 최대무게
k = 1
for i in range(N-2, -1, -1):
    k += 1
    tmp = arr[i] * k    
    answer = max(tmp, answer)
    
print(answer)