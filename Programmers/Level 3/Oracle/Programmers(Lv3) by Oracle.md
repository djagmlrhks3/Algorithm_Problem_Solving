# Programmers(Lv3) by MySQL

### 없어진 기록 찾기

```oracle
SELECT B.ANIMAL_ID, B.NAME
  FROM ANIMAL_INS A,
       ANIMAL_OUTS B
 WHERE B.ANIMAL_ID = A.ANIMAL_ID(+)
   AND A.ANIMAL_ID IS NULL
 ORDER BY B.ANIMAL_ID
```



### 있었는데요 없었습니다

```oracle
SELECT A.ANIMAL_ID, A.NAME
  FROM ANIMAL_INS  A,
       ANIMAL_OUTS B
 WHERE A.ANIMAL_ID = B.ANIMAL_ID
   AND A.DATETIME > B.DATETIME
 ORDER BY A.DATETIME
```



### 오랜 기간 보호한 동물(1)

```oracle
SELECT NAME, DATETIME
  FROM (
    SELECT A.NAME, A.DATETIME
      FROM ANIMAL_INS  A
          ,ANIMAL_OUTS B
     WHERE A.ANIMAL_ID = B.ANIMAL_ID(+)
       AND B.DATETIME IS NULL
     ORDER BY A.DATETIME
  )
 WHERE ROWNUM <= 3
```

> row 개수를 제한할 때 MySQL 에서는 LIMIT을 쓰지만 Oracle에서는 ROWNUM을 사용하면 된다.
>
> (주의) 단, rownum은 쿼리가 모두 마친 테이블에 대해서 사용해야 원하는 결과가 나온다.



### 오랜 기간 보호한 동물(2)

```oracle
SELECT ANIMAL_ID, NAME
  FROM (
    SELECT A.ANIMAL_ID, A.NAME, RANK() OVER(ORDER BY B.DATETIME - A.DATETIME DESC) AS R
      FROM ANIMAL_INS A,
           ANIMAL_OUTS B
     WHERE A.ANIMAL_ID = B.ANIMAL_ID
     )
 WHERE R <= 2
```



### 헤비 유저가 소유한 장소

```oracle
SELECT *
  FROM PLACES
 WHERE HOST_ID IN (
     SELECT HOST_ID 
       FROM PLACES 
      GROUP BY HOST_ID 
     HAVING COUNT(*) > 1)
 ORDER BY ID
```



