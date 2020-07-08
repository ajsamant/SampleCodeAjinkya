select * from actor
order by actor_id asc;

select * from actor
where first_name like 'An%'
order by first_name,last_name desc;