N = int(input())
A = list(map(int, input().split()))

mem = [0] * (N)
mem[0] = A[0]

for i in range(1, N):
    mem[i] = A[i]
    mem[i] = max(mem[i-1] + A[i], mem[i])

print(max(mem))


# 처음 제출했을 때 답이 틀렸다고 출력됨.
# 이유는 수열의 합을 저장하기 위한 mem 리스트를 N+1로 생성해서 0으로 초기화함. 이 때 답이 음수인데 
# max(mem)을 실행하면 index: N+1 에 0이 할당되어 최댓값이 0으로 출력됨.
