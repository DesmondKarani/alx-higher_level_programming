-- Script to list all genres and the number of shows linked to each from the hbtn_0d_tvshows database

SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;
