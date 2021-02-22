# Programmers(Lv1) by JavaScript

### 두 정수 사이의 합

```js
function solution(a, b) {
    var answer = 0;
    for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
        answer += i
    }
    return answer;
}
```



### 가운데 글자 가져오기

```js
function solution(s) {
    var answer = '';
    const center = Math.round(s.length/2)-1
    if (s.length%2) {
        answer = s[center]
    } else {
        answer = s[center] + s[center+1]
    }
    return answer;
}
```



> 삼항 연산자 사용

```js
function solution(s) {
    const center = Math.ceil(s.length/2)-1;
    return s.length % 2 ? s[center] : s[center] + s[center+1]  
}
```



### 수박수박수박수박수박수?

> 나의 풀이

```js
function solution(n) {
    var answer = '';
    const odd = "박";
    const even = "수";
    for (let i = 0; i < n; i++) {
        if (i % 2) {
            answer += odd
        } else {
            answer += even
        }
    }
    return answer;
}
```



> 삼항 연산자 사용

```js
function solution(n) {
    var answer = '';
    for (let i = 0; i < n; i++) {
        answer += i % 2 ? "박" : "수"; 
    }
    return answer;
}
```



### K번째수

* arr.slice()
* arr.sort((a, b) => a- b)
* arr.push()

```js
function solution(array, commands) {
    var answer = [];
    for (let arr of commands) {
        answer.push(array.slice(arr[0]-1, arr[1]).sort((a, b) => a - b)[arr[2]-1])
    }
    return answer;
}
```



### 2016

```js
function solution(a, b) {
    var month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    var weeks = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    var answer = weeks[(month.slice(0, a-1).reduce((a, b) => a+b, 0) + b) % 7]
    return answer;
}
```



### 핸드폰 번호 가리기

> ※ JS는 문자열 곱셈이 불가능하다.
>
> 따라서, 반복문이나 repeat 함수로 대체가 가능하다.

```js
function solution(phone_number) {
    var answer = ''
    for (let idx = 0; idx < phone_number.length - 4; idx++) {
        answer += '*'
    }
    answer += phone_number.slice(-4)
    return answer;
}
```



> repeat 함수 사용

```js
function solution(phone_number) {
    var answer = '*'.repeat(phone_number.length - 4) + phone_number.slice(-4)
    return answer;
}
```



### 문자열 내림차순으로 배치하기

```js
function solution(s) {
    var word_li = [];
    const words = s.split('');
    for (let i = 0; i < s.length; i++) {
        word_li.push(s[i])
    }
    word_li.sort().reverse()

    return word_li.join('');
}
```



> 함수 사용 - arr.split(), arr.sort(), arr.reverse(), arr.join()

```js
function solution(s) {
    return s.split('').sort().reverse().join('')
}
```



### 모의고사

> 나의 코드

```js
function solution(answers) {
    var answer = [];
    var man1 = [1, 2, 3, 4, 5];
    var man2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    var scores = [0, 0, 0];
    for (let idx = 0; idx < answers.length; idx++) {
        if (man1[idx%5] === answers[idx]) scores[0] += 1
        if (man2[idx%8] === answers[idx]) scores[1] += 1
        if (man3[idx%10] === answers[idx]) scores[2] += 1
    }
    var Maximum = Math.max(...scores)
    for (let i = 0; i < 3; i++) {
        if (scores[i] == Maximum) answer.push(i+1)
    }
    return answer;
}
```



> filter 함수 이용

```js
function solution(answers) {
    var answer = [];
    var a1 = [1, 2, 3, 4, 5];
    var a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    var a3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var a1c = answers.filter((a,i)=> a === a1[i%a1.length]).length;
    var a2c = answers.filter((a,i)=> a === a2[i%a2.length]).length;
    var a3c = answers.filter((a,i)=> a === a3[i%a3.length]).length;
    var max = Math.max(a1c,a2c,a3c);

    if (a1c === max) {answer.push(1)};
    if (a2c === max) {answer.push(2)};
    if (a3c === max) {answer.push(3)};


    return answer;
}

```



### 서울에서 김서방 찾기

```js
function solution(seoul) {
    return '김서방은 ' + seoul.indexOf("Kim") + '에 있다';
}
```

