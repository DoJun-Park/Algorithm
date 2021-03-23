from collections import deque

N,M = map(int, input().split())
a = [list(map(int, input())) for _ in range (N)]

que = deque()
chk = [[False] * M for _ in range(N)] # 지나간 경우를 체크하기 위한 리스트
dist = [[0] *M for _ in range(N)] # 거리를 저장하기 위한 리스트

que.append((0,0)) # 처음 (1,1)에서 시작
chk[0][0] = True
dist[0][0] = 1

# 좌표 위 오른쪽 아래 왼쪽 표현
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while que:
    x,y = que.popleft()
    for i in range(4):
        temp_x = dx[i] + x
        temp_y = dy[i] + y

        if temp_x >= 0 and temp_x <N and temp_y >= 0 and temp_y < M:
            if chk[temp_x][temp_y] == False and a[temp_x][temp_y] == 1:
                dist[temp_x][temp_y] = dist[x][y] + 1
                chk[temp_x][temp_y] = True
                que.append((temp_x, temp_y))
    

print(dist[N-1][M-1])