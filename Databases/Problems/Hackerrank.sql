-- -------------------------------SELECT----------------------------------

-- Q)Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
-- The CITY table is described as follows:
-- Ans
SELECT * FROM city WHERE countrycode = 'USA' AND population > 100000;
-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND population > 120000;
-- Query all columns(matlab *) (attributes) for every row in the CITY table.
SELECT * FROM CITY;
-- Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY WHERE ID = 1661;
-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';
-- Query a list of CITY and STATE from the STATION table.The STATION table is described as follows:
SELECT CITY , STATE FROM STATION;
-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
SELECT DISTINCT CITY FROM STATION WHER MOD[ID,2]=0;
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2)=0 ORDER BY CITY ASC;       
-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;
-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
select city, length(city) from station order by length(city) DESC,city ASC fetch first row only;
select city, length(city) from station order by length(city) asc ,city asc fetch first row only;     
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT(CITY) FROM STATION WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' 
OR CITY LIKE 'U%' ORDER BY CITY ASC; 
-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, -1, 1)) IN ('a', 'e', 'i', 'o', 'u') ORDER BY CITY;
-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u') AND LOWER(SUBSTR(CITY, -1)) IN ('a', 'e', 'i', 'o', 'u') ORDER BY CITY;
-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates. 
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u') OR
LOWER(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY, 1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u') AND
LOWER(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
-- Query the Name of any student in STUDENTS who scored higher than 75  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY SUBSTR(NAME. LENGTH(NAME),-2,3), ID;
-- Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
SELECT NAME FROM EMPLOYEE ORDER BY NAME;
-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than 2000 per month who have been employees for less than  months. Sort your result by ascending employee_id
SELECT NAME FROM EMPLOYEE WHERE SALARY > 2000 AND MONTH < 10 ORDER BY EMPLOYEE_ID;
-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
-- Equilateral: It's a triangle with  sides of equal length.
-- Isosceles: It's a triangle with  sides of equal length.
-- Scalene: It's a triangle with  sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.
SELECT CASE
WHEN A = B AND B = C THEN 'Equilateral'
WHEN A = B OR B = C OR A = C THEN 'Isosceles'
WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
ELSE 'Scalene'
END
FROM TRIANGLES;

-- --------------------------AGGREGATIONS FUNVTIONS ----------------------------------
-- Query a count of the number of cities in CITY having a Population larger than .
SELECT COUNT(POPULATION) FROM CITY WHERE POPULATION > 100000;
-- Query the total population of all cities in CITY where District is California.
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';
-- Query the average population of all cities in CITY where District is California.
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';
-- Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT FLOOR(AVG(POPULATION)) FROM CITY;
-- Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';
-- Query the difference between the maximum and minimum populations in CITY.
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY;
-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 00 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.
-- Write a query calculating the amount of error (i.e.: actual−miscalculated average monthly salaries), and round it up to the next integer.
SELECT CEIL(AVG(SALARY)) - AVG(REPLACE(SALARY,'0','')) AS ERROR FROM EMPLOYEE;
-- Notes:-where CEIL/ceiling difference between two salary round up using 'CEIL' function for final result.
-- We define an employee's total earnings to be their monthly salary*months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
-- SELECT MAX(salary * months), COUNT(*)
-- FROM Employee
-- WHERE salary * months = (SELECT MAX(salary * months) FROM Employee);
select months*salary, count(*) from employee group by months*salary order by months*salary desc limit 1;
-- Query the following two values from the STATION table:
-- The sum of all values in LAT_N rounded to a scale of  decimal places.
-- The sum of all values in LONG_W rounded to a scale of  decimal places.
SELECT ROUND(SUM(LAT_N), 2),ROUND(SUM(LONG_W), 2) FROM STATION;
-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880  and less than 137.2345. Truncate your answer to  decimal places.
SELECT ROUND(SUM(lAT_N), 4) FROM STATION WHERE LAT_N>38.7880 AND LAT_N < 137.2345;
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345 . Truncate your answer to 4 decimal places. 
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345;
-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to  4 decimal places.
SELECT ROUND(LONG_W,4) FROM STATION WHERE LAT_N<137.2345 ORDER BY LAT_N DESC LIMIT 1;
-- SELECT: This keyword specifies that we are retrieving data from the database.
-- SELECT ROUND(LONG_W, 4)
-- SELECT: This keyword specifies that we are retrieving data from the database.
-- ROUND(LONG_W, 4): This function rounds the value in the LONG_W column to 4 decimal places.
-- FROM STATION
-- FROM: Indicates that we are selecting data from the STATION table.
-- WHERE LAT_N < 137.2345
-- WHERE: This clause filters the rows to include only those where the LAT_N value is less than 137.2345.
-- ORDER BY LAT_N DESC
-- ORDER BY: Sorts the result set based on a specific column.
-- LAT_N: Specifies that the sorting will be done on the LAT_N column.
-- DESC: Indicates descending order, meaning the highest LAT_N values will come first.
-- LIMIT 1
-- LIMIT: Restricts the number of rows returned.
-- 1: Specifies that only one row should be returned.

-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780 . Round your answer to  decimal places.
SELECT ROUND(MIN(LAT_N), 4) FROM STATION WHERE LAT_N>38.7780;
-- Query the Western Longitude (LONG_W) for the smallest Northern Latitude (LAT_N) in STATION that is greater than 38.778038.7780. Round your answer to 4 decimal places.
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N>38.778038 ORDER BY LAT_N LIMIT 1;
-- Consider p1(a,b)  and p2(c,d) to be two points on a 2D plane.
-- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
-- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
-- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
-- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points p1and p2 and round it to a cale of 4 decimal places.
SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 2) AS distance
FROM STATION;
