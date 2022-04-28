import heapq
def solution(jobs):
    answer, heap = 0, []    
    for start, time in jobs:
        heapq.heappush(heap, [start, time, time])
    start, time, total = heapq.heappop(heap)
    now, answer = start + time, time
    while heap:
        for _ in range(len(heap)):
            start, time, total = heapq.heappop(heap)
            if start < now:
                diff = now - start
                start += diff
                total += diff
                heapq.heappush(heap, [start, time, total])
            else:
                heapq.heappush(heap, [start, time, total])
                break
        start, time, total = heapq.heappop(heap)
        diff = 0
        if start - now > 0:
            diff = start - now
        now += (diff + time)
        answer += total
    return answer // len(jobs)