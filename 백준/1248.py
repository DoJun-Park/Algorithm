N = int(input())
s = input()
sign = [['' for _ in range(N)] for _ in range(N)]

x = 0
for i in range(N):
    for j in range(i,N):
        if s[x] == '0':
            sign[i][j] = 0
        elif s[x] == '+':
            sign[i][j] = 1
        else: # s[x] == '-'
            sign[i][j] = -1

        x +=1

ans = [0]*N



def chk(index):
    sum = 0
    for i in range(index,-1,-1):
        sum += ans[i]
        if sign[i][index] < 0:
            if sum >=0:
                return False
        elif sign[i][index] > 0:
            if sum <=0:
                return False
        else: # sign[i][index] == 0
            if sum != 0:
                return False
    return True


def recur(index):
    if index == N: #0부터 시작했으므로
        return True
    
    if sign[index][index] == 0:
        ans[index] = 0
        return chk(index) and recur(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if chk(index) and recur(index+1):
            return True
    
    return False
        

recur(0)

print(' '.join(map(str,ans)))