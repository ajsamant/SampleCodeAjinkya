select last_name from actor
group by last_name limit 10;

select last_name, count(*) from actor
group by last_name limit 10;