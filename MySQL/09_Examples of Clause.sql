SELECT 
    c.customer_id AS 'Customer ID',
    c.first_name AS 'First Name',
    c.last_name AS 'Last Name',
    SUM(amount) AS 'Total Paid'
FROM
    sakila.payment p
        INNER JOIN
    customer c ON p.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING SUM(amount) > 180
ORDER BY SUM(amount) DESC;