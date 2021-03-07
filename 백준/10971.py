N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

def next_permu(a):   
    i = N-1
    
    while permu[i] <= permu[i-1]:
        i -= 1
        if i== 0:
            return False
   
    j = N-1
    while permu[j] <= permu[i-1]:
        j -= 1
    
    temp = permu[i-1]
    permu[i-1] = permu[j]
    permu[j] = temp

    j = N-1
    while i < j:
        temp = permu[i]
        permu[i] = permu[j]
        permu[j] = temp
        i += 1
        j -= 1
    
    return True


ans = 100000000000
permu = list(range(N))

while True:
    sum = 0
    chk = 0
    for i in range(N-1):
        if cost[permu[i]][permu[i+1]] == 0:
            chk =1
            break
        else:
            sum += cost[permu[i]][permu[i+1]]

    if chk == 0 and cost[permu[N-1]][permu[0]] != 0 :
        sum += cost[permu[N-1]][permu[0]]
        ans = min(ans, sum)

    if not next_permu(permu):
        break


print(ans)