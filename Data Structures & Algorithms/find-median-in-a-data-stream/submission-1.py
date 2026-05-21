from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.lower_half = [] # maxheap, neg values
        self.higher_half = [] # minheap
        

    def addNum(self, num: int) -> None:
        if not self.lower_half:
            self.lower_half.append(-num)
            print(self.lower_half, self.higher_half)
            return

        if len(self.lower_half) > len(self.higher_half):
            l = -self.lower_half[0]
            if num >= l:
                heappush(self.higher_half, num)
            else:
                heappush(self.lower_half, -num)
                heappush(self.higher_half, -heappop(self.lower_half))
        else:
            l = -self.lower_half[0]
            r = self.higher_half[0]
            if num <= r:
                heappush(self.lower_half, -num)
            else:
                heappush(self.higher_half, num)
                new_l = heappop(self.higher_half)
                heappush(self.lower_half, -new_l)
        # print(self.lower_half, self.higher_half)

    def findMedian(self) -> float:
        l = -self.lower_half[0]
        if len(self.lower_half) > len(self.higher_half):
            return l
        else:
            r = self.higher_half[0]
            return (l + r) / 2
        
        