#use for disable safe mode in sql
set sql_safe_updates = 0;
#use for enable safe mode in sql
set sql_safe_updates = 1;

select * from fruits;

Delete from fruits
where fruit_name = 'banana';

#adding banana again
INSERT INTO fruits
VALUES
(7,'Banana',20,6,'2018-08-17 13:30:00','2018-08-17 13:30:00');

