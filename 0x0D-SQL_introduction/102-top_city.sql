-- Script to display top 3 cities with highest average temperature in July and August
SELECT city, AVG(value) AS avg_temp 
FROM temperatures 
WHERE MONTH(record_date) IN (7, 8)  -- 7 and 8 represent July and August
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3;
