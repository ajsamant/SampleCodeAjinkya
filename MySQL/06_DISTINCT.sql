 SELECT first_name
 from actor
 where first_name like 'An%';
 
SELECT distinct first_name
from actor
where first_name like 'An%';

SELECT count(distinct first_name)
from actor
where first_name like 'An%';

SELECT distinct first_name, last_name
from actor
where first_name like 'An%';