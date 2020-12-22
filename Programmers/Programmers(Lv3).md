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



### 베스트앨범

> 풀이 1

```python
def solution(genres, plays):
    answer = []
    num_genres = {}
    num_plays = {}
    for i in range(len(genres)):
        if not genres[i] in num_genres.keys():
            num_genres[genres[i]] = plays[i]
            num_plays[genres[i]] = [(plays[i], i)]
        else:
            num_genres[genres[i]] += plays[i]
            num_plays[genres[i]].append((plays[i], i))

    for genre in sorted(num_genres.items(), key=lambda x: -x[1]):
        plays = sorted(num_plays[genre[0]], key=lambda x: (-x[0], x[1]))
        if len(plays) == 1:
            answer.append(plays[0][1])
        else:
            for idx in range(2):
                answer.append(plays[idx][1])

    return answer
```



> 풀이 2 : genres와 plays를 따로 나누지 않음

```python
def solution(genres, plays):
    answer = []
    genres_plays = {}
    for i in range(len(genres)):
        if not genres[i] in genres_plays.keys():
            genres_plays[genres[i]] = [plays[i], [(plays[i], i)]]
        else:
            genres_plays[genres[i]][0] += plays[i]
            genres_plays[genres[i]][1].append((plays[i], i))
    for genre in sorted(genres_plays.values(), key=lambda x: -x[0]):
        one_genre = sorted(genre[1], key=lambda x: (-x[0], x[1]))
        if len(one_genre) == 1:
            answer.append(one_genre[0][1])
        else:
            for idx in range(2):
                answer.append(one_genre[idx][1])
    return answer
```



### 네트워크

> BFS

```python
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = []
    for r in range(n):
        for c in range(n):
            if c in visited: break
            if computers[r][c] and (r, c) not in visited:
                answer += 1
                visited.append((r, c))
                queue.append(c)
                while len(queue):
                    nr = queue.popleft()
                    for c in range(n):
                        if computers[nr][c] and (nr, c) not in visited:
                            visited.append((nr, c))
                            queue.append(c)
    return answer
```



> DFS

```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def solution(n, computers):
    answer = 0
    stack = []
    visited = []
    for r in range(n):
        for c in range(n):
            if c in visited: break
            if computers[r][c] and (r, c) not in visited:
                answer += 1
                visited.append((r, c))
                stack.append(c)
                while len(stack):
                    nr = stack.pop()
                    for c in range(n):
                        if computers[nr][c] and (nr, c) not in visited:
                            visited.append((nr, c))
                            stack.append(c)
    return answer
```



### 단어 변환

```python
from collections import deque

def check(begin, compare):
    count = 0
    for i in range(len(begin)):
        a, b = begin[i], compare[i]
        if a != b:
            count += 1
        if count > 1:
            return False
    else:
        return True
    
def solution(begin, target, words):
    if target not in words: return 0

    queue = deque(words)
    step = deque([begin])
    cnt = 0
    
    while True:
        for _ in range(len(step)):
            start = step.popleft()
            for i in range(len(queue)):
                compare = queue.popleft()
                if check(start, compare):
                    if compare == target:
                        return cnt + 1
                    step.append(compare)
                else:
                    queue.append(compare)
        cnt += 1
```



### 정수 삼각형

```python
def solution(triangle):
    n = len(triangle)
    for height in range(1, n):
        for step in range(height+1):
            if step == 0:
                triangle[height][step] += triangle[height-1][0]
            elif step == height:
                triangle[height][step] += triangle[height-1][step-1]
            else:
                triangle[height][step] += max(triangle[height-1][step-1], triangle[height-1][step])
    return max(triangle[-1])
```



### 이중우선순위큐

> deque 사용

```python
from collections import deque
def solution(operations):
    numbers = deque([])
    for oper in operations:
        order, num = oper.split(' ')
        if order == "I":
            numbers.append(int(num))
        else:
            if not len(numbers): continue
            if num == '1':
                numbers.remove(max(numbers))
            else:
                numbers.remove(min(numbers))
    print([max(numbers), min(numbers)] if len(numbers) else [0, 0])
    return [max(numbers), min(numbers)] if len(numbers) else [0, 0]

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
```



> heapq 사용

```python
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
```

