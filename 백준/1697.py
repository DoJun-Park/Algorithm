from collections import deque

N,K = map(int, input().split())
Max = 200000
chk = [False] * (Max+1)
dist = [0] * (Max+1)
q = deque()
chk[N] = True
q.append(N)


while q:
    X = q.popleft()
    for i in [X-1, X+1, X*2]:
        if 0 <=i<= Max and chk[i] == False:
            chk[i] = True
            q.append(i)
            dist[i] = dist[X]+1

print(dist[K])

