N = int(input()) # 컴퓨터 수
n = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)] # 연결 쌍 행렬로 저장
visited = [0] * (N+1) # 방문 여부 체크
ans = 0 # 정답

for i in range(n):
    row,col = map(int, input().split())
    matrix[row][col] = matrix[col][row] = 1
    


def dfs(index):
    global ans
    visited[index] = 1
    for i in range(1, N+1):
        if matrix[index][i] == 1 and visited[i]==0:
            ans +=1
            dfs(i)
    return ans


print(dfs(1))
