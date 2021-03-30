N,M,R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cal = list(map(int, input().split()))


# 연산을 할 때 입력받은 N,M으로 수행하면 안됨.
# 연산을 수행하면서 행, 열의 길이가 달라질 수 있기 떼문에 연산을 수행할 때마다 리스트의 행,열의 길이를 구해서 해야함

def case1(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[n-i-1][j]
    return b

def case2(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][m-1-j]
    return b

def case3(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[n-j-1][i]
    return b

def case4(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][m-i-1]
    return b

def case5(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            b[i][j+m//2] = a[i][j]
            b[i+n//2][j+m//2] = a[i][j+m//2]
            b[i+n//2][j] = a[i+n//2][j+m//2]
            b[i][j] = a[i+n//2][j]
    return b

def case6(a):
    n = len(a)
    m = len(a[0])
    b = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            b[i+n//2][j] = a[i][j]
            b[i][j] = a[i][j+m//2]
            b[i][j+m//2] = a[i+n//2][j+m//2]
            b[i+n//2][j+m//2] = a[i+n//2][j]
    return b

for i in cal:
    if i == 1:
        A = case1(A)

    if i == 2:
        A = case2(A)
    
    if i == 3:
        A = case3(A)

    if i == 4:
        A = case4(A)
    
    if i == 5:
        A = case5(A)

    if i == 6:
        A = case6(A)
    

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()
    
    