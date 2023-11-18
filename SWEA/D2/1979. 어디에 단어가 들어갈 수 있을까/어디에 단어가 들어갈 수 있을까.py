T = int(input())

def checkingRow():
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            # 1이라면
            if arr[i][j] == 1:
                cnt += 1
            # 0이라면 여기서부터 다시시작
            if not arr[i][j]:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    return result

def checkingColumn():
    result = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if not arr[i][j]:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    return result

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    rowResult = checkingRow()
    colResult = checkingColumn()
    answer = rowResult + colResult
    
    print(f"#{tc} {answer}")

# 특정길이 K를 갖는 단어가 들어갈수있는 자리수 출력.
# 가로 세로 따로 확인 로직 만들기
# 세부적으로는 K개수 만큼의 공간이 있는지 확인
