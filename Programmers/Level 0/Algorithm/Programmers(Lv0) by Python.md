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



### 369게임

```python
def solution(order):
    return str(order).count('3')+str(order).count('6')+str(order).count('9')
```



### 직사각형 넓이 구하기

```python
def solution(dots):
    sort_li = sorted(dots, key=lambda x:[-x[1], -x[0]])
    return (sort_li[0][0]-sort_li[-1][0]) * (sort_li[0][1]-sort_li[-1][1])
```



### 공 던지기

```python
def solution(numbers, k):
    return numbers[((k-1)*2)%len(numbers)]
```



### 주사위의 개수

```python
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)
```



### 숨어있는 숫자의 덧셈(1)

```python
def solution(my_string):
    return sum([int(s) for s in my_string if s.isdigit()])
```



### 팩토리얼

```python
def solution(n):
    answer, factorial = 1, 1
    while factorial < n:
        answer += 1
        factorial *= answer
    return answer-1 if factorial > n else answer
```



### 모음 제거

```python
def solution(my_string):
    return ''.join([s for s in my_string if s not in 'aeiou'])
```



### 문자열 정렬하기 (1)

```python
def solution(my_string):
    return sorted([int(s) for s in my_string if s.isdigit()])
```



### 컨트롤 제트

```python
def solution(s):
    li = s.split()
    return sum([-int(li[i-1]) if li[i]=="Z" else int(li[i]) for i in range(len(li))])
```



### 합성수 찾기
```python
def solution(n):
    li = [1, 1] + [0] * (n-1)
    for i in range(2, n+1):
        if not li[i]:
            for j in range(i*i, len(li), i):
                li[j] = 1 
    return li.count(1)-2
```

​	

### 소인수분해
```python
def solution(n):
    answer, d = [], 2
    while d <= n:
        if not n%d:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d+=1
    return answer
```



### 캐릭터의 좌표

```python
def solution(keyinput, board):
    dir = {"left":(-1, 0), "right":(1, 0), "up":(0, 1), "down":(0, -1)}
    answer = [0, 0]
    for k in keyinput:
        dx, dy = dir[k]
        if abs(answer[0]+dx)>board[0]//2 or abs(answer[1]+dy)>board[1]//2:
            continue
        else:
            answer[0]+=dx
            answer[1]+=dy
    return answer
```



### 가까운 수

```python
def solution(array, n):
    arr = [(abs(num-n), num) for num in array]
    return sorted(arr, key=lambda x:[x[0], x[1]])[0][1]
```



### 삼각형의 완성조건 (1)

```python
def solution(sides):
    x, y, z = sorted(sides)
    return 1 if x+y>z else 2
```



### 최댓값 만들기(2)

```python
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
```



### 숨어있는 숫자의 덧셈(2)

```python
def solution(my_string):
    numbers = ''.join(s if s.isdigit() else ' ' for s in my_string)
    return sum([int(num) for num in numbers.split()])
```



### 배열의 유사도

```python
def solution(s1, s2):
    return len(set(s1)&set(s2))
```



### 중복된 문자 제거

```python
def solution(my_string):
    answer = ''
    for s in list(''.join(my_string)):
        if s not in answer:
            answer += s
    return answer
```



### k의 개수

```python
def solution(i, j, k):
    return sum(str(n).count(str(k)) for n in range(i, j+1))
```



### A로 B만들기

```python
def solution(before, after):
    return 1 if sorted(''.join(before)) == sorted(''.join(after)) else 0
```



### 문자열안에 문자열

```python
def solution(str1, str2):
    return 1 if str2 in str1 else 2
```



### 제곱수 판별하기

```python
def solution(n):
    return 1 if int(n**(0.5))**2 == n else 2
```



### 암호 해독

```python
def solution(cipher, code):
    return ''.join(cipher[i-1] for i in range(code, len(cipher)+1, code))
```



### 세균 증식

```python
def solution(n, t):
    return n*2**t
```



### 숫자 찾기

```python
def solution(num, k):
    return str(num).find(str(k))+1 if str(k) in str(num) else -1
```



### 약수 구하기

```python
def solution(n):
    return [i for i in range(1, n+1) if not n%i]
```



### 문자열 정렬하기(2)

```python
def solution(my_string):
    return ''.join(sorted([s.lower() for s in my_string]))
```



### 한 번만 등장한 문자

```python
def solution(s):
    return ''.join(sorted(w for w in s if s.count(w) == 1))
```



### 7의 개수

```python
def solution(array):
    return str(array).count('7')
```



### 이진수 더하기

```python
def solution(bin1, bin2):
    return bin(int(bin1, 2)+int(bin2, 2))[2:]
```



### 잘라서 배열로 저장하기

```python
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
```



### 영어가 싫어요

```python
def solution(numbers):
    for idx, num in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        numbers = numbers.replace(num, str(idx))
    return int(numbers)
```



### 문자열 계산하기

```python
def solution(my_string):
    return eval(my_string)
```



### 외계어 사전

> (1) sorted
```python
def solution(spell, dic):
    for d in dic:
        if sorted(spell) == sorted(d):
            return 1
    return 2
```

> (2) set
```python
def solution(spell, dic):
    for d in dic:
        if not set(spell) - set(d):
            return 1
    return 2
```



### 종이 자르기

```python
def solution(M, N):
    return M*N-1
```



### 치킨 쿠폰

```python
def solution(chicken):
    answer = 0
    while True:
        if chicken // 10:
            answer += chicken//10
            chicken = chicken//10 + chicken%10
        else:
            break
    return answer
```



### 로그인 성공?

```python
def solution(id_pw, db):
    flag = False
    for li in db:
        id, pw = li
        if(id == id_pw[0] and pw == id_pw[1]):
            return "login"
        if(id == id_pw[0] and pw != id_pw[1]):
            flag = True
    return "wrong pw" if flag else "fail"
```



### 등수 매기기

```python
def solution(score):
    rank = sorted([sum(s) for s in score], reverse=True)
    return [rank.index(sum(s))+1 for s in score]
```



### 다항식 더하기

```python
def solution(polynomial):
    a, b = 0, 0
    for s in polynomial.split(' + '):
        if 'x' in s:
            a += (1 if s == 'x' else int(s[:-1]))  
        else:
            b += int(s)
    return (str(a)+'x' if a > 1 else a * 'x') + (' + ' if a and b else '') + (str(b) if b else '')
```



### 특이한 정렬

```python
def solution(numlist, n):
    rank = sorted([(abs(num-n), num)for num in numlist], key=lambda x:[x[0], -x[1]])
    return [r[1] for r in rank]
```



### 다음에 올 숫자

```python
def solution(common):
    return common[-1] + common[2]-common[1] if common[2] - common[1] == common[1] - common[0] else common[-1] * common[1]/common[0]
```



### 문자열 밀기

```python
def solution(A, B):
    candidates = [(A[-i:]+A[:-i], i) for i in range(len(A))]
    for key, value in candidates:
        if B == key:
            return value
    return -1
```



### 저주의 숫자 3

```python
def solution(n):
    answer, t = 1, 1
    while t < n:
        if (answer+1)%3 and '3' not in str(answer+1):
            t+=1
        answer += 1
    return answer
```



### 연속된 수의 합

```python
import math
def solution(num, total):   
    start = math.ceil(total/num) - num//2
    return [i for i in range(start, start+num)]
```



### 삼각형의 완성조건 (2)

```python
def solution(sides):
    answer = 0
    a, b = max(sides), min(sides)
    for c in range(1, 2000):
        if (c+b > a and a >= c) or (a+b > c and c >= a):
            answer += 1
    return answer
```



### 안전지대

```python
d = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
def solution(board):
    answer, n = 0, len(board)
    for r in range(n):
        for c in range(n):
            if not board[r][c]:
                for i in range(8):
                    nr, nc = r+d[i][0], c+d[i][1]
                    if 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc]:
                            break
                else:
                    answer+=1       
    return answer
```



### 겹치는 선분의 길이

```python
def solution(lines):
    li = [set(range(line[0], line[1])) for line in lines]
    return len(li[0] & li[1] | li[1] & li[2] | li[0] & li[2])
```



### 옹알이(1)

```python
def solution(babbling):
    answer = 0
    for bab in babbling:
        for candidate in ["aya", "ye", "woo", "ma"]:
            if candidate in bab:
                bab = bab.replace(candidate, ' ')
            if not bab.strip():
                answer += 1
                break
    return answer
```



### 소문자로 바꾸기

```python
def solution(myString):
    return myString.lower()
```



### 대문자로 바꾸기

```python
def solution(myString):
    return myString.upper()
```



### 길이에 따른 연산

```python
def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    
    result = 1
    for num in num_list:
        result *= num
    return result
```



### n번째 원소까지

```python
def solution(num_list, n):
    return [num_list[i] for i in range(n)]
```



### 정수 찾기

```python
def solution(num_list, n):
    return 1 if n in num_list else 0
```



### flag에 따라 다른 값 반환하기

```python
def solution(a, b, flag):
    return a+b if flag else a-b
```



### n개 간격의 원소들

```python
def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]
```



### rny_string

```python
def solution(rny_string):
    return rny_string.replace('m', 'rn')
```



### 정수 부분

```python
def solution(flo):
    return int(flo)
```



### 첫 번째로 나오는 음수

```python
def solution(num_list):
    for i in range(0, len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
```



### 문자열로 변환

```python
def solution(n):
    return str(n)
```



### 문자열의 앞의 n글자

```python
def solution(my_string, n):
    return my_string[:n]
```



### 공배수

```python
def solution(number, n, m):
    return 1 if not((number%n)+(number%m)) else 0
```



### 문자열을 정수로 변환하기

```python
def solution(n_str):
    return int(n_str)
```



### 문자열 정수의 합

> CASE 1

```python
def solution(num_str):
    return sum([int(num) for num in num_str])
```



> CASE 2

```python
def solution(num_str):
    return sum(map(int, list(num_str))) 
```



### 문자열의 뒤의 n글자

```python
def solution(my_string, n):
    return my_string[len(my_string)-n:]
```



### 카운트 업

```python
def solution(start, end):
    return [num for num in range(start, end+1)]
```



### n의 배수

```python
def solution(num, n):
    return 0 if num%n else 1
```



### 배열에서 문자열 대소문자 변환하기

```python
def solution(strArr):
    return [strArr[i].upper() if i%2 else strArr[i].lower() for i in range(len(strArr))]
```



### n번째 원소부터

```python
def solution(num_list, n):
    return [num_list[i] for i in range(n-1, len(num_list))]
```



### 원소들의 곱과 합

```python
def solution(num_list):
    multiple = 1
    for num in num_list:
        multiple *= num
    return 1 if multiple < sum(num_list) ** 2 else 0
```



### 부분 문자열인지 확인하기

```python
def solution(my_string, target):
    return 1 if my_string.count(target) else 0
```



### 문자열 곱하기

```python
def solution(my_string, k):
    return my_string * k
```



### 조건에 맞게 수열 변환하기 1

```python
def solution(arr):
    return [a//2 if (a >= 50 and not a%2) else (a*2 if a < 50 and a%2 else a) for a in arr]
```



### 접두사인지 확인하기

```python
def solution(my_string, is_prefix):
    return 1 if my_string[:len(is_prefix)] == is_prefix else 0
```



### 부분 문자열

```python
def solution(str1, str2):
    return 1 if str2.count(str1) else 0
```



### 카운트 다운

```python
def solution(start, end):
    return [i for i in range(start, end-1, -1)]
```



### 조건에 맞게 수열 변환하기 3

```python
def solution(arr, k):
    return [a*k if k%2 else a+k for a in arr]
```



> lambda 사용

```python
def solution(arr, k):
    return list(map((lambda x:x*k) if k%2 else (lambda x:x+k), arr))
```



### 글자 이어 붙여 문자열 만들기

```python
def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])
```



### 접미사인지 확인하기

```python
def solution(my_string, is_suffix):
    return 1 if my_string[-len(is_suffix):] == is_suffix else 0
```



### 마지막 두 원소

```python
def solution(num_list):
    return num_list+[num_list[-1]-num_list[-2]]if num_list[-1] > num_list[-2] else num_list+[num_list[-1]*2]
```



### 특정한 문자를 대문자로 바꾸기

```python
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())
```









