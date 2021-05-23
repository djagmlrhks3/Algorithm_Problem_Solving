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

```oracle
select I.ANIMAL_ID, I.NAME
from ANIMAL_INS I
left outer join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
where O.DATETIME < I.DATETIME
order by I.DATETIME
```



### 오랜 기간 보호한 동물(1)

```oracle
select *
from (
    select I.NAME, I.DATETIME
    from ANIMAL_INS I
    left outer join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
    where O.DATETIME IS NUll
    order by I.DATETIME
)
where rownum <= 3
```

> row 개수를 제한할 때 MySQL 에서는 LIMIT을 쓰지만 Oracle에서는 ROWNUM을 사용하면 된다.
>
> (주의) 단, rownum은 쿼리가 모두 마친 테이블에 대해서 사용해야 원하는 결과가 나온다.



### 오랜 기간 보호한 동물(2)

```oracle
select *
from (
    select I.ANIMAL_ID, I.NAME
    from ANIMAL_INS I
    left join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
    where O.DATETIME is not null
    order by O.DATETIME - I.DATETIME desc
    )
where rownum <= 2
```



### 헤비 유저가 소유한 장소

```oracle
select ID, NAME, HOST_ID
from PLACES
where HOST_ID IN (
    select HOST_ID
    from PLACES
    group by HOST_ID
    having count(*) >= 2
)
ORDER BY ID;
```



