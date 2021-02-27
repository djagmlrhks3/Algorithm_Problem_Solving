# JavaScript



> Number 객체

* **toFixed()** : 소수점 이하 몇 자리까지만 출력
  * ex) toFixed(2) - 2자리까지 출력

* **isNaN()** : NaN 판별
  * 주의 : NaN인 값과 === NaN으로 비교 X



> String 객체

* trim() : 문자열 양쪽 끝의 공백 없애기
* split() : 문자열을 특정 기호로 자르기 
  * 주의 : 배열을 만들어 return
* localeCompare() : 두 문자열 사전순 비교
  * ex) string1.localeComapre(string2)
    * -1 : string1 < string2
    * 0 : string1 == string 2
    * 1 : string2 < string1

* string.repeat(cnt) : 문자열 'string' cnt만큼 반복

* toUpperCase
* toLowerCase
* string.slice(start, end)
* string.replace("from", "to")

> Array 배열

* push - append
* splice - pop 
  * 주의 : String에서는 slice
* indexOf

* 최대값/최소값 구하기
  * Math.max(...arr)
  * Math.min(...arr)



> Object

* 키 존재여부 확인 : "Key" in Object
* 키 배열로 받아오기 : Object.keys("Object")
* 