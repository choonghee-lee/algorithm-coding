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
            print(i, j)
            if len(m) >= j-i:           # To reduce time
                print('break')
                break
            elif s[i:j] == s[i:j][::-1]:
                print(i,j, s[i:j], s[i:j][::-1])
                m = s[i:j]
                break
    return m


    