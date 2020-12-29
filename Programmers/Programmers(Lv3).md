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

def solution(operations):
    max_heap = []
    min_heap = []
    for oper in operations:
        if oper == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif oper == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(oper[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
```



### 2 x n 타일링

```python
def solution(n):
    a, b = 1, 2
    for i in range(n-2):
        a, b = b, a+b
    return b % 1000000007
```



### 여행 경로

```python
from collections import deque

def solution(tickets):
    queue = deque(tickets)
    city = 'ICN'
    candidate = []
    answer = []
    def dfs(city, queue, candidate, route):
        nonlocal tickets, answer
        if len(route) == len(tickets):
            route.append(queue.popleft()[1])
            answer = route
            return

        for _ in range(len(queue)):
            start, end = queue.popleft()
            if start == city:
                candidate.append([start, end])
            else:
                queue.append([start, end])
        if not len(candidate):
            return
        candidate = sorted(candidate, key=lambda x: x[1], reverse=True)
        for i in range(len(candidate)):
            new_city = candidate[i][1]
            temp = []
            for j in range(len(candidate)):
                if i == j:
                    continue
                else:
                    temp.append(candidate[j])
            dfs(new_city, queue + deque(temp), [], route + [new_city])

    dfs(city, queue, candidate, ['ICN'])
    return answer
```



### 디스크 컨트롤러

> 풀이 1 - deque사용

```python
from collections import deque

def solution(jobs):
    queue = deque(sorted(jobs))
    idx, length, answer, candidate = 0, 0, 0, []
    while idx < len(jobs):
        if not candidate:
            start, time = queue.popleft()
            length = start + time
            answer += time
        else:
            candidate = sorted(candidate, key=lambda x: -x[1])
            start, time = candidate.pop()
            length += time
            answer += length - start
        idx += 1

        while queue and queue[0][0] <= length:
            candidate.append(queue.popleft())
    return answer // len(jobs)
```



> 풀이 2 - heapq, deque 사용

```python
import heapq
from collections import deque

def solution(jobs):
    queue = deque(sorted(jobs))
    idx, length, answer, candidate = 0, 0, 0, []
    while idx < len(jobs):
        if not candidate:
            start, time = queue.popleft()
            length = start + time
            answer += time
        else:
            time, start = heapq.heappop(candidate)
            length += time
            answer += length - start
        idx += 1

        while queue and queue[0][0] <= length:
            heapq.heappush(candidate, queue.popleft()[::-1])
    return answer // len(jobs)
```



### 멀리 뛰기

```python
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b % 1234567
```



### 등굣길

```python
def solution(m, n, puddles):
    matrix = [[0] * n for _ in range(m)]
    for puddle in puddles:
        matrix[puddle[0]-1][puddle[1]-1] = -1

    for c in range(1, n):
        if matrix[0][c] == 0:
            matrix[0][c] = 1
        else:
            break
    for r in range(1, m):
        if matrix[r][0] == 0:
            matrix[r][0] = 1
        else:
            break
            
    for row in range(1, m):
        for col in range(1, n):
            if matrix[row][col] == -1:continue
            l_t = [matrix[row-1][col], matrix[row][col-1]]
            matrix[row][col] = sum(l_t) + l_t.count(-1)
    return matrix[m-1][n-1] % 1000000007
```



### N으로 표현

```python
def solution(N, number):
    if len(str(number)) == str(number).count(str(N)):
        if len(str(number)) < 9:
            return len(str(number))
        else:
            return -1

    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N) * i)}
        for i_half in range(1, i // 2 + 1):
            for x in S[i_half]:
                for y in S[i - i_half]:
                    case_set.add(x + y)
                    case_set.add(x - y)
                    case_set.add(y - x)
                    case_set.add(x * y)
                    if x != 0:
                        case_set.add(y // x)
                    if y != 0:
                        case_set.add(x // y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1
```



### 가장 긴 팰린드롬

> 나의 풀이

```python
def solution(s):
    if len(s) == 1: return 1
    for le in range(len(s), 0, -1):
        for idx in range(len(s) - le + 1):
            temp = s[idx:idx+le+1]
            if temp == temp[::-1]:
                return len(temp)
```



> 다른사람의 풀이(재귀 이용) 
>
> 시간초과가 발생하지만 재귀를 적절히 사용한 코드

```python
def solution(s):
    return len(s) if s[::-1] == s else max(solution(s[:-1]), solution(s[1:]))
```



### 최고의 집합

```python
def solution(n, s):
    quotient  = s // n
    if not quotient : return [-1]
    answer = [quotient] * n
    for i in range(1, (s%n)+1):
        answer[-i] += 1
    return answer
```



### 방문 길이

```python
def check(r, c, nr, nc, used):
    if [[r, c], [nr, nc]] not in used and [[nr, nc], [r, c]] not in used:
        used.append([[r, c], [nr, nc]])
    return used

def solution(dirs):
    r, c = 5, 5
    used = []
    for dir in dirs:
        if dir == "U":
            if r-1 < 0:continue
            used = check(r, c, r-1, c, used)
            r -= 1
        elif dir == "D":
            if r+1 > 10:continue
            used = check(r, c, r+1, c, used)
            r += 1
        elif dir == "R":
            if c+1 > 10:continue
            used = check(r, c, r, c+1, used)
            c += 1
        else:
            if c-1 < 0:continue
            used = check(r, c, r, c-1, used)
            c -= 1
    return len(used)
```



### 입국심사

```python
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left < right:
        middle = (left + right) // 2
        total = 0
        for time in times:
            total += middle // time
            if total >= n: break
        if total >= n:
            right = middle+1
        else:
            left = middle+1
    return left
```





