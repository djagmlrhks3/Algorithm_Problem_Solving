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

