-- Script to list all genres not linked to the show Dexter from the hbtn_0d_tvshows database

SELECT g.name
FROM genres g
WHERE g.id NOT IN (
    SELECT sg.genre_id
    FROM tv_show_genres sg
    JOIN tv_shows s ON s.id = sg.show_id
    WHERE s.title = 'Dexter'
)
ORDER BY g.name;
