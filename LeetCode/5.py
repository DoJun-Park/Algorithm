class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        maxlen = 0
        ans = ""

        for i in range(s_len):
            # 길이 홀수인 팰린드롬 판별
            left,right = i,i
            while True:
                if left >= 0 and right < s_len and (s[left] == s[right]) : #팰린드롬 조건을 만족하는 경우
                    if right-left+1 > maxlen: # 이전의 팰린드롬 최대 길이와 비교
                        maxlen = right-left+1 
                        ans = s[left:right+1] #left부터 right 인덱스까지의 문자 저장
                    left -= 1
                    right += 1
                else:
                    break

            # 길이 짝수인 팰린드롬 판별
            left,right = i,i+1
            while True:
                if left >= 0 and right < s_len and (s[left] == s[right]) :
                    if right-left+1 > maxlen:
                        maxlen = right-left+1
                        ans = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
            
        return ans


# 주의할 점은 팰린드롬의 조건을 확인하는 if문(11,23번째 줄)에서 s[left]==s[right]를 left >= 0 and right < s_len 보다 먼저 적으면 안된다.
# 왜냐하면 만약 left가 -1 또는 right가 s_len 이상의 값을 가지게 되는 경우 s의 인덱스 범위를 넘어서 string index out of range 에러가 발생한다.