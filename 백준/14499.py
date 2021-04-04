N,M,x,y,K = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]

dice = [0]*7
move = list(map(int, input().split()))
dx = [0,0,-1,1] # 동서남북 순서대로
dy = [1,-1,0,0]

for i in move:
  
    new_x, new_y = x+dx[i-1], y+dy[i-1]
    
    if new_x <0 or new_x >= N or new_y <0 or new_y >=M:
        continue

    if i == 1: #동
        temp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = temp
    elif i == 2: #서
        temp = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = temp
    elif i == 3: #북
        temp = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = temp
    elif i == 4: #남
        temp = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = temp

    x,y = new_x,new_y
    
    if a[x][y] == 0: #이동칸에 0
        a[x][y] = dice[6] #바닥면

    else:
        dice[6] = a[x][y]
        a[x][y] = 0

    print(dice[1])

