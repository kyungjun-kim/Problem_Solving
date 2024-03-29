# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/151138
SELECT HISTORY_ID,CAR_ID, LEFT(START_DATE,10) START_DATE, LEFT(END_DATE,10) END_DATE
, CASE WHEN DATEDIFF(END_DATE,START_DATE) +1 >= 30 THEN '장기 대여' ELSE '단기 대여' END RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE LEFT(START_DATE,7) = "2022-09"
ORDER BY HISTORY_ID DESC