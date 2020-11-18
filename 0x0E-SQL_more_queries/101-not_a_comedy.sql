-- Lists all genres that are not of the show Dexter
-- Display: tv_genres.name
SELECT title
FROM tv_shows
WHERE title NOT IN (
    SELECT tv_shows.title
    FROM tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = "Comedy"
    )
ORDER BY title
