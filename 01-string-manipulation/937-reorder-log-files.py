"""
937 Reorder Log File
    https://leetcode.com/problems/reorder-data-in-log-files/
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for l in logs:
            if l.split()[1].isdigit():
                digits.append(l)
            else:
                letters.append(l)
                
        # tuple을 리턴하는 람다로 ORDER BY 조건1, 조건2 할 수 있다.
        # sort() -> reverse=False 오름차순, reverse=True 내림차순
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits