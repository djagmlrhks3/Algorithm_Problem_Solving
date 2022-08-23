# Programmers(Lv2) by Oracle

### 최솟값 구하기

```oracle
SELECT MIN(DATETIME) AS 시간
  FROM ANIMAL_INS
```



### 동물 수 구하기

```oracle
SELECT COUNT(*) as COUNT
  FROM ANIMAL_INS
```



### 중복 제거하기

```oracle
SELECT COUNT(DISTINCT NAME) AS COUNT
  FROM ANIMAL_INS
 WHERE NAME IS NOT NULL
```



### 고양이와 개는 몇 마리 있을까

```oracle
SELECT ANIMAL_TYPE, COUNT(*) AS count
  FROM ANIMAL_INS
 GROUP BY ANIMAL_TYPE
 HAVING ANIMAL_TYPE IN ('Dog', 'Cat')
 ORDER BY ANIMAL_TYPE
```

* GROUP BY : 컬럼 값(ANIMAL_TYPE)이 같은 것 끼리 하나로 묶어준다.



### NULL 처리하기

```oracle
SELECT ANIMAL_TYPE, NVL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID
```

* NVL(컬럼명, 바꿀 값)



### 동명 동물 수 찾기

```oracle
SELECT NAME, COUNT(*) AS COUNT
  FROM ANIMAL_INS
 WHERE NAME IS NOT NULL
 GROUP BY NAME
 HAVING COUNT(*) >= 2
 ORDER BY NAME
```



### 입양 시각 구하기(1)

```oracle
SELECT TO_NUMBER(HOUR) AS HOUR, CNT AS COUNT
  FROM (
SELECT TO_CHAR(DATETIME, 'HH24') AS HOUR, COUNT(*) AS CNT
  FROM ANIMAL_OUTS
 GROUP BY TO_CHAR(DATETIME, 'HH24')
     )
 WHERE HOUR BETWEEN 9 AND 19
 ORDER BY HOUR
```

> 'HH24' 옵션으로 시간 값을 얻을 수 있다.



### 루시와 엘라 찾기

```oracle
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
 WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
 ORDER BY ANIMAL_ID
```



### 이름에 el이 들어가는 동물 찾기

```oracle
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE UPPER(NAME) LIKE '%EL%'
   AND ANIMAL_TYPE = 'Dog'
 ORDER BY NAME
```

* Oracle에서 대소문자를 구별하는 방법은 모든 문자를 소문자 또는 대문자로 바꾼 후에 비교한다.



### 중성화 여부 파악하기

```oracle
SELECT ANIMAL_ID
     , NAME
     , CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
            WHEN SEX_UPON_INTAKE LIKE '%Spayed%'   THEN 'O'
            ELSE 'X'
            END AS 중성화
 FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

* case문 사용

> CASE 
>
> WHEN 조건 THEN 결과 값
>
> WHEN 조건 THEN 결과 값
>
> ELSE 조건이 아닌 경우
>
> END



### DATETIME에서 DATE로 형 변환

```oracle
SELECT ANIMAL_ID, NAME, TO_CHAR(DATETIME, 'YYYY-MM-DD') AS 날짜
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID
```
