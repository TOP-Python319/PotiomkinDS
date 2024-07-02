SELECT
	name,
	year,
	appearances 
FROM
	MarvelCharacters
WHERE
	HAIR = 'Bald' and
	ALIGN = 'Bad Characters' and
	year BETWEEN 1990 and 1999;

2.	
SELECT
	name,
	year,
	eye 
FROM
	MarvelCharacters
WHERE
	identify = 'Secret Identity' AND 
	eye != 'Blue Eyes' and eye != 'Brown Eyes' and eye != 'Green Eyes';

3.	
SELECT
	name,
	HAIR 
FROM
	MarvelCharacters
WHERE
	hair = 'Variable Hair';

4.	
SELECT
	name,
	EYE 
FROM
	MarvelCharacters
WHERE
	eye in ('Gold Eyes', 'Amber Eyes') and 
	sex = 'Female Characters';
	
5.
SELECT
	name,
	FIRST_APPEARANCE 
FROM
	MarvelCharacters
WHERE
	identify = 'No Dual Identity'
order by 
	year DESC;

6.
SELECT 
	name,
	align,
	hair
FROM MarvelCharacters	
WHERE
	ALIGN in ('Good Characters', 'Bad Characters') AND
	hair not in ('Brown Hair', 'Blond Hair', 'Black Hair', 'Red Hair', 'null');
	
7.
SELECT 
	name,
	YEAR 
FROM
	MarvelCharacters
WHERE 
	year BETWEEN 1960 and 1969;
	
8.
SELECT 
	name,
	eye,
	hair
FROM
 	MarvelCharacters
 WHERE 
 	eye = 'Yellow Eyes' AND 
 	HAIR = 'Red Hair'; 
 	
 9.
 SELECT 
 	name,
 	appearances
 FROM
 	MarvelCharacters
 WHERE 
 	APPEARANCES < 10;
 	
 10.
 SELECT 
 	name,
 	appearances
 FROM
 	MarvelCharacters
 WHERE 
 	APPEARANCES is not null
 ORDER by APPEARANCES DESC 
 LIMIT 5;
 
11.
SELECT 
	name,
	year
FROM
	MarvelCharacters
WHERE 
	YEAR BETWEEN 2000 and 2009;
	
12.
SELECT 
	name,
	eye
FROM
	MarvelCharacters
WHERE 
	eye in ('Magenta Eyes', 'Pink Eyes', 'Violet Eyes');
	
13.
SELECT 
	name,
	identify ,
	YEAR 
FROM
	MarvelCharacters
WHERE 
	identify = 'Public Identity' 
ORDER BY YEAR ASC; 

14.
SELECT 
	name,
	hair,
	eye
FROM
	MarvelCharacters
WHERE 
	HAIR = 'Black Hair' AND 
	eye = 'Green Eyes' 
ORDER BY name; 

15.
SELECT  
	name,
	sex
FROM
	MarvelCharacters
WHERE 
	ALIGN = 'Bad Characters' AND 
	sex not in ('Male Characters', 'Female Characters');
	
16. 
SELECT 
	name,
	appearances,
	sex
FROM 
	MarvelCharacters
WHERE 
	sex in ('Male Characters', 'Female Characters')
GROUP BY SEX 
ORDER BY APPEARANCES DESC 
LIMIT 2;

17.
SELECT 
	hair,
	eye,
	sum(APPEARANCES) 
FROM 
	MarvelCharacters
WHERE 
	HAIR is not null AND 
	eye is not null AND 
	APPEARANCES is not null
GROUP BY 
	hair,
	eye;
	
18.
SELECT 
	name,
	max(appearances),
	decade
FROM (select name, appearances, (year / 10) * 10 as decade
		from MarvelCharacters
	WHERE year is not null)
WHERE 
	decade BETWEEN 1940 and 2013
GROUP BY decade
ORDER BY decade
19.
SELECT 
	ALIGN, 
	YEAR, 
	COUNT(*) as cnt
FROM
	MarvelCharacters
WHERE 
	ALIGN in ('Good Characters', 'Bad Characters') AND 
	year BETWEEN 1980 and 1989
GROUP BY 
	ALIGN,
	YEAR;
	
20.
SELECT 
	hair,
	sum(appearances)
FROM
	MarvelCharacters
WHERE 
	hair is not null 
GROUP BY HAIR 
ORDER BY APPEARANCES DESC 
limit 3;