# Programmers(Lv4) by Oracle

### 우유와 요거트가 담긴 장바구니

```oracle
select CART_ID
from CART_PRODUCTS
where NAME in ('Milk', 'Yogurt')
group by CART_ID
having count(distinct NAME) >= 2
order by CART_ID
```



### 입양 시각 구하기(2)

```mysql

```



### 보호소에서 중성화한 동물

```oracle
select I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
from ANIMAL_INS I
left outer join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
where (I.SEX_UPON_INTAKE not like '%Spayed%' and I.SEX_UPON_INTAKE not like '%Neutered%') and (O.SEX_UPON_OUTCOME like '%Spayed%' or O.SEX_UPON_OUTCOME like '%Neutered%')
order by I.ANIMAL_ID
```



