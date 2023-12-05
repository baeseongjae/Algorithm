data = input()
dict = {}

for a in data:
    tmp = a.upper()
    if tmp not in dict:
        dict[tmp] = 1
    else:
        dict[tmp] += 1

maxValue = max(dict.values())
cnt = 0

for key, value in dict.items():
    if value == maxValue:
        answer = key
        cnt += 1

if cnt == 1:
    print(answer)
else:
    print('?')