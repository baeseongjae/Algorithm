T = int(input())

for _ in range(T):
    n = int(input())
    dict = {}
    
    for i in range(n):
        wear = list(input().split())
        # 기존에 있었다면 리스트에 추가
        if wear[1] in dict:
            dict[wear[1]].append(wear[0])
        # 없던 옷종류라면 리스트 생성하여 옷 삽입
        else:
            dict[wear[1]] = [wear[0]]
    
    # 알몸만 아니면 되므로
    # 1종류 이상은 착용해야 한다.
    # 3종류(a, b, c) 가 있다면 착용가능한 조합은
    # (a개수+1) * (b개수+1) * (c개수+1)
    cnt = 1
    for key in dict:
        # 각 키에 해당하는값(배열이므로)의 길이
        cnt *= (len(dict[key]) + 1)
    
    # 집합 {a, b, c}로 나올 수 있는 경우
    # 공집합, {a}, {b}, {c}, {a,b}, {b,c}, {c,a}, {a,b,c}
    # 즉, 아무옷도 입지않은 경우를 빼준다.
    print(cnt - 1)