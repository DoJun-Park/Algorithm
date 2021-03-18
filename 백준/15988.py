T = int(input())
mem = [0] * 1000001
mem[0] = 1

for i in range(1,1000001):
    if i >= 1 :
        mem[i] += mem[i-1]
    if i >= 2 :
        mem[i] += mem[i-2]
    if i >= 3 :
        mem[i] += mem[i-3]

    mem[i] %= 1000000009

for i in range(T):
    num = int(input())
    print(mem[num])
