# Programmers(Lv0) by Python

### 가장 큰 수 찾기

```python
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answera
```



### 편지

```python
def solution(message):
    return len(message) * 2
```



### 자릿수 더하기

```python
def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer
```



### 나머지 구하기

```python
def solution(num1, num2):
    return num1 % num2
```



### 배열 두 배 만들기

```python
def solution(numbers):
    return [num*2 for num in numbers]
```



### 중앙값 구하기

```python
def solution(array):
    array.sort()
    return array[len(array)//2] 
```



### 숫자 비교하기

```python
def solution(num1, num2):
    return 1 if num1 == num2 else -1
```



### 두 수의 나눗셈

```python
def solution(num1, num2):
    return int((num1 / num2) * 1000)
```



### 몫 구하기

```python
def solution(num1, num2):
    return num1 // num2
```



### 두 수의 곱

```python
def solution(num1, num2):
    return num1 * num2
```



### 두 수의 차

```python
def solution(num1, num2):
    return num1 - num2
```



### 두 수의 합

```python
def solution(num1, num2):
    return num1 + num2
```



### 중복된 숫자 개수

```python
def solution(array, n):
    return array.count(n)
```



### 머쓱이보다 키 큰 사람

```python
def solution(array, height):
    answer = 0
    for h in array:
        if h > height:
            answer += 1
    return answer
```



### 분수의 덧셈

```python
from math import gcd
def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    val = gcd(numer, denom)
    return [numer//val, denom//val]
```



### 최빈값 구하기

```python
def solution(array):
    chk = [0] * 1000
    for num in array:
        chk[num]+= 1
    return -1 if chk.count(max(chk)) > 1 else chk.index(max(chk))
```



### 짝수는 싫어요

```python
def solution(n):
    return [i for i in range(1, n+1) if i%2]
```



### 피자 나눠 먹기(1)

```python
def solution(n):
    return n//7 + 1 if n%7 else n//7
```



### 피자 나눠 먹기(2)

```python
def solution(n):
    for i in range(1, n+1):
        if not (6*i % n):
            return i
```



### 피자 나눠 먹기(3)

```python
def solution(slice, n):
    return n // slice + 1 if n % slice else n // slice
```



### 배열의 평균값

```python
def solution(numbers):
    return sum(numbers) / len(numbers)
```



### 옷가게 할인 받기

```python
from math import floor

def solution(price):
    if (price >= 500000):
        return floor(price * 0.8)
    elif (price >= 300000):
        return floor(price * 0.9)
    elif (price >= 100000):
        return floor(price * 0.95)
    return price
```



### 아이스 아메리카노

```python
def solution(money):
    return [money//5500, money%5500]
```



### 나이 출력

```python
def solution(age):
    return 2022 - age + 1
```



### 배열 뒤집기

```python
def solution(num_list):
    return num_list[::-1]
```



### 문자열 뒤집기

```python
def solution(my_string):
    return my_string[::-1]
```



### 직각삼각형 출력하기

```python
n = int(input())
for i in range(1, n+1):
    print("*" * i)s
```



### 짝수 홀수 개수

```python
def solution(num_list):
    odd, even = 0, 0
    for num in num_list:
        if num%2:
            odd+=1
        else:
            even+=1
    return [even, odd]
```



### 문자 반복 출력하기

```python
def solution(my_string, n):
    return ''.join(s*n for s in my_string)
```



### 특정 문자 제거하기

```python
def solution(my_string, letter):
    return ''.join(s for s in my_string if s not in letter)
```



````python
def solution(my_string, letter):
    return my_string.replace(letter, "")
````



### 각도기

```python
def solution(angle):
    return (angle // 90) * 2 + (angle % 90 > 0) * 1
```



### 양꼬치

```python
def solution(n, k):
    return n*12000 + (k-n//10)*2000
```



### 짝수의 합

```python
def solution(n):
    return sum(i for i in range(2, n+1, 2))
```



### 배열 자르기

```python
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
```



### 외계행성의 나이

```python
def solution(age):
    return ''.join(chr(int(s)+97) for s in str(age))
```



### 진료순서 정하기

```python
def solution(emergency):
    emergency_w = sorted(emergency, reverse=True)
    return [emergency_w.index(num)+1 for num in emergency]
```



### 개미 군단

```python
def solution(hp):
    return hp//5 + (hp%5)//3 + ((hp%5)%3)
```



### 모스부호 (1)

```python
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    return ''.join(morse[w] for w in letter.split(" "))
```



### 순서쌍의 개수

```python
def solution(n):
    num = int(n**(0.5))
    answer = -1 if num**2 == n else 0
    for i in range(1, num+1):
        if not n%i:
            answer+=2
    return answer
```



### 구슬을 나누는 경우의 수

```python
def solution(balls, share):
    answer = 1
    for i in range(2, balls+1):
        answer*=i
    for i in range(2, balls-share+1):
        answer//=i
    for i in range(2, share+1):
        answer//=i
    return answer
```



```python
from math import comb
def solution(balls, share):
    return comb(balls, share)
```



### 점의 위치 구하기

```python
def solution(dot):
    x, y = dot
    if x*y > 0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
```



### 최댓값 만들기(1)

```python
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]
```



### 2차원으로 만들기

```python
def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]
```



### 인덱스 바꾸기

```python
def solution(my_string, num1, num2):
    li = list(''.join(my_string))
    li[num1], li[num2] = li[num2], li[num1]
    return ''.join(li)
```



### 대문자와 소문자

```python
def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer += s.lower()
        if s.islower():
            answer += s.upper()
    return answer
```



### 배열 원소의 길이

```python
def solution(strlist):
    return [len(s) for s in strlist]
```



### n의 배수 고르기

```python
def solution(n, numlist):
    return [num for num in numlist if not num%n]
```



### 배열 회전시키기

> deque

```python
from collections import deque
def solution(numbers, direction):
    queue = deque(numbers)
    queue.rotate(1) if direction == "right" else queue.rotate(-1)
    return list(queue)
```



```python
def solution(numbers, direction):
    return numbers[1:]+[numbers[0]] if direction == "left" else [numbers[-1]] + numbers[:-1]
```

