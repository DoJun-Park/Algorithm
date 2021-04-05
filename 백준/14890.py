N,L = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]



def slide(a, l):
    n = len(a)
    chk = [False] * n #칸에 경사로 유무 확인

    for i in range(1,n): #첫번째 칸은 그냥 갈 수 있으니깐
        if a[i-1] != a[i]: #인접칸의 높이가 다르면 경사로
            diff = abs(a[i-1]-a[i])
            
            if diff != 1: # 높이 차가 1이 아니면
                return False

            if a[i-1] < a[i]: # 왼쪽이 더 큰 경우 왼쪽으로 L개 같은 높이의 칸이 존재해야함
                for j in range (1, 1+l):
                    if i-j <0: #범위를 벗어나는 경우(0을 넘어서면 안됨)
                        return False
                    if a[i-1] != a[i-j]: #낮은 지점의 칸의 높이가 모두 같지 않거나 L개 연속하지 않는 경우
                        return False
                    if chk[i-j]: #이미 경사로 존재하는 경우
                        return False
                    chk[i-j] = True
                

            else: # 오른쪽이 더 큰경우
                for j in range (l): 
                    if i+j >= n : 
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if chk[i+j]:
                        return False
                    chk[i+j] = True
                
    
    return True


                
ans = 0
for i in range(N): # 행 검사
    row = a[i]
    if slide(row, L):
        ans +=1

for j in range(N): # 열 검사
    col = [a[i][j] for i in range(N)]
    if slide(col, L):
        ans += 1

print(ans)

