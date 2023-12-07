# N = 2, M = 2, K = 2 라면
# aazz, azaz, azza, zaaz, zaza, zzaa

# D[1][2] 는 D[2][2] 안에서
# azz, zaz, zza 이다. 
# (모두 맨앞에 a를 이어 D[2][2]에 포함될 후보군)
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
D = [[0 for _ in range(M+1)] for _ in range(N+1)]
answer = ''

#a와 z중 하나로만 만들 수 있는 문자열 조합 경우의수 전부 1로 초기화
for i in range(N+1):
    D[i][0] = 1
for j in range(M+1):
    D[0][j] = 1 

# 점화식 기반으로 경우의수 계산
for i in range(1, N+1):
    for j in range(1, M+1):
        D[i][j] = D[i-1][j] + D[i][j-1]

maxArr = list(map(max, D))
maxVal = max(maxArr)

if maxVal < K:
    print(-1)
else:
    while N > 0 and M > 0:
        tmp = D[N-1][M] # 현재 타겟 인덱스의 알파벳을 a로 고정했을때, 후보군 경우의수

        if K <= tmp:  # 현재 알파벳을 a로 고정한 인덱스 범위 안에 K가 속해있을때,
            N -= 1  # 그 자리 a로 확정
            answer += 'a'
        else: # K가 더 크다는 말은, a를 고정한 인덱스들의 범위안에 없으므로 z가 되어야한다.
            M -= 1
            K -= tmp
            answer += 'z'

    # N, M 중 하나가 0이 되어 반복문 빠져나오면, 나머지 하나 마저 이어주기
    answer += ('a' * N + 'z' * M)
    print(answer)