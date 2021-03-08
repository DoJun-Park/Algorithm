N,S = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(1, 1<<N): # 리스트의 크기가 N일때 만들 수 있는 양수인 부분수열의 경우
    sum = 0
    for j in range(0, N): 
        if (i & (1<<j)) > 0: # 확인하려는 자릿수(1<<j)와 i를 and하여 0보다 크면 값이 존재하기 때문에 리스트에서 그 위치의 값을 sum에 더해준다.
            sum += a[j]
    if sum == S:
        ans += 1

print(ans)
