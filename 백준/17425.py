MAX = 1000000

d = [1] * (MAX +1)
s = [0] * (MAX +1)


for i in range(2,MAX+1):
    j=1
    while i*j<=MAX:
        d[i*j] += i
        j+=1

for i in range(1,MAX+1):
    s[i] = d[i]+s[i-1]

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    ans.append(s[N])

print('\n'.join(map(str, ans)))




# 아래의 방법은 O(N^2)으로 시간초과 발생
# n = int(input())
# N = list(map(int, (input() for _ in range(n))))

# j=0
# GN = 0

# while True:
#     for i in range(1, N[j]+1):
#         GN += i * int(N[j]/i)
        
#     print(GN)
#     GN = 0
#     j += 1

#     if j == n
#         break 
    
