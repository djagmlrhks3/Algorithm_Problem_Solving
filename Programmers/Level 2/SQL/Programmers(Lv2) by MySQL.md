# Programmers(Lv2) by MySQL

### 최솟값 구하기

```sql
SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS;
```



### 동물 수 구하기

```sql
SELECT COUNT(*) AS "count"
FROM ANIMAL_INS;
```



### 중복 제거하기

```sql
SELECT COUNT(DISTINCT NAME) AS "count"
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
```

* COUNT 하려는 column에서 중복을 제거하려면 `COUNT(DISTINCT column)` 으로 할 수 있다!



### 고양이와 개는 몇 마리 있을까

```sql
SELECT ANIMAL_TYPE, COUNT(*) AS "count"
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

* GROUP BY : 컬럼 값(ANIMAL_TYPE)이 같은 것 끼리 하나로 묶어준다.



### NULL 처리하기

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

* IFNULL(컬럼명, NULL일 경우 입력할 값)



### 동명 동물 수 찾기

```sql
SELECT NAME, COUNT(*) AS "COUNT"
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME;
```



### 입양 시각 구하기(1)

```sql
SELECT HOUR(DATETIME) AS "HOUR", COUNT(*) AS "COUNT"
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR
ORDER BY HOUR;
```



> WHERE의 조건문을 HAVING으로 대체

```sql
SELECT HOUR(DATETIME) AS "HOUR", COUNT(*) AS "COUNT"
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 20
ORDER BY HOUR;
```



### 루시와 엘라 찾기

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```



### 이름에 el이 들어가는 동물 찾기

```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE = "Dog"
ORDER BY NAME;
```

* My SQL에서는 기본적으로 대소문자를 구별하지 않는다. (구별하는 방법은 있다.)



### 중성화 여부 파악하기

```sql
SELECT ANIMAL_ID, NAME,
IF (SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%', 'O', 'X') AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

* IF(조건, '참', '거짓')



> CASE 
>
> WHEN 조건 THEN 결과 값
>
> WHEN 조건 THEN 결과 값
>
> ELSE 조건이 아닌 경우
>
> END

```sql
SELECT ANIMAL_ID, NAME, CASE
WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
ELSE 'X' END AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### DATETIME에서 DATE로 형 변환

```SQL
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS "날짜"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

