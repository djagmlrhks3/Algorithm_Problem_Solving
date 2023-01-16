# Programmers(Lv1) by Oracle

### 모든 레코드 조회하기

```oracle
SELECT * 
  FROM ANIMAL_INS 
 ORDER BY ANIMAL_ID;
```



### 이름이 없는 동물의 아이디

```oracle
SELECT ANIMAL_ID
  FROM ANIMAL_INS
 WHERE NAME IS NULL
 ORDER BY ANIMAL_ID;
```



### 최댓값 구하기

```oracle
SELECT MAX(DATETIME) AS 시간
  FROM ANIMAL_INS;
```



### 이름이 있는 동물의 아이디

```oracle
SELECT ANIMAL_ID
  FROM ANIMAL_INS
 WHERE NAME IS NOT NULL
 ORDER BY ANIMAL_ID;
```



### 역순 정렬하기

```oracle
SELECT NAME, DATETIME
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID DESC;
```



### 아픈 동물 찾기

```oracle
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE INTAKE_CONDITION = 'Sick'
 ORDER BY ANIMAL_ID
```



### 어린 동물 찾기

```oracle
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE INTAKE_CONDITION != 'Aged'
 ORDER BY ANIMAL_ID
```



### 동물의 아이디와 이름

```oracle
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### 여러 기준으로 정렬하기

```oracle
SELECT ANIMAL_ID, NAME, DATETIME
  FROM ANIMAL_INS
 ORDER BY NAME, DATETIME DESC
```



### 상위 n개 레코드

> MySQL에는 LIMIT가 있지만 Oracle에는 없다.
>
> Oracle은 자동으로 생성되는 rownum을 이용하면 된다.
>
> 하지만 order by는 where을 선행할 수 없으므로 서브쿼리를 이용하여 해결!

```oracle
SELECT *
  FROM (
    SELECT NAME
      FROM ANIMAL_INS
     ORDER BY DATETIME
     )
 WHERE ROWNUM = 1
```



> RANK() OVER(ORDER BY) 이용

```Oracle
SELECT NAME
  FROM (	
    SELECT NAME, RANK() OVER(ORDER BY DATETIME) AS R
      FROM ANIMAL_INS
       )
 WHERE R = 1
```



### 자동차 대여 기록에서 장기/단기 대여 구분하기

```oracle
SELECT HISTORY_ID
      ,CAR_ID
      ,TO_CHAR(START_DATE, 'YYYY-MM-DD') "START_DATE"
      ,TO_CHAR(END_DATE, 'YYYY-MM-DD')   "END_DATE"
      ,CASE WHEN END_DATE - START_DATE + 1 >= 30 THEN '장기 대여'
               ELSE '단기 대여'
               END  RENT_TYPE
  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
 WHERE TO_CHAR(START_DATE, 'YYYYMM') = '202209'
 ORDER BY HISTORY_ID DESC
```



### 강원도에 위치한 생산공장 목록 출력하기

```ORACLE
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
  FROM FOOD_FACTORY
 WHERE ADDRESS LIKE '강원도%'
 ORDER BY 1
```



### 나이 정보가 없는 회원 수 구하기

```oracle
SELECT COUNT(*) USERS
  FROM USER_INFO
 WHERE AGE IS NULL
```



### 경기도에 위치한 식품창고 목록 출력하기

```oracle
SELECT WAREHOUSE_ID
      ,WAREHOUSE_NAME
      ,ADDRESS
      ,CASE WHEN FREEZER_YN IS NULL THEN 'N'
            ELSE FREEZER_YN
            END  FREEZER_YN
  FROM FOOD_WAREHOUSE
 WHERE ADDRESS LIKE '%경기도%'
 ORDER BY WAREHOUSE_ID
```



### 조건에 맞는 회원수 구하기

```Oracle
SELECT COUNT(*)
  FROM USER_INFO
 WHERE TO_CHAR(JOINED, 'YYYY') = '2021'
   AND AGE BETWEEN 20 AND 29
```



### 가장 비싼 상품 구하기

```Oracle
SELECT MAX(PRICE) MAX_PRICE
  FROM PRODUCT
```



