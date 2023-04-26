# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131530

SELECT TRUNCATE(PRICE/ 10000 , 0)*10000 PRICE_GROUP, COUNT(*) PRODUCTS
FROM product P
GROUP BY TRUNCATE(PRICE/ 10000 , 0)
ORDER BY PRICE_GROUP