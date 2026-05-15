class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        l, r = 0, n - 1

        while l < r:
            l_h, r_h = heights[l], heights[r]
            ans = max(ans, min(l_h, r_h) * (r - l))
            if l_h < r_h:
                l += 1
            else:
                r -= 1

        return ans
