N = int(input())
P = list(map(int, input().split()))

mem = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1, i+1):
        mem[i] = max(mem[i], mem[i-j] + P[j-1])



print(mem[N])
