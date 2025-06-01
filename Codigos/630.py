import heapq

class Solution:
    def scheduleCourse(self, courses):
        # Ordena pelo deadline
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        time = 0
        
        for duration, lastDay in courses:
            time += duration
            heapq.heappush(max_heap, -duration)  # Usamos heap negativo para simular max-heap
            
            if time > lastDay:
                longest = -heapq.heappop(max_heap)
                time -= longest  # Remove o curso de maior duração
        return len(max_heap)
