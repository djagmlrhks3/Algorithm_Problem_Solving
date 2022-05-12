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





