"""
[문제]
로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 
아래는 로또의 순위를 정하는 방식입니다.

1등 - 6개 일치
2등 - 5개 일치
3등 - 4개 일치
4등 - 3개 일치
5등 - 2개 일치
6등 - 낙점

로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 
하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 
당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 합니다.

민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 
이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.


[조건]
1. 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
2. lottos는 길이 6인 정수 배열입니다.
3. lottos의 모든 원소는 0 이상 45 이하인 정수입니다.(0은 알아볼 수 없는 숫자를 의미합니다.)
4. win_nums은 길이 6인 정수 배열입니다.
5. win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.

"""



def solution(lottos, win_nums):
    answer = []
    same = 0 #lottos와 win_nums 중에 동일한 수의 갯수
    zero_cnt = 0 # lottos에 있는 0의 갯수


    for i in range(0,6):
        if lottos[i] == 0 :
            zero_cnt = zero_cnt + 1

        if lottos[i] in win_nums: #lottos의 수가 win_nums에 있는 경우
            same = same + 1
  

    if same == 0 and zero_cnt==0: # lottos에 0이 없으면서 win_nums가 같은 수가 없는 경우
        answer.append(6)

    else:
        answer.append(7-(same + zero_cnt))



    if same<2: # 일치하는 수가 2개 미만일때는 무조건 6등
        answer.append(6)
        min_rank=6
        
    else:
        answer.append(7-same)


    return answer
