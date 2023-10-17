N = int(input())

dict = {}

for _ in range(N):
    book = input()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] += 1

dictArr = list(dict.items())

dictArr.sort(key=lambda x: (-x[1], x[0]))

print(dictArr[0][0])