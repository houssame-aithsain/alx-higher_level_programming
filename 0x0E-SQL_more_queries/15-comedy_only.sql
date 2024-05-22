-- Show the title of all comedies in the database, sorted in ascending order.
SELECT t.title
  FROM tv_shows AS t
       INNER JOIN tv_show_genres AS poi
       ON t.id = poi.show_id
       INNER JOIN tv_genres AS coi
       ON coi.id = poi.genre_id
       WHERE coi.name = "Comedy"
 ORDER BY t.title;
