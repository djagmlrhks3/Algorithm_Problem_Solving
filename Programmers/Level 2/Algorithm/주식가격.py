from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        price = queue.popleft()
        cnt = 0
        for compare in queue:
            if price <= compare:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

solution([1, 2, 3, 2, 3])