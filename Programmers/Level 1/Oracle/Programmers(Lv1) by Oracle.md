# Programmers(Lv1) by Oracle

### 모든 레코드 조회하기

```oracle
select * 
from animal_ins 
order by animal_id;
```



### 이름이 없는 동물의 아이디

```oracle
select animal_id
from animal_ins
where name is null
order by animal_id;
```



### 최댓값 구하기

```oracle
select max(DATETIME) as 시간
from ANIMAL_INS;
```



### 이름이 있는 동물의 아이디

```oracle
select animal_id
from animal_ins
where name is not null
order by animal_id;
```



### 역순 정렬하기

```oracle
select NAME, DATETIME
from ANIMAL_INS
order by ANIMAL_ID desc;
```



### 아픈 동물 찾기

```oracle
select ANIMAL_ID, NAME 
from ANIMAL_INS 
where INTAKE_CONDITION = 'Sick' 
order by ANIMAL_ID;
```



### 어린 동물 찾기

```oracle
select ANIMAL_ID, NAME
from ANIMAL_INS
where INTAKE_CONDITION != 'Aged'
order by ANIMAL_ID;
```



### 동물의 아이디와 이름

```oracle
select ANIMAL_ID, NAME
from ANIMAL_INS
order by ANIMAL_ID;
```



### 여러 기준으로 정렬하기

```oracle
select ANIMAL_ID, NAME, DATETIME 
from ANIMAL_INS
order by NAME asc, DATETIME desc;
```



### 상위 n개 레코드

> MySQL에는 LIMIT가 있지만 Oracle에는 없다.
>
> Oracle은 자동으로 생성되는 rownum을 이용하면 된다.
>
> 하지만 order by는 where을 선행할 수 없으므로 서브쿼리를 이용하여 해결!

```oracle
select NAME
from (
select *
from ANIMAL_INS
order by DATETIME
)
where rownum = 1;
```





