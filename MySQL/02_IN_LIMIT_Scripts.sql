SELECT 
    title, release_year, rental_duration
FROM
    film
WHERE
    rental_duration IN (3 , 5)
LIMIT 7;

SELECT title FROM film LIMIT 7;