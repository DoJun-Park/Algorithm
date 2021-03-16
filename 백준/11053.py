N = int(input())
A = list(map(int, input().split()))

mem = [1] * (N+1)

for i in range(0, N):
    for j in range(0, i+1):

        if A[i] > A[j]:
            mem[i] = max(mem[i], mem[j]+1)
    


print(max(mem))
