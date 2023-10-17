# 이제껏 메모장에서 사이트의 비밀번호를 직접 찾았다.
# 메모장에서 비밀번호를 찾는 프로그램

# 해시맵 (딕셔너리로 구현)을 활용하자
N, M = map(int, input().split())
dict = {} # item 쌍은 (key=주소, value=비밀번호)로 삽입하자.

for _ in range(N):
    item = list(input().split())
    dict[item[0]] = item[1]

for _ in range(M):
    targetKey = input()
    print(dict[targetKey])
