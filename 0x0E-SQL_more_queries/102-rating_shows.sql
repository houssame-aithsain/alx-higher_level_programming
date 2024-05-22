-- 102-rating_shows.sql
-- Show the title and rating of all TV shows, ordered by rating in descending order.
SELECT t.title, SUM(r.rate) AS rating
FROM tv_shows t
INNER JOIN tv_show_ratings r ON t.id = r.show_id
GROUP BY t.title
ORDER BY rating DESC;
