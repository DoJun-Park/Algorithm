import sys

N,M = map(int, input().split())

# chk = [False] * (N+1) # 사용했는지 여부 확인, 사용했으면 True, 사용하지 않았다면 False
ans = [0] * M # 답을 저장하기 위한 list


def recur(index,previous_val):
    if index == M:
        sys.stdout.write(' '.join(map(str,ans))+'\n')
        
        return 
        # 값 출력
    
    for i in range(1,N+1):
        if i<previous_val:
            continue

        ans[index] = i
        # chk[i] = True
        recur(index+1, i)
        # chk[i] = False


recur(0,1)

