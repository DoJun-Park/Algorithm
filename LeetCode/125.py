class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs = []
        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        for i in strs:
            compare_back_word = strs.pop()
            if i != compare_back_word:
                return False
        
        return True
