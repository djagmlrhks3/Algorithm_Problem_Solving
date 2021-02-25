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

