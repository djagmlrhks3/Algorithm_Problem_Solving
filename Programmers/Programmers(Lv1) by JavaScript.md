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

