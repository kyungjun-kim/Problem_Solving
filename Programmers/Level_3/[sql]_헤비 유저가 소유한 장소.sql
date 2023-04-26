-- 코드를 입력하세요
SELECT *
from PLACES
Where HOST_ID in (
    Select Host_ID
    From PLACES
    GROUP BY HOST_ID
    HAVING COUNT(ID) > 1)
order by ID