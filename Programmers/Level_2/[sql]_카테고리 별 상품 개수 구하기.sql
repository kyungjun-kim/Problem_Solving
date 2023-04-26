# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59046

SELECT LEFT(PRODUCT_CODE, 2) CATEGORY , COUNT(PRODUCT_ID) PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY