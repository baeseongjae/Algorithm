s, p = map(int, input().split())
data = input()
acnt, ccnt, gcnt, tcnt = map(int, input().split())
answer = 0
# 두개의 포인터 지정
i = 0
j = p - 1

# 딕셔너리
dict = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
targetStr = data[i:j]

for item in targetStr:
    dict[item] += 1

# 슬라이딩 윈도우
while j <= s-1:
    # 인덱스 초과 나니까 j+=1 하기전에, 오른쪽 원소 추가하는 로직을 먼저.
    dict[data[j]] += 1

    # 비밀번호 유효성 검사
    if dict['A'] >= acnt and dict['C'] >= ccnt and dict['G'] >= gcnt and dict['T'] >= tcnt:
        answer += 1

    dict[data[i]] -= 1 # 인덱스 맨 왼쪽 문자열 제거
    i += 1
    j += 1

print(answer)