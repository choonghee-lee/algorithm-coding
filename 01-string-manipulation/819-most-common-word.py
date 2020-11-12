"""
819 Most Common Word
    https://leetcode.com/problems/most-common-word/
"""

import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # b,b,b,c 같은 케이스 때문에 translate로 punctuation 지우는건 안된다. (125번 참조)
        l = [word for word in re.sub('[^\w\s]', ' ', paragraph).lower().split() if word not in banned]
        counter = collections.Counter(l)
        return counter.most_common(1)[0][0]