N = int(input())
day =[0]*(N+1)
profit=[0]*(N+1)
# accumulate_profit = [0] * (N+1)

for i in range(1,N+1):
    day[i],profit[i] = map(int, input().split())

ans = 0

def recur(index, sum):

    global ans

    if index == N+1: # N일까지 상담한다면 N+1일때 정산, 만약 N일에 1일 걸리는 상담을 한다면 이것까지 포함
        ans = max(ans, sum)
        return
    if index > N+1:
        return

    recur(index+1, sum) #상담을 하지 않을 경우
    recur(index+day[index], sum + profit[index]) #상담을 할 경우

           

recur(1,0)
print(ans)


