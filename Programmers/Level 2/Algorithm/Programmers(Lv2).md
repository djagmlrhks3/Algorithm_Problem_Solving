# Programmers(Lv2)

### 124나라의 숫자

```python
def solution(n):
    answer = ''
    while n > 0:
        if n%3 == 1:
            answer += '1'
        elif n%3 == 2:
            answer += '2'
        else:
            answer += '4'
        n = (n-1)//3
    return answer[::-1]
```



### 기능개발

```python
def solution(progresses, speeds):
    answer = []
    #candidate - 일을 마치기까지 소요되는 시간을 담을 배열
    candidate = []
    #100% - progresses(%) // speeds 계산으로 일을 마칠 때 까지 걸리는 시간을 구한다.
    for i in range(len(progresses)):
        candidate.append((100-progresses[i])//speeds[i])
	#첫 번째 값부터 비교 - pop(0)을 할 경우 생겨나는 비효율적인 메로리사용, 시간복잡도를 
    #줄이기 위해서 idx를 이용
    num = candidate[0]
    #num의 숫자가 있을 때 같이 배포할 수 있는 작업의 수를 구하기위한 변수
    cnt = 1
    #1번부터 마지막까지 탐색
    for i in range(1,len(candidate)):
        #num이 더 크면 동시에 배포할 수 있으므로 cnt += 1
        if num >= candidate[i]:
            cnt += 1
        #num이 더 작으면 동시 배포가 불가능하므로 cnt는 answer에 넣어주고
        #cnt값과 num을 갱신
        else:
            answer.append(cnt)
            cnt = 1
            num = candidate[i]
    #반복문을 끝마치고 남은 cnt를 answer에 추가
    answer.append(cnt)
    return answer
```



### 탑

```python
def solution(heights):
    N = len(heights)
    answer = []
    re_heights = heights[::-1]
    for send in range(N):
        for receive in range(send+1,N):
            if re_heights[send] < re_heights[receive]:
                answer.append(N-receive)
                break
        else:
            answer.append(0)
    answer = answer[::-1]
    return answer
```



### 전화번호 목록

```python
def solution(phone_book):
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
            if phone_book[j] == phone_book[i][:len(phone_book[j])]:
                return False
    return True
```



### 최댓값과 최솟값

```python
def solution(s):
    answer = ''
    numbers = list(map(int,s.split()))
    print(numbers)
    answer += str(min(numbers))+' '+str(max(numbers))
    return answer
```



### 영어 끝말잇기

```python
def solution(n, words):
    first = words[0]
    said = [first]
    for i in range(1,len(words)):
        if first[-1] == words[i][0] and words[i] not in said:
            said.append(words[i])
            first = words[i]
        else:
            answer = [len(said)%n+1, len(said)//n+1]
            break
    else:
        answer = [0,0]
    return answer
```



### 멀쩡한 사각형

```python
#수학적접근의 중요성!
def solution(w,h):
    big = max(w,h)
    small = min(w,h)
    for i in range(small,0,-1):
        if not big %i and not small%i:
            gcd = i
            break
    print(gcd)
    return w*h-(w+h-gcd)
```



### 스킬트리

```python
def solution(skill, skill_trees):
    answer = 0
    for sample in skill_trees:
        check = [0] * len(skill) #스킬 이수여부 확인
        for course in sample:
            if course not in skill: #관련없는 스킬 continue
                continue
            x = skill.index(course) #몇 번째 스킬인지 x변수에 담기
            if not x and not sum(check[1:]): #첫 번째 스킬(index=0)이면서 뒤의 스킬을 배우지 않았으면
                check[x] = 1                 #첫 번째 스킬 이수
            elif x and sum(check[:x]) == x:  #n번째 스킬일 때 자기 이전에 배운스킬을 다 이수 했으면(선행스킬을 다 이수했으면 x와 같은값이 되야 함.)
                check[x] = 1                 #n번째 스킬이수
            else:break                       #위 두 사건에 해당안되면 break
        else:answer+=1                       #break문 없이 for문을 통과하였다면 answer += 1
  return(answer)
```



### 쇠막대기

```python
def solution(arrangement):
    answer = 0
    #이전에 들어온 값이 무엇인지 확인하는 변수 before
    #지금까지의 "("[막대기]수를 세는 변수 count
    count = 0
    for v in arrangement:
        #막대기 시작 or 레이저시작
        if v == "(":
            count += 1
            before = "("
        #레이저 끝(레이저 발사)
        elif v == ")" and before == "(":
            count -= 1
            before = ")"
            answer += count
        #막대기 끝
        else:
            count -= 1
            before = ")"
            answer += 1
    return answer

"""
다른방법)
새로운 배열을 만든 후 주어진 arrangement에서 레이저에 해당하는 '()'을 미리 표현하고 '('와 ')'로 막대기만 세주는 방법을 생각함.
→ 또 다른 배열을 만들어 반복문으로 찾을필요 없이 replace 함수를 이용하여arrangement.replace('()','0') 다음과 같이 표현해주면 레이저 발사구간을 쉽게 바꿔줄 수 있다.
"""
```



### 프린터

```python
from collections import deque
def solution(priorities, location):
    answer = 0
    now = max(priorities)
    cnt = [0] * (now + 1)
    queue = deque()
    for idx in range(len(priorities)):
        cnt[priorities[idx]] += 1
        queue.append([idx, priorities[idx]])
    while queue:
        idx, pri = queue.popleft()
        if pri >= now:
            answer += 1
            if idx == location:
                return answer
            cnt[pri] -=1
            if not cnt[pri]:
                while True:
                    now -= 1
                    if not now: break
                    if cnt[now]: break
        else:
            queue.append((idx, pri))
```



### 가장 큰 수

>풀이 1 - 재귀
>
>샘플 테스트 케이스의 경우 input의 크기가 작기 때문에 통과하였으나
>테스트 케이스의 경우 문자열의 길이가 매우크면 시간초과 및 런타임에러가 발생...

```python
def perm(n, k, numbers):
    global answer
    if n == k:
        if int(''.join(numbers)) > answer:
            answer = int(''.join(numbers))
    else:
        for i in range(k, n):
            numbers[k], numbers[i] = numbers[i], numbers[k]
            perm(n, k+1, numbers)
            numbers[k], numbers[i] = numbers[i], numbers[k]

def solution(numbers):
    global answer
    numbers = list(map(str, numbers))
    perm(len(numbers), 0, numbers)
    print(answer)
    return None
answer = 0
numbers = [1000, 555, 464, 489, 239, 193, 134, 125, 154, 542, 75, 978, 67, 456]
solution(numbers)
```



> 풀이 2 - 문자열 접근

```python
def solution(numbers):
    answer = '' #결과를 담을 변수
    strnum = list(map(str, numbers)) #리스트의 int형을 string형으로 변환
    same_length = [[i, i * (12//len(i)) ] for i in strnum] #문자로 변환후 대소비교하기위한 세팅
    #1~100까지숫자를 문자로 나타냈을 대 길이가 1~4이므로 길이 통일을 위해 12(최소공배수)값
  
    same_length.sort(key=lambda x:x[1], reverse=True) #1번째 인덱스값을 기준으로 정렬
    for i in same_length:answer += i[0] #정렬후 원래 값인 0번째 인덱스를 answer에 더해준다.
    answer = str(int(answer)) #만약, 숫자가 0만 나올 경우 [0, 0, 0, 0] 0000으로 출력되면 안되므로 형변환이 필요하다.(11번 테스트케이스...)
    return answer

	#+) 세자리까지만 비교해도 충분하다... 1000은 100보다 낮은 우선순위 
    #따라서, same_length 리스트를 만들필요 없이 strnum.sort(key=lambda x:x*3, reverse=True)를 해주면 된다.
```



### 다리를 지나는 트럭

```python
def solution(bridge_length, weight, truck_weights):
    answer = 0

    from collections import deque
    trucks = deque(truck_weights)
    onbridge = deque()
    while trucks:
        if len(onbridge) == bridge_length:
            onbridge.popleft()
        if trucks[0] + sum(onbridge) <= weight:
            onbridge.append(trucks.popleft())
            answer += 1
        else:
            while len(onbridge) < bridge_length:
                onbridge.append(0)
                answer += 1
    return answer+bridge_length
```



### 문자열 압축

```python
def check(num, word, answer):
    res = ''
    now = word[:num]
    cnt = 1
    for i in range(num, len(word), num):
        if now == word[i:i + num]:
            cnt += 1
        else:
            if cnt == 1:
                res += now
                now = word[i:i+num]
            else:
                res += str(cnt) + now
                now = word[i:i + num]
                cnt = 1
        if len(res) >= answer:
            return answer
    if cnt == 1:
        res += now
    else:
        res += str(cnt) + now
    return len(res)

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        result = check(i, s, answer)
        if answer > result:
            answer = result
    return answer
```



### 삼각 달팽이

```python
def solution(n):
    answer = []
    candidates = [[0]*n for _ in range(n)]

    direction = 'd'

    row = 0
    col = 0
    num = 1
    cnt = n
    while(cnt):
        if direction == 'd':
            for i in range(cnt):
                if not candidates[row][col]:
                    candidates[row][col] = num
                    row += 1
                    num += 1
                else:
                    break
            row -= 1
            col += 1
            direction = 'r'
            cnt -= 1
        elif direction == 'r':
            for i in range(cnt):
                if not candidates[row][col]:
                    candidates[row][col] = num
                    col += 1
                    num += 1
                else:
                    break
            row -= 1
            col -= 2
            direction = 'u'
            cnt -= 1
        else:
            for i in range(cnt):
                if not candidates[row][col]:
                    candidates[row][col] = num
                    row -= 1
                    col -= 1
                    num += 1
                else:
                    break
            row += 2
            col += 1
            direction = 'd'
            cnt -= 1
            
    for li in candidates:
        for num in li:
            if num:
                answer.append(num)
    return answer
```



### 구명보트

```python
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    front, back = 0, len(people)-1
    while front <= back:
        if people[front] + people[back] <= limit:
            front += 1
            back -= 1
        else:
            front += 1
        answer += 1
    return answer
```



### H-index

```python
def solution(citations):
    answer = 0
    candidates = [0] * (max(citations)+1)
    for i in citations:
        candidates[i] += 1
    for j in range(len(candidates)-1, -1, -1):
        if sum(candidates[j:]) >= j:
            answer = j
            break
    return answer
```



### 타겟 넘버

> DFS/BFS라는 힌트를 받았지만 어떻게 풀어야할지 막막했던 문제
>
> DFS 방법 - 재귀를 이용하여 풀었다.
>
> 또한 함수 안의 함수 형태에서 변수의 사용범위에 대해서 고민이 많았는데
>
> 굳이 인자로 넘기지 않고 **nonlocal**로 처리할 수 있음을 배웠다.

```python
def solution(numbers, target):
    answer = 0
    def dfs(step, total):
        if step == len(numbers):
            if total == target:
                nonlocal  answer
                answer += 1
        else:
            dfs(step+1, total+numbers[step])
            dfs(step+1, total-numbers[step])
    dfs(0, 0)
    print(answer)
```



### JadenCase 문자열 만들기

```python
def solution(s):
    answer = ''
    empty = ''
    for word in s:
        if not empty and word.isalpha():
            empty += word.upper()
        elif word == ' ':
            answer += empty + ' '
            empty = ''
        else:
            empty += word.lower()
    return answer + empty
```



### 올바른 괄호

```python
def solution(s):
    left = 0
    for i in s:
        if i == '(':
            left += 1
        else:
            if left == 0:
                return False
            else:
                left -= 1
    return True if not left else False 
```



### 더 맵게

> 풀이 1

```python
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_1 = heapq.heappop(scoville)
        if min_1 < K:
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + min_2*2)
            answer += 1
        else:
            heapq.heappush(scoville, min_1)
            break
    return answer if scoville[0] >= K else -1
```

> 풀이 2

```python
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_1 = heapq.heappop(scoville)
        if min_1 < K:
            if not len(scoville):
                return -1
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + min_2*2)
            answer += 1
        else:
            heapq.heappush(scoville, min_1)
            break
    return answer
```



### 위장

```python
def solution(clothes):
    answer = 1
    total = dict()
    for clothe in clothes:
        if clothe[1] not in total:
            total[clothe[1]] = 1
        else:
            total[clothe[1]] += 1
    if len(total) == 1:
        return len(clothes)
    else:
        for i in total.values():
            answer *= i+1
    return answer - 1
```



### 카펫

```python
def solution(brown, yellow):
    total = brown + yellow # 카펫의 총 면적
    for i in range(3, brown): # 최소 3부터 시작
        if not total % i: # 면적으로 만들 수 있는 행, 열이 존재
            col = max(i, total//i)
            row = min(i, total//i)
            if (col * 2 + row * 2) - 4 == brown: # brown 개수 일치여부
                return [col, row]
```



### 피보나치 수

```python
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1234567
```



### 소수 찾기

>파이썬의 내장 라이브러리인 itertools를 활용

```python
from itertools import permutations
def check(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**(0.5))+1):
            if not num%i:
                return False
    return True

def solution(numbers):
    answer = 0
    candidates = []
    for i in range(1, len(numbers)+1):
        for n in list(map(''.join, permutations(numbers, i))):
            if int(n) not in candidates:
                candidates.append(int(n))            
                if check(int(n)):
                    answer += 1
    return answer
             
```



### 오픈채팅방

```python
def solution(record):
    users = dict()
    userid = []
    answer = []
    for re in record:
        info = re.split()
        if info[0] == "Enter":
            users[info[1]] = info[2]
            userid.append(info[1])
            answer.append("님이 들어왔습니다.")
        elif info[0] == "Change":
            users[info[1]] = info[2]
        else:
            answer.append("님이 나갔습니다.")
            userid.append(info[1])
    for i in range(len(userid)):
        answer[i] = users[userid[i]] + answer[i]
    return answer
```



### 최솟값 만들기

```python
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

solution([1, 4, 2], [5, 4, 4])
```



> 다른사람의 풀이 - zip을 사용!!!

```python
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
```



### 큰 수 만들기

```python
def solution(number, k):
    answer = ''
    stack = [number[0]]
    while k:
        for i in range(1, len(number)):
            if int(stack[-1]) >= int(number[i]):
                stack.append(number[i])
            else:
                while len(stack) and k and int(stack[-1]) < int(number[i]):
                    stack.pop()
                    k -= 1
                stack.append(number[i])
        else:
            return ''.join(stack[:len(number)-k])
    return ''.join(stack)
```



### 다음 큰 숫자

```python
def solution(n):
    binary = bin(n)[2:]
    cnt = binary.count('1')
    if len(binary) == cnt:
        return int('0b' + '10'+'1'*(cnt-1),2)
    else:
        if binary[-1] == '1':
            for i in range(len(binary)-1, 0, -1):
                if binary[i] == '0':
                    return int('0b' + binary[:i] + '10' + binary[i+2:], 2)
        else:
            flag = False
            chk = 0
            for i in range(len(binary)-1, 0, -1):
                if binary[i] == '0':
                    flag = True
                if binary[i] == '1' and flag and chk == 0:
                    chk = 1
                    flag = False
                if binary[i] == '0' and chk == 1:
                    idx = i
                    count_1 = binary[idx+2:].count('1')
                    count_0 = len(binary[idx+2:]) - count_1
                    return int('0b' + binary[:idx] + '10' + '0' * count_0 + '1' * count_1, 2)

            else:
                count_1 = binary.count('1')
                count_0 = binary.count('0')
                return int('0b' + '10' + '0'* (count_0) + '1' * (count_1-1), 2)
```



> 다른사람의 풀이

```python
def solution(n):
    cnt = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == cnt:
            return i
```



### 괄호 변환

```python
def divide(p):
    last = 0
    flag = True
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
            if right > left:
                flag = False
        if left == right:
            last = i
            break
    else:
        last = len(p)-1
    return p[:last+1], p[last+1:], flag

def recursive(p):
    if p == '':
        return ''
    u, v, flag = divide(p)
    if flag:
        return u + recursive(v)
    else:
        return '(' + recursive(v) + ')' + ''.join([')' if i == '(' else '(' for i in u[1:-1]])

def solution(p):
    return recursive(p)
```



### 숫자의 표현

```python
def solution(n):
    answer = 1
    numbers = [i for i in range(1, n)]
    print(numbers)
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            res = sum(numbers[i:j+1])
            if res == n:
                answer += 1
            if res > n:
                break
    return answer
```



### N개의 최소공배수

```python
def divide(num, n):
    cnt = 0
    while True:
        if n % num:
            return cnt, n
        else:
            n //= num
            cnt += 1
            
def solution(arr):
    answer = 1
    num = 2
    while sum(arr) != len(arr):
        count = 0
        for i in range(len(arr)):
            if not arr[i] % num:
                cnt, res = divide(num, arr[i])
                arr[i] = res
                count = max(count, cnt)
        answer *= (num ** count)
        num += 1
    return answer
```



### 조이스틱

```python
def check(idx, step):
    left = right = idx
    cnt = 0
    while True:
        right += 1
        left -= 1
        cnt += 1
        if right == len(step):
            right = len(step)-1
        if left  == -1:
            left = len(step)-1
        if step[right]:
            return right, cnt
        if step[left]:
            return left, cnt


def solution(name):
    answer = 0
    step = [0] * len(name)
    for i in range(len(name)):
        step[i] = min(abs(ord("A")-ord(name[i])), abs(ord("Z")+1 - ord(name[i])))

    idx = 0
    while sum(step):
        if step[idx]:
            answer += step[idx]
            step[idx] = 0
        else:
            idx, cnt = check(idx, step)
            answer += cnt + step[idx]
            step[idx] = 0
    return answer
```



### [1차] 캐시

```python
from collections import deque

def goToBack(city, queue):
    queue.remove(city.lower())
    queue.append(city.lower())
    return queue

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    queue = deque([])
    idx = 0
    while True:
        if len(queue) == cacheSize:
            break
        if idx == len(cities):
            break
        if cities[idx].lower() not in queue:
            queue.append(cities[idx].lower())
            idx += 1
        else:
            goToBack(cities[idx], queue)
            answer += 1
            idx += 1
    answer += len(queue) * 5

    for i in range(idx, len(cities)):
        if cities[i].lower() in queue:
            answer += 1
            goToBack(cities[i], queue)
        else:
            answer += 5
            queue.popleft()
            queue.append(cities[i].lower())
    return answer
```



### [1차] 뉴스 클러스터링

> 1차 풀이

```python
def solution(str1, str2):
    son = mother = 0
    str1_dict = dict()
    str2_dict = dict()
    for i in range(len(str1)-1):
        string1 = str1[i:i+2].lower()
        if string1.isalpha():
            if string1 not in str1_dict.keys():
                str1_dict[string1] = 1
            else:
                str1_dict[string1] += 1
    for i in range(len(str2)-1):
        string2 = str2[i:i+2].lower()
        if string2.isalpha():
            if string2 not in str2_dict.keys():
                str2_dict[string2] = 1
            else:
                str2_dict[string2] += 1

    used = []
    for idx, value in str1_dict.items():
        if idx not in used:
            if idx in str2_dict.keys():
                son += min(str1_dict[idx], str2_dict[idx])
                mother += max(str1_dict[idx], str2_dict[idx])
            else:
                mother += str1_dict[idx]
            used.append(idx)

    for idx, value in str2_dict.items():
        if idx not in used:
            mother += str2_dict[idx]
    return 65536 if mother == 0 else int(son/mother * 65536)
```



> 2차 풀이

```python
def solution(str1, str2):
    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        string1 = str1[i:i+2].lower()
        if string1.isalpha():
            str1_list.append(string1)
    for i in range(len(str2)-1):
        string2 = str2[i:i+2].lower()
        if string2.isalpha():
            str2_list.append(string2)
            
    intersection = set(str1_list) & set(str2_list)
    union = set(str1_list) | set(str2_list)

    son = [min(str1_list.count(i), str2_list.count(i)) for i in intersection]
    mother = [max(str1_list.count(i), str2_list.count(i)) for i in union]

    return int(sum(son)/sum(mother) * 65536) if len(mother) else 65536
```



### 소수 만들기

```python
from itertools import combinations

def check(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True

def solution(nums):
    answer = 0
    for li in combinations(nums, 3):
        num = sum(li)
        if check(num):
            answer += 1

    return answer
```

면접은 꾸준히 준비해야한다고 하는데 꾸준히 연습하거나 준비하고 계신거 있으신가요?



### 땅따먹기

> 풀이 1

```python
from copy import deepcopy

def solution(land):    
    candidates = deepcopy(land[0])
    for i in range(1, len(land)):
        step = deepcopy(candidates)
        for j in range(4):
            idx = 0
            while True:
                if j == idx:
                    idx += 1
                    continue
                if idx == 4:
                    break
                candidates[idx] = max(candidates[idx], step[j] + land[i][idx])
                idx += 1
    return max(candidates)
```

> 풀이 2 

```python
def solution(land):
    for i in range(1, len(land)):
        land[i][0] = max(land[i-1][1], land[i-1][2], land[i-1][3]) + land[i][0]
        land[i][1] = max(land[i-1][0], land[i-1][2], land[i-1][3]) + land[i][1]
        land[i][2] = max(land[i-1][0], land[i-1][1], land[i-1][3]) + land[i][2]
        land[i][3] = max(land[i-1][0], land[i-1][1], land[i-1][2]) + land[i][3]

    return max(land[-1])
```



### 가장 큰 정사각형 찾기

```python
def solution(board):
    for row in board:
        if sum(row):
            answer = 1
            break
    else:
        return 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i-1][j-1] and board[i-1][j] and board[i][j-1] and board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2
```



### 폰켓몬

> 풀이1) 시간초과

```python
from itertools import combinations

def solution(nums):
    answer = 0
    N = len(nums)
    for li in combinations(nums, N//2):
        answer = max(answer, len(set(li)))
    print(answer)
```



> 풀이2)

```python
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
```



### [1차] 프렌즈4블록

```python
def eraser(square, matrix):
    for i, j in square:
        matrix[i-1][j-1] = ''
        matrix[i][j-1] = ''
        matrix[i-1][j] = ''
        matrix[i][j] = ''
    return matrix

def down(matrix):
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, -1, -1):
            if not matrix[i][j]:
                for z in range(i-1, -1, -1):
                    if matrix[z][j]:
                        matrix[i][j] = matrix[z][j]
                        matrix[i][j], matrix[z][j] = matrix[z][j], matrix[i][j]
                        break
    return matrix

def solution(m, n, board):
    answer = 0
    matrix = [list(''.join(string)) for string in board]
    square = []
    while True:
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] == matrix[i][j] and matrix[i][j] != '':
                    square.append((i, j))
        if len(square):
            matrix = eraser(square, matrix)
            square.clear()
            matrix = down(matrix)
        else:
            break
    for li in matrix: answer += li.count('')
    return answer
```



### 점프와 순간 이동

> 풀이1

```python
def solution(n):
    ans = 1
    while n != 1:
        if n % 2:
            ans += 1
            n = (n-1) // 2
        else:
            n //= 2
    return ans
```

> 풀이2

```python
def solution(n):
    return bin(n).count('1')
```



### 후보키

```python
from itertools import combinations

def find(candidate):
    keys = []
    idx = [i for i in range(len(candidate))]
    for k in range(2, len(candidate)+1):
        for li in combinations(idx, k):
            res = list(zip(*(candidate[i] for i in li)))
            if len(set(res)) != len(res):
                continue
            for key in keys:
                if set(key).issubset(li):
                    break
            else:
                keys.append(set(li))
    return len(keys)

def solution(relation):
    answer = 0
    reverse = list(zip(*relation))
    candidate = []
    for col in reverse:
        if len(set(col)) == len(col):
            answer += 1
        else:
            candidate.append(col)
    answer += find(candidate)
    return answer
```



### 짝지어 제거하기

> 풀이1

```python
from collections import deque

def solution(s):
    stack = []
    words = deque(''.join(s))
    while len(words):
        if len(stack) and stack[-1] == words[0]:
            stack.pop(-1)
            words.popleft()
            continue
        stack.append(words.popleft())
        if len(words) and stack[-1] == words[0]:
            stack.pop(-1)
            words.popleft()

    return 0 if len(stack) else 1
```



> 풀이2 - 풀이1 개선

```python
def solution(s):
    stack = []
    for word in s:
        if not stack:
            stack.append(word)
            continue
        if stack[-1] == word:
            stack.pop(-1)
        else:
            stack.append(word)

    return 0 if len(stack) else 1
```



### 예상 대진표

> 풀이1

```python
def solution(n,a,b):
    a, b = min(a,b), max(a,b)
    answer = 0
    cnt = 0
    for i in range(1, 21):
        if 2**i == n:
            cnt = i
    left = 1
    right = n
    center = (left + right) // 2
    while True:
        if center >= a and center < b:
            break
        elif a >= center:
            left = center
            center = (right + center) // 2
            cnt -= 1
        elif center >= b:
            right = center
            center = (left + center) // 2
            cnt -= 1
    return cnt
```



> 풀이 2

```python
def solution(n,a,b):
    answer = 0

    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1
    return answer
```



### [3차] n진수 게임

```python
def solution(n, t, m, p):
    answer = ''
    length = m * t
    candidate = '0'
    num = 1
    alpha = 'ABCDEF'
    
    while len(candidate) < length:
        res = ''
        number = num
        while True:
            if number == 0:
                break
            if number % n:
                if number % n >= 10:
                    res += alpha[(number%n) % 10]
                else:
                    res += str(number % n)
            else:
                res += '0'
            number //= n
        num += 1
        candidate += res[::-1]
    for i in range(p-1, length, m): answer += candidate[i]
    return answer
```



### [3차] 압축

>  풀이1

```python
def check(idx, msg, words):
    new = True
    for i in range(idx+1, len(msg)):
        if msg[idx:i+1] not in words:
            words.append(msg[idx:i+1])
            break
    else:
        new = False
    return new, words, i

def solution(msg):
    answer = []
    words = []
    idx = 0
    while idx < len(msg):
        if msg[idx:idx+2] in words: # 만약 다음 문자가 answer에 있다면 check으로 확인
            new, words, end = check(idx, msg, words)
            if new:
                answer.append(words.index(msg[idx:end]) + 27)
                idx += (end - idx)
            else:
                answer.append(words.index(msg[idx:len(msg)]) + 27)
                idx = len(msg)
        else: # 만약 다음 문자가 answer에 없다면
            answer.append(ord(msg[idx]) - 64)
            words.append(msg[idx:idx+2])
            idx += 1
    return answer
```



> 풀이2

```python
def solution(msg):
    answer = []
    words = []
    idx = 0
    while idx < len(msg):
        if msg[idx:idx+2] in words: # 만약 다음 문자가 answer에 있다면 check으로 확인
            for i in range(idx+2, len(msg)):
                if msg[idx:i+1] not in words:
                    words.append(msg[idx:i + 1])
                    answer.append(words.index(msg[idx:i]) + 27)
                    idx += (i-idx)
                    break
            else:
                answer.append(words.index(msg[idx:len(msg)]) + 27)
                break
        else: # 만약 다음 문자가 answer에 없다면
            answer.append(ord(msg[idx]) - 64)
            words.append(msg[idx:idx+2])
            idx += 1
    return answer
```



> TIP)

```python
myDic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,27)))

또는

tmp = {chr(e + 64): e for e in range(1, 27)}
```



### [3차] 파일명 정렬

```python
def solution(files):
    answer = []
    candidate = []
    for i in range(len(files)):
        head = ''
        number = ''
        for word in files[i]:
            if not word.isnumeric() and not number:
                head += word
            if word.isnumeric():
                number += word
            if not word.isnumeric() and number:
                break
        candidate.append([head, number, i])

    arrange = sorted(candidate, key = lambda x : (x[0].lower(), int(x[1])))
    for arr in arrange: answer.append(files[arr[2]])
    return answer
```



다른 사람의 풀이

```python
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
```

number 부분이 5자리 이상일 경우에 대한 예외처리 필요...

→  '\d+' 대신 '\d{1,5}'로 정확한 범위를 주면 더 좋은 코드가 될 것 같다.



### [3차] 방금그곡

```python
def change(res):
    res = res.replace("C#", "c")
    res = res.replace("D#", "d")
    res = res.replace("F#", "f")
    res = res.replace("G#", "g")
    res = res.replace("A#", "a")
    return res

def hear(code, length):
    idx = 0
    res = ''
    while len(res) != length:
        res += code[idx]
        idx += 1
        if idx == len(code):
            idx = 0
    return res

def solution(m, musicinfos):
    musics = []
    m = change(m)

    for i in range(len(musicinfos)):
        musicinfos[i] = (musicinfos[i].split(','))

    for music in musicinfos:
        music[3] = change(music[3])

    for music in musicinfos:
        length = (int(music[1][:2])-int(music[0][:2]))*60 + int(music[1][3:])-int(music[0][3:])
        res = hear(music[3], length)
        musics.append([length, musicinfos.index(music), res, music[2]])

    for li in sorted(musics, key = lambda x: (-x[0], x[1])):
        if m in li[2]:
            return li[3]
    else:
        return "(None)"
```



### 수식 최대화

> 풀이1

```python
from itertools import permutations
from collections import deque

def solution(expression):
    num = ''
    origin_numbers = []
    origin_orders = []
    candidates = []
    for ex in expression:
        if ex.isnumeric():
            num += ex
        else:
            origin_orders.append(ex)
            origin_numbers.append(int(num))
            num = ''
    origin_numbers.append(int(num))
    for turn in permutations(['+', '-', '*']):
        numbers = deque(origin_numbers[:])
        orders =  deque(origin_orders[:])
        for order in turn:
            after_numbers = deque([])
            after_orders = deque([])
            while orders.count(order):
                now_o = orders.popleft()
                now_n = numbers.popleft()
                if now_o == order:
                    if order == '+':
                        numbers.appendleft(now_n + numbers.popleft())
                    elif order == '-':
                        numbers.appendleft(now_n - numbers.popleft())
                    else:
                        numbers.appendleft(now_n * numbers.popleft())
                    continue
                else:
                    after_orders.append(now_o)
                    after_numbers.append(now_n)
            orders = after_orders + orders
            numbers = after_numbers + numbers
        candidates.append(abs(numbers[0]))

    return max(candidates)
```



> 풀이2

우선순위가 높은 애들 기준으로 먼저 분리시킨 다음에(split)

낮은순서부터 join을 이용하여 계산한다.

```python
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n+1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))
    
    return answer
```



### 쿼드압축 후 개수 세기

```python
def calculate(i, j, n, arr):
    total = 0
    for r in range(i, i+n):
        total += sum(arr[r][j:j+n])
    if total == n**2:
        for r in range(i, i+n):
            for c in range(j, j+n):
                arr[r][c] = 1/(n**2)
        return arr
    elif total == 0:
        for r in range(i, i+n):
            for c in range(j, j+n):
                arr[r][c] = -1
        arr[r][c] = 0
        return arr
    else:
        return arr

def solution(arr):
    n = len(arr)
    num_one = 0
    num_zero = 0
    while n != 1:
        for i in range(0, len(arr), n):
            for j in range(0, len(arr), n):
                arr = calculate(i, j, n, arr)
        n //= 2
    for i in arr:
        num_one += sum(i) + i.count(-1)
        num_zero += i.count(0)
    return num_zero, int(num_one)
```



### 이진 변환 반복하기

```python
def solution(s):
    cnt = 0
    num_zero = 0
    while s != '1':
        num_zero += s.count("0")
        num = s.count('1')
        s = bin(num)[2:]
        cnt += 1
    return [cnt, num_zero]
```



### 메뉴 리뉴얼

> 나의 풀이
>
> 통과는 했지만 시간이 많이 걸렸다...
>
> * 불필요한 변수와 과정이 많은 것이 문제였다. 
>   * ex) candidates, new_menu는 하나의 딕셔너리로 가능

```python
from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        new_menu = {}
        for menu in orders:
            menu_li = list(''.join(menu))
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                if res not in candidates:
                    candidates.append(res)
                else:
                    if res not in new_menu.keys():
                        new_menu[res] = 2
                    else:
                        new_menu[res] += 1
        sort_menu = sorted(new_menu.items(), key=lambda x:[len(x[0]), x[1]])
        if len(sort_menu):
            now = course[-1]
            maxi = sort_menu[-1][1]
        while sort_menu:
            menu, cnt = sort_menu.pop()
            if len(menu) == now and cnt >= maxi:
                answer.append(menu)
            elif len(menu) != now:
                now = len(menu)
                maxi = cnt
                answer.append(menu)
    return sorted(answer)
```



> collections의 Counter 사용

```python
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
```



### 순위 검색

> 하드 코딩(효율성 실패)

```python
def solution(info, query):
    answer = []
    for q in query:
        orders = q.split()
        cnt = 0
        for i in info:
            people = i.split()
            if orders[0] != "-":
                if orders[0] != people[0]:
                    continue
            if orders[2] != "-":
                if orders[2] != people[1]:
                    continue
            if orders[4] != "-":
                if orders[4] != people[2]:
                    continue
            if orders[6] != "-":
                if orders[6] != people[3]:
                    continue
            if int(people[4]) >= int(orders[7]):
                cnt += 1
        answer.append(cnt)
    return answer
```



> 정답

```python
from bisect import bisect_left
from itertools import combinations

def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys(): all_people[case] = [int(seperate_info[4])]
            else: all_people[case].append(int(seperate_info[4]))

    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)

    return answer
```



### 주차 요금 계산

```python

from math import ceil

def calculate(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    cars = dict()
    answer = []
    for record in records:
        time, num, flag = record.split()
        if flag == "IN":
            if num not in cars.keys():
                cars[num] = [time, flag, 0]
            else:
                cars[num][0], cars[num][1] = time, flag
        else:
            cars[num][2] += calculate(time) - calculate(cars[num][0])
            cars[num][1] = "OUT"

    for key, value in cars.items():
        if value[1] == "IN":
            cars[key][2] += calculate("23:59") - calculate(value[0])

    for key, value in cars.items():
        if value[2] >= fees[0]:
            cars[key][2] = fees[1] + ceil((value[2] - fees[0]) / fees[2]) * fees[3]
        else:
            cars[key][2] = fees[1]

    for num in sorted(cars.keys()):
        answer.append(cars[num][2])

    return answer
```



