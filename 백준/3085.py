N = int(input())
N_list = [list(input()) for _ in range(N)]


def check(arg_list):
    adj_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if N_list[i][j] == N_list[i][j-1]:
                cnt +=1
            else:
                cnt = 1

            if cnt > adj_cnt:
                adj_cnt = cnt
        cnt = 1
        for j in range(1,N):
            if N_list[j][i] == N_list[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > adj_cnt:
                adj_cnt = cnt
    return adj_cnt    

adj_cnt = 0

for i in range(N):
    for j in range(N):
        if i+1<N: # 오른쪽으로
            N_list[i][j], N_list[i+1][j] = N_list[i+1][j], N_list[i][j]
            tmp = check(N_list)
            if  adj_cnt < tmp:
                adj_cnt = tmp
            N_list[i][j], N_list[i+1][j] = N_list[i+1][j], N_list[i][j] #원상복구
            
        if j+1<N: # 아래쪽으로  
            N_list[i][j], N_list[i][j+1] = N_list[i][j+1], N_list[i][j]
            tmp = check(N_list)
            if adj_cnt < tmp:
                adj_cnt = tmp
            N_list[i][j], N_list[i][j+1] = N_list[i][j+1], N_list[i][j]

print(adj_cnt)
