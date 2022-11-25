# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(*)
FROM ANIMAL_INS
GROUP BY NAME   HAVING COUNT(NAME) >= 2
ORDER BY NAME ASC