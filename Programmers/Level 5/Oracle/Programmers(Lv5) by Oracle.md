# Programmers(Lv5) by Oracle



### 상품을 구매한 회원 비율 구하기

```SQL
SELECT YEAR, TO_NUMBER(MONTH), USERS PURCHASED_USERS
      ,ROUND(USERS/(SELECT COUNT(*) FROM USER_INFO WHERE TO_CHAR(JOINED, 'YYYY') = '2021'), 1)
  FROM (SELECT TO_CHAR(B.SALES_DATE, 'YYYY') YEAR
              ,TO_CHAR(B.SALES_DATE, 'MM') MONTH
              ,COUNT(DISTINCT B.USER_ID) USERS
          FROM USER_INFO A
              ,ONLINE_SALE B
         WHERE A.USER_ID = B.USER_ID
           AND TO_CHAR(A.JOINED, 'YYYY') = '2021'
         GROUP BY TO_CHAR(B.SALES_DATE, 'YYYY'), TO_CHAR(B.SALES_DATE, 'MM'))
 ORDER BY 1, 2
```
