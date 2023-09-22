USE sherlock;

SELECT s.first_name, s.last_name, a.address, a.district, c.city, a.postal_code
FROM staff s
JOIN address a ON a.address_id = s.address_id
JOIN city c ON c.city_id = a.city_id;

SELECT i.inventory_id, f.title, i.store_id
FROM inventory i
left join film  f on i.film_id = f.film_id;

SELECT * FROM staff, store;

SELECT film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate,
length, replacement_cost, rating, special_features
FROM film
group by film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate,
length, replacement_cost, rating, special_features
having count(*) > 1;

select release_year, name as film_language, sum(replacement_cost) as sum_replacement_cost from (
SELECT film_id, title, description, release_year, l.name, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features
FROM film f
join language l on f.language_id = l.language_id) a
group by release_year, name
order by sum_replacement_cost desc;

SELECT release_year, rental_rate,
DENSE_RANK() OVER (PARTITION BY release_year ORDER BY rental_rate) AS rnk
FROM film;

