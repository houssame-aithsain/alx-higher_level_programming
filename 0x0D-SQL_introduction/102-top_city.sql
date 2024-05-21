-- Show the top 3 cities with the highest average temperature in July and August.
SELECT city, avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY avg_temp DESC
LIMIT 3;
