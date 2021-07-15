-- import the database dump from hbtn_0d_tvshows

SELECT tv_genres.name AS 'gen',COUNT(tv_show_genres.genre_id) AS 'numshows' FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY gen
ORDER BY numshows DESC;
