
def sol(place):

    x1 = [0,0,-1,1] # 상하좌우
    y1 = [-1,1,0,0] # 상하좌우

    x2 = [0,0,-2,2] #상하좌우 
    y2 = [-2,2,0,0] #상하좌우 

    x3 = [-1,1,1,-1] # 왼위대 오위대 오아대 왼아대
    y3 = [-1,-1,1,1] # 왼위대 오위대 오아대 왼아대

    chk_x = [-1,0,1,0]
    chk_y = [0,-1,0,1]


    for i in range(5):
        for j in range(5):
            if place[i][j]== 'P':
                for k in range(4):
                    if i + x1[k] >=0 and i + x1[k] <= 4 and j + y1[k] >=0 and j + y1[k] <=4:
                        if place[i + x1[k]][j + y1[k]] == 'P':
                            return 0

                for l in range(4):
                    if i + x2[l] >=0 and i + x2[l] <=4 and j + y2[l] >=0 and j + y2[l] <=4:
                        if place[i + x2[l]][j + y2[l]] == 'P':
                            if place[i + x1[l]][j + y1[l]] != 'X':
                                return 0

                for m in range(4):
                    if i + x3[m] >=0 and i + x3[m] <=4 and j + y3[m] >=0 and j + y3[m] <=4:
                        if place[i+x3[m]][j+y3[m]] == 'P':
                            if place[i+chk_x[m]][j+chk_y[m]] != 'X' or place[i+chk_x[(m+1)%4]][j+chk_y[(m+1)%4]] != 'X':
                                return 0

    return 1


            



def solution(places):
    answer = []
    plc = [['' for _ in range(5)] for _ in range(5)]

    x,y = 0,0
    for i in places:
        for j in i:
            for k in j:
                plc[x][y] = k
                y = y+1
            x = x+1
            y = 0
        x = 0
        y = 0
        answer.append(sol(plc))
        

    return answer