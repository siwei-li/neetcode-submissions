class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= end:
                end = max(end, e)
            else:
                ans.append([start, end])
                start, end = s, e
        
        ans.append([start, end])

        return ans


        