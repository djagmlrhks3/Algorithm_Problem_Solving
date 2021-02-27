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



### 문자열 내 p와 y의 개수

```js
function solution(s){
    var num_p = 0;
    var num_y = 0;
    for (let idx = 0; idx < s.length; idx++) {
        if (s[idx] === 'p' || s[idx] === 'P') {
            num_p++
        } else if (s[idx] === 'y' || s[idx] === 'Y') {
            num_y++
        }
    }
    return num_p === num_y ? true : false;
}
```



> 다른 사람의 풀이 - toUpperCase(), split() 사용

```js
function solution(s){
    return s.toUpperCase().split('P').length === s.toUpperCase().split('Y').length ? true : false
}
```



### 문자열을 정수로 바꾸기

```js
function solution(s) {
    var answer = '';
    for (let idx = 0; idx < s.length; idx++) {
        if (s[idx] !== '+') answer += s[idx]
    }
    return Number(answer);
}
```



> JS의 형변환 이용...

```js
function solution(s) {
    return s/1
}
```



### 두 개 뽑아서 더하기

```js
function solution(numbers) {
    var answer = [];
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            if (!answer.includes(numbers[i] + numbers[j])) {
                answer.push(numbers[i] + numbers[j])
            }
        }
    }
    answer.sort((a, b) => a - b)
    return answer;
}
```



> spread operator 사용

```js
function solution(numbers) {
    var answer = [];
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            answer.push(numbers[i] + numbers[j])
        }
    }
    answer = [...new Set(answer)]
    return answer.sort((a, b) => (a - b));
}
```



### 같은 숫자는 싫어

```js
function solution(arr) {
    var answer = [arr[0]];
    for (let idx = 1; idx < arr.length; idx++) {
        if (answer[answer.length-1] !== arr[idx]) {
            answer.push(arr[idx])
        }
    }
    return answer;
}
```



### 콜라츠 추측

```js
function solution(num) {
    var answer = 0;
    while (answer < 500) {
        if (num === 1) break
        if (num % 2 === 0) {
            num /= 2
        } else {
            num = num * 3 + 1
        }
        answer += 1
    }
    return answer === 500 ? -1 : answer
}
```



### 자릿수 더하기

```js
function solution(n)
{
    var answer = 0;
    for (const num of String(n)) {
        answer += Number(num)
    }
    return answer;
}
```



### 문자열 다루기 기본

> isNaN
>
> ※ 주의 '1e10'처럼 지수로 표현할 수 있는 문자열은 false 결과값이 나온다. 

```js
function solution(s) {
    if (s.length === 4 || s.length === 6) {
        for (const n of s) {
            if (isNaN(n)) {
                return false
            }
        } return true
    } else {
        return false
    }
}
```



### 나누어 떨어지는 숫자 배열

```js
function solution(arr, divisor) {
    var answer = [];
    for (const num of arr) {
        if (num % divisor === 0) {
            answer.push(num)
        }
    }
    answer.sort((a, b) => (a - b))
    return answer.length ? answer : [-1]
}
```



> filter 사용

```js
function solution(arr, divisor) {
    var answer = arr.filter(v => v % divisor === 0)
    return answer.length ? answer.sort((a, b) => (a - b)) : [-1]
}
```



### 문자열 내 마음대로 정렬하기

```js
function solution(strings, n) {
    return strings.sort(function(a, b) {
        if (a[n] === b[n]) {
            return (a > b) - (a < b)
        } else {
            return (a[n] > b[n]) - (a[n] < b[n])
        }
    })
}
```



> localeCompare 사용 - 두 문자열의 사전순을 알려준다.
>
> string1.localeCompare(string2) 
>
> * -1 : string1 - string2
> * 0 : string1 - string2
> * 1 : string2 - string1

```js
function solution(strings, n) {
    return strings.sort((a, b) => (a[n] === b[n]) ? a.localeCompare(b) : a[n].localeCompare(b[n]))
}
```



### 하샤드 수

```js
function solution(x) {
    var divide = 0
    for (const num of String(x)) {
        divide += Number(num)
    }
    return x % divide ? false : true
}
```



### 소수 찾기

> 길이 n만큼의 배열 생성 + 초기값 0
>
> new Array(n).fill(0)

```js
function solution(n) {
    var answer = 0;
    var arr = new Array(n+1).fill(0)
    for (let idx = 2; idx < n+1; idx++) {
        if (!arr[idx]) {
            answer += 1
            for (let i = idx*2; i < n+1; i+=idx) {
                arr[i] = 1
            }
        }
    }
    return answer
}
```



### 직사각형 별찍기

```js
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    for (let row = 0; row < b; row++) {
        console.log('*'.repeat(a))
    }
});
```



### 행렬의 덧셈

```js
function solution(arr1, arr2) {
    var answer = [];
    for (let row = 0; row < arr1.length; row++) {
        var li = []
        for (let col = 0; col < arr1[0].length; col++) {
            li.push(arr1[row][col] + arr2[row][col])
        }
        answer.push(li)
    }
    return answer;
}
```



### 짝수와 홀수

```js
function solution(num) {
    return num%2 ? "Odd" : "Even"
}
```



### 평균 구하기

```js
function solution(arr) {
    return arr.reduce((a, b) => (a + b)) / arr.length
}
```



### 제일 작은 수 제거하기

```js
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)), 1)
    return arr.length > 0 ? arr : [-1] ;
}
```



### 최대공약수와 최소공배수

> 유클리드 호제법

```js
function solution(n, m) {
    var max = Math.max(n, m)
    var min = Math.min(n, m)
    while (true) {
        var divide = max % min
        if (divide === 0) {
            break
        } else {
            max = Math.max(divide, min)
            min = Math.min(divide, min)
        }
    }
    return [min, (n / min) * m]
}
```



> 다른 사람의 풀이 - 재귀 함수

```js
function greatestCommonDivisor(a, b) {return b ? greatestCommonDivisor(b, a % b) : Math.abs(a);}
function leastCommonMultipleOfTwo(a, b) {return (a * b) / greatestCommonDivisor(a, b);}
function solution(a, b) {
    return [greatestCommonDivisor(a, b),leastCommonMultipleOfTwo(a, b)];
}
```



### 정수 제곱근 판별

```js
function solution(n) {
    return n ** (0.5) === Math.round(n ** (0.5)) ? (n ** (0.5) + 1) ** 2 : -1
}
```



### 자연수 뒤집어 배열로 만들기

```js
function solution(n) {
    var answer = [];
    for (let num of String(n)) answer.push(Number(num));
    return answer.reverse();
}
```



> 다른 사람의 풀이

```js
function solution(n) {
	return n.toString().split('').reverse().map(o => o = parseInt(o));
}
```



### 시저 암호

> "String".charCodeAt(index) : "String" 문자열에서 index위치에 해당하는 문자의 아스키 코드 반환
>
> String.fromCharCode(숫자) : 숫자에 해당하는 아스키코드 문자 반환

```js
function solution(s, n) {
    var answer = '';
    for (const word of s) {
        if (word !== ' ') {
            let temp = word.charCodeAt(0)
            if (temp >= 65 && temp <= 90) {
                temp += n
                answer += String.fromCharCode(temp > 90 ? temp - 26 : temp)
            }
            else {
                temp += n    
                answer += String.fromCharCode(temp > 122 ? temp - 26 : temp)
            } 
        } else {
            answer += ' '
        }
    }
    return answer;
}
```



> String 사용

```js
function solution(s, n) {
    var answer = '';
    const big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const small = 'abcdefghijklmnopqrstuvwxyz'
    for (const word of s) {
        if (word === ' ') {
            answer += word
            continue
        }
        var location = big.includes(word) ? big : small
        var index = location.indexOf(word) + n
        if (index  >= location.length) {
            index %= location.length
        }
        answer += location[index]
    }
    return answer;
}
```



### 이상한 문자 만들기

```js
function solution(s) {
    var answer = ''
    var words = s.split(' ')
    for (const word of words) {
        for (const idx in word) {
            answer += idx%2 ? word[idx].toLowerCase() : word[idx].toUpperCase()
        }
        answer += ' '
    }
    return answer.slice(0, answer.length-1)
}
```



### 정수 내림차순으로 배치하기

```js
function solution(n) {
    var answer = 0;
    var numbers = []
    for (const num of String(n)) {
        numbers.push(Number(num))
    }
    numbers.sort((a, b) => (a - b)).reverse()
    return Number(numbers.join(''))
}
```



> 함수 이용

```js
function solution(n) {
    return parseInt(String(n).split("").sort().reverse().join(""))
}
```



### 완주하지 못한 선수

```js
function solution(participant, completion) {
    var answer = '';
    var check = {}
    for (const man of completion) {
        if (man in check) {
            check[man] += 1
        } else {
            check[man] = 1
        }
    }
    for (const man of participant) {
        if (man in check && check[man]) {
            check[man] -= 1
        } else {
            return man
        }
    }
}
```

