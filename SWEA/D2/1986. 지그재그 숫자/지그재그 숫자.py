T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    D = [0] * 11
    answer = 0

    D[1] = 1
    D[2] = -1
    for i in range(3, N+1):
        # i가 홀수라면
        if i % 2 != 0:
            D[i] = D[i-1] + i
        elif i % 2 == 0:
            D[i] = D[i-1] - i

    answer = D[N]
    print(f"#{test_case} {answer}")