SELECT COUNT(FISH_NAME) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO AS F1, FISH_NAME_INFO AS F2
WHERE F1.FISH_TYPE = F2.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC