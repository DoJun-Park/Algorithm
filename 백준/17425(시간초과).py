n = int(input())
N = list(map(int, (input() for _ in range(n))))

j=0
GN = 0

while True:
    for i in range(1, N[j]+1):
        GN += i * int(N[j]/i)
        
    print(GN)
    GN = 0
    j += 1

    if j == n:
        break 
    
