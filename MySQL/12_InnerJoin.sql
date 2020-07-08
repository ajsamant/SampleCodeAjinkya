select city, country from city
INNER JOIN country ON city.country_id = country.country_id;

# with alias define a for city and b for country
select city, country from city a
INNER JOIN country b ON a.country_id = b.country_id;

# using group by clause 
select country, count(city) from country a
INNER JOIN city b ON a.country_id = b.country_id
group by country;