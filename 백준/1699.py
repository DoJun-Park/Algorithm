N = int(input())

mem = [0] * (N+1)

for i in range(1, N+1):
    mem[i] = i
    j = 1
    while j*j <= i:
        if mem[i] > mem[i-j*j] + 1:
            mem[i] = mem[i-j*j] + 1
        j += 1


print(mem[N])
