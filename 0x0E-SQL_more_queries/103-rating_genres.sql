-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT name, SUM(rate) AS rating
FROM tv_genres AS gen
INNER JOIN tv_show_genres AS s_gen
       ON s_gen.genre_id = gen.id

       INNER JOIN tv_show_ratings AS s_rating
       ON s_rating.show_id = s_gen.show_id
 GROUP BY name
 ORDER BY rating DESC;
