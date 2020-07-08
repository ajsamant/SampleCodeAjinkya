SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    a.actor_id,
    a.first_name,
    a.last_name
FROM
    customer c
        RIGHT JOIN
    actor a ON c.last_name = a.last_name
ORDER BY a.last_name;
