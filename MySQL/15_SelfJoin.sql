#self join with inner join
select a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name from customer a
inner join customer b on a.last_name = b.first_name;

#left join with inner join
select a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name from customer a
left join customer b on a.last_name = b.first_name
order by a.customer_id;

#right join with inner join
select a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name from customer a
right join customer b on a.last_name = b.first_name
order by b.first_name;
