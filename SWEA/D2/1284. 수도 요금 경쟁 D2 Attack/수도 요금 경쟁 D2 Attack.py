T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    answer = 0
    aFee = 0
    bFee = 0

    # B사 이용시 금액계산
    # 월간 사용량이 R이하라면
    if R >= W:
        bFee = Q
    else:
        bFee = Q + (W-R) * S

    # A사 이용시 금액
    aFee = W * P

    answer = min(aFee, bFee)

    print(f"#{tc} {answer}")