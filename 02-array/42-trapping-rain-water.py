"""
42. Trapping Rain Water
    https://leetcode.com/problems/trapping-rain-water/
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        v = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            
            if lmax <= rmax:
                v += lmax - height[l]
                l += 1
            else:
                v += rmax - height[r]
                r -= 1
        
        return v