N = int(input())

for i in range(1, N+1):
    iStr = str(i)
    answer = 0
    for item in iStr:
        num = int(item)
        if num != 0 and num % 3 == 0:
            answer += 1

    if answer:
        print('-' * answer, end=' ')
    else:
        print(i, end=' ')
