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



### 조건별로 분류하여 주문상태 출력하기

```Oracle
SELECT ORDER_ID
      ,PRODUCT_ID
      ,TO_CHAR(OUT_DATE, 'YYYY-MM-DD')
      ,CASE WHEN TO_CHAR(OUT_DATE, 'YYYYMMDD') <= '20220501' THEN '출고완료'
            WHEN TO_CHAR(OUT_DATE, 'YYYYMMDD') >  '20220501' THEN '출고대기'
            ELSE '출고미정'
            END 출고여부
  FROM FOOD_ORDER
  ORDER BY 1
```



### 즐겨찾기가 가장 많은 식당 정보 출력하기

```Oracle
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
  FROM REST_INFO
 WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) FAVORITES
                                    FROM REST_INFO
                                GROUP BY FOOD_TYPE)
 ORDER BY 1 DESC
```



### 카테고리 별 도서 판매량 집계하기

```Oracle
SELECT A.CATEGORY, SUM(B.SALES) TOTAL_SALES
  FROM BOOK A
      ,BOOK_SALES B
 WHERE A.BOOK_ID = B.BOOK_ID
   AND TO_CHAR(B.SALES_DATE, 'YYYYMM') = '202201'
 GROUP BY A.CATEGORY
 ORDER BY 1
```

