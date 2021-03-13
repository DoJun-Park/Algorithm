N = int(input())
mem = [0] * (N+1)
mem[0] = 1 #아무 타일도 사용하지 않는 경우도 한 가지
mem[1] = 1

for i in range(2, N+1):
    mem[i] = mem[i-1] + mem[i-2]

print(mem[N]%10007)
