# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131534

SELECT DATE_FORMAT(sales_date,'%Y') YEAR, CAST(DATE_FORMAT(sales_date,'%m') AS UNSIGNED) MONTH
, COUNT(DISTINCT OS.USER_ID) "PUCHASED_USERS"
, ROUND(COUNT(DISTINCT OS.USER_ID) 
        / (SELECT COUNT(USER_ID)
    FROM USER_INFO UI
    WHERE DATE_FORMAT(JOINED,'%Y') = 2021),1) "PUCHASED_RATIO"
FROM USER_INFO UI
JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
WHERE LEFT(JOINED,4) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH