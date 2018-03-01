-- Lists all genres by their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating 
FROM tv_genres 
INNER JOIN tv_show_ratings ON tv_genres.id=tv_show_ratings.rate 
GROUP BY tv_genres.name
ORDER BY rating DESC;
