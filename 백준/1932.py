N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
mem = [[0]*N for i in range(N)]

mem[0][0] = A[0][0]

for i in range (1, N):
    for j in range(0, i+1):
        if i == 0:
            mem[i][j] = mem[i-1][j] + A[i][j]

        mem[i][j] = max(mem[i-1][j], mem[i-1][j-1]) + A[i][j]
        # if j>0 and mem[i][j] < mem[i-1][j-1] + A[i][j]:    
        #     mem[i][j] = mem[i-1][j-1] + A[i][j]


print(max(mem[N-1]))



