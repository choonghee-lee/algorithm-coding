"""
5. Longest Palindromic Substring
    https://leetcode.com/problems/longest-palindromic-substring/
"""

# 실패작
# Time Limit Exceeded!
from itertools import combinations

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        # 모든 substring 조합을 찾는다.
        # itertools.combinations(iterable, r)
        # Return 'r' length subsequences of elements from the input 'iterable'
        subs = [s[i:j] for i, j in combinations(range(len(s) + 1), r=2)]
        for sub in subs:
            if sub == sub[::-1]:    # palinrome 검사
                if len(result) < len(sub):
                    result = sub
                    
        return result
    
# LeetCode 답안
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Memory to remember a palindrome
        m = ''
        for i in range(len(s)):             # i = start, O(n)
            for j in range(len(s), i, -1):  # j = end, O(n^2)
                if len(m) >= j-i:           # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m

"""
파이썬은 모든 문자열이 ASCII 범위에 있다면 Latin-1 인코딩(고정 1바이트),
대부분의 문자여른 UCS-2(고정 2바이트),
특수 기호, 이모지, 희귀 언어 등은 UCS-4(고정 4바이트)로 인코딩한다.

UTF-8 인코딩은 가변적으로 바이트를 결정하기 때문에 인덱싱을 빠르게 할 수 없다.
그래서 파이썬은 위와 같은 고정 길이 인코딩 방식을 적용한다.
"""