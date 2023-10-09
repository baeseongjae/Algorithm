str = input()
p = 0
zCnt = 0
oCnt = 0
end = len(str)-1

while p <= end:
    if int(str[p]) == 0:
      while int(str[p]) == 0:
          p += 1
          if p > end:
              break
      zCnt += 1
    
    else:
      while int(str[p]) == 1:
          p += 1
          if p > end:
              break
      oCnt += 1 

print(min(zCnt,oCnt))

