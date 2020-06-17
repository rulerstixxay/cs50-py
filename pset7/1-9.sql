1.sql
SELECT title FROM movies WHERE year = 2008;

2.sql
SELECT birth FROM people WHERE name = "Emma Stone";

3.sql
SELECT title FROM movies WHERE year >= 2018
ORDER BY title ASC;

4.sql
SELECT COUNT(*)title FROM movies WHERE id IN (SELECT movie_id FROM ratings WHERE rating = 10.0);

4.1.sql
SELECT COUNT(*)title FROM movies JOIN
ratings ON movies.id = ratings.movie_id WHERE rating = 10.0;

5.sql
SELECT title, year FROM movies WHERE title LIKE "Harry Potter%"
ORDER BY year ASC;

6.sql
SELECT AVG(rating) FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year = 2012;

7.sql
SELECT title, rating FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2010
ORDER BY rating ASC, title ASC;

8.sql
SELECT name from people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title = "Toy Story";

8.1.sql
SELECT name FROM people WHERE id IN (SELECT person_id FROM stars
WHERE movie_id = (SELECT id FROM movies WHERE title = "Toy Story"));

9.sql
SELECT DISTINCT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.person_id = movies.id
WHERE year = 2004
ORDER BY birth ASC;
