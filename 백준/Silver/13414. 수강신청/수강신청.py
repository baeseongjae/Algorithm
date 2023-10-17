# 수강신청 부하 관리 시스템
# - 중복된 경우 대기번호 밀려난다. => 이전꺼 지우고 다시 삽입하면 될듯?
# - 가장 앞에 있는 학생부터 수강 가능인원만큼 출력.
import sys

input = sys.stdin.readline
K, L = map(int, input().split())
db = {}

for _ in range(L):
    student = input().rstrip()

    # db에 학생데이터 없다면
    if student not in db:
        db[student] = 1
    # 있다면 (버튼을 한번 더 누른 것이므로 맨뒤로 밀려남)
    else:
        del db[student]
        db[student] = 1

dbArr = list(db)
if len(dbArr) < K:
    for item in dbArr:
        print(item)
else:
    for i in range(K):
        print(dbArr[i])