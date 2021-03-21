N = int(input())
a = list(map(int, input().split()))

memL = [0] * N
memR = [0] * N

memL[0] = a[0]

for i in range(1, N):
    memL[i] = a[i]

    if memL[i] < memL[i-1] + a[i]:
        memL[i] = memL[i-1] + a[i]

memR[N-1] = a[N-1]

for i in range(N-2, -1, -1):
    memR[i] = a[i]

    if memR[i] < memR[i+1] + a[i]:
        memR[i] = memR[i+1] + a[i]


ans = max(memL)

for i in range(1, N-1):
    if ans < memL[i-1] + memR[i+1]:
        ans = memL[i-1] + memR[i+1]


print(ans)