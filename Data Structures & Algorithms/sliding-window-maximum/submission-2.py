import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [(-num, idx) for idx, num in enumerate(nums[:k])]
        heapq.heapify(h)
        n = len(nums)
        ans = [-h[0][0]]
        # print(ans)

        for i in range(1, n - k + 1):
            if nums[i - 1] == -h[0][0]:
                heapq.heappop(h)
            heapq.heappush(h, (-nums[i + k - 1], i + k - 1))
            # print(h)
            
            while h[0][1] < i:
                heapq.heappop(h)
            # print(h)
            ans.append(-h[0][0])
            # print(i, ans)

        return ans


        