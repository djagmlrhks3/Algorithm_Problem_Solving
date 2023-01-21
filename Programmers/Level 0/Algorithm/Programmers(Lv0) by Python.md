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

