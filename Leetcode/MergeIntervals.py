class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        p1 = 0
        
        p2 = p1 + 1
        
        intervals.sort(key = lambda x : x[0])
        
        while p2 < len(intervals):
            if intervals[p1][1] >= intervals[p2][0]:
                intervals[p1][1] = max(intervals[p1][1], intervals[p2][1])
                intervals[p1][0] = min(intervals[p1][0], intervals[p2][0])
                intervals.pop(p2)
                
            else:
                p1 += 1
                p2 += 1
                
        return intervals
        
