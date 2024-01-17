-- Script to list all genres and the number of shows linked to each from the hbtn_0d_tvshows database

SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.id, g.name
HAVING COUNT(sg.show_id) > 0
ORDER BY COUNT(sg.show_id) DESC;
