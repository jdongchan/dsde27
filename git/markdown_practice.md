# [프로그래머스] 상품을 구매한 회원 비율 구하기
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131534)
## 문제
`USER_INFO` 테이블과 `ONLINE` 테이블에서 2021년에 가입한 전체 회원들 중 상품을 구매한 회원의 비율 (=2021년에 가입한 전체 회원 수)을 년, 월 별로 출력하는 SQL문을 작성해주세요. 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬해주세요.

---
## 문제 해석
2021년에 가입한 회원 중 상품을 구매한 회원 수 / 2021년에 가입한 전체 회원 수를 년, 월 별로 출력하는 문제이다. 문제를 이해하는 데에 어려움은 없었으므로 비교적 빠른 시간에 풀게 되었다. `USER_INFO` 테이블의 2021년에 가입한 회원을 조건으로 하여 `ONLINE_SALES` 테이블의 회원 수를 구한 후에 `USER_INFO` 테이블의 가입한 회원 수로 나누어주면 되는 문제이다.

---

## 문제 해결과정
먼저, 2021년에 가입한 회원을 조건으로 설정하여 쿼리를 작성한다.

```SQL
SELECT *
FROM USER_INFO
WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31'
```
이 때, WHERE절에 사용한 `BETWEEN`은 >= '2021-01-01, <= '2021-12-31'을 의미하여 두 날짜를 모두 포함한다.

그리고, 2021년에 가입한 회원의 상품구매내역의 쿼리를 작성한다. WHERE절 서브쿼리를 사용하여 2021년에 가입한 유저의 구매내역을 출력하도록 하였다.

```SQL
-- 2021년에 가입한 유저가 구매한 내역
SELECT *
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                  FROM USER_INFO
                  WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31')
```
한번에 작성하지 않고 이렇게 나누어 작성하는 이유는 쿼리 작성을 하다 꼬이는 경우에도 쉽게 되돌아갈 수 있기 때문이다. 일종의 `SAVEPOINT`를 설정하는 작업이라고 할 수 있다.

그리고나서, `GROUP BY`를 통해 위 코드를 연별, 월별로 나누어 회원 수를 세어준다.

```SQL
-- 상품을 구매한, 2021년에 가입한, 연별 월별 회원 수
SELECT EXTRACT(YEAR FROM SALES_DATE) AS 'YEAR'
     , EXTRACT(MONTH FROM SALES_DATE) AS 'MONTH'
     , COUNT(DISTINCT USER_ID)
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                  FROM USER_INFO
                  WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31')
GROUP BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE);
````
마지막으로 첫 번째 만들었던 쿼리를 SELECT절 서브쿼리로 하여 나눠주면 끝!

```SQL
SELECT EXTRACT(YEAR FROM SALES_DATE) AS 'YEAR'
     , EXTRACT(MONTH FROM SALES_DATE) AS 'MONTH'
     , COUNT(DISTINCT USER_ID) AS 'PURCHASED_USERS'
     , ROUND(COUNT(DISTINCT USER_ID) / 
       (SELECT COUNT(DISTINCT USER_ID) AS ‘JOINED_CNT_2021’
        FROM USER_INFO
        WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31'),1) AS 'PURCHASED_RATIO'
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                  FROM USER_INFO
                  WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31')
GROUP BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE)
ORDER BY 1 ASC, 2 ASC;
```
WITH 서브쿼리를 통해 예쁘게 만들 수 있지만, 이 정도는 SELECT절에 포함하여도 전체 쿼리를 해석하는 데에 무리가 없다고 판단했다. 마지막으로, 비율을 소수 1자리까지 반올림하고, 연, 월로 정렬을 하면 완료.

## 실행결과

| YEAR | MONTH | PURCHASED_USERS | PURCHASED_RATIO |
|------|------|------|------|
|2022|1|47|0.3|
|2022|2|48|0.3|
|2022|3|6|0.0|