"""
49 Group Anagram
    https://leetcode.com/problems/group-anagrams/
"""

# 내가 푼 답
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = dict()
        
        for w in strs:
            k = ''.join(sorted(w))
            if k in r:
                r[k].append(w)
            else:
                r[k] = list()
                r[k].append(w)
                
        return r.values()
    
# More Pythonic
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.values()