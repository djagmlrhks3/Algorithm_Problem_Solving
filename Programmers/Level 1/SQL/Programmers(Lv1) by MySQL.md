# Programmers(Lv1) by MySQL

### 모든 레코드 조회하기

```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```

- ORDER BY를 그대로 적용하면 오름차순이다. - ASC 생략

  ```sql
  ORDER BY column ASC;
  ```

- 내림차순 정렬은 DESC를 적어줘야 한다.

  ```sql
  ORDER BY column DESC;
  ```



### 최댓값 구하기

> MAX(column) AS "String"

```sql
SELECT MAX(DATETIME) AS "시간"
FROM ANIMAL_INS;
```

> LIMIT

```sql
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;
```



### 역순 정렬하기

```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```



### 아픈 동물 찾기

```sql
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = "Sick"
ORDER BY ANIMAL_ID;
```



### 어린 동물 찾기

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged"
ORDER BY ANIMAL_ID;
```



### 동물의 아이디와 이름

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### 이름이 없는 동물의 아이디

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;
```

- WHERE에서 특정 값의 일치여부를 판단할 때 `=` , `!=` 를 사용하면 된다.
- 반면, NULL의 경우에는 `IS NULL`, `IS NOT NULL` 을 사용하면 된다.



### 여러 기준으로 정렬하기

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```



### 상위 n개 레코드

```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```



### 이름이 있는 동물의 아이디

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;
```
