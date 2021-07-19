'''
[문제]
작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

1. 알파벳 소문자로 이루어진 문자열 W가 주어진다.
2. 양의 정수 K가 주어진다.
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

위와 같은 방식으로 게임을 T회 진행한다.

[입력]
문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)
다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000) 

[출력]
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.
만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.
'''

'''
구해야 하는 것은 2개(3번과 4번)
- 문자열에서 어떤 문자열을 k개 포함하는 가장 짧은 연속 문자열의 길이
- 문자열에서 어떤 문자열을 k개 포함하면서 첫번째와 마지막 글자가 같은 가장 긴 문자열의 길이

[해결 방법]
구해야하는 2가지 경우 모두 맨앞과 마지막 자리의 수는 같아야한다
우선 입력받는 문자열의 문자를 하나씩 선택하여 count()를 통해 포함되어야 하는 k개 이상이 
문자열에 있는지부터 확인한다.
그리고 k개 이상이 있으면 해당 문자의 위치 다음부터 같은 문자가 k개 있을때까지 인덱스를 옮겨간다.
k개의 문자가 카운트됐을때, 시작 인덱스와 해당 인덱스의 차이를 통해 길이를 구하고 
이를 가장 짧은 거리과 가장 긴 거리와 비교하여 최종적인 답을 구한다.
'''

'''
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5


1
abaaaba
3
'''





def str_game(w,k):
    min_len =10000
    max_len = 0
    
    if k ==1 : # k가 1이면 무조건 최대 최소 길이가 1
        print(1,1)
        return
    
    for i in range(0, len(w)):
        if w.count(w[i]) >= k: # k개 이상만큼 문자가 문자열에 속해 있는지 확인
            k_cnt = 1 # 시작하는 문자부터 포함하고 카운트하므로
            for j in range(i+1, len(w)):
                if w[j] == w[i]:
                    k_cnt += 1
                    if k_cnt == k: # 만약 k갯수만큼의 문자가 포함되었을 때
                        if min_len > (j-i)+1:
                            min_len = (j-i)+1
                        if max_len < (j-i)+1:
                            max_len = (j-i)+1
                        break
    

    
    if min_len == 10000 and max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)

    return



T = int(input())
for i in range(0,T):
    W = input()
    K = int(input())
    str_game(W,K)





