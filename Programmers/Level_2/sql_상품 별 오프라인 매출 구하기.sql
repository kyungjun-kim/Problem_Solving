# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131533

SELECT PRODUCT_CODE, SUM(price * SALES_AMOUNT) SALES
FROM PRODUCT P
INNER JOIN OFFLINE_SALE OS ON P.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC