'''
문제 분석
1. 연산자(+,-,*)에 대해 우선순위를 정할 수 있다.
2. 같은 우선순위의 연산자를 둘 수 없다.
3. 음수이면 절대값으로 생각
4. expression의 길이가 3 이상 100 이하인 문자열
5. expression은 공백문자, 괄호문자 없이 오로지 숫자와 3가지의 연산자 `+,-,*`로만 이루어진 올바른 중위연산자
6. expression의 피연산자(operand)는 0 이상 999 이하의 숫자,
7. expression은 적어도 1개 이상의 연산자를 포함
8. 같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높다.

''' 

import re

# def cal(express):



# def solution(v):
#     expression = re.compile('(\D)').split(v)
#     cal(expression)
    