T = int(input())

tmp = []

for _ in range(T):
    tmp.append(int(input()))

cache = [0,1,2,4]

for i in range(4,max(tmp)+1): #4부터 N까지 저장된 최댓값까지
    cache.append(cache[i-1]+cache[i-2]+cache[i-3])

for n in tmp:
    print(cache[n])

