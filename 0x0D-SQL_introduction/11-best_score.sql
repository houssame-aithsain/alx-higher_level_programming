-- Show the best score and the name of the student who got it, only if the score is greater than or equal to 10, ordered from highest to lowest score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
