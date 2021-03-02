t = int(input())
def recur(sum, goal):
    if sum == goal:
        return 1
    if sum > goal:
        return 0

    ans_cnt = 0

    for i in range(1,4):
        ans_cnt += recur(sum + i, goal)
    return ans_cnt


for _ in range(t):
    n = int(input())
    # print(recur(0,n))

