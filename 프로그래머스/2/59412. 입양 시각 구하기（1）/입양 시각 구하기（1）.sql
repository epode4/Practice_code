-- 코드를 입력하세요
SELECT  
CASE WHEN hour < 10
THEN (A.hour % 10)
ELSE A.hour
END AS HOUR,
A.COUNT
FROM (
    SELECT DATE_FORMAT(DATETIME,'%H') AS hour, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY hour
    ORDER BY hour
) A
WHERE hour >= 9 AND hour < 20