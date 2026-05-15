class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        left_max = height.copy()  # [0,2,2,3,3,3,3,3,3,3]
        for i, h in enumerate(height):
            if i == 0:
                left_max[i] = 0
                continue
            left_max[i] = max(left_max[i - 1], height[i - 1])
            # print(i, left_max)

        right_max = 0
        for i in range(n - 1, -1, -1):
            h = height[i]
            l = left_max[i]  # 7, 7
            result += max(min(l, right_max) - h, 0)  # +0,
            right_max = max(right_max, h)  # 1
            # print(i, h, l, result, right_max)

        return result