# Programmers(Lv1) by Python

### 완주하지 못한 선수

```python
#리스트를 사용하였을 때 효율성문제 극복X
#→ Python 에서의 dict 는 내부적으로 해시를 이용하여 구현되어있다. 따라서 특정한 키에 해당하는 값을 삽입, 삭제, 조회하는 데 상수 시간이 걸림

def solution(participant, completion):
    answer = ''z
    candidate = {}
    for man in participant:
        if man not in candidate:
            candidate[man] = 1
        else:
            candidate[man] += 1
    for winner in completion:
        candidate[winner] -= 1
    for who in candidate:
        if candidate[who]:
            answer = who
            break
    return answer
```



### 모의고사

```python
def solution(answers):
    #맞춘 문제수를 담을 count 배열
    count = [0, 0, 0, 0]
    #man1 ~ man3의 찍는 패턴을 리스트로 구현
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx1 = idx2 = idx3 = 0
    
    for num in answers:
        #man1 ~ man3이 찍는 패턴이 끝나면 처음부터 다시작해야 하므로 인덱스 0 초기화
        if idx1 == len(man1):idx1 = 0
        if idx2 == len(man2):idx2 = 0
        if idx3 == len(man3):idx3 = 0
        #man1 ~ man3이 정답 숫자와 같을 경우 count 배열에 +1
        if man1[idx1] == num:count[1] += 1
        if man2[idx2] == num:count[2] += 1
        if man3[idx3] == num:count[3] += 1
     	#man1 ~ man3의 idx + 1
        idx1 += 1;idx2 += 1;idx3 += 1
    answer = []
    #동점자가 나올수도 있으므로 최대 점수를 maximum에 담아
    maximum = max(count)
    #반복문으로 최대점수와 동일한 사람을 answer에 append
    for i in range(1,len(count)):
        if count[i] == maximum:
            answer.append(i)
    return answer
```



### K번째수

```python
def solution(array, commands):
    answer = []
    for command in commands:
        #unpacking
        i, j, k = command
        #slicing
        candidate = array[i-1:j]
        candidate.sort()
        #k번째에 해당하는 숫자를 answer에 추가
        answer.append(candidate[k-1])
    return answer
```



### 2016년

```python
def solution(a, b):
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = week[(sum(months[:a-1])+b)%7]
    return answer
```



### 가운데 글자 가져오기

```python
def solution(s):
    answer = s[len(s)//2] if len(s)%2 else s[len(s)//2-1:len(s)//2+1]
    return answer
```



### 같은 숫자는 싫어

```python
def solution(arr):
    answer = []
    answer.append(arr[0])
    for a in arr[1:]:
        if answer[-1] != a:
            answer.append(a)
    return answer
```



### 나누어 떨어지는 숫자 배열

```python
def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num%divisor:
            answer.append(num)
    if len(answer):
        answer.sort()
    else:
        answer = [-1] 
    return answer
```



### 두 정수 사이의 합

```python
def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        for i in range(min(a,b),max(a,b)+1):
            answer += i
    return answer
```



### 문자열 내 마음대로 정렬하기

```python
def solution(strings, n):
    answer = []
    before = []
    for i in strings:
        before.append((ord(i[n]), i))
    before.sort()
    for b in before:
        answer.append(b[1])
    return answer
```



### 수박수박수박수박수박수?

```python
def solution(n):
    rest = n%2
    quotient = n//2
    answer = '수박'*quotient + '수'*rest
    return answer
```



### 서울에서 김서방 찾기

```python
def solution(seoul):
    answer = '김서방은 {}에 있다'.format(seoul.index("Kim"))
    return answer
```



### 문자열 내 p와 y의 개수

```python
def solution(s):
    nump = 0
    numy = 0
    for word in s:
        if word == 'p' or word == 'P':
            nump += 1
        elif word == 'y' or word == 'Y':
            numy += 1
    answer = True if nump == numy else False
    return answer
```



### 핸드폰 번호 가리기

```python
def solution(phone_number):
    answer = '*'*(len(phone_number)-4)+phone_number[-4:]
    return answer
```



### 문자열 다루기 기본

```python
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isnumeric():
            return True
    return False
```



### 약수의 합

```python
def solution(n):
    if n <= 1: return n
    answer = 1 + n
    for num in range(2,n//2+1):
        if not n%num:
            answer += num
    return answer
```



### 문자열 내림차순으로 배치하기

```python
#join을 활용
def solution(s):
    s = list(''.join(s))
    s.sort(reverse=True)
    answer = ''.join(s)
    return answer
```



### 시저 암호

```python
def solution(s, n):
    answer = ''
    for word in s:
        if ord(word) == ord(' '):
            answer += ' '
        else:
            plus_n = ord(word)+n
            if word.isupper() and plus_n > ord('Z'):
                answer += chr(ord('A')+(plus_n-ord('Z'))-1)
            elif word.islower() and plus_n > ord('z'): 
                answer += chr(ord('a')+(plus_n-ord('z'))-1)
            else:
                answer += chr(plus_n)         
    return answer
```



### 직사각형 별찍기

```python
a, b = map(int, input().strip().split(' '))
for row in range(b):
    print('*'*a)
```



### x만큼 간격이 있는 n개의 숫자

```python
def solution(x, n):
    first = x
    answer = [first*i + x for i in range(n) ]
    return answer
```



### 행렬의 덧셈

```python
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        empty = []
        for j in range(len(arr1[i])):
            empty.append(arr1[i][j]+arr2[i][j])
        answer.append(empty)
    return answer
```



### 짝수와 홀수

```python
def solution(num):
    answer = "Odd" if num & 1 else "Even"
    return answer

#다른 사람의 풀이
#def solution(num):
#    return ["Even", "Odd"][num & 1]
```



### 하샤드 수

```python
def solution(x):
    str_x = str(x)
    sum_x = 0
    for i in str_x:sum_x += int(i)  
    return False == (x % sum_x) #나머지가 0이면 False

# 다른 사람의 풀이
# def solution(n):
    #return n % sum([int(c) for c in str(n)]) == 0
```



### 콜라츠 추측

```python
def solution(num):
    answer = 0
    while answer < 500 and num!=1:
        num = num*3+1 if num & 1 else num//2
        answer += 1
    answer = -1 if answer >= 500 else answer
    return answer
```



### 평균 구하기

```python
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer
```



### 자릿수 더하기

```python
def solution(n):
    str_n = str(n)
    answer = sum(int(i) for i in str_n)
    return answer
```



### 자연수 뒤집어 배열로 만들기

```python
def solution(n):
    str_n = str(n)
    answer = [int(i) for i in str_n[::-1]]
    return answer
```



### 정수 내림차순으로 배치하기

```python
def solution(n):
    str_n = str(n)
    test = [i for i in str_n]
    test.sort(reverse=True)
    answer = int(''.join(test))
    return answer
```



### 정수 제곱근 판별

```python
def solution(n):
    answer = int(((n**(0.5))+1)**2) if int(n**(0.5)) == n**(0.5) else -1
    return answer
```



### 제일 작은 수 제거하기

```python
def solution(arr):
    arr.remove(min(arr))
    answer = arr if arr else [-1]
    return answer
```



### 최대공약수와 최소공배수

```python
def solution(n, m):
    x, y = max(n, m), min(n, m)
    while x%y > 0:
        rest = x % y
        y, x = y, rest
    gcd = y
    lcm = gcd * (n//gcd) * (m//gcd)
    return [gcd, lcm]
```



### 예산

```python
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i >= 0:
            budget -= i
            answer += 1
        else:break
    return answer
```



### 키패드 누르기

> 누르게 될 키패드가 숫자가 아닌 문자('*', '#')까지 나올 경우엔
>
> 딕셔너리로 key(키패드) - value(좌표) 푸는 것이 좋을 것 같다. 

```python
def check(L, R, num, hand, phone):
    if num == 0: num = 11
    if L == 0: L = 11
    if R == 0: R = 11
    left = abs(phone[L-1][0]-phone[num-1][0]) + abs(phone[L-1][1]-phone[num-1][1])
    right = abs(phone[R-1][0]-phone[num-1][0]) + abs(phone[R-1][1]-phone[num-1][1])
    if left > right:
        return "right"
    elif right > left:
        return "left"
    else:
        return hand

def solution(numbers, hand):
    phone = [ (i, j) for i in range(4) for j in range(3) ]
    answer = ''
    nowL = 10 # '*'
    nowR = 12 # '#'
    for num in numbers:
        # 왼손
        if num % 3 == 1:
            answer += 'L'
            nowL = num
        # 오른손
        elif num != 0 and num % 3 == 0:
            answer += 'R'
            nowR = num
        # 중앙(2, 5, 8, 0)
        else: 
            if check(nowL, nowR, num, hand, phone) == "left":
                nowL = num
                answer += 'L'
            else:
                nowR = num
                answer += 'R'
    return answer
```



### 두 개 뽑아서 더하기

```python
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    return sorted(answer)
```



### 3진법 뒤집기

```python
def solution(n):
    answer = 0
    three = ""
    while(n > 2):
        three += str(n % 3)
        n //= 3
    three += str(n)
    for idx in range(len(three)):
        answer += 3**(idx) * int(three[::-1][idx])
    
    return answer
```



### 내적

```python
def solution(a, b):
    answer = 0
    for idx in range(len(a)):
        answer += a[idx] * b[idx]
    return answer
```



### 신규 아이디 추천

> 문자열 다루는데 익숙해지자... (많이 배웠던 문제)

```python
def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    # 5단계
    answer = 'a' if answer == '' else answer
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer
```



### 음양 더하기

```python
def solution(absolutes, signs):
    for i in range(len(signs)):
        absolutes[i] *= 1 if signs[i] else -1
    return sum(absolutes)
```



### 로또의 최고 순위와 최저 순위

```python
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt, zero = 0, 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        elif num == 0:
            zero += 1
    return [rank[cnt+zero], rank[cnt]]
```



### 약수의 개수와 덧셈

```python
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if (int(num**(0.5))) ** 2 == num:
            answer -= num
        else:
            answer += num
    return answer
```



### 숫자 문자열과 영단어

```python
def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 
               'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(numbers)):
        s = s.replace(numbers[i], str(i))
    return int(s)
```



### 없는 숫자 더하기

```python
def solution(numbers):
    return 45 - sum(set(numbers))
```



### 1주차_부족한 금액 계산하기

```python
def solution(price, money, count):
    total = 0
    for cnt in range(count, 0, -1):
        total += price * cnt
    return 0 if money >= total else total - money
```



### 2주차_상호평가

```python
def rank(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    n = len(scores)
    T = list(zip(*scores))
    answer = ''

    for i in range(n):
        compare = T[i][i]
        if (compare == max(T[i]) or compare == min(T[i])) and T[i].count(compare) == 1:
            average = (sum(T[i])-compare)/(n-1)
        else:
            average = sum(T[i])/n
        
        answer += rank(average)
    return answer
```



### 4주차_직업군 추천하기

```python
def solution(table, languages, preference):
    answer, max_score = 'ZZZ', 0
    for t in table:
        row = t.split()
        score = 0
        for l, p in zip(languages, preference):
            if l in row:
                score += (6 - row.index(l)) * p
        if score > max_score:
            answer = row[0]
            max_score = score
        elif score == max_score:
            answer = min(answer, row[0])
    return answer
```



### 6주차_복서 정렬하기

```python
def solution(weights, head2head):
    N = len(head2head)
    players = [[key+1, value] for key, value in enumerate(weights)]

    for i in range(N):
        W, L, cnt = 0, 0, 0
        for j in range(N):
            if head2head[i][j] == 'W':
                W += 1
                if weights[j] > weights[i]:
                    cnt += 1
            elif head2head[i][j] == 'L':
                L += 1
        if W + L:	
            ratio = W / (W + L)
        else:
            ratio = 0
        players[i] += [ratio, cnt]
    result = sorted(players, key=lambda x:[-x[2], -x[3], -x[1], x[0]] )
    return [rank[0] for rank in result]
```



### 나머지가 1이 되는 수 찾기

```python
def solution(n):
    for i in range(2, 1000001):
        if n%i == 1:
            return i
```

