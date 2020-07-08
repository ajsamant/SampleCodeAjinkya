SELECT COUNT(*) FROM film;

SELECT COUNT(film_id)
from film where replacement_cost > 27;

SELECT distinct rental_duration from film;

SELECT count(distinct rental_duration) from film;