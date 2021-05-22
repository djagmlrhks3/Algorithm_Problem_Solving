# Programmers(Lv2) by Oracle

### 최솟값 구하기

```oracle
select DATETIME as 시간
from (
    select DATETIME
    from ANIMAL_INS
    order by DATETIME
)
WHERE rownum = 1
```



### 동물 수 구하기

```oracle
select count(*) as count
from ANIMAL_INS
```



### 중복 제거하기

```oracle
select count(distinct name) as count
from ANIMAL_INS
where NAME is not null
```



### 고양이와 개는 몇 마리 있을까

```oracle
select ANIMAL_TYPE, count(*) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE
```

* GROUP BY : 컬럼 값(ANIMAL_TYPE)이 같은 것 끼리 하나로 묶어준다.



### NULL 처리하기

```oracle
select ANIMAL_TYPE, nvl(NAME, 'No name') as NAME, SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID
```

* NVL(컬럼명, 바꿀 값)



### 동명 동물 수 찾기

```oracle
select NAME, count(*)
from ANIMAL_INS
where NAME is not null
group by NAME
HAVING COUNT(*) > 1
order by NAME	
```



### 입양 시각 구하기(1)

```oracle
select hour, count(*) as count
from (
    select to_char(DATETIME, 'HH24') as hour
    from ANIMAL_OUTS
)
group by hour
having hour between 9 and 20
order by hour
```



> 'HH24' 옵션으로 시간 값을 얻을 수 있다.



### 루시와 엘라 찾기

```oracle
select ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by ANIMAL_ID
```



### 이름에 el이 들어가는 동물 찾기

```oracle
select ANIMAL_ID, NAME
from ANIMAL_INS
where lower(name) like '%el%' and ANIMAL_TYPE = 'Dog'
order by name
```

* Oracle에서 대소문자를 구별하는 방법은 모든 문자를 소문자 또는 대문자로 바꾼 후에 비교한다.



### 중성화 여부 파악하기

```oracle
select ANIMAl_ID, NAME, case
    when SEX_UPON_INTAKE like '%Neutered%' then 'O'
    when SEX_UPON_INTAKE like '%Spayed%' then 'O'
    else 'X'
    end
    as 중성화
from ANIMAL_INS
order by ANIMAL_ID
```

* case문 사용

> CASE 
>
> WHEN 조건 THEN 결과 값
>
> WHEN 조건 THEN 결과 값
>
> ELSE 조건이 아닌 경우
>
> END



### DATETIME에서 DATE로 형 변환

```oracle
select ANIMAL_ID, NAME, to_char(datetime, 'yyyy-mm-dd') as 날짜
from ANIMAL_INS
order by ANIMAL_ID;
```

