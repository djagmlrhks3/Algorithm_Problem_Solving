# Programmers(Lv3)

### 가장 먼 노드

```python
from collections import deque

def solution(n, edge):
    distance = [0] * (n + 1)
    distance[1] = 1
    matrix = [[] for _ in range(n+1)]
    for e in edge:
        matrix[e[0]].append(e[1])
        matrix[e[1]].append(e[0])

    queue = deque([1])
    while (queue):
        num = queue.popleft()
        for i in matrix[num]:
            if not distance[i] :
                queue.append(i)
                distance[i] = distance[num] + 1
    answer = distance.count(max(distance))

    return answer
```

