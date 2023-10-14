# 구멍개수, 전기용품 총 사용횟수
N, K = map(int, input().split())
# 전기용품 이름 
arr = list(map(int, input().split()))
answer = 0
tap = []

for i, item in enumerate(arr):
    # 이미 멀티탭에 꽂혀있을 경우
    if item in tap:
        continue
    
    # 빈자리 있을경우
    if len(tap) < N:
        tap.append(item)
    # 멀티탭 꽉 차있으면
    else:
        # 우선순위를 매겨야함
        # 해당 전기용품이 다음 순번에 또 사용해야 하는지 기준으로 
        far = 0
        tmp = 0
        for p in tap:
            # 이제 사용할 일 없는 용품이면
            if p not in arr[i:]:
                tmp = p
                break
            # 사용할 일이 모두 있으면 해당 원소의 가장 끝 인덱스 추출하여 비교
            # 가장 마지막에 사용할 용품 제거위해
            elif arr[i:].index(p) > far:
                far = arr[i:].index(p)
                tmp = p
        tap.remove(tmp)
        answer += 1
        tap.append(item)

print(answer)