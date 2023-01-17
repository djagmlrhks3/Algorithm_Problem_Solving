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

