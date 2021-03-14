N = int(input())
mem = [[0]*10 for _ in range(N+1)]


for i in range(1, 10):
    mem[1][i] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        if j-1 >= 0:
            mem[i][j] += mem[i-1][j-1]
        if j+1 <= 9:
            mem[i][j] += mem[i-1][j+1]
        
ans = sum(mem[N]) % 1000000000
print(ans)