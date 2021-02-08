# Programmers(Lv1) by JavaScript

### 두 정수 사이의 합

```javascript
function solution(a, b) {
    var answer = 0;
    for (let i = Math.min(a, b); i <= Math.max(a, b); i++) {
        answer += i
    }
    return answer;
}
```

