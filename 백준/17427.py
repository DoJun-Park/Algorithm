N = int(input())
GN=0

for i in range(1,N+1):
    GN += i * int(N/i)

print(GN)