N = int(input())
permu = list(map(int, input().split()))
ans = 0

def cal(a):
    sum = 0
    for i in range(N-1):
        sum += abs(a[i] - a[i+1])
    
    global ans
    if ans < sum:
        ans = sum
    return 0


def next_permu(a):
    if N == 1:
        return False
        
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


permu.sort()
cal(permu)

while True:
    if next_permu(permu):
        cal(permu)
    else:
        break

print(ans)


