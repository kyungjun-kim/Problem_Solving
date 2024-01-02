# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/59040

SELECT ANIMAL_TYPE, COUNT(*) as count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE in ('Dog', 'Cat')
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC