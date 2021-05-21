# Programmers(Lv3) by MySQL

### 없어진 기록 찾기

```oracle
select O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS O
left join ANIMAL_INS I on I.ANIMAL_ID = O.ANIMAL_ID
where I.DATETIME is null
order by O.ANIMAL_ID;
```



### 있었는데요 없었습니다

```mysql

```



### 오랜 기간 보호한 동물(1)

```mysql

```



### 오랜 기간 보호한 동물(2)

```mysql

```