#use for disable safe mode in sql
set sql_safe_updates = 0;
#use for enable safe mode in sql
set sql_safe_updates = 1;


select * from fruits;

update fruits
set unit_id = 2
where fruit_name = 'Orange' and unit_id = 5;


