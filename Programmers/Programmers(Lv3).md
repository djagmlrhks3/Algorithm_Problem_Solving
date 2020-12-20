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



> 풀이 2

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

