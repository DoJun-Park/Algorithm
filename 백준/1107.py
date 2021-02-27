N = int(input())
M = int(input())
broken = [False] * 10

if M > 0:
    broken_list = list(map(int, input().split()))
else:
    broken_list = []

for i in broken_list: #고장난 리모콘 값은 True로
    broken[i] = True

ans = abs(N-100)

def possible(c): # 버튼으로 가능한지
    if c ==0 :
        if broken[0]: #원하는 채널이 0이고 0번 버튼이 고장일 때
            return 0 #불가능
        else:
            return 1 #
    l = 0
    while c >0:
        if broken[c%10]: # 버튼 고장이면
            return 0 # 바로 못감
        l += 1
        c //=10
    return l



for i in range(0, 1000001):
    channel = i
    l = possible(channel)
    if l >0:
        press = abs(channel-N)
        if ans > l + press:
            ans = l + press


print(ans)
    
    