N = int(input())

cost = [(0,0,0)] + [tuple(map(int, input().split())) for _ in range(N)]
mem = [[0,0,0] for _ in range(N+1)]


for i in range(1,N+1):
    mem[i][0] = min(mem[i-1][1],mem[i-1][2]) + cost[i][0]
    mem[i][1] = min(mem[i-1][0],mem[i-1][2]) + cost[i][1]
    mem[i][2] = min(mem[i-1][0],mem[i-1][1]) + cost[i][2]

print(min(mem[N][0],mem[N][1],mem[N][2]))
 
    