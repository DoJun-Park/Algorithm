from collections import deque

N,M,V = list(map(int, input().split()))
chk = [False] * (N+1)
a = [[] for _ in range(N+1)]


for i in range(M):
    x,y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for i in range(N+1):
    a[i].sort()




def dfs(x):
    chk[x] = True
    print(x,end = ' ')
    for i in a[x]:
        if chk[i] == False:
            dfs(i)


def bfs(x):
    que = deque()
    que.append(x)
    chk[x] = True

    while que:
        que_pop = que.popleft()
        print(que_pop,end = ' ')
        for i in a[que_pop]:
            if chk[i] == False:
                chk[i] = True
                que.append(i)



dfs(V)
print()
chk = [False]*(N+1)
bfs(V)

