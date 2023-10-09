
arr = input().split("-")
sum = 0

for item in arr[0].split("+"):
    sum += int(item)

for str in arr[1:]:
    for item in str.split("+"): 
        sum -= int(item)
        
print(sum)