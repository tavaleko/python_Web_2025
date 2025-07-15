# Базовый синтаксис
# SELECT перчень полей
# FROM имя_
# WHERE условия
# ORDER BY

# # выборка по году выпуска всех параметров
# SELECT *
# FROM films
# WHERE year = 2010
# # выборка по названию фильма
# SELECT title
# FROM films
# WHERE year = 2010

# SELECT title
# FROM films
# WHERE year > 2005

# SELECT title
# FROM films
# WHERE year > 2005 AND year <2007

# SELECT title
# FROM films
# WHERE year > 2005 AND year <2007 and duration <90 # не чуствителен к регистру
#
# SELECT title,year
# FROM films
# WHERE year > 2005 AND year <2010 and duration <90

# SELECT title,year
# FROM films
# WHERE year > 2005 AND year <2010 and duration <90
# ORDER BY year # сортировка от меньшего к большему

# SELECT title,year
# FROM films
# WHERE year BETWEEN 2005 and 2010 выборка с битвин

# (пример не коректного запроса)
SELECT title,year FROM films
WHERE genres = 8

# исправили запрос

SELECT title,year FROM films
WHERE genres =(
SELECT id FROM genres
WHERE title = 'ужасы')
# выборка по перечню ключевых значений
SELECT title,duration FROM films
WHERE duration IN (45,60,90)

SELECT title,duration FROM films
WHERE duration IN (45,60,90)
order by duration desc
 
# выборка  с групировкой по id
SELECT * FROM films
WHERE year >= 2005
and duration between 45 and 90
group by id

# выбрать с LIKE

SELECT title FROM films
WHERE title LIKE 'А_к%'
% любое количество символов от 0
_ любой символ

# не похожие not like
SELECT title FROM films
WHERE title NOT LIKE 'А_к%' 
# вывести все уникальные года Disting удет без повторение
SELECT DISTINCT year FROM films

Примечание: 
DISTING

# из одной базы вытащили названия фильмов из другой жанры и объеднеини с помощью join
SELECT 
films.title as фильм,
genres.title as Жанр
FROM  films
JOIN genres
Where films.genre = genres.id
# тоже самое join можно не писать выведет тоже самое только нужна запятая
SELECT 
films.title as фильм,
genres.title as Жанр
FROM  films, genres
Where films.genre = genres.id
# выведет количество фильмов в каком году было произведено в 1996 году их вышло 938
SELECT year, count(*) as Кол_во
FROM films
Group by year
order by Кол_во desc
# выведет кол во фильмов в каких годах и более 500 в год
SELECT year, count(*) as Кол_во
FROM films
Group by year HAVING >500
order by Кол_во desc
 # добавление через sql
# INSERT INTO
# users(name, age)
# VALUES('Bill',21)
# насколько одновременно
# INSERT INTO
# users(name, age)
# VALUES('TOM',20),
# ('Tim',41)
# меняем параметры лучше по id  так как других параметров может быть насколько
# UPDATE users
# SET age =22
# WHERE id = 2
# удобно по названию фирмы что то нужно поменять сколпом
# удаляет таблицу
drop table users if exists

# добавим новый столбец
alter table ysers
add  colums