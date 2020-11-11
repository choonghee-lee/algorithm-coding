"""
125 Valid Palindrome
    https://leetcode.com/problems/valid-palindrome/
"""
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string.punctuation == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        # str.maketrans() -> 변환할 딕셔너리 리턴
        # translate() -> 실제 변환
        s = s.lower().translate(str.maketrans('', '', string.punctuation+' '))

        # 뒤집기 슬라이싱
        return s == s[::-1]