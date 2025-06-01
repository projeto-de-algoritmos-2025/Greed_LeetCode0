from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == max_freq)
        
        part_count = max_freq - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_freq * max_count
        idles = max(0, empty_slots - available_tasks)
        
        return len(tasks) + idles