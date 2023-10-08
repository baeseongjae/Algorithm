N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
targetIdx = 0

sortArr = sorted(medals, key=lambda x: (-x[1], -x[2], -x[3]))

for idx, item in enumerate(sortArr):
    if item[0] == K:
        targetIdx = idx
        
# K국가의 인덱스를 뽑아서 sortArr조회

for i in range(len(sortArr)):
    if sortArr[i][1:] == sortArr[targetIdx][1:]:
        print(i+1)
        break