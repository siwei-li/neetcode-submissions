"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        starts = [0, 5, 15]
                        |
        ends = [10, 20, 40]
                     |

        s = 0, e = 10, num = 1
        move s = 5, num += 1
        move s = 15, num -= 1
        we can now move e = 20, num += 1

        """
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        n = len(starts)

        s, e = 0, 0
        ans = 0
        rooms = 0

        while s <= n - 1 and e <= n - 1:
            if starts[s] < ends[e]:
                rooms += 1
                ans = max(ans, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1

        return ans

