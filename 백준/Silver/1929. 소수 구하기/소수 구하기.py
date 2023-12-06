M, N = map(int, input().split())

checkArr = [True] * (N+1)

# ★에라토스 테네스의 체
# 먼저 특정 범위 내의 모든 숫자에 대해 소수 여부를 판별한 다음, 
# 이 정보를 이용하여 원하는 범위의 소수를 찾자!

checkArr[0] = False
checkArr[1] = False

# 제곱근까지만 반복 => 시간 줄이기
for i in range(2, int(N**0.5)+1):
    if checkArr[i]:
        for j in range(i*2, N+1, i):
            checkArr[j] = False

for i in range(M, N+1):
    if checkArr[i]:
        print(i)