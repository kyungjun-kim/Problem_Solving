# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131536

SELECT USER_ID, product_id
FROM ONLINE_SALE 
GROUP BY USER_ID, product_id
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC