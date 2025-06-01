class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        
        count = 0        
        prev_end = float('-inf') 

        for interval in intervals:
            start, end = interval
            if start >= prev_end:
                count += 1
                prev_end = end
        return len(intervals) - count
