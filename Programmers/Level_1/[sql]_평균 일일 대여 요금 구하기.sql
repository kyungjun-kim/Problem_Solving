# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/151136

SELECT ROUND(AVG(DAILY_FEE),0) AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR T
WHERE T.CAR_TYPE ='SUV'
