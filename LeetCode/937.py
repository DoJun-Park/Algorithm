class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit=[]
        letter=[]

        # 배열 각 요소들의 로그가 문자인지 숫자인지 구분
        for i in logs:
            if i.split()[1].isdigit():
                digit.append(i)
            else:
                letter.append(i)
        
        # 문자에서 우순위로 로그를 기준으로 정렬, 그리고 로그가 동일한 경우 후순위로 식별자를 기준으로 정렬
        letter.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        return letter + digit