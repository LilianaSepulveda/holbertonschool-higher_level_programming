-- Lists all shows from hbtn_0d_tvshows_rate by their rating

SELECT title, SUM(rate) AS rating
FROM tv_shows AS shows
INNER JOIN tv_show_ratings AS s_rating
ON shows.id = s_rating.show_id
GROUP BY title
ORDER BY rating DESC;
