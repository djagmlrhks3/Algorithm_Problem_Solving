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

