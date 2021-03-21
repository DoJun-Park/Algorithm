N = int(input())
A = [0] + list(int(input()) for _ in range(N))
mem = [0] * (N+1)
mem[1] = A[1]
if(N>1):
    mem[2] = A[1] + A[2]


for i in range(3,N+1):
    mem[i] = max(mem[i-1], mem[i-2]+A[i], mem[i-3]+A[i-1]+A[i])

print(mem[N])
