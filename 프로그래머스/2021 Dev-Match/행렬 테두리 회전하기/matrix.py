'''
[문제]
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다.
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 
각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.
[x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.]

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 
각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

[조건]
1. rows는 2 이상 100 이하인 자연수입니다.
2. columns는 2 이상 100 이하인 자연수입니다.
3. 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
   즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
4. queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
5. queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
    x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
    1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
    모든 회전은 순서대로 이루어집니다.
    예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.

'''

'''
[문제 풀이]
크기가 rowsxcolumns인 행렬 생성하여 ((i-1) x columns + j)의 숫자를 넣어준다.
그리고 queries에 있는 행의 갯수만큼 반복문을 돌며 행렬을 회전시키다.

행렬이 회전하는 것을 구현하기 위해 새로운 matrix(temp_matrix)를 깊은 복사로 생성하였는데,
이는 matrix를 회전시키기 전의 값을 저장하기 위함이다.

그리고 회전시키는 값들 중 가장 작은 값은 회전 시킬 때마다 값들을 비교하여 min_num에 저장해둔다.


[새로 알게된 점]
처음에는 그냥 temp_matrix=matrix와 같이 얕은 복사를 했다. 
그러다보니 matrix의 값을 변경하니 temp_matrix의 값도 같이 변경되어 제대로 회전되지 않았다.
그래서 깊은 복사를 하기 위해 deepcopy()를 사용했지만 시간 초과가 발생했다.
결국 slicing을 이용하였고 문제를 해결할 수 있었다.
'''



def solution(rows, columns, queries):

    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]


    for i in range(rows):
        for j in range(columns):
            matrix[i+1][j+1] = (i)*columns + (j+1)


    for x1,y1,x2,y2 in queries:
        min_num = 10001
        temp_matrix = [i[:] for i in matrix]         # 깊은 복사    

        for i in range(y1,y2): #윗면 회전
            matrix[x1][i+1] = temp_matrix[x1][i]
            min_num = min(min_num,temp_matrix[x1][i])

        for i in range(x1,x2): #오른쪽면 회전
            matrix[i+1][y2] = temp_matrix[i][y2]
            min_num=min(min_num,temp_matrix[i][y2])
        
        for i in range(y2,y1,-1): #아랫면 회전
            matrix[x2][i-1] = temp_matrix[x2][i]
            min_num = min(min_num,temp_matrix[x2][i])
        
        for i in range(x2,x1,-1): #왼쪽면 회전
            matrix[i-1][y1] = temp_matrix[i][y1]
            min_num = min(min_num,temp_matrix[i][y1])



    #     for i in range(rows+1):
    #         for j in range(columns+1):
    #             print(matrix[i][j], end=' ')
    #         print()
    #     print()
    #     # min,matrix = rotate(x1,y1,x2,y2,matrix)

        answer.append(min_num)
    
    # print(answer)
    return answer


q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(6,6,q)