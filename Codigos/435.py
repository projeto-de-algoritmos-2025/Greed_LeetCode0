class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Ordena os intervalos pelo tempo de término (end)
        intervals.sort(key=lambda x: x[1])
        
        count = 0         # número de intervalos que serão mantidos
        prev_end = float('-inf')  # fim do último intervalo aceito

        for interval in intervals:
            start, end = interval
            if start >= prev_end:
                # intervalo não sobrepõe → manter
                count += 1
                prev_end = end
            # caso contrário, sobrepõe → ignorar (remover)

        # Total de remoções = total - quantos conseguimos manter
        return len(intervals) - count
