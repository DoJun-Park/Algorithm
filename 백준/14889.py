N = int(input())
S = [list(map(int, input().split())) for _ in range (N)]



# index는 1부터 시작하므로 S에 참고할때는 1씩 빼서 참고

def recur(index, first, second):

    if index == N: # first와 second에 있는 값들을 각각 모두 더해서 뺀다
        # 만약 N이 6개이고 first에 2개, second에 3개가 들어간 상태라고 하면 30번째와 33번째 줄의 조건문에는 들어가지 않는다.
        # 그리고 다시 재귀로 함수를 호출하게 되는데 여기서 second에 index가 추가되면 문제의 조건을 만족하지 못하게 된다.
        # 때문에 아래와 같이 각각의 리스트의 수가 N/2가 아닌 경우에는 -1로 return을 한다.
        if len(first) != N/2:
            return -1 

        if len(second) != N/2:
            return -1 

        sum_first, sum_second = 0,0
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue

                sum_first += S[first[i]][first[j]]
                sum_second += S[second[i]][second[j]]
            
        min_diff = abs(sum_first-sum_second)
        return min_diff

    if (len(first)) > N/2 : #first 배열이 N/2의 수를 넘으면 조건을 만족하지 않기 때문에 
        return -1 # min_diff결과는 -1이 나올 수 없기 때문에
    
    if (len(second)) > N/2 : #second 배열이 N/2의 수를 넘으면 조건을 만족하지 않기 때문에 
        return -1

    ans = -1 
    a = recur(index+1,first+[index],second)
    if ans == -1 or (a != -1 and ans > a):
        ans = a
    b = recur(index+1,first,second+[index])
    if ans == -1 or (b != -1 and ans > b):
        ans = b
    
    return ans


print(recur(0,[], []))
