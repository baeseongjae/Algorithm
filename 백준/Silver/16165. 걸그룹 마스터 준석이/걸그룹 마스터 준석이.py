
# N 걸그룹수, M 퀴즈수
N, M = map(int, input().split())
dict1 = {} # {'팀이름' : ['멤버이름','멤버이름', ...] }
dict2 = {} # 

# 걸그룹 데이터 전부 입력완료
# 형식 
# {
#     ('팀이름', 인원수): ['멤버1','멤버2', ...]
#   }
for i in range(N):
    team = input()
    num = int(input())
    dict1[team] = []
    for _ in range(num):
        name = input()
        dict1[team].append(name)
        dict2[name] = team

# => ?
# 아마 

for _ in range(M):
    quiz = input()
    type = int(input())

    # 타입이 1이라면 멤버의 소속팀 출력
    if type:
        print(dict2[quiz])
    # 0이라면 팀의 소속멤버 모두 출력
    else:
        memberArr = sorted(dict1[quiz])
        for member in memberArr:
            print(member)