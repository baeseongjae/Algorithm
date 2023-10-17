import sys
input = sys.stdin.readline
N = int(input())
dict = {}
# enter 삽입 , leave 삭제로 해석해서 해시맵 구현하자

# 입력값 받아서 딕셔너리 아이템 삽입, 삭제
for _ in range(N):
    item = list(input().split())
    
    if item[1] == 'enter':
        dict[item[0]] = 1
    elif item[1] == 'leave':
        del dict[item[0]]

dictArr = sorted(dict.keys(), reverse=True)

for person in dictArr:
    print(person)