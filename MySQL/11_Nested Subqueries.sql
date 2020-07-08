select title from film_text
where film_id=2;

select * from actor
where actor_id IN
(select actor_id from film_actor
where film_id = 2);

select * from actor
where actor_id IN
	(select actor_id from film_actor
	where film_id = 
		(select film_id from film
		where title = 'ACE GOLDFINGER') );