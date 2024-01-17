-- Script to list all genres not linked to the show Dexter from the hbtn_0d_tvshows database

SELECT name
FROM genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE title = 'Dexter'
)
ORDER BY name ASC;
